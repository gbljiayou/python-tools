# !/usr/lib/python3

import tkinter as tk
from tkinter import filedialog

from logging_config import logger

'''
选择Excel文件
返回文件绝对路径
'''


def get_file_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[('Excel', '.xls .xlsx .csv')])

    if len(file_path) == 0:
        logger.info('未选择文件！')
        return ""
    else:
        logger.info('选择的文件路径是:%s', file_path)
        return file_path
