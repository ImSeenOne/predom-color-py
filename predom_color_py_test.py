import unittest
import pytest
import predom_color_py
import numpy


def test_dominantColors():
    dc = predom_color_py.DominantColors("./scrabble.jpg",5)

    var = dc.dominantColors()

    assert type(var) == numpy.ndarray
