import json

import requests

from ak_enum import AKEnum


# 驾车路径规划
def get_driving_distance(no, lnglat_array):
    try:
        if len(lnglat_array) != 0:
            length = len(lnglat_array)
            origin = lnglat_array[0]  # 起点经纬度
            destination = lnglat_array[length - 1]  # 终点经纬度
            waypoints = ";".join(lnglat_array[1:length - 1])  # 途径点经纬度
            url = f"https://restapi.amap.com/v3/direction/driving?origin={origin}&waypoints={waypoints}&destination={destination}&output=json&key={AKEnum.MT_DISTANCE_AK.value}"
            print("[第" + str(no) + "行数据处理] " + "[getDrivingDistance]url=", url)
            res = requests.get(url)
            json_data = json.loads(res.text)

            if json_data["status"] == "1":
                return get_min_driving_distance(json_data["route"]["paths"])
            else:
                return None
        else:
            return None
    except Exception as e:
        print("[第" + str(no) + "行数据处理] " + "[get_driving_distance]异常 e=", e)
        return None
    finally:
        print("[第" + str(no) + "行数据处理] " + "[get_driving_distance]结束")


# 获取最小路径
def get_min_driving_distance(paths):
    driving_distance = []
    for i in range(0, len(paths)):
        driving_distance.append(paths[i]["distance"])
    return min(driving_distance)
