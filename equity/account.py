#!/usr/bin/env python3

from enum import Enum


class AccountType(str, Enum):
    equity = "Equity"
    assets = "Assets"
    liabilities = "Liabilities"
    income = "Income"
    expenses = "Expenses"
