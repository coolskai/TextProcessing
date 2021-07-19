import numpy as np
from time import time

def basic_test():
    #1~1000000까지 더하기 - 일반 리스트 사용
    a_list = list(range(1, 1_000_001))
    print('sum : ', sum(a_list))

    #1~1000000까지 더하기 - numpy 사용
    a_np = np.arange(1, 1_000_001, dtype=np.int64)
    print('sum : ', sum(a_np))

def func_array_test():
    data = [1,2,3,4]
    a = np.array(data)
    print(a)
    a = np.array([1,2,3,4])
    print(a)
    a = np.array([[1,2],[3,4]])
    print(a)
    a = np.array([[1,2],[3,4,5]]) #list object 2개를 갖는 1차원 배열
    print(a)

def basic_func_test():
    print(np.array([[1,2],[3,4]]))
    print(np.arange(1,11))
    print(np.linspace(0, 1, num=10))
    print(np.empty((3,3), dtype='float32'))
    print(np.eye(6, dtype='float32'))
    print(np.zeros(3, dtype='float32'))
    print(np.zeros((3,3), dtype='float32'))
    print(np.zeros((3,3,3), dtype='float32'))
    print(np.ones((3,3), dtype='float32'))
    print(np.full((3,3), 0.5))
    a = np.zeros(3)
    b = np.copy(a)
    b[1] = 2
    print(a)
    print(b)
    print(np.fromfunction(lambda i, j : i+j, (2,3), dtype='int'))
    print(np.fromfunction(lambda i, j : (i+1)*(j+1), (10,10), dtype='int'))

def op_test(npr):
    print(npr * 5)
    print(npr / 5)
    print(npr ** 5)
    print(npr // 5)
    print(npr + npr)
    print(npr * npr)
    print(npr ** npr)

def slicing_test(npr):
    print(npr[0:3])
    npr[0:3] = 100
    print(npr)
    npr[3:11] += 10
    print(npr)

if __name__ == '__main__':
    a = np.arange(1,10)
    print(a)
    slicing_test(a)
    print(a)
    op_test(a)