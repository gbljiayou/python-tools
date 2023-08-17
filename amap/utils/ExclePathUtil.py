# !/usr/lib/python3

import tkinter as tk
from tkinter import filedialog

'''
选择Excel文件
返回文件绝对路径
'''


def getFilePath():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[('Excel', '.xls .xlsx .csv')])

    if len(file_path) == 0:
        print('未选择文件！')
        return ""
    else:
        print('选择的文件路径是:', file_path)
        return file_path
