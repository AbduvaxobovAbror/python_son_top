# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 11:15:20 2026

@author: Abror
"""

import  random

def sontop(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan  {x} gacha son o'yladm, Topa olasizmi?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:")
        elif taxmin>tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling:")
        else:
            break
    print(f"tabriklaymiz. {taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar

def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang keyin istalgan tugmani bosing. Men esa sizni topaman!")
    quyi = 1
    yuqori = x
    taxminlar =0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f" Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar

def play(x=10):
    yana = True
    while yana:
        t = sontop(x)
        a = sontop_pc(x)
        if t>a:
            print("men yutdim")
        elif t<a:
            print("siz yutdingiz")
        else:
            print("durrang")
            
        yana =int(input("yana o'ynayszmi? ha(1)/yo'q(0):"))
        

        
               
        
                                    
    
   

