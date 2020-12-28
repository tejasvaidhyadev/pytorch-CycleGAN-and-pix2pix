import os 
import shutil

dir_test = 'E:\Tejas_pix\pytorch-CycleGAN-and-pix2pix\datasets\york\_train\_test'
dir_train = 'E:\Tejas_pix\pytorch-CycleGAN-and-pix2pix\datasets\york\_train\_train'

for (dirpath, dirnames, filenames) in os.walk(dir_test):
    print(filenames)

arr1 = os.listdir('E:\Tejas_pix\pytorch-CycleGAN-and-pix2pix\datasets\york\_train')


Y = []
X = []

for i in arr1:
    flag = 0
    val = str(i)
    for j in range(0,len(val)):
        if(val[j] == '_'):
            flag = 1
            break
    if(flag == 1):
        X.append(i)
        flag = 0
        src = 'E:/Tejas_pix/pytorch-CycleGAN-and-pix2pix/datasets/york/_train/' + i
        dest =  'E:/Tejas_pix/pytorch-CycleGAN-and-pix2pix/datasets/york/X/'   + i
        shutil.move(src,dest)

    else:
        Y.append(i)
        src = 'E:/Tejas_pix/pytorch-CycleGAN-and-pix2pix/datasets/york/_train/' + i
        dest =  'E:/Tejas_pix/pytorch-CycleGAN-and-pix2pix/datasets/york/Y/'   + i
        shutil.move(src,dest)

    
arr2 = os.listdir('E:\Tejas_pix\pytorch-CycleGAN-and-pix2pix\datasets\york\_test')

for i in arr2:
    flag = 0
    val = str(i)
    for j in range(0,len(val)):
        if(val[j] == '_'):
            flag = 1
            break
    if(flag == 1):
        X.append(i)
        src = 'E:/Tejas_pix/pytorch-CycleGAN-and-pix2pix/datasets/york/_test/' + i
        dest =  'E:/Tejas_pix/pytorch-CycleGAN-and-pix2pix/datasets/york/X/'   + i
        shutil.move(src,dest)
        flag = 0
    else:
        Y.append(i)
        src = 'E:/Tejas_pix/pytorch-CycleGAN-and-pix2pix/datasets/york/_test/' + i
        dest =  'E:/Tejas_pix/pytorch-CycleGAN-and-pix2pix/datasets/york/Y/'   + i
        shutil.move(src,dest)



# print("\nthe lists are")
print(Y)
print("\n")
print(X)

# print(type(Y[0]))
# import pathlib

# flist = []
# for p in pathlib.Path('E:\Tejas_pix\pytorch-CycleGAN-and-pix2pix\datasets').iterdir():
#     if p.is_file():
#         print(p)
#         flist.append(p)
