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
    assert N == None
    assert instructions == None
