import numpy as np
import cv2

#t
#result_folder = ''
#seq_list = ['']
#tracker_list = ['']

#given a result ([x,y,w,h]) and a jpg, draw bbox and save it
def generateJPGfromResult(result, jpg_source_path, jpg_save_path, bbox_color=(0,255,0), bbox_thickness=1):
	x, y, w, h = result
	upper_left = (int(x),int(y))
	lower_right = (int(x+w),int(y+h))
	img = cv2.imread(jpg_source_path)
	img = cv2.rectangle(img, lower_left, upper_right, bbox_color, bbox_thickness)
	cv2.imwrite(jpg_save_path, img)

#return shape: (num_lines, 4)
def getArrayFromTxt(result_txt_path):
	file = open(result_txt_path, 'r')
	lines = file.read().splitlines()
	#print(lines)
	results_list = []
	for line in lines:
		result = line.split(',')
		result = [float(i) for i in result]
		if(len(result) < 4):
			result = [-result[0],-result[0],-result[0],-result[0]]
		results_list.append(result)
	return np.array(results_list)

# 1 -> 00000001.jpg
def int2jpg(i):
	s = str(i)
	l = len(s)
	temp = ""
	for j in range(8-l):
		temp += "0"
	temp += s
	temp += ".jpg"
	return temp


#source jpg name format: 8-digit_num_padding_by_0.jpg
def generateForResultPatch(result_txt_path, jpg_source_folder, jpg_save_folder, bbox_color=(0,255,0), bbox_thickness=1):
	results = getArrayFromTxt(result_txt_path)
	num_lines = results.shape[0]
	#print(results)
	#print(range(num_lines))
	for i in range(num_lines):
		#print("processing pic: " + str(num_lines+1))
		jpg_source_path = jpg_source_folder + int2jpg(i+1)
		jpg_save_path = jpg_save_folder + int2jpg(i+1)
		generateJPGfromResult(list(results[i]), jpg_source_path, jpg_save_path, bbox_color, bbox_thickness)

#test generateJPGfromResult
def test1():
	result = [50,50,20,20]
	jpg_source_path = '/home/fang/Pictures/test_minion.jpg'
	jpg_save_path = '/home/fang/Pictures/test_minion_result.jpg'
	generateJPGfromResult(result, jpg_source_path, jpg_save_path)

#test int2jpg
def test2():
	print(int2jpg(0))
	print(int2jpg(1))
	print(int2jpg(22))
	print(int2jpg(333))
	print(int2jpg(4444))

#test generateForResultPatch
def test3():
	result_txt_path = "/home/fang/Pictures/test3/source/result.txt"
	jpg_source_folder = "/home/fang/Pictures/test3/source/"
	jpg_save_folder = "/home/fang/Pictures/test3/save/"
	generateForResultPatch(result_txt_path, jpg_source_folder, jpg_save_folder)