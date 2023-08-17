import json

import requests

from ak_enum import AKEnum

LocationDict = {'成翔电子(东莞)有限公司': '114.116952,22.856414'}


# 获取地理编码
def get_location(no, address):
    lnglatCache = LocationDict.get(address)
    if lnglatCache is None:
        url = f"https://restapi.amap.com/v3/place/text?keywords={address}&output=json&key={AKEnum.MT_DISTANCE_AK.value}"
        res = requests.get(url)
        json_data = json.loads(res.text)

        if json_data["status"] == "1":  # 成功时返回1
            lnglat = json_data["pois"][0]["location"]
            LocationDict[address] = lnglat
            print("[第" + str(no) + "行数据处理] " + "getLocation[高德],lnglat=", lnglat)
            return lnglat
        else:
            print("[第" + str(no) + "行数据处理] " + "getLocation[高德异常],lnglat=", None)
            return None
    else:
        print("[第" + str(no) + "行数据处理] " + "getLocation[缓存],lnglat=", lnglatCache)
        return lnglatCache


# 循环获取地址集合-地理坐标集合
def get_locations(no, address_array):
    try:
        lnglat_array = []
        for i in range(0, len(address_array)):
            lngLat = get_location(no, address_array[i])
            lnglat_array.append(lngLat)
        return lnglat_array
    except Exception as e:
        print("[第" + str(no) + "行数据处理]异常 ""e=", e)
        return None
