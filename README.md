# 🌿 Plant Disease Diagnosis using Meta-Ensemble Deep Learning Framework

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.1+-red.svg)](https://pytorch.org/)
[![Accuracy](https://img.shields.io/badge/Accuracy-99.21%25-green.svg)]()
[![Model](https://img.shields.io/badge/Model-Meta--Ensemble-purple.svg)]()
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Project Overview
This project presents a **high-performance plant disease detection system** built using a **Meta-Ensemble Deep Learning Framework**, combining:
- ⚡ **MobileNetV2 (Lightweight, efficient)**
- 🧠 **DenseNet121 (Deep feature reuse)**

Inspired by IEEE research, this system achieves **99.21% accuracy** while providing actionable insights for farmers.

---

## 🧠 What Makes This Project Special?
Unlike traditional models, this system:
- ✔ Predicts disease labels with high confidence.
- ✔ Explains **WHY it happened** (Root causes).
- ✔ Suggests **HOW to fix it** (Actionable remedies).
- ✔ Optimized for **edge devices** and practical agricultural use.

---

## 🏗️ System Architecture
```text
Input Image
     ↓
Preprocessing (Resize + Normalize + Enhancement)
     ↓
MobileNetV2  ─┐
              ├──► Meta-Ensemble Fusion ───► Final Prediction
DenseNet121 ──┘                  ↓
     ↓                Explainability Layer
     ↓                   (JSON Mapping)
     ↓                           ↓
 Disease Name  <--->  Root Causes  <--->  Effective Solutions
```

---

## 📂 Repository Assets

| File | Description |
| :--- | :--- |
| **[📜 Base_Research_Paper.pdf](research/Base_Research_Paper.pdf)** | IEEE baseline research paper. |
| **[📑 Advanced_Technical_Report.pdf](docs/Advanced_Technical_Report.pdf)** | Our 15-page deep-dive technical report. |
| **[🎓 Plant_Disease_Enhanced_Tutorial.ipynb](notebooks/Plant_Disease_Enhanced_Tutorial.ipynb)** | Fully annotated pipeline (Training Walkthrough). |
| **[🧠 best_plant_disease_model.pth](model_weights/best_plant_disease_model.pth)** | Trained Meta-Ensemble weights (Git LFS). |
| **[📗 class_names_enhanced.json](metadata/class_names_enhanced.json)** | Disease → Causes → Solutions mapping. |
| **[🚀 CV_Final_Evaluation.ipynb](notebooks/CV_Final_Evaluation.ipynb)** | Production-ready interactive prediction portal. |
| **[⚙️ requirements.txt](requirements.txt)** | Dependency list for environment reproduction. |
| **[⚖️ LICENSE](LICENSE)** | MIT Open-Source License. |

---

## 🚦 Quick Start
1. Clone the repository: `git clone https://github.com/nishantrs0404/Crops_Disease_Detection.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Open **`notebooks/CV_Final_Evaluation.ipynb`** to diagnose symptoms and get remedies.

---

## 📝 Authorship
- **Author**: Nishant Raushan
- **Affiliation**: Netaji Subhas University of Technology (NSUT)
- **Project**: Computer Vision Final Project
