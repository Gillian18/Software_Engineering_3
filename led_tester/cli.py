# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
import click
import argparse
from led_tester import utils
from led_tester import led_tester
click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for led_tester."""
    print("input", input)
    
    N, instructions = utils.parseFile(input)
    
    ledTester = led_tester.LightTester(N)
    
    
    ledTester.apply(instructions)
    
    print('#occupied: ', ledTester.count()) 
    return 0
    
    
if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover