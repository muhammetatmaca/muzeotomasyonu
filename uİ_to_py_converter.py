# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 18:01:11 2023

@author: muham
"""

from PyQt5 import uic

with open('AnaSayfaUI.py', 'w', encoding="utf-8") as fout:
   uic.compileUi('AnaSayfa.ui', fout)