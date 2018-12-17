# 自行训练
# 回来加一个保存训练样本的功能
import numpy as np
import scipy.io as sio
import math
import pygame.font, pygame.event, pygame.draw
import matplotlib.pyplot as plt


def sigmod_function(vec):
	sig_vec = []
	for i in vec:
		sig_vec.append(1/(1+math.exp(-i)))
	sig_vec = np.array(sig_vec)
	return sig_vec

def main():
    global my_own_train_img
    global my_own_train_label
    my_own_train_img = []
    my_own_train_label = []
    print("trainning bp network")
    trainBPNetwork()
    #visualize_test()
    
    
    global screen
    pygame.init()
    screen = pygame.display.set_mode((112, 112))
    
    background = pygame.Surface((112,112))
    background.fill((0, 0, 0))
 
    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (255, 255, 255)
    lineWidth = 4

    pygame.display.update()
    image = None

    
    
            
    while keepGoing:
        
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEMOTION:
                lineEnd = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.line(background, drawColor, lineStart, lineEnd, lineWidth)
                lineStart = lineEnd
            elif event.type == pygame.MOUSEBUTTONUP:
                # 用28，28可以比较准确 因为获得的像素图比较准确
                # sb scale也丢了太多点了吧....
                # using warping
                #scaledBackground = pygame.transform.scale(background, (28, 28))
                arr = pygame.surfarray.array3d(background)
                #print(arr)
                #下面来一个scale
                arr = scale(arr, 112, 112, 28, 28)
                ##########################################################
                #print(arr)
                white_block = [255, 255, 255]
                count = 0
                test_img = []
                for i in range(0, 28):
                    for j in range(0, 28):
                        
                        if arr[j,i, 0] > 0 or arr[j,i,1] > 0 or arr[j,i,2] > 0:  # 块是白色的
                            count+=1
                            test_img.append(int(1))
                        else:
                            test_img.append(int(0))
                  
                print(test_img)
                predict(test_img)
                
            elif event.type == pygame.KEYDOWN:
                # 按一下c清除画板
                if event.key == pygame.K_c:
                    background.fill((0, 0, 0))
                elif event.key == pygame.K_1:
                    print(test_img)
                    my_own_train_img.append(test_img)
                    my_own_train_label.append(1)  
                    train(test_img, 1)
                
                elif event.key == pygame.K_2:
                    print(test_img)
                    my_own_train_img.append(test_img)
                    my_own_train_label.append(2)  
                    train(test_img, 2)
                
                elif event.key == pygame.K_3:
                    print(test_img)
                    my_own_train_img.append(test_img)
                    my_own_train_label.append(3)  
                    train(test_img, 3)
                
                elif event.key == pygame.K_4:
                    print(test_img)
                    my_own_train_img.append(test_img)
                    my_own_train_label.append(4)  
                    train(test_img, 4)
                
                elif event.key == pygame.K_5:
                    print(test_img)
                    my_own_train_img.append(test_img)
                    my_own_train_label.append(5)  
                    train(test_img, 5)

                elif event.key == pygame.K_6:
                    print(test_img)
                    my_own_train_img.append(test_img)
                    my_own_train_label.append(6)  
                    train(test_img, 6)

                elif event.key == pygame.K_7:
                    print(test_img)
                    my_own_train_img.append(test_img)
                    my_own_train_label.append(7)  
                    train(test_img, 7)

                elif event.key == pygame.K_8:
                    print(test_img)
                    my_own_train_img.append(test_img)
                    my_own_train_label.append(8)  
                    train(test_img, 8)
                elif event.key == pygame.K_9:
                    print(test_img)
                    my_own_train_img.append(test_img)
                    my_own_train_label.append(9)  
                    train(test_img, 9)

                elif event.key == pygame.K_0:
                    print(test_img)
                    my_own_train_img.append(test_img)
                    my_own_train_label.append(0)  
                    train(test_img, 0)
                
                
                
                
                
                
                    

        screen.blit(background, (0, 0))
        pygame.display.flip()
        

# 数据读入与处理
def trainBPNetwork():
    # train_img = sio.loadmat('mnist_train.mat')
    # train_img = train_img['mnist_train']
    
    # 读入特制的二维数据集a.txt(训练集) orz
    train_img = np.empty([892,784])
    row = 0
    for line in open("my_own_train_img.txt"):
        train_img[row] = np.fromstring(line, sep=",")
        row += 1
    train_label = []

    row = 0
    
    for line in open("my_own_train_label.txt"):
        train_label.append(int(np.fromstring(line, sep=",")[0]))
        #train_label[row] = np.fromstring(line, sep=",")
        #train_label[row] = train_label[row][0]
        
        row += 1
    # train_label.astype(int)
    train_label = np.array(train_label)
    train_label.astype(int)
    train_label.reshape(892,1)
    print(train_label)


    #train_label = sio.loadmat('mnist_train_labels.mat')
    #train_label = train_label['mnist_train_labels']

    # test_img = sio.loadmat('mnist_test.mat')
    # test_img = test_img['mnist_test']

    # 读入特制的二维数据集b.txt(测试集)
    # global test_img
    # test_img = np.empty([10000,784])
    # row = 0
    # for line in open("b.txt"):
    #     test_img[row] = np.fromstring(line, sep=",")
    #     row += 1
    # global test_label
    # test_label = sio.loadmat('mnist_test_labels.mat')
    # test_label = test_label['mnist_test_labels']

    # 特制的数据集都是0和1就不除了
    # train_img = train_img / 255.0
    # test_img = test_img / 255.0

    train_size = len(train_img)
    global input_size
    global output_size
    global hid_size
    input_size = len(train_img[0])
    output_size = 10
    hid_size = 15
    global learning_rate_1
    global learning_rate_2
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
    # right_recog = np.zeros(10)
    # number_statis = np.zeros(10)
    # for kk in test_img[0]:
    #     print(kk)
    # #print(test_img[0])
    # print(test_label[0])
    # for i in range(0, len(test_img)):
    #     number_statis[test_label[i]]+=1
    #     test_hid_vec = np.dot(test_img[i], w1) + b1
    #     test_hid_vec = sigmod_function(test_hid_vec)
    #     test_out_vec = np.dot(test_hid_vec, w2) + b2
    #     test_out_vec = sigmod_function(test_out_vec)
        
    #     # 找出最大的那个
    #     if np.argmax(test_out_vec) == test_label[i]:
    #         right_recog[test_label[i]]+=1

    # print (right_recog)
    # print (number_statis)
    # print (right_recog/number_statis)
    # sum = right_recog.sum()
    # print (sum/len(test_img))
   
   
def predict(arr):
    test_hid_vec = np.dot(arr, w1) + b1
    test_hid_vec = sigmod_function(test_hid_vec)
    test_out_vec = np.dot(test_hid_vec, w2) + b2
    test_out_vec = sigmod_function(test_out_vec)
        
    # 找出最大的那个
    print("predict:\n")
    print(np.argmax(test_out_vec))

def train(img_test, num):
   
    global b1
    global b2
    img_test = np.array(img_test)
    
    hid_vec = np.dot(img_test, w1) + b1
    #print(len(hid_vec))
    hid_vec = sigmod_function(hid_vec)
        #print(len(hid_vec))
        #print(hid_vec)
        
        # 隐藏层 -> 输出层
    out_vec = np.dot(hid_vec, w2)+b2
    out_vec = sigmod_function(out_vec)
        #print(len(out_vec))
        
        # 计算误差
    expected_vec = np.zeros(output_size)
    expected_vec[num] = 1.0
    err = expected_vec - out_vec
     
        # 根据误差反向回去更新权值和bias值
    tmp = np.dot(w2, err)
    tmp2 = hid_vec * (1 - hid_vec) * tmp
        
        # 矩阵
        # 隐含层 -> 输出层
    for j in range(0, output_size):
        w2[:,j] += learning_rate_2 * err[j] * hid_vec
        
        # 输出层 -> 隐含层
    for j in range(0, output_size):
        w1[:,j] += learning_rate_1 * tmp2[j] * img_test
      
        # bias
        # 隐含层 -> 输出层
    b2 = b2 + learning_rate_2 * err

        # 输出层 -> 隐含层
    b1 = b1 + learning_rate_1 * hid_vec * (1-hid_vec) * tmp
 
def scale(arr, origin_width, origin_height, output_width, output_height):
    x1 = 0
    y1 = 0

    x2 = 0
    y2 = origin_height-1

    x3 = origin_width-1
    y3 = 0

    x4 = origin_width-1
    y4 = origin_height-1

    u1 = 0
    v1 = 0

    u2 = 0
    v2 = output_height-1

    u3 = output_width-1
    v3 = 0

    u4 = output_width-1
    v4 = output_height-1

    b_vec = np.array([u1, v1, u2, v2, u3, v3, u4, v4])
    b_vec = b_vec.T # 记得转置
    A = np.array([[x1, y1, 1, 0, 0, 0, -u1*x1, -u1*y1],\
    [0,0,0, x1, y1, 1, -v1*x1, -v1*y1],\
    [x2, y2, 1, 0, 0, 0, -u2*x2, -u2*y2],\
    [0,0,0, x2, y2, 1, -v2*x2, -v2*y2],\
    [x3, y3, 1, 0, 0, 0, -u3*x3, -u3*y3],\
    [0,0,0, x3, y3, 1, -v3*x3, -v3*y3],\
    [x4, y4, 1, 0, 0, 0, -u4*x4, -u4*y4],\
    [0,0,0, x4, y4, 1, -v4*x4, -v4*y4]])

    x = np.linalg.solve(A, b_vec)
    global aaa, bbb, ccc, ddd, eee, fff, mmm, lll
    aaa = x[0]
    bbb = x[1]
    ccc = x[2]
    ddd = x[3]
    eee = x[4]
    fff = x[5]
    mmm = x[6]
    lll = x[7]

    #print(arr)

    print(x)
    print(x[0])
    print(x[1])
    print(x[2])
    print(x[3])
    print(x[4])
    print(x[5])
    print(x[6])
    print(x[7])

    scaled_img = np.zeros(output_height * output_width * 3)
    scaled_img = scaled_img.reshape(output_height, output_width, 3)

    for r in range(0, output_height-1):
        for c in range(0, output_width-1):
            r_ori = getRow(c, r)
            #print(r_ori)
            
            c_ori = getCol(c, r)
            scaled_img[r, c, 0] = biliner(arr, r_ori, c_ori, 0)
            scaled_img[r, c, 1] = biliner(arr, r_ori, c_ori, 1)
            scaled_img[r, c, 2] = biliner(arr, r_ori, c_ori, 2)

            #print(c_ori)
            #scaled_img[r, c] = arr[r_ori, c_ori]


    return scaled_img
def biliner(arr, r_ori, c_ori, channel_no):
    r = int(r_ori)
    c = int(c_ori)

    delta_a = c_ori - c
    delta_b = r_ori - r

    
    result = (1-delta_a) * (1-delta_b) * arr[r, c, channel_no] + delta_a * (1-delta_b) * arr[r+1, c, channel_no] + (1-delta_a) * delta_b * arr[r, c+1, channel_no] + delta_a * delta_b * arr[r+1, c+1, channel_no]
    return result

def getCol(u, v):
    result = ((ccc-u)*(v*lll-eee) - (fff-v)*(u*lll-bbb))/((u*mmm-aaa)*(v*lll-eee)-(v*mmm-ddd)*(u*lll-bbb)) 
    #print(result)
    return result

def getRow(u, v):
    result = ((ccc-u)*(v*mmm-ddd) - (fff-v)*(u*mmm-aaa))/((u*lll-bbb)*(v*mmm-ddd)-(v*lll-eee)*(u*mmm-aaa)) 
    #print(result)
    return result


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
    np.savetxt("my_own_train_img2.txt", my_own_train_img, fmt="%d", delimiter=",") #改为保存为整数，以逗号分隔
    np.savetxt("my_own_train_label2.txt", my_own_train_label, fmt="%d", delimiter=",") #改为保存为整数，以逗号分隔















