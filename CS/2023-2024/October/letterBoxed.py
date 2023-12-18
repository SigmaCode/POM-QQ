#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 10:55:55 2023

@author: ads22
"""


## Example usage:
#input_filename = 'input.txt'  # Replace with your input file's name
#copy_lowercase_words(input_filename, output_filename)
#output_filename = 'output.txt'  # Replace with your output file's name


def load_words_to_dict(file_name):
    # Loads a file with valid words into a dict of lists. Each entry
    # in the outer dictionary is keyed by a letter. The associated value is a sorted list of all the words that start with the key.

    # Initialize an empty dictionary to store words organized by the
    # first character
    words_dict = {}

    # Open the file for reading
    with open(file_name, 'r') as file:
        for line in file:
            # Split each line into words
            words = line.strip().split()

            # Skip empty lines
            if not words:
                continue

            # Get the first word from the line, converted to upper case
            first_word = words[0].strip().upper()

            # Get the first character of the first word
            first_char = first_word[0]

            # Check if the character is a Latin letter
            if first_char.isalpha() and first_char.isascii():
                # Create a dictionary for the character if it doesn't exist
                if first_char not in words_dict:
                    words_dict[first_char] = []

                # Add the word to the dictionary under the character's key
                words_dict[first_char].append(first_word)

    for first_char in words_dict:
        words_dict[first_char].sort()

    return words_dict

## Example usage:
#file_name = 'example.txt'  # Replace with the name of your text file
#result = load_words_to_dict(file_name)
#print(result)



def string2board(board_description):
    # Split the board into sets, each representing a side
    # input should be a space-separated list of strings
    sidestrings = board_description.strip().split(' ')
    for i in range(len(sidestrings)):
        sidestrings[i] = sidestrings[i].strip().upper()
    board = [set(x) for x in sidestrings]
    return board

def board2string(board):
    # converts a list of sets of letters to a string, with spaces separating the sets
    sidestrings = ["".join(sorted(side)) for side in board]
    return ' '.join(sidestrings)


def board2list(board):
    sidelists = [sorted(side) for side in board]
    # The following comprehension "flattens" a list of lists into one big list
    return [item for sublist in sidelists for item in sublist]

def board2frozenset(board):
    # Turn the list of strings into a list of lists
    sidelists = [sorted(side) for side in board]
    # The following comprehension "flattens" a list of lists into one big list
    biglist = [letter for sidelist in sidelists for letter in sidelist]
    return frozenset(biglist)


# Find the side index containing the first letter
def find_side(board,letter):
    for i, side in enumerate(board):
        if letter in side:
            return (True, i)
    return (False, None) #only executes if letter was not found.

def is_valid_word(word, board, last_letter):
    # Check if a word is valid according to the game rules
    # Set last_letter to None if word is first in sequence
    # Returns a pair of the form (bool, string), where the first entry is the boolean result of the check, and the second is a string which explanation of the error.

    if not word:
        return False, "Empty word"  # An empty word is never valid
        
    first_letter = word[0] 
    first_letter = first_letter
    
    # Check if the first letter is the last letter from the previous word
    if last_letter is not None and first_letter != last_letter:
            return False, "Word '{}' does not start with the last letter of previous word ('{}')".format(word,last_letter)

    prev_side_number = None
    for j, current_letter in enumerate(word):
        found, side_number = find_side(board,current_letter)
        if not found:
            return False, "Letter {} in word '{}' not found on board".format(current_letter,word)
        if prev_side_number != None and prev_side_number == side_number:
            return False, "The pile '{}' was used twice in a row in word '{}'.".format(board2string([board[side_number]]),word)
        prev_side_number = side_number
    
    return True, "Valid"    


def string2sequence(sequence_description):
    word_list = sequence_description.strip().split(" ")
    return word_list

def sequence2string(sequence):
    return " ".join(sequence)

def sequence2set(sequence):
    if sequence == []:
        return set()
    wordlists = [list(word) for word in sequence]
    # The following comprehension "flattens" a list of list into one big list
    return set([letter for listofletters in wordlists for letter in listofletters])


##################################################
# Five-point solution main function
##################################################

def fivePoint(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            lines = input_file.readlines()
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return 

    if len(lines) < 2:
        print("Input file contains fewer than 2 lines")
        return
    else:
        board = string2board(lines[0])
        sequence_description = lines[1].strip().upper()
        word_list = string2sequence(sequence_description)
        last_letter = None
        valid_so_far = True
        for i, word in enumerate(word_list):
            word_i_valid, infostring = is_valid_word(word, board, last_letter)
            valid_so_far = valid_so_far and word_i_valid
            last_letter = word[-1]
        # After for loop, valid_so_far is true if the sequence is valid
        uses_all_letters = all([x in sequence_description for x in board2list(board)])
        correct =  valid_so_far and uses_all_letters

    try:
        with open(output_filename, 'w') as output_file:
            if correct:
                output_file.write("Correct\n")
            else:
                output_file.write("Incorrect\n")
            return correct
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    return

    
##################################################
# Ten-point solution main function
##################################################

def ten_point(input_filename, output_filename, words_file="words.txt"):
    try:
        with open(input_filename, 'r') as input_file:
            textline = input_file.readline()
            board = string2board(textline.strip())
        words_dict = load_words_to_dict(words_file)
        
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return 
    except Exception as e:
        print("An error occurred: \n{}".format(e))
        return
    solutions = find_shortest_seq_DP(board, words_dict)
    if solutions == []:
        outString = "IMPOSSIBLE"
    else:
        first_seq = solutions[0]
        outString = sequence2string(first_seq)
    with open(output_filename, 'w') as output_file:
        output_file.write(outString + "\n")
    return outString, solutions
        

def filter_valid_words(board,words_dict):
    # Returns a dict contain ONLY words that are valid for this board. 
    filtered_dict = {}
    for start_letter in words_dict:
        for word in words_dict[start_letter]:
            if is_valid_word(word, board, None)[0]:
                if start_letter not in filtered_dict: # We only add letters that actually begin valid words
                    filtered_dict[start_letter] = []
                filtered_dict[start_letter].append(word)
    for start_letter in filtered_dict:
        filtered_dict[start_letter].sort()
    return filtered_dict

    

########################################################################
########################################################################
def find_shortest_seq_DP(board, words_dict, verbose = False):
    # This function actually solves the 10-point problem.
    
    filtered_dict = filter_valid_words(board, words_dict)
    if verbose:
        for start_let in filtered_dict:
            print(start_let, len(filtered_dict[start_let]))
    
    board_fr_set = board2frozenset(board) # Contains all the letters on the board
    config_queue = [] #These represent configurations to be extended 
    # A confguration is a tuple (L,c,s) where L is possibly empty list of words 
    # (in the sequence so far), c is a character, and s is a frozenset 
    # containing all the characters covered by this configuration. 
    # Now initialize queue with each of the possible start characters
    
    visited = set() # Use to keep track of which nodes we have visited
    for end_char in sorted(filtered_dict):
        config_queue.append(([], end_char, frozenset()))
        
    queue_pos = 0 # represents the index in the queue to be explored  

    depth = 0
    solutions = []
    done = False # True when we have explored all solutions of the shortest length
    found = False # True if some solution has been found
    while (not done):
        if queue_pos >= len(config_queue): # we have checked everything in the queue.
            done = True
            break
        (seq, end_char, covered_chars) = config_queue[queue_pos]
        if len(seq) > depth:
            if verbose:
                print("Done with depth", depth)
            depth += 1
            if found:
                done = True
                break
        queue_pos += 1
        if (end_char, covered_chars) in visited:
            # This means we have already processed some sequence that 
            # ends with end_char and covers the letters in covered_char_str
            continue
        else:
            visited.add((end_char, covered_chars))
        # Try extending seq with words that start with end_char
        # Ignore if end_char does not start any valid words.
        if end_char in filtered_dict:
            for word in filtered_dict[end_char]:
                if verbose:
                    print(".", end ="")
                # check if we have now exahusted all the letters
                new_seq = seq.copy() # Would be better to keep a pointer to previous sequence
                new_seq.append(word)
                new_covered_chars = covered_chars.union(word)
                new_end_char = word[-1]
                covers_all_chars = (new_covered_chars == board_fr_set)
                if covers_all_chars:
                    solutions.append(new_seq)
                    if verbose: 
                        print("\n", new_seq)
                    found = True
                if not found: # add to queue if and only if we haven't found anything yet
                    config_queue.append((new_seq, new_end_char, new_covered_chars))         
    return solutions



#############################################
# This function was useful for preparing words.txt. It's not part of the problem solution.
#############################################


def copy_lowercase_words(input_filename, output_filename, lengthbound=None):
    assert lengthbound == None or (lengthbound > 0)
    try:
        wordlist = []
        with open(input_filename, 'r') as input_file:
            for line in input_file:
                strippedline = line.strip()
                if all(char.islower() for char in strippedline):
                    if lengthbound == None or len(strippedline) >= lengthbound:
                        wordlist.append(strippedline)
        wordlist.sort()
        wordlist.sort(key=len)
        with open(output_filename, 'w') as output_file:
            for word in wordlist:
                output_file.write(word + "\n")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
