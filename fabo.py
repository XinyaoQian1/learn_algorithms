"""
# @File    :    fabo.py
# @Time    :    13/10/2022 19:43
# @Author  :    Xinyao Qian
# @SN      :    19021373
# @Description: 
"""



import numpy as np
import math
def fabo():

    helper = math.sqrt(5)
    n = 0
    result =0
    while result <= 3.4028235e+200:
        result = ((((1+helper)/2)**n - ((1-helper)/2)**n)/helper)
        print(n)
        n+=1

def fabo2(n):
    helper = math.sqrt(5)
    result = np.float16((((1 + helper) / 2) ** n - ((1 - helper) / 2) ** n) / helper)
    print(n)
    print(result)


print(np.finfo(np.float32))

fabo2(1475)


