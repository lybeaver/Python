import os;
def file_dir(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            curDir = "E:\\20.vacro\\"+file;
            # encoding="utf-8_sig"
            fo = open(curDir,"r+",encoding="utf-8");
            lines = fo.readlines();
            str = ""
            for line in lines:
                if line.find("DROP TABLE ") == 0:
                    arr = line.replace(";\n","").split("_")
                    leng =len(arr)
                    for i in range(1,leng):
                        if i!=(leng-1):
                            str += arr[i]+"_"
                        else:
                            str += arr[i]
                    print(str);
            fo.close();
            wf = open(curDir, 'w+', encoding='utf-8')  # wf的 w+打开是删除txt内容，写入rf中修改的内容
            for line in lines:
                if line.find("ENGINE=InnoDB DEFAULT") == 0:
                    wf.write(str)
                else:
                    wf.write(line)
            wf.close()
file_dir(r"E:\20.vacro")