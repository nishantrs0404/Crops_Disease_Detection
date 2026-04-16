# 🌿 Plant Disease Diagnosis: Meta-Ensemble Framework

![Project Banner](visuals/banner.png)

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.1+-red.svg)](https://pytorch.org/)
[![Accuracy](https://img.shields.io/badge/Accuracy-99.21%25-green.svg)]()
[![Model](https://img.shields.io/badge/Model-Meta--Ensemble-purple.svg)]()
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Project Overview
This repository presents a **World-Class Plant Disease Detection System** powered by a **Meta-Ensemble** of MobileNetV2 and DenseNet121. Achieving a staggering **99.21% accuracy**, this system provides farmers with not just a diagnosis, but a multi-dimensional treatment plan including root causes and precision remedies.

---

## 🚀 Key Innovations
- **Dual-Engine Fusion**: Hierarchical spatial feature extraction combined with dense connectivity for unparalleled robustness.
- **Explainable AI Pipeline**: Dynamic mapping of labels to expert-verified reasons and solutions.
- **Production-Ready GUI**: Interactive web-based diagnostic application using Gradio.

---

## 📂 Repository Architecture

| File | Description |
| :--- | :--- |
| **[📜 research/](research/)** | Latest Academic Research Paper (`Our_Research_Paper.pdf`). |
| **[📑 docs/](docs/)** | 15-page deep-dive technical analysis report. |
| **[🎓 notebooks/](notebooks/)** | Annotated Training Pipeline & Inference Demo. |
| **[🚀 demo/](demo/)** | **Gradio Web Application** for interactive diagnosis. |
| **[🧠 model_weights/](model_weights/)** | Trained Meta-Ensemble weights (LFS). |
| **[📗 metadata/](metadata/)** | Enhanced Disease → Solution mapping database. |
| **[⚙️ requirements.txt](requirements.txt)** | One-click environment setup. |
| **[⚖️ LICENSE](LICENSE)** | MIT Open-Source Compliance. |

---

## 🎨 Dataset Discovery
Our model is trained on a diverse subset of the **PlantVillage Dataset**, covering 38 distinct classes across 14 plant species.

![Dataset Gallery](visuals/gallery.png)

---

## 🏗️ System Flow
```mermaid
graph TD
    A[Leaf Image] --> B[Preprocessing]
    B --> C[MobileNetV2 Engine]
    B --> D[DenseNet121 Engine]
    C --> E[Weighted Fusion]
    D --> E
    E --> F[Diagnosis Predicted]
    F --> G[Explainability Layer]
    G --> H[Reasons & Solutions]
```

---

## 🔮 Future Evolution & Roadmap
To elevate this project further, we are exploring:
- **🛰️ Drone Integration**: Real-time canopy monitoring using the Meta-Ensemble.
- **📱 Mobile Deployment**: Converting model weights to CoreML/TFLite for offline smartphone use.
- **☁️ Cloud Streaming**: Deploying as an API for agricultural sensor networks.
- **🌍 Multilingual Solutions**: Translating diagnostic reports into regional languages.

---

## 🚦 Quick Start

### 1. Installation
```bash
git clone https://github.com/nishantrs0404/Crops_Disease_Detection.git
cd Crops_Disease_Detection
pip install -r requirements.txt
```

### 2. Launch Web App (GUI)
```bash
cd demo
python gradio_app.py
```
*Navigate to the local URL provided to upload photos and get instant results!*

### 3. Interactive Notebook
Explore **`notebooks/CV_Final_Evaluation.ipynb`** for a programmatic walkthrough.

---

## 📝 Authorship & Acknowledgements
- **Author**: Nishant Raushan
- **Affiliation**: Netaji Subhas University of Technology (NSUT)
- **Project**: Computer Vision Portfolio
