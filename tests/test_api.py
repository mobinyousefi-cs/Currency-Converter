#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ct: Currency Converter (Tkinter)
File: test_api.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-18
Updated: 2025-10-18
License: MIT License (see LICENSE file for details)
============================================================================================================================
"""
from currency_converter.api import FxClient
from currency_converter.model import Symbols
import types




class DummyResp:
def __init__(self, json_data):
self._json = json_data


def raise_for_status(self):
return None


def json(self):
return self._json




def patch_requests(monkeypatch, responses):
def fake_get(url, params=None, timeout=10.0):
key = "symbols" if "currencies" in url or url.endswith("/symbols") else "convert"
return DummyResp(responses[key])


import requests # noqa: WPS433


monkeypatch.setattr(requests, "get", fake_get)




def test_get_symbols_frankfurter(monkeypatch):
responses = {"symbols": {"USD": "US Dollar", "EUR": "Euro"}, "convert": {}}
patch_requests(monkeypatch, responses)
c = FxClient(provider="frankfurter")
syms = c.get_symbols()
assert isinstance(syms, Symbols)
assert set(syms.codes) >= {"USD", "EUR"}




def test_convert_frankfurter(monkeypatch):
responses = {
"symbols": {"USD": "US Dollar", "EUR": "Euro"},
"convert": {"base": "EUR", "date": "2025-10-18", "rates": {"USD": 1.1}},
}
patch_requests(monkeypatch, responses)
c = FxClient(provider="frankfurter")
quote = c.convert(1.0, "EUR", "USD")
assert quote.rate == 1.1
assert quote.base == "EUR" and quote.quote == "USD"