#!/usr/bin/env python

#import sys

def make_chains(corpus):

    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    chain_dict = {}
    for i in range(len(corpus)-2):
        tup1 = corpus[i]
        tup2 = corpus[i+1]
        out_tuple = (tup1, tup2)
       # chain_dict[out_tuple] = corpus[i+2]
        if out_tuple not in chain_dict.keys():
            chain_dict[out_tuple] = [corpus[i+2]]
        else:
            chain_dict[out_tuple].append(corpus[i+2])
        i += 1
        print out_tuple
      

    return chain_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

def main():
 #   args = sys.argv

    # Change this to read input_text from a file
    f = open("short.txt")
    input_text = f.read()
    input_text = input_text.strip().split()
    #print input_text
    

    #input_text = "Some text"
    chain_dict = make_chains(input_text)
    print chain_dict
 #   random_text = make_text(chain_dict)
    #print random_text
    

if __name__ == "__main__":
    main()