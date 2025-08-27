# Hackathon 2025 - Transcripción y Análisis Automático

## 🚀 Objetivo
Sistema que:
1. Transcribe llamadas de audio a texto.
2. Detecta errores críticos como:
   - Venta de divisas a precio incorrecto.
   - Información errónea de tasas/comisiones.
   - Omisión de advertencias regulatorias.
   - Contradicciones con políticas oficiales.

## 📂 Estructura
- `src/` → Código modular.
- `notebooks/` → Experimentos en Colab.
- `data/` → Audios y transcripciones.
- `requirements.txt` → Dependencias.
- `setup.ipynb` → Instalación rápida.

## ▶️ Cómo empezar en Colab

0. Clonar el REPO
 ```python
!git clone https://github.com/<tu_usuario>/hackathon2025.git
```
2. Montar Drive:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
