import pandas as pd


def write_excel(file_path, result, excel_header):
    pd.DataFrame(result).to_excel(
        file_path.replace(".xlsx", "-result.xlsx"),
        header=excel_header
    )


'''
读取excel
返回表头数组/excel内容
'''


def read_excel(file_path):
    data = pd.read_excel(file_path)
    return data.columns.tolist(), data
