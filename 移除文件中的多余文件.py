import os
path='/Users/chenyu/Desktop/Medical paper/test'
baseName='.DS'

for root,dirs,files in os.walk(path):
    for file in files:
        if baseName in file:
            filePath=os.path.join(root,file)
            print(filePath)
            try:
                os.remove(filePath)
            except:
                print('meet an errot')