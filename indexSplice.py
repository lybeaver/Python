# coding=utf-8
import sys
import string
import json
import xlwt
import xlrd
import mysql
import re
def writeDef():
    openPath = r"E:\indexSlice\emscIndex.xlsx";
    savePath = r"E:\indexSlice\emscNew.xls";
    print(openPath)
    data = xlrd.open_workbook(openPath);
    table = data.sheet_by_name('Sheet1');
    if(table):
        print(table);
        totalRows = table.nrows
        print(totalRows)
        js = {"key":"","tableName":"","tableIndex":"","tableIndexs":[]}
        temp = {"tableName":"","tableIndex":"","tableIndexs":[]}
        arr = []
        for i in range(0,totalRows-1):
            rowtable = table.row_values(i, 0, 4)
            beforeStr = ""
            nowStr = rowtable[0] + rowtable[1]
            if (i != 0):
                beforeRow =  table.row_values(i-1, 0, 4)
                beforeStr = beforeRow[0] + beforeRow[1]
            if beforeStr == nowStr:
                js["tableIndexs"].append(rowtable[3])
            else:
                # print(js)
                arr.append(js)
                js = {"key": "", "tableName": "", "tableIndex": "", "tableIndexs": []}
                js["key"] = rowtable[0] + rowtable[1]
                js["tableName"] = rowtable[0]
                js["tableIndex"] = rowtable[1]
                js["tableIndexs"].append(rowtable[3])
        # print(arr)
        if arr:
            book = xlwt.Workbook(encoding='utf-8', style_compression=0)
            sheet1 = book.add_sheet(u'sheet1', cell_overwrite_ok=True)
            i = 0
            try:
                for index in arr:
                    sheet1.write(i, 0, index["tableName"])
                    sheet1.write(i, 1, index["tableIndex"])
                    sheet1.write(i, 2, ','.join(index["tableIndexs"]))
                    print(index["tableName"])
                    print(index["tableIndex"])
                    print(index["tableIndexs"])
                    i = i + 1
            except:
                print("error")
            book.save(savePath)
writeDef();