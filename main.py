from genericpath import isdir
import os
import argparse
from splitting import split_img
import numpy as np
import imageio

pargser = argparse.ArgumentParser()

pargser.add_argument('-p', '--path', type=str, required= True,
    help="image folder")
pargser.add_argument('-f', '--factor', type=int, required=True,
    help="splitting factor of picture x by x ex. 2 (2 x 2)")
pargser.add_argument('-o', '--output', type=str, required= True,
    help='out put directory (folder name)')

pargser.add_argument('-s', '--save', type=bool, default=True,
    help="save result")


arg = pargser.parse_args()

base_path = arg.path


img_dict = {}
for i in range(len(os.listdir(base_path))):
    tem = (base_path + "/" + os.listdir(base_path)[i])
    print(os.listdir(base_path)[i] + ' spliting.....')
    arr_tem = split_img(tem, arg.factor)
    a = 0
    for x in range(arg.factor):
        for y in range(arg.factor):
            img_dict[os.listdir(base_path)[i] + str(x) + str(y) + '.jpg'] = np.array(arr_tem[a])
            a += 1
print(f'splitting complete with {len(list(img_dict.keys()))} images ready to generate....')

#save images
if ~(os.path.isdir(arg.output)):
    os.makedirs(arg.output)

for i in range(len(list(img_dict.keys()))):
    print(f'generating....{i + 1}/{len(list(img_dict.keys()))}')
    imageio.imsave(arg.output + '/' + list(img_dict.keys())[i], img_dict[list(img_dict.keys())[i]])

print(f'outputs are saved at {arg.output}.')