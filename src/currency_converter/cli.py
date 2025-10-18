#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
============================================================================================================================
Project: Currency Converter (Tkinter)
File: cli.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-18
Updated: 2025-10-18
License: MIT License (see LICENSE file for details)
============================================================================================================================


Description:
Small CLI wrapper for quick conversions without the GUI.
Usage:
python -m currency_converter.cli 100 USD EUR
"""
from __future__ import annotations


import argparse
from .api import FxClient
from .utils import format_money




def main(argv: list[str] | None = None) -> int:
p = argparse.ArgumentParser(prog="currency-converter")
p.add_argument("amount", type=float)
p.add_argument("base")
p.add_argument("quote")
args = p.parse_args(argv)


client = FxClient()
quote = client.convert(args.amount, args.base.upper(), args.quote.upper())
result = args.amount * quote.rate
print(format_money(result, quote.quote))
return 0




if __name__ == "__main__": # pragma: no cover
raise SystemExit(main())