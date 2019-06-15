import random
import numpy as np
import math
#random.seed(300)
n_rooll=100
data_set=20
WL = np.array([[random.choice([1,-1])  for i in range(n_rooll)] for i in range(data_set)])
BASE =1
MAX = 128
balance = np.array([0 for i in range(data_set)])
MULTIPLE = 2
current_bet = np.array([BASE for i in range(data_set)])
round = 1

for j in range(n_rooll):
    balance = balance + current_bet * WL[:,j]
    current_bet = np.array([1 if WL[i, j] == 1 else 1 if current_bet[i] * MULTIPLE > MAX else current_bet[i] * MULTIPLE for i in range(data_set)])
print(f"max = {np.max(balance)} min = {np.min(balance)} std = {np.std(balance)} mean = {np.mean(balance)}")