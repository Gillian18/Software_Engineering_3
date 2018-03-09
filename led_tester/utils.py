'''
Created on 9 Mar 2018

@author: gilliandonlon
'''
import pytest
def parseFile(input):

    if input.startswith('http'):
        # use requests
        return None, None
    else:
        # read from disk
        # haven't written the code yet...
        return None, None
    return
        