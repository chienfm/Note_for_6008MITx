# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 00:29:23 2016

@author: Chiennv

Description: Simulate the probability of tossing a coin.

Alice has five coins in a bag: two coins are normal, two are double-headed, 
and the last one is double-tailed. She reaches into the bag and randomly 
pulls out a coin. Without looking at the coin she drew, she tosses it.

"""
import random
import numpy as np

coin_faces = {"HH": {1:"H", 2:"H"}, "HH":{1:"H", 2:"H"}, "TT" :{1: "T", 2:"T"}, 
         "HT": {1: "H",2:"T"}, "HT":{1: "H",2:"T"}}

coins = ["HH", "HH", "HT", "HT", "TT"]

#### Questtion a #########################################################
"""
(a) What is the probability that once the coin lands, the side of the coin that
is face-down is heads? (Please be precise with at least 3 decimal places, 
unless of course the answer doesn't need that many decimal places. You could 
also put a fraction.)

"""
def question_a(n):
    count = 0
    list_faces = []
    for i in range(n):
        coin = random.choice(coins)
        list_faces.append(coin_faces[coin][random.choice([1, 2])])
    for face in list_faces:
        if face == "H":
            count += 1
    print(count/len(list_faces))

### Question b ###########################################################
"""
(b) The coin lands and shows heads face-up. What is the probability that 
the face-down side is heads? (Please be precise with at least 3 decimal places,
unless of course the answer doesn't need that many decimal places. You could 
also put a fraction.)
"""
    
def question_b(n):
    count = 0
    list_faces = []
    for i in range(n):
        coin = random.choice(coins)
        key = random.choice([1, 2])
        if coin_faces[coin][key] == "H":
            if key == 1:
                list_faces.append(coin_faces[coin][2])
            else:
                list_faces.append(coin_faces[coin][1])
    for face in list_faces:
        if face == "H":
            count += 1
    print(count/len(list_faces))
    
            
#### Question c #########################################################

def question_c(n):
    count = 0
    list_faces = []
    
    for i in range(n):
        list_coins = list(coins)
        coin = random.choice(coins)
        key = random.choice([1, 2])
        if coin_faces[coin][key] == "H":
            list_coins.remove(coin)
            coin = random.choice(list_coins)
            list_faces.append(coin_faces[coin][random.choice([1, 2])])
        
    for face in list_faces:
        if face == "H":
            count += 1
    print(count/len(list_faces))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            