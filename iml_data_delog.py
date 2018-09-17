import logging
import copy
# logging.disable(logging.CRITICAL)

import numpy as np
import csv
from decimal import Decimal

def read_demo():
    print("####### Reading Demo #######")
    paths = []
    for fi in range(1,8):

        f = open(('results_%d.csv')%fi)
        observations = []
        actions = []
        csv_f = csv.reader(f)
        joint_buff = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        o = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        a = [0.0,0.0,0.0,0.0]
        done = False
        t = 0
        for row in csv_f:
            if row[0] == 's':
                for k in range(4,7):
                    joint_buff[k] = float(row[k+1-4])
                continue
            if row[0] == 'j':
                for k in range(0,4):
                    if (k+1 == len(row)) or (row[k+1] == ''):
                        done = True
                        break
                    joint_buff[k] = float(row[k+1])
            if t == 0:
                o = copy.deepcopy(joint_buff)
                t += 1
                continue
            for i in range(len(a)):
                a[i] = joint_buff[i]
            observations.append(o)
            actions.append(a.copy())
            t += 1
            o = copy.deepcopy(joint_buff)
            if done == True:
                break
        print(('results_%d.csv read')%fi)
        path = dict(observations=np.array(observations),actions=np.array(actions))
        paths.append(path)

    return paths

if __name__ == '__main__':
    paths = read_demo()
    for path in paths:
        for i in range(len(path["observations"])):
            print("Time :", i)
            print("state is :", path["observations"][i])
            print("action is :", path["actions"][i])
            print("---------------------------------------------")
            c = input()
