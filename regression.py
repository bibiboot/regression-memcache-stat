import pdb
import ols
import math
import random
import numpy as np

"""
Single variable regression co-efficent is determined
"""

def variables():
    """
    Create a variables array
    """
    data_list = []

    with open('test.txt','r') as f:
        data_list = eval(f.readlines()[0])

    total = sum([int(data_dict['value']['get']) for data_dict in data_list[:100]])
    total_inv = sum([int(data_dict['value']['inv']) for data_dict in data_list[:100]])

    for index, data_dict in enumerate(data_list[:50]):
        adv = int(data_dict['_id']['advanceperiod'])
        hits = int(data_dict['value']['hit'])
        fail = int(data_dict['value']['fail_set'])
        weights = int(data_dict['value']['get'])
        invs = int(data_dict['value']['inv'])
        #weights = int(float(data_dict['value']['get']/total)*100)
        #invs = int(float(data_dict['value']['inv']/total_inv)*100)
        #pdb.set_trace()
        adv+=1
        timeperiod = __timeperiod(adv)
        if index ==0:
            x = np.array([[adv]], dtype=int)
            y = np.array([hits])
        else:
            x = np.append(x,[[adv]], axis=0)
            y = np.append(y,[hits])

    return x, y

def __timeperiod(adv):
    if adv > 50:
        return 30
    elif adv > 20:
        return 12
    elif adv > 10:
        return 15
    elif adv > 2:
        return 5
    else:
        return 0.5

def regression():
    """
    Multiple varibale regression takes place
    """
    x, y = variables()
    print y
    print x
    cachemodel = ols.ols(y,x,'Hit',['advanceperiod'])
    print cachemodel.p
    cachemodel.summary()

if __name__ == "__main__":
    regression()
