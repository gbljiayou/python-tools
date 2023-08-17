import pandas as pd

from gaode_distance import getDrivingDistance
from gaode_poi import getLocations
from utils import ExclePathUtil


def callDrivingDistance(addressArray):
    lnglatArray = getLocations(addressArray)
    return getDrivingDistance(lnglatArray)


def get_result(data):
    result = []
    for i in range(0, len(data)):
        addr = data.iloc[i, 0]
        addressArray = addr.split("-")
        dist = int(callDrivingDistance(addressArray))
        result.append([addr, dist / 1000, data.iloc[i, 2]])
        return result


if __name__ == "__main__":
    # 1:读取excel源数据
    selectedFile = ExclePathUtil.getFilePath()
    # 循环遍历excel行数据
    result = get_result(pd.read_excel(selectedFile))
    # 导出excel
    pd.DataFrame(result).to_excel(
        selectedFile.replace(".xlsx", "-result.xlsx")
    )
