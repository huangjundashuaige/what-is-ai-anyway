import pygame.font, pygame.event, pygame.draw
import numpy as np
def main():
    """Main method. Draw interface"""
    
    global screen
    pygame.init()
    screen = pygame.display.set_mode((730, 280))
    pygame.display.set_caption("Handwriting recognition")
    
    background = pygame.Surface((280,280))
    background.fill((0, 0, 0))
    background2 = pygame.Surface((360,360))
    background2.fill((255, 255, 255))
    
    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (255, 255, 255)
    lineWidth = 15
    
    # inputTheta = sio.loadmat('scaledTheta.mat')
    # theta = inputTheta['t']
    # num_hidden = 25
    # num_input = 900
    # num_lables = 10

    # Theta1 = np.reshape(theta[:num_hidden*(num_input+1)], (num_hidden,-1))
    # Theta2 = np.reshape(theta[num_hidden*(num_input+1):], (num_lables,-1))

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
                screen.fill((0, 0, 0))
                screen.blit(background2, (370, 0))
                focusSurface = pygame.surfarray.array3d(background)
                # print(focusSurface)
                # print(len(focusSurface))
                # print(len(focusSurface[0]))
                # print(focusSurface[0][0])
                
                scaledBackground = pygame.transform.scale(background, (28, 28))
                arr = pygame.surfarray.array3d(scaledBackground)
                white_block = [255, 255, 255]
                count = 0
                test_img = []
                for i in range(0, 28):
                    for j in range(0, 28):
                        
                        if arr[i,j, 0] == 255:  # 块是白色的
                            count+=1
                            test_img.append(1)
                        else:
                            test_img.append(0)
                            
                print(test_img)
                # 构建一个一维 784 数组 用于待会传入
                # image = pygame.surfarray.array3d(scaledBackground)
                # image = abs(1-image/255)
                # image = np.mean(image, 2) 
                # image = np.matrix(image.ravel())
                # print(arr)
                print(len(test_img))
                # print(count)
               # print(pygame.transform.scale(focusSurface, (28, 28), DestSurface = None))
                #w = threading.Thread(name='worker', target=worker)
                # 在这里把我的神经网络加在这里
                #image = calculateImage(background, screen, Theta1, Theta2, lineWidth)

            elif event.type == pygame.KEYDOWN:
                myData = (event, background, drawColor, lineWidth, keepGoing, screen, image)
                #myData = checkKeys(myData)
                (event, background, drawColor, lineWidth, keepGoing) = myData
        
        
        screen.blit(background, (0, 0))
        pygame.display.flip()
        

def calculateImage(background, screen, Theta1, Theta2, lineWidth):
    """Crop and resize the input"""
    
    global changed
    focusSurface = pygame.surfarray.array3d(background)
    focus = abs(1-focusSurface/255)
    focus = np.mean(focus, 2) 
    x = []
    xaxis = np.sum(focus, axis=1)
    for i, v in enumerate(xaxis):
        if v > 0:
            x.append(i)
            break
    for i, v in enumerate(xaxis[ : :-1]):
        if v > 0:
            x.append(len(xaxis)-i)
            break
    
    y = []
    yaxis = np.sum(focus, axis=0)
    for i, v in enumerate(yaxis):
        if v > 0:
            y.append(i)
            break
    for i, v in enumerate(yaxis[ : :-1]):
        if v > 0:
            y.append(len(yaxis)-i)
            break

    try:
        dx = x[1]-x[0]
        dy = y[1]-y[0]
        bound = focus.shape[0]      
        if dx > dy:
            d = dx-dy
            y0t = y[0] - d//2
            y1t = y[1] + d//2+d%2
            if y0t < 0: y0t = y[0]; y1t = y[1] + d
            if y1t > bound: y0t = y[0] - d; y1t = y[1]
            y[0], y[1] = y0t, y1t
        else:
            d = dy-dx
            x0t = x[0] - d//2
            x1t = x[1] + d//2+d%2
            if x0t < 0: x0t = x[0]; x1t = x[1] + d
            if x1t > bound: x0t = x[0] - d; x1t = x[1]
            x[0], x[1] = x0t, x1t 
        dx = x[1]-x[0]
        dy = y[1]-y[0]
        changed = True
        crop_surf =  pygame.Surface((dx,dy))
        crop_surf.blit(background,(0,0),(x[0],y[0],x[1],y[1]), special_flags=BLEND_RGBA_MAX)
        scaledBackground = pygame.transform.smoothscale(crop_surf, (30, 30))
            
        image = pygame.surfarray.array3d(scaledBackground)
        image = abs(1-image/253)
        image = np.mean(image, 2) 
        image = np.matrix(image.ravel())
        drawPixelated(image, screen)
        (value, prob), (value2, prob2) = probabilty(Theta1,Theta2,image)
        prob = round(prob,1)
        prob2 = round(prob2, 1)
                   
        myLabel = showStats(lineWidth, value, prob)
        myLabelSmall = showStatsSmall(lineWidth, value2, prob2)
        (x,y) = screen.get_size()
        screen.blit(myLabel, (17, y-90))
        screen.blit(myLabelSmall, (20, y-38))
    except:
        image = np.zeros((30,30))

    return image
    
        
if __name__ == "__main__":
    main()