'''
Created on 9 Mar 2018

@author: gilliandonlon
'''
import pytest
import urllib.request
import re

def parseFile(input):
        # use requests
    if input.startswith('http'):
        N, instructions = None, []
        req = urllib.request.urlopen(input)
        buffer = req.read().decode('utf-8')
        N = int(buffer.split('\n')[0])
        for line in buffer.split('\n')[1:]:
            instructions.append(line)
        return N, instructions
    else:
        # read from disk
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        return N, instructions
    return




        