# 가중치에서 편향을 도입해보기

import numpy as np
x = np.array([0, 1]) # 입력
w = np.array([0.5, 0.5]) # 가중치
b = -0.7 # 편향
w*x
np.sum(w*x)
np.sum(w&x) + b
