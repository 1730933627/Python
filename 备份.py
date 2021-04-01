import os,zipfile,time

backup_file = "./server" #要备份的目录
sleep_time = 600         #间隔时间(秒)

def make_zip(source_dir, output_filename):
    zipf = zipfile.ZipFile(output_filename, 'w')    
    pre_len = len(os.path.dirname(source_dir))
    for parent, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)
            zipf.write(pathfile, arcname)
    zipf.close()

def loop():
    zip_list = []
    while True:
        zip_name = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()) 
        make_zip(backup_file,"./backup/"+zip_name+".zip")
        zip_list.append(zip_name)
        print(zip_name+"\t备份完成")
        time.sleep(sleep_time)
        print(zip_list)
        print(len(zip_list))
        if len(zip_list) >= 3:
            os.remove("./backup/"+zip_list[0]+".zip")
            print("已删除"+zip_name+".zip")    
            zip_list[0] = zip_list[1]
            zip_list[1] = zip_list[2]
            del zip_list[2]

if __name__ == "__main__":
    loop()
