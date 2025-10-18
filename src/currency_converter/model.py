#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
============================================================================================================================
Project: Currency Converter (Tkinter)
File: model.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-18
Updated: 2025-10-18
License: MIT License (see LICENSE file for details)
============================================================================================================================


Description:
Domain models and value objects for currency conversion.
"""
from __future__ import annotations


from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional




@dataclass(frozen=True)
class RateQuote:
base: str
quote: str
rate: float
provider: str
as_of: datetime




@dataclass(frozen=True)
class Symbols:
codes: List[str]
names: Dict[str, str]


def sorted_codes(self) -> List[str]:
return sorted(self.codes)