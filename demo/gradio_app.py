import gradio as gr
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import models, transforms
from PIL import Image
import json
import os

# Configuration
NUM_CLASSES = 38
PTH_PATH = '../model_weights/best_plant_disease_model.pth'
JSON_PATH = '../metadata/class_names_enhanced.json'

# Model Definition (Modular) 
class PlantDiseaseEnsemble(nn.Module):
    def __init__(self, num_classes=38):
        super(PlantDiseaseEnsemble, self).__init__()
        # Weights=None for safe loading
        self.model_A = models.mobilenet_v2(weights=None)
        in_A = self.model_A.classifier[1].in_features
        self.model_A.classifier = nn.Sequential(nn.Dropout(0.3), nn.Linear(in_A, num_classes))
        
        self.model_B = models.densenet121(weights=None)
        in_B = self.model_B.classifier.in_features
        self.model_B.classifier = nn.Sequential(nn.Dropout(0.3), nn.Linear(in_B, num_classes))
        
    def forward(self, x):
        return (0.635 * self.model_A(x)) + (0.365 * self.model_B(x))

# Resource Loading
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = PlantDiseaseEnsemble(num_classes=NUM_CLASSES)

if os.path.exists(PTH_PATH):
    checkpoint = torch.load(PTH_PATH, map_location=device)
    state_dict = checkpoint['state_dict'] if 'state_dict' in checkpoint else checkpoint
    model.load_state_dict(state_dict)
model.to(device).eval()

with open(JSON_PATH, 'r') as f:
    metadata = json.load(f)

class_names = sorted(list(metadata.keys()))

# Inference Logic 
def predict_disease(input_img):
    if input_img is None:
        return "Please upload an image.", ""
    
    # Preprocess
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    input_tensor = transform(input_img).unsqueeze(0).to(device)
    
    with torch.no_grad():
        output = model(input_tensor)
        probs = F.softmax(output, dim=1)[0]
    
    conf, idx = torch.max(probs, dim=0)
    prediction = class_names[idx.item()]
    info = metadata.get(prediction, {})
    
    # Format Results
    result_text = f"## Diagnosis: {prediction} ({conf.item()*100:.1f}%)"
    details = f" **Plant**: {info.get('plant', 'N/A')}\n"
    details += f" **Disease**: {info.get('disease', 'N/A')}\n\n"
    details += "###  Reasons:\n" + "\n".join([f"- {r}" for r in info.get('reasons', [])]) + "\n\n"
    details += "###  Solutions:\n" + "\n".join([f" {s}" for s in info.get('solutions', [])])
    
    return result_text, details

# UI Interface 
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("#  Plant Disease Meta-Ensemble Diagnosis")
    gr.Markdown("Upload a leaf image to receive a high-precision AI diagnosis and treatment plan.")
    
    with gr.Row():
        with gr.Column():
            input_img = gr.Image(type="pil", label="Upload Leaf Image")
            btn = gr.Button("Diagnose", variant="primary")
        with gr.Column():
            output_header = gr.Markdown()
            output_details = gr.Markdown()
            
    btn.click(fn=predict_disease, inputs=input_img, outputs=[output_header, output_details])
    
    gr.Examples(
        examples=[], # Add local sample paths here if available
        inputs=input_img
    )

if __name__ == "__main__":
    demo.launch()
