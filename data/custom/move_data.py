import os
import shutil
import numpy as np



# in_dir = "final"
# out_img = "images"
# out_label = "labels"
# a = os.listdir(in_dir)
# for file in os.listdir(in_dir):
# 	if file == 'classes.txt':
# 		continue
# 	if file.endswith('.jpg'):
# 		if file.replace('.jpg','.txt') in a:
# 			file_path = os.path.join(in_dir,file)
# 			out_file_pth_img = os.path.join(out_img,file)
# 			shutil.move(file_path, out_file_pth_img)

# 			file_txt_pth = os.path.join(in_dir, file.replace('.jpg','.txt'))
# 			out_file_pth_lab = os.path.join(out_label, file.replace('.jpg','.txt'))
# 			shutil.move(file_txt_pth, out_file_pth_lab)	





# in_dir = "images"
# a = open('train.txt','a')
# b = open('valid.txt','a')
# for file in os.listdir(in_dir):
# 	prob = np.random.random_sample()
# 	if prob <= 0.85:
# 		a.write('data/custom/images/{}'.format(file))
# 		a.write('\n')
# 	else:
# 		b.write('data/custom/images/{}'.format(file))
# 		b.write('\n')




# in_dir = 'labels'
# for file in os.listdir(in_dir):
# 	file_pth = os.path.join(in_dir,file)
# 	with open(file_pth, 'r') as f:
# 		lines = f.readlines()
# 	with open(file_pth, 'w') as f:
# 		for line in lines:
# 			pos_0 = line.split(' ')[0]
# 			if pos_0 == '6' or pos_0 =='7':
# 				continue
# 			f.write(line)


in_file = 'valid.txt'
out_pth = '/home/zeeshan/Monolith/PyTorch-YOLOv3/data/samples/'

with open(in_file, 'r') as f:
	for line in f:
		pth = line.split('/')[-1].rstrip()
		out_ = out_pth+pth
		pth = 'images/'+pth
		shutil.copy(pth, out_)
		input('.............................')
