import json

import requests

from AkEnum import AKEnum


# 驾车路径规划
def getDrivingDistance(lnglatArray):
    if len(lnglatArray) != 0:
        length = len(lnglatArray)
        origin = lnglatArray[0]  # 起点经纬度
        destination = lnglatArray[length - 1]  # 终点经纬度
        waypoints = ";".join(lnglatArray[1:length - 1])  # 途径点经纬度
        url = f"https://restapi.amap.com/v3/direction/driving?origin={origin}&waypoints={waypoints}&destination={destination}&output=json&key={AKEnum.MT_DISTINCE_AK.value}"
        print("[getDrivingDistance]url=", url)
        res = requests.get(url)
        json_data = json.loads(res.text)

        if json_data["status"] == "1":
            return json_data["route"]["paths"][0]["distance"]
        else:
            return -1
    else:
        return -1
