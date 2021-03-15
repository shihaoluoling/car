# -!- coding: utf-8 -!-
# 排布的模块
str1 = {
    "model1": [
        [
            39.500001,
            36.390000000000015
        ],
        [
            4,
            7.100000999999999
        ],
        [
            2,
            3.390000000000015
        ],
        [
            8,
            368.20503639000054
        ]
    ],
    "model2": [
        [
            7.100000999999999,
            33
        ],
        [
            1,
            1.5000009999999993
        ],
        [
            2,
            0
        ],
        [
            2,
            49.50003299999997
        ]
    ]
}
# 大矩形坐标
str2 = [
    [
        -274.920461,
        -208.824746
    ],
    [
        -274.920461,
        -172.434746
    ],
    [
        -235.42046,
        -172.434746
    ],
    [
        -235.42046,
        -208.824746
    ]
]

# 排布开始位置 左下:leftDown 左上:leftUp 右上:rightUp 右下:rightDown
site = 'leftUp'

# 模块参数
M = {
    "model1": [
        # 长
        16.5,
        # 宽
        8.1
    ],
    "model2": [
        16.5,
        5.6
    ]
}


def stall_car(stall, car):
    if car.__len__() == 0:
        return "排布模块不能为空"
    if stall.__len__() == 0:
        return "大矩形坐标不能为空"
    # print(list(car.keys()))
    # 总返回参数
    let = []
    # 上一个排布的模块的key
    last_key = ""
    # 沿x轴的起始坐标
    last_x = []
    # y轴的起始坐标
    last_y = []
    for key in list(car.keys()):
        if site == "leftUp":
            la = {"modelKey": key}
            cood = []
            if last_x.__len__() == 0 or last_y.__len__() == 0 or last_key == "":
                start_x_0 = stall[1][0]
                start_y_0 = stall[1][1]
            elif M[key][0] == M[last_key][0]:
                start_x_0 = last_x[0]
                start_y_0 = last_x[1]
            else:
                start_x_0 = last_y[0]
                start_y_0 = last_y[1]
            for model1_num_y in range(car[key][2][0]):
                start_x = start_x_0
                start_y = start_y_0 - model1_num_y*M[key][0]
                # x方向排布
                for model1_num_x in range(car[key][1][0]):
                    # 坐标数组
                    coord = []
                    # 左下角坐标
                    leftDown = [start_x, start_y - M[key][0]]
                    # 左上角坐标
                    leftUp = [start_x, start_y]
                    # 右上角
                    rightUp = [start_x + M[key][1], start_y]
                    # 右下角
                    rightDown = [start_x + M[key][1], start_y - M[key][0]]
                    coord.append(leftDown)
                    coord.append(leftUp)
                    coord.append(rightUp)
                    coord.append(rightDown)
                    cood.append(coord)
            la["cood"] = cood
            let.append(la)
            last_x = [cood[cood.__len__()-1][3][0], cood[0][1][1]]
            last_y = [cood[0][1][0], cood[cood.__len__()-1][3][1]]
            last_key = key
    return let


print(stall_car(str2, str1))
