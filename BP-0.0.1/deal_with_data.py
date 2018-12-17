import scipy.io as sio
import numpy as np


train_img = sio.loadmat('mnist_train.mat')
train_img = train_img['mnist_train']

train_label = sio.loadmat('mnist_train_labels.mat')
train_label = train_label['mnist_train_labels']

test_img = sio.loadmat('mnist_test.mat')
test_img = test_img['mnist_test']

test_label = sio.loadmat('mnist_test_labels.mat')
test_label = test_label['mnist_test_labels']

train_size = len(train_img)
print(train_size)

test_size = len(test_img)
print(test_size)

# for i in range(0, train_size):
#     for j in range(0, 784):
#         if train_img[i, j] > 0:
#             train_img[i, j] = 1
# np.savetxt("a.txt", train_img, fmt="%d", delimiter=",") #改为保存为整数，以逗号分隔
# print(train_img[0])
# print(train_label[0])

for i in range(0, test_size):
    for j in range(0, 784):
        if test_img[i, j] > 0:
            test_img[i, j] = 1
np.savetxt("b.txt", test_img, fmt="%d", delimiter=",") #改为保存为整数，以逗号分隔