#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 00:40:30 2020

@author: paulberraute
"""

import pytest
import sys

sys.path.append("../project")

from numbers_to_dec import list_to_decimal

def test_notInRange():
    with pytest.raises(ValueError):
        list_to_decimal([-1,0]) 

def test_notInRange2():
    with pytest.raises(ValueError):
        list_to_decimal([10,0]) 

def test_float():
    with pytest.raises(TypeError):
        list_to_decimal([1.2,0,10]) 

def test_char():
    with pytest.raises(TypeError):
        list_to_decimal(['a',0]) 

def test_char():
    with pytest.raises(TypeError):
        list_to_decimal([True,0]) 

def test_char():
    assert list_to_decimal([0, 4, 2, 8]) == 428
