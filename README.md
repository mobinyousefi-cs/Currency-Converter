# Currency Converter (Tkinter)

A professional, testable Python project by **Mobin Yousefi**, featuring a modern Tkinter GUI, clean architecture, and full CI pipeline — designed for clarity, maintainability, and academic-grade quality.

---

## 🌍 Overview

This project implements a **Currency Converter** application that allows users to convert between currencies using **real-time foreign exchange rates**. It features both a **graphical interface** built with Tkinter and a **command-line interface (CLI)** for quick conversions.

The application fetches live exchange rates using free and reliable APIs such as **Frankfurter** (European Central Bank) and **Exchangerate.host**.

---

## ✨ Features

✅ **Live exchange rates** from trusted providers
✅ **Beautiful Tkinter GUI** — modern, lightweight, responsive
✅ **Swap & Copy-to-Clipboard** features for user convenience
✅ **CLI Support** — run quick conversions directly in your terminal
✅ **Thread-safe background fetching** (non-blocking UI)
✅ **Unit-tested, typed code** using `pytest` and `mypy`
✅ **CI pipeline** via GitHub Actions (Black, Ruff, Pytest)

---

## 🧠 Tech Stack

* **Python 3.9+**
* **Tkinter** for GUI
* **Requests** for API calls
* **Pytest** for testing
* **Ruff + Black** for linting & formatting

---

## 🧩 Project Structure

```
currency-converter/
├── src/
│   └── currency_converter/
│       ├── main.py          # GUI app (Tkinter)
│       ├── cli.py           # CLI interface
│       ├── api.py           # HTTP client for FX APIs
│       ├── utils.py         # Validation & formatting helpers
│       ├── model.py         # Domain data models
│       └── __main__.py      # Entry point for module run
├── tests/                   # Unit tests
│   ├── test_api.py
│   └── test_utils.py
├── requirements.txt
├── pyproject.toml
├── README.md
├── LICENSE
└── .github/workflows/ci.yml # GitHub Actions CI setup
```

---

## 🚀 Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/mobinyousefi-cs/currency-converter.git
cd currency-converter
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the GUI App

```bash
python -m currency_converter
```

### 4. Run via CLI

```bash
python -m currency_converter.cli 100 USD EUR
```

### 5. Run Tests

```bash
pytest -q
```

---

## ⚙️ Configuration

* **Default API:** Frankfurter ([https://www.frankfurter.app](https://www.frankfurter.app))
* **Environment Variable:** You can override with your own endpoint:

  ```bash
  export CURRENCY_API_BASE=https://api.exchangerate.host
  ```

---

## 🧪 Example Usage

### GUI Mode

Enter amount → choose base currency → choose target currency → click **Convert**.

### CLI Mode

```bash
$ python -m currency_converter.cli 250 USD EUR
229.74 EUR
```

---

## 🧰 Developer Notes

* GUI uses **threading** for API calls (non-blocking UX)
* All modules are **PEP8-compliant** and **type-annotated**
* Ready for **packaging and PyPI publication**
* Integrated **continuous integration (CI)** pipeline for automated testing & linting

---

## 🧾 License

This project is licensed under the **MIT License**.
© 2025 **Mobin Yousefi** — All rights reserved.

---

## 👨‍💻 Author

**Mobin Yousefi**
📍 Master’s Student in Computer Science
🔗 [GitHub Profile](https://github.com/mobinyousefi-cs)
💡 Passionate about AI, Optimization, and Intelligent Systems.
