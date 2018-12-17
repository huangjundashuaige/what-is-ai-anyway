import numpy as np
import scipy.io as sio
import math
import matplotlib.pyplot as plt


def sigmod_function(vec):
	sig_vec = []
	for i in vec:
		sig_vec.append(1/(1+math.exp(-i)))
	sig_vec = np.array(sig_vec)
	return sig_vec

def main():
    print("trainning bp network...")
    trainBPNetwork()
    visualize_test()

# 数据读入与处理
def trainBPNetwork():
    global train_img
    # 读取mat
    train_img = sio.loadmat('mnist_train.mat')
    train_img = train_img['mnist_train']

    # 读取txt
    # train_img = np.empty([60000,784])
    # row = 0
    # for line in open("a.txt"):
    #     train_img[row] = np.fromstring(line, sep=",")
    #     row += 1
    #train_img = np.loadtxt("a.txt",delimiter=",")

    global train_label
    train_label = sio.loadmat('mnist_train_labels.mat')
    train_label = train_label['mnist_train_labels']

    global test_img
    # 读取mat
    test_img = sio.loadmat('mnist_test.mat')
    test_img = test_img['mnist_test']

    # 读取txt
    # test_img = np.empty([10000,784])
    # row = 0
    # for line in open("b.txt"):
    #     test_img[row] = np.fromstring(line, sep=",")
    #     row += 1
    global test_label
    test_label = sio.loadmat('mnist_test_labels.mat')
    test_label = test_label['mnist_test_labels']

    # normalize 0-1
    train_img = train_img / 255.0
    test_img = test_img / 255.0

    global train_size
    global input_size
    global output_size
    train_size = len(train_img)
    input_size = len(train_img[0])
    output_size = 10
    hid_size = 15
    learning_rate_1 = 0.2   # 输入层->隐藏层学习率
    learning_rate_2 = 0.2   # 隐藏层->输出层学习率

    global w1
    global w2
    global b1
    global b2

    # 输入层-》隐藏层 
    # 权值矩阵初始化
    w1 = np.random.randn(input_size, hid_size)
    # bias初始化
    b1 = np.random.randn(hid_size)

    # 隐藏层 -》输出层 
    # 权值矩阵初始化
    w2 = np.random.randn(hid_size, output_size)
    # bias初始化
    b2 = np.random.randn(output_size)


    # 开始训练神经网络
    for i in range(0, train_size):
        hid_vec = np.dot(train_img[i], w1) + b1
        #print(len(hid_vec))
        hid_vec = sigmod_function(hid_vec)
        #print(len(hid_vec))
        #print(hid_vec)
        
        # 隐藏层 -> 输出层
        out_vec = np.dot(hid_vec, w2) + b2
        out_vec = sigmod_function(out_vec)
        #print(len(out_vec))
        
        # 计算误差
        expected_vec = np.zeros(output_size)
        expected_vec[train_label[i]] = 1.0
        err = expected_vec - out_vec
       
        # 根据误差反向回去更新权值和bias值
        # 梯度法
        # https://blog.csdn.net/zhaoyuxia517/article/details/78116683
        tmp = np.dot(w2, err)
        tmp2 = hid_vec * (1 - hid_vec) * tmp
        
        # 矩阵
        # 隐含层 -> 输出层
        for j in range(0, output_size):
            w2[:,j] += learning_rate_2 * err[j] * hid_vec
        
        # 输出层 -> 隐含层
        for j in range(0, output_size):
            w1[:,j] += learning_rate_1 * tmp2[j] * train_img[i] 
        
        # bias
        # 隐含层 -> 输出层
        b2 = b2 + learning_rate_2 * err

        # 输出层 -> 隐含层
        b1 = b1 + learning_rate_1 * hid_vec * (1-hid_vec) * tmp
        
    # 测试
    right_recog = np.zeros(10)
    number_statis = np.zeros(10)
    for kk in test_img[0]:
        print(kk)

    print(test_label[0])
    for i in range(0, len(test_img)):
        number_statis[test_label[i]]+=1
        test_hid_vec = np.dot(test_img[i], w1) + b1
        test_hid_vec = sigmod_function(test_hid_vec)
        test_out_vec = np.dot(test_hid_vec, w2) + b2
        test_out_vec = sigmod_function(test_out_vec)
        
        # 找出最大的那个
        if np.argmax(test_out_vec) == test_label[i]:
            right_recog[test_label[i]]+=1

    print (right_recog)
    print (number_statis)
    print (right_recog/number_statis)
    sum = right_recog.sum()
    print (sum/len(test_img))

def predict(arr):
    test_hid_vec = np.dot(arr, w1) + b1
    test_hid_vec = sigmod_function(test_hid_vec)
    test_out_vec = np.dot(test_hid_vec, w2) + b2
    test_out_vec = sigmod_function(test_out_vec)
        
    # 找出最大的那个
    print("predict:\n")
    print(np.argmax(test_out_vec))
    
def visualize_test():
    # 展示的个数
    show_size = 15
    a = np.random.randint(1,9999,show_size)
    for i in a:
        # 运用神经网络进行预测
        test_hid_vec = np.dot(test_img[i], w1) + b1
        test_hid_vec = sigmod_function(test_hid_vec)
        test_out_vec = np.dot(test_hid_vec, w2) + b2
        test_out_vec = sigmod_function(test_out_vec)
        
        # 找出最大的那个
        print("predict:\n")
        predict_num = np.argmax(test_out_vec)
        print(predict_num)
        #print(test_img[i])
        two_d = (np.reshape(test_img[i], (28, 28)) * 255).astype(np.uint8)
        plt.title('Expected: {0}  Predicted: {1}'.format(test_label[i][0],predict_num))
        plt.imshow(two_d, interpolation='nearest',cmap='gray')
        plt.show()
    
            
if __name__ == "__main__":
    main()














