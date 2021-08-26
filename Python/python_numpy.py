# -*- coding: utf-8 -*-
import numpy as np
# ndarr = np.array([3,-4,5])
# print(ndarr)

# data1 = np.array([1,3,4,55])
# data1 = np.ones(3);data1 = zeros(3)
# data1 = np.empty(3);data1 = np.arange(5)

# data2 = np.array([[2,3],[3,3],[3,2]])
# data2 = np.empty([3,3]);data2 = np.ones([3,4])
# data3 = np.array([
#     [
#         [2,5,7],[1,5,33]
#     ],[
#         [3,4,5],[7,1,3]
#     ]
# ])
# data4 = np.zeros([1,2,3,4,5])

# 一維運算
# data1 = np.array([3,1,4])
# data2 = np.array([6,2,7])
# data = data1 == data2

# 二維運算
data0 = np.array([1,4,6,8,2])
data1 = np.array([[2,3,4],[5,4,2]])
data2 = np.array([[1,3],[6,3],[7,-1]])
# data = data1@data2; data = data1.dot(data2) # dot product
# data = np.outer(data1,data2) # outer product
# data = data1.sum();data = data1.sum(axis=1);data =data1.min()
# data = data1.cumsum();data =data1.mean();data=data1.std()
# data = data1.mean(axis=1)
# data = data1.shape
# data = data1.T
# data = data.ravel()
# data = data.reshape([2,3])
# data = np.zeros(18).reshape(3,3,2)
# data = data2[2,0]

# slice
# data = data0[1:]
# data = data2[:2][:]
# data = data2[1:,...]

# stack
# data = np.vstack((data0,[3,4,5,3,4],[1,-2,3,-2,1]))   # 一維
# data = np.hstack((data0,[1,2,3]))                     # 二維

# split
# data = np.hsplit(data0,5)   # 二維
# data = np.vsplit(data2,3)   # 一維

# print(data)