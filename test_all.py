import result_viewer as V
from shutil import copyfile

B = "ADNet"
G = "MAVOT"
R = "GT"
pre = "/home/yuwing/2018CK2/vot/vot-workspace/adnet_2017/results/"
video_list = ["basketball"]

for video in video_list:

	result_txt_path_list = [pre+B+"/baseline/"+video+"/"+video+"_001.txt", pre+G+"/baseline/"+video+"/"+video+"_001.txt", "/home/yuwing/2018CK2/vot/vot-workspace/adnet_2017/sequences/"+video+"/groundtruth.txt"]
	jpg_source_folder = "/home/yuwing/2018CK2/vot/vot-workspace/adnet_2017/sequences/"+video+"/color/"
	jpg_save_folder = "/home/yuwing/2018CK2/test/"+video+"/"

	V.generateForResultPatch_MultiBBOX(result_txt_path_list, jpg_source_folder, jpg_save_folder)
	#copyfile('./show.html', jpg_save_folder+'show.html')
	with open(jpg_save_folder+'color.txt','w+') as f:
    	f.write("Blue:  "+B+'\n')
    	f.write("Green: "+G+'\n')
    	f.write("Red:   "+R+'\n')
    	f.close()

    print(video + " DONE")

print("DONE")

