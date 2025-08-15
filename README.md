# Code Accuracy & Style Checker

A Python desktop app for checking code logic, style (PEP8), scoring, and AI-based improvement (Python, Java support planned).

## Features

- GUI with code input/output
- Detects logical/style issues (uses `pylint`)
- Error explanations and suggestions
- Score based on readability, logic, syntax
- AI improvement placeholder (integrate with OpenAI/HuggingFace)
- Java support coming soon

## Setup

```bash
pip install -r requirements.txt
# Ensure you also have pylint installed globally if needed
python main.py
```

## Usage

1. Paste Python code in the input panel.
2. Click "Check Code" for analysis and scoring.
3. Click "Improve with AI" to apply AI-based improvements (placeholder).

## Extend

- Integrate AI improvement via OpenAI API in `analysis.py`.
- Add Java analysis using Checkstyle/SpotBugs.
