# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 18:20:47 2016

@author: chiennb

Simple code for homework 1

Description: Alice hates doing Math. Alice loves hunting Drag. 

Alice khong biet lam gi nen di san rong (_ _!). Ranh hon chi Alice con lap bang

danh so rong: theo muc do ban khoe X = [1, 2, 3, 4] va het to Y = [1, 2, 3].

Chi gai phat hien ra rang ty le rong tuan theo qui luat f(x, y) = x^2 + y^2 neu

{x,y} ={[1,2,4], [1,3]}. Truong hop con lai: f(x,y) = 0.

Chi ranh qua ha.

"""
import numpy as np

drag_X = [1, 2, 3, 4]
drag_Y = [1, 2, 3]

X_mapping = {label: index for index, label in enumerate(drag_X)} # axis 0
Y_mapping = {label: index for index, label in enumerate(drag_Y)} # axis 1

joint_table = np.zeros((4,3))
joint_prob_table = np.zeros((4,3))

##### Build Table ###############################################
for x in drag_X:
   for y in drag_Y:
       if x == 3 or y == 2:
           joint_table[X_mapping[x], Y_mapping[y]] = 0
       else:
           joint_table[X_mapping[x], Y_mapping[y]] = x**2 + y**2
           
##### Bulid probability table #####################################
for x in drag_X:
   for y in drag_Y:
       joint_prob_table[X_mapping[x], Y_mapping[y]] = joint_table[X_mapping[x], 
                        Y_mapping[y]]/np.sum(joint_table)           

##### Print probability results ##################################
prob_x = dict(zip(drag_X, np.sum(joint_prob_table, axis=1)))
prob_y = dict(zip(drag_Y, np.sum(joint_prob_table, axis=0)))
                    
        












































    