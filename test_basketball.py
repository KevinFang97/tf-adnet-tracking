import result_viewer as V
result_txt_path = "/home/yuwing/2018CK2/vot/vot-workspace/adnet_2017/results/ADNet/baseline/basketball/basketball_001.txt"
jpg_source_folder = "/home/yuwing/2018CK2/vot/vot-workspace/adnet_2017/sequences/basketball/color/"
jpg_save_folder = "/home/yuwing/2018CK2/test/basketball/"
V.generateForResultPatch(result_txt_path, jpg_source_folder, jpg_save_folder)

print("DONE")

