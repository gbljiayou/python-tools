from amap.utils import excel_util, tk_util
from distance import get_driving_distance
from logging_config import logger
from poi import get_locations


def call_driving_distance(no, address_array):
    lnglat_array = get_locations(no, address_array)
    if lnglat_array is None:
        return None
    logger.info("[第%s行数据处理]线路经纬度array=%s", str(no), lnglat_array)
    dist_str = get_driving_distance(no, lnglat_array)
    if dist_str is None:
        return None
    logger.info("[第%s行数据处理]线路dist=%s", str(no), dist_str)
    return dist_str


def get_result(data):
    result = []
    for i in range(0, len(data)):
        no = i + 2  # 记录excel的行号
        addr = data.iloc[i, 0]
        logger.info("[第%s行数据处理]线路=%s", str(no), addr)
        address_array = addr.split("-")
        dist_str = call_driving_distance(no, address_array)
        if not dist_str is None:
            dist = int(dist_str) / 1000
        else:
            dist = 0
        result.append([addr, dist, data.iloc[i, 2]])
    return result


if __name__ == "__main__":
    # 1:os选择文件
    selectedFile = tk_util.get_file_path()
    # 2: 读取excel源数据
    excel_header, data = excel_util.read_excel(selectedFile)
    # 3:循环遍历excel行数据
    result = get_result(data)
    # 4:导出结果excel
    excel_util.write_excel(selectedFile, result, excel_header)
