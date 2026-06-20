# AI_3D_Designer


# AI_3D_Designer is a desktop application that uses Large Language Models (LLMs) to generate, edit, and visualize parametric 3D CAD models from natural language prompts. It combines AI-powered design generation with a real-time 3D viewport, allowing users to create models suitable for 3D printing without writing CAD scripts manually.

---

## Features

- 🤖 AI-assisted CAD generation using natural language
- 🧩 Parametric CAD modeling with CadQuery
- 🖥️ Interactive desktop interface built with Tkinter and ttkbootstrap
- 📐 Live parameter editing (dimensions, angles, radii, etc.)
- 🎯 Real-time 3D visualization using VTK
- 💬 Chat-based AI interaction
- 🔄 Design regeneration after parameter modifications
- 📦 Export models to STL and STEP formats
- 💾 Save and load AI CAD projects
- 📝 Modular architecture for easy maintenance and extension

---

## Technology Stack

- Python 3.10+
- Tkinter
- ttkbootstrap
- CadQuery
- VTK
- Ollama
- Gemma 4
- NumPy
- Requests

---

## Project Structure

```
AI_CAD_Studio/
│
├── core/
│   ├── ai/
│   ├── cad/
│   ├── services/
│   ├── storage/
│   ├── utils/
│   └── ...
│
├── ui/
│   ├── chat_panel.py
│   ├── viewport_panel.py
│   ├── parameter_panel.py
│   ├── toolbar.py
│   └── ...
│
├── models/
├── exports/
├── projects/
├── logs/
├── assets/
├── config.py
└── main.py
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-CAD-Studio.git
cd AI-CAD-Studio
```

Create a virtual environment

```bash
py -3.10 -m venv venv
```

Activate it

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python main.py
```

---

## Workflow

1. Enter a design prompt.
2. The AI interprets the request and generates a parametric design.
3. CadQuery creates the 3D model.
4. The model is rendered in the 3D viewport.
5. Modify parameters or provide additional prompts to refine the design.
6. Export the final model as STL or STEP for manufacturing or 3D printing.

---

## Example Prompt

```
Design a phone stand with:

- 75° viewing angle
- Cable management slot
- Width: 80 mm
- Foldable base
- Optimized for FDM 3D printing
```

---

## Future Improvements

- Assembly modeling
- Sketch-based editing
- Constraint solver
- AI design optimization
- Cloud project synchronization
- Multi-material support
- Real-time collaborative editing
- Mesh repair and validation
- Printability analysis

---

## License

This project is intended for educational and research purposes.
