#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
============================================================================================================================
Project: Currency Converter (Tkinter)
File: api.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-18
Updated: 2025-10-18
License: MIT License (see LICENSE file for details)
============================================================================================================================


Description:
HTTP client for fetching FX symbols and conversion rates. Uses Frankfurter (ECB) or
Exchangerate Host as free, no-key providers. Provider can be overridden via env var
`CURRENCY_API_BASE`.


Notes:
- Network errors are wrapped in RuntimeError with a helpful message.
- Designed so tests can mock `requests.get` easily.
"""
from __future__ import annotations


import os
from datetime import datetime
from typing import Dict, Tuple


import requests


from .model import RateQuote, Symbols




DEFAULT_PROVIDER = "frankfurter" # "frankfurter" or "exchangerate_host"


_PROVIDERS: Dict[str, Dict[str, str]] = {
# Frankfurter.app (ECB rates)
"frankfurter": {
"base": os.getenv("CURRENCY_API_BASE", "https://api.frankfurter.app"),
"symbols": "/currencies",
"convert": "/latest",
},
# Exchangerate.host
"exchangerate_host": {
"base": os.getenv("CURRENCY_API_BASE", "https://api.exchangerate.host"),
"symbols": "/symbols",
"convert": "/latest",
},
}




class FxClient:
def __init__(self, provider: str | None = None, timeout: float = 10.0) -> None:
self.provider = (provider or DEFAULT_PROVIDER).lower()
return RateQuote(base=base, quote=quote, rate=rate, provider=self.provider, as_of=as_of)