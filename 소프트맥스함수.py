import numpy as np

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

# 그러나 숫자 갑이 너무 크면 오버플로우가 발생함...
# 아래는 개선판

def softmax_fix(a):
    c = np.max(a)
    exp_a = np.exp(a - c)  # 오버플로우 대책
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

