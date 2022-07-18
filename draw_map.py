import map_io
import sys
import matplotlib.pyplot as plt

def draw(path_rmap,path_img):
    epm1 = map_io.from_file(path_rmap)
    for i in range(epm1.data.shape[0]):
        plt.imshow(epm1.data[i])
        plt.colorbar()
        plt.imsave(path_img + "{}.png".format(i),epm1.data[i])


