import pdb
import ols
import math
import random
import numpy as np

T_COEF = 0
A_COEF = 0
CONST = 0

"""
Multi variable regregression
"""

def variables():
    """
    Create a variables array.
    Which works as a input to the regression method.
    """
    data_list = []

    # Read data from the file
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

        # Uncomment if the weight are to be calculated in percentages
        #weights = int(float(data_dict['value']['get']/total)*100)
        
        # Uncomment if the weight are to be calculated in percentages
        #invs = int(float(data_dict['value']['inv']/total_inv)*100)

        adv+=1
        timeperiod = __timeperiod(adv)
        print timeperiod, ':', adv, ':', hits
        if index ==0:
            x = np.array([[timeperiod, adv]], dtype=int)
            y = np.array([hits])
        else:
            x = np.append(x,[[timeperiod, adv]], axis=0)
            y = np.append(y,[hits])

    return x, y

def __timeperiod(adv):
    """
    Original expiry set from which the
    data was derived.
    """
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
    cachemodel = ols.ols(y,x,'Hit',['timeper','advance'])
    cachemodel.p
    cachemodel.summary()

# Hit percentage formula where co-efficents are to be determined
hit  = lambda timeperiod, adv : CONST+T_COEF*timeperiod + A_COEF*adv

def validate():
    # Check for the sample inputs
    sample = { 10: 20, 20: 30, 40: 40 }
    sample = { 50: 30 }
    
    for adv, timeperiod in sample.items():
        print hit(timeperiod, adv)

if __name__ == "__main__":
    regression()
    validate()
