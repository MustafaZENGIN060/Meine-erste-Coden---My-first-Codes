# -*- coding: utf-8 -*-
"""Fibonaccimz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ffxfs9LNm4_1kbZ8aI9xQyULwt5_VXrR
"""

liste=["1","1"]
n=1
toplam=["0"]
while int(liste[n])<58:
  liste.append(str(int(liste[n])+int(liste[n-1])))
  n=n+1
liste.pop()
print(liste)