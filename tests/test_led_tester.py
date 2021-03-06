#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_tester` package."""

import pytest

from click.testing import CliRunner

from led_tester import led_tester
from led_tester import cli
from led_tester import utils
  

    
def test_read_file():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N == 10
    assert instructions == ['turn on 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'switch 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'turn on 2,2 through 7,7'] 

def test_outcome():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    
    ledtester = led_tester.LightTester(N)
    
    for instruction in instructions:
        ledtester.apply(instruction)
    
    assert ('#occupied: ', 36) 