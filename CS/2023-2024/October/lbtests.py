#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 19:53:59 2023

@author: ads22
"""

import letterBoxed as lb


# Example: Loading a dictionary
file_name = 'words.txt'  # Replace with the name of your text file
words_dict = lb.load_words_to_dict(file_name)
print(words_dict['A'][:20])

# Example usage:
board_description = "ABC DEF GHI JKL"
board = lb.string2board(board_description)
print(board)
new_desc = lb.board2string(board)
print(new_desc)


# Continuing the example above
print("=== Testing word validity checks ===")
print(lb.is_valid_word("AFI", board, last_letter = None))
print(lb.is_valid_word("AFIZ", board, last_letter = None))
print(lb.is_valid_word("AEFI", board, last_letter = None))
print(lb.is_valid_word("AFI", board, last_letter = "B"))
print(lb.is_valid_word("AFI", board, last_letter = "A"))

# Continuing the same example
print("=== Testing five-point solution (see file for appropriate outputs) ===")
test_sequences = ["AFIJB BECLH HDIKG\n", # correct
                  "AFIJZB BECLH HDIKG\n", # uses an incorrect letter
                  "AFIJB AECLH HDIKG\n", # second word doesn't follow first
                  "AFIJB BAECLH HDIKG\n", # repeated pile
                  "AFIJB BECLH HDIK\n"] # doesn't cover all letters
for i, seq in enumerate(test_sequences): 
    input_filename = "input-5pt-{}.txt".format(i)
    output_filename = "output-5pt-{}.txt".format(i)
    with open(input_filename,'w') as input_file:
        input_file.write(board_description + "\n")
        input_file.write(seq)
    lb.fivePoint(input_filename, output_filename)
    with open(output_filename,'r') as output_file:
        print(output_file.readline())


print("=== Testing shortest sequence finder ===")
words_dict = lb.load_words_to_dict("words.txt")
test_board_descs = ["ABC DEF GHI JKL",
                "RNY TCI DBA OFH",
                "TRE HIP VSZ OBA",
                "OLE HSA RUC ITQ"]
for i, board_desc in enumerate(test_board_descs):
    board = lb.string2board(board_desc)
    sols = lb.find_shortest_seq_DP(board, words_dict)
    # sols is a list of all the solutions (not just the first)
    print("Board:", board)
    print("Solution:", sols[0])
    
print("=== Testing 10-point solution ===")
for i, board_desc in enumerate(test_board_descs):
    input_filename = "input-10pt-{}.txt".format(i)
    output_filename = "output-10pt-{}.txt".format(i)
    with open(input_filename,'w') as input_file:
        input_file.write(board_desc + "\n")
    lb.ten_point(input_filename, output_filename)
    with open(output_filename,'r') as output_file:
        print(output_file.readline())









