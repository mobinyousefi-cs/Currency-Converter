# Currency Converter (Python + Tkinter)


A clean, professional Python project that converts currencies using a public exchange rates API and offers both a Tkinter GUI and a simple CLI. Designed for readability, testability, and easy inclusion in a GitHub portfolio.


## Features
- Tkinter GUI with currency selection, amount input, swap support and live rate status
- CLI for quick conversions
- Uses a robust `CurrencyConverter` class with caching and error handling
- Unit tests (pytest) with network calls mocked
- GitHub Actions workflow for CI


## Requirements
- Python 3.10+
- See `requirements.txt` for Python packages


## Install
```bash
python -m venv .venv
source .venv/bin/activate # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```


## Run the GUI
```bash
python -m src.main --gui
```


## Use the CLI
```bash
python -m src.main convert --amount 100 --from USD --to EUR
```


## Run tests
```bash
pytest -q
```


## Project structure
```
CurrencyConverter/
├─ src/
│ ├─ __init__.py
│ ├─ main.py
│ ├─ converter.py
│ └─ ui.py
├─ tests/
│ └─ test_converter.py
├─ requirements.txt
├─ README.md
└─ .github/workflows/ci.yml
```