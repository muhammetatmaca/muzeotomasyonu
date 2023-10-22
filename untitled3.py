# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 13:16:38 2023

@author: muham
"""

import copy
liste1= [1,2,[3,4]]
liste2=copy.copy(liste1)
liste3=copy.deepcopy(liste1)
liste1[-1].append(5)