import tempfile
import subprocess
import json

def analyze_python_code(code):
    """Analyzes Python code for logic errors, style issues, scores, and suggestions."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as tmp:
        tmp.write(code)
        tmp_path = tmp.name

    # Run pylint for static analysis
    try:
        result = subprocess.run(
            ["pylint", "--output-format=json", tmp_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        issues = json.loads(result.stdout) if result.stdout else []
    except Exception as e:
        return f"Error running analysis: {e}"

    # Parse pylint results
    style_issues = []
    logic_issues = []
    total_score = 100
    for issue in issues:
        typ = issue.get("type")
        msg = issue.get("message")
        line = issue.get("line")
        symbol = issue.get("symbol")
        # Heuristics: convention/refactor = style, error/warning = logic
        if typ in ("convention", "refactor"):
            style_issues.append(f"Line {line}: {msg} [{symbol}]")
            total_score -= 2
        elif typ in ("error", "warning"):
            logic_issues.append(f"Line {line}: {msg} [{symbol}]")
            total_score -= 5

    # Suggestions
    suggestions = []
    if style_issues:
        suggestions.append("Fix style issues (PEP8, formatting).")
    if logic_issues:
        suggestions.append("Check logic for potential errors.")
    if not issues:
        suggestions.append("No issues found! Code looks good.")

    # Compose output
    output = []
    output.append(f"Score: {max(total_score,0)}/100\n")
    if style_issues:
        output.append("Style Issues:\n" + "\n".join(style_issues) + "\n")
    if logic_issues:
        output.append("Logic Issues:\n" + "\n".join(logic_issues) + "\n")
    output.append("Suggestions:\n" + "\n".join(suggestions))
    return "\n".join(output)

def ai_improve_code(code):
    """
    Placeholder for AI-based code improvement.
    Replace with real model or API integration.
    """
    # For now, just return the original code.
    # You can integrate OpenAI/HuggingFace here for improvement.
    return code
