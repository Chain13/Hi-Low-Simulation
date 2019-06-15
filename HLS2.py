import random
import numpy as np
import math
random.seed(300)


N_ROLL=100
DATA_SET=10
CHANCE=0.0002
ODD=0.95/CHANCE-1
MULTIPLE = 2
WL = np.array([[1 if random.random() <= CHANCE else -1 for i in range(N_ROLL)] for i in range(DATA_SET)])
BASE =1
MAX = 64
balance = np.array([0 for i in range(DATA_SET)])
current_bet = np.array([BASE for i in range(DATA_SET)])
round = 1

for j in range(N_ROLL):
    balance = balance + np.array([i*j if j == -1 else i*j*ODD for (i,j) in zip(current_bet,WL[:,j])])#current_bet * WL[:,j]
    current_bet = np.array([1 if WL[i, j] == 1 else 1 if current_bet[i] * MULTIPLE > MAX else current_bet[i] * MULTIPLE for i in range(DATA_SET)])
    print(balance)
print(f"max = {np.max(balance)} min = {np.min(balance)} std = {np.std(balance)} mean = {np.mean(balance)}")
