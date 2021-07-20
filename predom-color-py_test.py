import unittest
import pytest

import predom-color-py

def test_sum_happy_path():
    current_value = my_calc.add(10,20)
    expected_value = 30

    assert expected_value == current_value
