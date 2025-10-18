#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
============================================================================================================================
Project: Currency Converter (Tkinter)
File: main.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-18
Updated: 2025-10-18
License: MIT License (see LICENSE file for details)
============================================================================================================================


Description:
Tkinter GUI application for converting currencies using live rates.
"""
from __future__ import annotations


import threading
import tkinter as tk
from tkinter import ttk, messagebox


from .api import FxClient
from .utils import format_money, safe_parse_amount




APP_TITLE = "Currency Converter"




class ConverterApp(ttk.Frame):
def __init__(self, master: tk.Tk) -> None:
super().__init__(master, padding=16)
self.master.title(APP_TITLE)
self.master.minsize(520, 260)
self.pack(fill="both", expand=True)


# State
self.client = FxClient()
self.symbols: list[str] = []


# Variables
self.var_amount = tk.StringVar(value="1.00")
self.var_from = tk.StringVar(value="USD")
self.var_to = tk.StringVar(value="EUR")
self.var_result = tk.StringVar(value="—")
self.btn_convert: ttk.Button | None = None


self._build_ui()
self.after(50, self._load_symbols_async)


# UI builders
def _build_ui(self) -> None:
self.master.option_add("*Font", "Segoe UI 10")


title = ttk.Label(self, text=APP_TITLE, font=("Segoe UI", 14, "bold"))
title.grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 12))


ttk.Label(self, text="Amount:").grid(row=1, column=0, sticky="e", padx=(0, 8))
run_app()