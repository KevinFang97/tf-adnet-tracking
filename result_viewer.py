import numpy as np
import cv2

#t
#result_folder = ''
#seq_list = ['']
#tracker_list = ['']

#given a result ([x,y,w,h]) and a jpg, draw bbox and save it
def generateJPGfromResult(result, jpg_source_path, jpg_save_path, bbox_color=(0,255,0), bbox_thickness=1):
	x, y, w, h = result
	lower_left = (int(x-w/2),int(y-h/2))
	upper_right = (int(x+w/2),int(y+h/2))
	img = cv2.imread(jpg_source_path)
	img = cv2.rectangle(img, lower_left, upper_right, bbox_color, bbox_thickness)
	cv2.imwrite(jpg_save_path, img)

#return shape: (num_lines, 4)
def getArrayFromTxt(result_txt_path):
	file = open(result_txt_path, 'r')
	lines = file.read().splitlines()
	results_list = []
	for line in lines:
		result = line.split(',')
		result = [float(i) for i in result]
		if(len(result) < 4):
			result = [-result[0],-result[0],-result[0],-result[0]]
			results_list.append(result)
	return np.array(results_list)

#source jpg name format: <seqname><number>.jpg
def generateForResultPatch(seq_name, result_txt_path, jpg_source_folder, save_folder, bbox_color=(0,255,0), bbox_thickness=1):
	results = getArrayFromTxt(result_txt_path)
	num_lines = results.shape[0]
	for i in num_lines:
		jpg_source_path = jpg_source_folder + seq_name + str(num_lines) + '.jpg'
		jpg_save_path = save_folder + seq_name + str(num_lines) + 'jpg'
		generateJPGfromResult(list(results[num_lines]), jpg_source_path, jpg_save_path, bbox_color, bbox_thickness)

#test generateJPGfromResult
def test1():
	result = [50,50,20,20]
	jpg_source_path = '/home/fang/Pictures/test_minion.jpg'
	jpg_save_path = '/home/fang/Pictures/test_minion_result.jpg'
	generateJPGfromResult(result, jpg_source_path, jpg_save_path)