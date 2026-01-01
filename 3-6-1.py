import sys, os

curr_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curr_dir)
from dataset.mnist import load_mnist

# 데이터 읽기
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)