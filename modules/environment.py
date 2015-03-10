#!/usr/bin/env python

__author__ = "bt3"

import os

def run(**args):
    print '[*] enviroment.py module'
    return str(os.environ)

if __name__ == '__main__':
    print run()