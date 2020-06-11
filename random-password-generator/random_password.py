#!/usr/bin/env python3

#Random password generator
import random

#define a lambda function which return random number ASCII Number with given range and convert it into character
rand_char = lambda start, stop: chr(random.randint(start, stop))

#initalizing variables of different ASCII char ranges
digits = rand_char(48,57)

#for punctuations we need differenct ranges of ASCII characters
#create a list of various puctuations to get more varities of punctuations and choose one among them
p = lambda st, sp : list(range(st,sp))
punc_ascii_num = p(33,47) + p(58, 64) + p(93, 96) + p(123,126)

#creating list of 8 ASCII characters of various categories
pass_list = [
             rand_char(65,90), rand_char(65,90),
             rand_char(97,122),rand_char(97,122),
             rand_char(48,57), rand_char(48,57),
             chr(random.choice(punc_ascii_num)), chr(random.choice(punc_ascii_num))
            ]

random.shuffle(pass_list) # randomly shuffle the pass_list 
password  = ''.join(pass_list) #join the elements of pass_list into password string
print("Your Randomly Generated Password is: {}".format(password))
