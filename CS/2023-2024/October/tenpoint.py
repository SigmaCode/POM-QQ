#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 20:12:28 2023

To run this program, execute the following on the command line: 
    
      python tenpoint.py input.txt output.txt
      
replacing the filenames as appropriate.


@author: ads22
"""

import sys
import letterBoxed as lb

def main(args):
    if len(args) != 2:
        print("Expected two command-line arguments but got", len(args))
        return 1
    else:
        input_filename = args[0]
        output_filename = args[1]
        result = lb.ten_point(input_filename, output_filename)
        print(result[0]) #This is what was written to the output file (either first solution or "IMPOSSIBLE")
        return 0


if __name__ == '__main__':
    args = sys.argv[1:]
    # args is a list of the command line args
    main(args)
