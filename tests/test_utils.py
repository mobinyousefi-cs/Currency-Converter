#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
============================================================================================================================
Project: Currency Converter (Tkinter)
File: test_utils.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-18
Updated: 2025-10-18
License: MIT License (see LICENSE file for details)
============================================================================================================================
"""
from currency_converter.utils import format_money, safe_parse_amount
import math
import pytest




def test_format_money_rounds():
assert format_money(123.456, "USD").startswith("123.46")




def test_format_money_small_values():
assert format_money(0.00091, "EUR").startswith("0.0009")




def test_format_money_raises_on_nan():
with pytest.raises(ValueError):
format_money(float("nan"), "USD")




def test_safe_parse_amount_valid():
assert safe_parse_amount("1,25") == 1.25




def test_safe_parse_amount_negative():
with pytest.raises(ValueError):
safe_parse_amount("-5")