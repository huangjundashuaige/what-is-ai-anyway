import numpy as np
# 验证过啦
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
    global a, b, c, d, e, f, m, l
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    e = x[4]
    f = x[5]
    m = x[6]
    l = x[7]

    print(x)
    print(x[0])
    print(x[1])
    print(x[2])
    print(x[3])
    print(x[4])
    print(x[5])
    print(x[6])
    print(x[7])

    scaled_img = np.empty([output_height,output_width])

    for r in range(0, output_height):
        for c in range(0, output_width):
            r_ori = getRow(c, r)
            c_ori = getCol(c, r)
            scaled_img[r, c] = arr[r_ori, c_ori]
    
def getRow(u, v):
    return int((c-u)*(v*l-e) - (f-v)*(u*l-b))/((u*m-a)*(v*l-e)-(v*m-d)*(u*l-b))

def getCol(u, v):
    return int((c-u)*(v*m-d) - (f-v)*(u*m-a))/((u*l-b)*(v*m-d)-(v*l-e)*(u*m-a))

scale([], 56, 56, 28, 28)