#!/usr/bin/env python

import sys
import random
chain_dict = {}
def make_chains(corpus):

    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    
    for i in range(len(corpus)-2):
        tup1 = corpus[i]
        tup2 = corpus[i+1]
        out_tuple = (tup1, tup2)
       # chain_dict[out_tuple] = corpus[i+2]
        if out_tuple not in chain_dict.keys():
            chain_dict[out_tuple] = [corpus[i+2]]
        else:
            chain_dict[out_tuple].append(corpus[i+2])
    
        #print out_tuple
      
    return chain_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    
    rand_key = random.choice(chains.keys())
    third_word = random.choice(chains[rand_key])
    #Create a new list to hold the string that we construc
    our_list = []
    our_list.append(rand_key[0])
    our_list.append(rand_key[1])
    our_list.append(third_word)
    
    while len(our_list) < 10:
      next_tup = (our_list[-2], our_list[-1])
      next_third_word = random.choice(chains[next_tup])
      
      our_list.append(our_list[-2])
      our_list.append(our_list[-2])
      our_list.append(next_third_word)
    
    return our_list

    # next_word = our_list([rand_key][1])
    # next_next_word = our_list[third_word]
    
    # tup3 = (next_word,next_next_word)
    # next_third_word = chains.get(tup3)
    
    # our_list.append(next_next_word)
    # our_list.append(next_third_word)
    
def read_txt(files):
    f = open(files)
    input_text = f.read()
    input_text = input_text.strip().split()
    chain_dict = make_chains(input_text)
    f.close()

    return chain_dict

def main():
   from sys import argv
   script, filename1, filename2 = argv

   
   #filename1 = raw_input("What is the first file? ")
   #filename2 = raw_input("What is the second file? ")
   
   read_txt(filename1)
   read_txt(filename2)

   random_text = make_text(chain_dict)
   string = " ".join(random_text)
   print string
    

if __name__ == "__main__":
    main()