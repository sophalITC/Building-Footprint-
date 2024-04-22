import numpy as np
import imageio
import matplotlib.pyplot as plt

# transform Image to numpy array first before spliting
def split_img(imgPath, factor):

    dt = plt.imread(imgPath)
    
    x, y, z = dt.shape

    #find x and y distance to split
    x_batch, y_batch = int(x / factor), int(y / factor)

    a, b = 0, 0
    arr = []

    for i in range(int(factor)):
        for j in range(int(factor)):
            tem_pic = dt[a: a + x_batch, b: b + y_batch, :]
            arr.append(tem_pic)
            a += x_batch
        a = 0
        b += y_batch
    return arr

# In case we want to see how our image is splited
# Use this to check it and also we can save or not (just show by default)
def splited_show(imgPath,factor, isSave = False):
    pic = split_img(imgPath, int(factor))
    fig, axs = plt.subplots(nrows=factor, ncols=factor)
    a = 0
    for i in range(factor):
        for j in range(factor):
            axs[j][i].set_axis_off()
            axs[j][i].imshow(pic[a])

            if isSave:
                imageio.imsave(imgPath.split('/')[-2] + "/" + imgPath.split('/')[-1].split('.')[0] + str(i) + str(j) + ".jpg", pic[a])
            a += 1