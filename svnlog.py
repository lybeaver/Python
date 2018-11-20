import xlwt;
import os;
def file_dir(dir):
    outFiles = []
    for root, dirs, files in os.walk(dir):
        # print("当前目录路径",root)  # 当前目录路径
        # print("当前路径下所有子目录",dirs)  # 当前路径下所有子目录
        # print("当前路径下所有非目录子文件",files)  # 当前路径下所有非目录子文件
        for file in files:
            svnlogDir = root + "\\" + file;
            print(svnlogDir)
            command = "svn log --limit 1 "+svnlogDir;
            res = os.popen(command)
            resLines = res.read()
            res.close()
            for line in resLines.splitlines():
                if line is None or (len(line) < 1):
                    continue
                if '--------' in line:
                    continue
                if line.count("|") >= 3:
                    temp = {"filename":'',"update":''};
                    temp["filename"] = file
                    temp["update"] = line.split(' | ')[2]
                    outFiles.append(temp);
                    # print(file, ":", line.split(' | ')[2])
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet1 = book.add_sheet(u'sheet1', cell_overwrite_ok=True)
    xlsHeader = ['文件名', '日期']
    i = 1
    j = 0
    try:
        for head in xlsHeader:
            sheet1.write(0, j, head)
            j = j + 1
        for arr in outFiles:
            sheet1.write(i, 0, arr['filename'])
            sheet1.write(i, 1, arr['update'][0:10])
            temp = arr['update']
            print(temp[0:10])
            i = i + 1
    except:
        print('出异常')
    book.save(r"E:\ビジネスロジック.xls")
    for outfile in outFiles:
        print(outfile)
file_dir(r"D:\chindai\trunk\20設計\20詳細設計\10_EMS賃貸")