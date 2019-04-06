import os
import glob
import shutil

hanji1={'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,'十':10}
hanji2={'十一':11,'十二':12,'十三':13,'十四':14,'十五':15,'十六':16,'十七':17,'十八':18,'十九':19,'二十':20}

files = glob.glob("*.mp4")

cur_path=""
cur_name=""
new_name=""

for name in files:
    # 分开两类，有十位数的字符串比个位的长度多一（这个长度值自己修改，我这里是8）
    if len(name) == 8: 
        for key,value in hanji1.items():
            if key in name:                 # 判断文件名是否包含hanji1中的字符
                print(key+' \n')
                cur_name=name
                cur_path=os.path.dirname(__file__)    # 获取当前路径（注意，要以绝对路径执行该脚本，才能获得当前文件的绝对路径）   
                new_name=cur_path+'\\'+str(value)+')'+cur_name 
                print(new_name+'\n') 
                shutil.copy(cur_name,new_name)
    if len(name) == 9: 
        for key,value in hanji2.items():
            if key in name:                 # 判断文件名是否包含hanji2中的字符
                print(key+' \n')
                cur_name=name
                cur_path=os.path.dirname(__file__)
                new_name=cur_path+'\\'+str(value)+')'+cur_name
                print(new_name+'\n') 
                shutil.copy(cur_name,new_name)



            
