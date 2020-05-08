import os

cartoons = ['shinchan','doraemon','conan','bean','naruto']
path = "dataset/data"

for cartoon in cartoons:
	dirt = path + cartoon
	print("Processing Directory: "+dirt)
	print("Images Found: "+str(len(os.listdir(dirt))))

	#Renaming All Files : Appending Class Name
	for img in os.listdir(dirt):
		name = cartoon+"_"+img
		src = dirt+"/"+img
		des = dirt+"/"+name
		os.rename(src,des)


