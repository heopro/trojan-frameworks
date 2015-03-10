#!/usr/bin/env python

__author__ = "bt3"

import os

def run(**args):
    print '[*] dir_lister.py module'
    files = os.listdir('.')
    return str(files)

if __name__ == '__main__':
    print run()