# coding=utf-8
import sys
import string
import json
import xlwt
import re
# from tkinter import *
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox as mes

#判断变量是否被声明过
def isset(v):
    try:
        type(eval(v))
    except:
        return 0
    else:
        return 1

def wirteFile():
    detPath = r"E:\\doc\boardDoc.txt";
    savePath = r'e:\\数据api文档.xls';
    if (isset('selectFileName') and selectFileName != ''):
        detPath = selectFileName
    elif isset('selectFileName') and selectFileName == '':
        return mes.showinfo('提示','请选择文件')
    if (isset('saveFilePath') and saveFilePath != ''):
        savePath = saveFilePath+'\数据api文档.xls'
    elif isset('saveFilePath') and saveFilePath == '':
        return mes.showinfo('提示','请选择保存文件路径')
    print("777777",detPath)
    with open(detPath, "r") as f:
        line = f.readline()
        array = []
        num = 0
        action = '- action:'
        api = '  api:'
        cls = '  class:'
        des = '  description:'
        filters = '  filters:'
        selects = '  selects:'
        parameter = '      parameter:'
        key = '      key:'
        js = {"api": "", "cls": "", "description": "", "filters": [], "selects": []}
        while line:
            if line.find(action) != 0 and num == 0:
                return mes.showerror('错误','导入的文件格式不对')
            if (line.find(action) == 0 and num != 0):
                array.append(js)
                js = {"api": "", "cls": "", "description": "", "filters": [], "selects": []}
            elif (line.find(api) == 0):
                js['api'] = line.split(':')[1].strip().replace('\n', '')
            elif (line.find(cls) == 0):
                js['cls'] = line.split(':')[1].strip().replace('\n', '')
            elif (line.find(des) == 0):
                js['description'] = line.split(':')[1].strip().replace('\n', '')
            elif (line.find(filters) == 0):
                tempLine = line
                while (tempLine):
                    if (tempLine.find(parameter) == 0):
                        js['filters'].append(tempLine.split(':')[1].strip().replace('\n', ''))
                    elif (tempLine.find('  free:') == 0):
                        break
                    tempLine = f.readline()
            elif (line.find(selects) == 0):
                tempLine = line
                while (tempLine):
                    if (tempLine.find(key) == 0):
                        js['selects'].append(tempLine.split(':')[1].strip().replace('\n', ''))
                    elif (tempLine.find('  type:') == 0 or tempLine.find('  sorts:') == 0):
                        break
                    tempLine = f.readline()
            num = num + 1
            # print(line,end="")
            line = f.readline()
            if (line == ''):
                array.append(js)
        book = xlwt.Workbook(encoding='utf-8', style_compression=0)
        sheet1 = book.add_sheet(u'sheet1',cell_overwrite_ok=True)
        xlsHeader = ['接口','表名','说明','条件','返回值']
        i = 1
        j = 0
        for ar in array:
            print(ar)
        try:
            for head in xlsHeader:
                sheet1.write(0, j, head)
                j = j+1
            for arr in array:
                sheet1.write(i, 0, arr['api'])
                sheet1.write(i, 1, arr['cls'])
                sheet1.write(i, 2, arr['description'])
                sheet1.write(i, 3, ','.join(arr['filters']))
                sheet1.write(i, 4, ','.join(arr['selects']))
                i = i+1
        except:
            print('出异常')
        book.save(savePath)

def openFile():
    global selectFileName
    selectFileName = tk.filedialog.askopenfilename(filetypes=[("text file", "*.txt")])
    if selectFileName != '':
        lb1.config(text = "选择的文件是:"+selectFileName)
    else:
        lb1.config(text = "请选择文件")

def dirFile():
    global saveFilePath
    saveFilePath = tk.filedialog.askdirectory()
    if saveFilePath != '':
        lb2.config(text = "选择的路径是:"+saveFilePath)
    else:
        lb2.config(text="请选择路径")
    print(saveFilePath)

# class App:
#     def __init__(self,master):
#         fm1 = tk.Frame(master)
#         tk.Button(fm1,text='center').pack(side=tk.TOP,anchor=tk.W,fill=tk.X,expand=tk.YES)
#         fm1.pack(side=tk.LEFT,fill=tk.BOTH,expand=tk.YES)
winForm = tk.Tk()
winForm.geometry('480x380+150+200')
winForm.title("API文档EXCEL导出")
lb1 = tk.Label(winForm,text = r'默认路径:E:\\doc\boardDoc.txt')
lb1.grid(row=0,column=0,padx=0,pady=0)
lb2 = tk.Label(winForm,text = r'默认保存路径:E:')
lb2.grid(row=1,column=0,padx=0,pady=0)
but1 = tk.Button(winForm,text = '选择文本文件',width = 10,command=openFile)
but2 = tk.Button(winForm,text='选择保存路径',width = 10,command=dirFile)
but3 = tk.Button(winForm,text = '开始',width = 10,command=wirteFile)
but4 = tk.Button(winForm,text = '退出',width = 10,command=winForm.quit)
but1.grid(row=0,column=10, padx=10, pady=30)
but2.grid(row=1,column=10, padx=10, pady=50)
but3.grid(row=2,column=10, padx=10, pady=60)
but4.grid(row=2,column=0, padx=60, pady=60)
# but1.pack()
# but1.grid(row = 2,column = 5,sticky = tk.S)
# App(winForm)
winForm.mainloop()

