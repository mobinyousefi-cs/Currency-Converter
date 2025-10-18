#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
============================================================================================================================
Project: Currency Converter (Tkinter)
File: utils.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-18
Updated: 2025-10-18
License: MIT License (see LICENSE file for details)
============================================================================================================================


Description:
Formatting helpers and simple validation utilities.
"""
from __future__ import annotations


import math
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation




def format_money(amount: float, currency: str) -> str:
"""Format a float to a money-like string with 2-4 decimals depending on magnitude."""
if math.isnan(amount) or math.isinf(amount):
raise ValueError("Invalid amount")


# Use 2 decimals normally; use up to 4 for small values
q = Decimal(str(amount))
prec = Decimal("0.01") if abs(amount) >= 0.01 else Decimal("0.0001")
rounded = q.quantize(prec, rounding=ROUND_HALF_UP)
return f"{rounded} {currency}"




def safe_parse_amount(text: str) -> float:
"""Parse user input into a positive float; raises ValueError on invalid."""
t = (text or "").strip().replace(",", ".")
try:
value = float(t)
except (ValueError, TypeError):
raise ValueError("Please enter a numeric amount.")
if value < 0:
raise ValueError("Amount must be non-negative.")
return value