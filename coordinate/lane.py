# 模块坐标
model = [[-274.920461, -188.934746], [-274.920461, -172.434746], [-266.82046099999997, -172.434746],
         [-266.82046099999997, -188.934746]]
# 左柱网距离
left_column = 0
# 右柱网距离
right_column = 0
# 车长
car_length = 0
# 车宽
car_width = 0
# 柱子长宽
column = 0


# 车道


def lane(model_x_y):
    lane_arr = []
    # 车道左下角坐标
    left_lane_down_x = model_x_y[0][0]
    left_lane_down_y = model_x_y[0][1] + car_length
    left_lane_down = [left_lane_down_x, left_lane_down_y]
    # 车道左上角坐标
    left_lane_up_x = model_x_y[1][0]
    left_lane__up_y = model_x_y[1][1] - car_length
    left_lane_up = [left_lane_up_x, left_lane__up_y]
    # 车道右上角坐标
    right_lane_up_x = model_x_y[2][0]
    right_lane_up_y = model_x_y[2][1] - car_length
    right_lane_up = [right_lane_up_x, right_lane_up_y]
    # 车道右下角坐标
    right_lane_down_x = model_x_y[3][0]
    right_lane_down_y = model_x_y[3][1] + car_length
    right_lane_down = [right_lane_down_x, right_lane_down_y]
    lane_arr.append(left_lane_down)
    lane_arr.append(left_lane_up)
    lane_arr.append(right_lane_up)
    lane_arr.append(right_lane_down)
    return lane_arr


def model1(model_list):
    model_1 = {}
    stall = []
    # 上方三个模块坐标
    stall_x = model_list[1][0] + left_column
    stall_y = model_list[1][1]

    stall_0 = []
    # 左下 减去车长
    stall_left_down_x_0 = stall_x
    stall_left_down_y_0 = stall_y - car_length
    stall_left_down_0 = [stall_left_down_x_0, stall_left_down_y_0]
    stall_0.append(stall_left_down_0)
    # 左上
    stall_left_up_x_0 = stall_x
    stall_left_up_y_0 = stall_y
    stall_left_up_0 = [stall_left_up_x_0, stall_left_up_y_0]
    stall_0.append(stall_left_up_0)
    # 右上 加上车宽
    stall_right_up_x_0 = stall_x + car_width
    stall_right_up_y_0 = stall_y
    stall_right_up_0 = [stall_right_up_x_0, stall_right_up_y_0]
    stall_0.append(stall_right_up_0)
    # 右下 左下的y 右上的x
    stall_right_down_x_0 = stall_x + car_width
    stall_right_down_y_0 = stall_y - car_length
    stall_right_down_0 = [stall_right_down_x_0, stall_right_down_y_0]
    stall_0.append(stall_right_down_0)
    # 第二个车位
    # 左下 上一个右下的坐标
    stall_1 = []
    stall_left_down_x_1 = stall_x + car_width
    stall_left_down_y_1 = stall_y - car_length
    stall_left_down_1 = [stall_left_down_x_1, stall_left_down_y_1]
    stall_1.append(stall_left_down_1)
    # 左上 上一个右上的坐标
    stall_left_up_x_1 = stall_x + car_width
    stall_left_up_y_1 = stall_y
    stall_left_up_1 = [stall_left_up_x_1, stall_left_up_y_1]
    stall_1.append(stall_left_up_1)
    # 右上 x加两个车宽
    stall_right_up_x_1 = stall_x + 2 * car_width
    stall_right_up_y_1 = stall_y
    stall_right_up_1 = [stall_right_up_x_1, stall_right_up_y_1]
    stall_1.append(stall_right_up_1)
    # 右下 左下的y 右上的x
    stall_right_down_x_1 = stall_x + 2 * car_width
    stall_right_down_y_1 = stall_y - car_length
    stall_right_down_1 = [stall_right_down_x_1, stall_right_down_y_1]
    stall_1.append(stall_right_down_1)

    # 第三个车位
    # 左下 上一个右下坐标
    stall_2 = []
    stall_left_down_x_2 = stall_x + 2 * car_width
    stall_left_down_y_2 = stall_y - car_length
    stall_left_down_2 = [stall_left_down_x_2, stall_left_down_y_2]
    stall_2.append(stall_left_down_2)
    # 左上 上一个右上坐标
    stall_left_up_x_2 = stall_x + 2 * car_width
    stall_left_up_y_2 = stall_y
    stall_left_up_2 = [stall_left_up_x_2, stall_left_up_y_2]
    stall_2.append(stall_left_up_2)
    # 右上
    stall_right_up_x_2 = stall_x + 3 * car_width
    stall_right_up_y_2 = stall_y
    stall_right_up_2 = [stall_right_up_x_2, stall_right_up_y_2]
    stall_2.append(stall_right_up_2)
    # 右下  左下的y 右上的x
    stall_right_down_x_2 = stall_x + 3 * car_width
    stall_right_down_y_2 = stall_y - car_length
    stall_right_down_2 = [stall_right_down_x_2, stall_right_down_y_2]
    stall_2.append(stall_right_down_2)

    # 模块1下方的车位
    stall_down_x = model_list[0][0] + left_column
    stall_down_y = model_list[0][1]
    stall_3 = []
    # 左下
    stall_left_down_x_3 = stall_down_x
    stall_left_down_y_3 = stall_down_y
    stall_left_down_3 = [stall_left_down_x_3, stall_left_down_y_3]
    stall_3.append(stall_left_down_3)
    # 左上
    stall_left_up_x_3 = stall_down_x
    stall_left_up_y_3 = stall_down_y + car_length
    stall_left_up_3 = [stall_left_up_x_3, stall_left_up_y_3]
    stall_3.append(stall_left_up_3)
    # 右上
    stall_right_up_x_3 = stall_down_x + car_width
    stall_right_up_y_3 = stall_down_y + car_length
    stall_right_up_3 = [stall_right_up_x_3, stall_right_up_y_3]
    stall_3.append(stall_right_up_3)
    # 右下
    stall_right_down_x_3 = stall_down_x + car_width
    stall_right_down_y_3 = stall_down_y
    stall_right_down_3 = [stall_right_down_x_3, stall_right_down_y_3]
    stall_3.append(stall_right_down_3)

    # 下方车位2
    # 左下 上一个车位右下
    stall_4 = []
    stall_left_down_x_4 = stall_down_x + car_width
    stall_left_down_y_4 = stall_down_y
    stall_left_down_4 = [stall_left_down_x_4, stall_left_down_y_4]
    stall_4.append(stall_left_down_4)
    # 左上 上一个车位右上
    stall_left_up_x_4 = stall_down_x + car_width
    stall_left_up_y_4 = stall_down_y + car_length
    stall_left_up_4 = [stall_left_up_x_4, stall_left_up_y_4]
    stall_4.append(stall_left_up_4)
    # 右上
    stall_right_up_x_4 = stall_down_x + 2 * car_width
    stall_right_up_y_4 = stall_down_y + car_length
    stall_right_up_4 = [stall_right_up_x_4, stall_right_up_y_4]
    stall_4.append(stall_right_up_4)
    # 右下
    stall_right_down_x_4 = stall_down_x + 2 * car_width
    stall_right_down_y_4 = stall_down_y
    stall_right_down_4 = [stall_right_down_x_4, stall_right_down_y_4]
    stall_4.append(stall_right_down_4)

    # 下方第三个车位 模块第六
    # 左下上一个右下
    stall_5 = []
    stall_left_down_x_5 = stall_down_x + 2 * car_width
    stall_left_down_y_5 = stall_down_y
    stall_left_down_5 = [stall_left_down_x_5, stall_left_down_y_5]
    stall_5.append(stall_left_down_5)
    # 左上 上一个右上
    stall_left_up_x_5 = stall_down_x + 2 * car_width
    stall_left_up_y_5 = stall_down_y + car_length
    stall_left_up_5 = [stall_left_up_x_5, stall_left_up_y_5]
    stall_5.append(stall_left_up_5)
    # 右上
    stall_right_up_x_5 = stall_down_x + 3 * car_width
    stall_right_up_y_5 = stall_down_y + car_length
    stall_right_up_5 = [stall_right_up_x_5, stall_right_up_y_5]
    stall_5.append(stall_right_up_5)
    # 右下
    stall_right_down_x_5 = stall_down_x + 3 * car_width
    stall_right_down_y_5 = stall_down_y
    stall_right_down_5 = [stall_right_down_x_5, stall_right_down_y_5]
    stall_5.append(stall_right_down_5)
    stall.append(stall_0)
    stall.append(stall_1)
    stall.append(stall_2)
    stall.append(stall_3)
    stall.append(stall_4)
    stall.append(stall_5)
    model_1["stall"] = stall
    model_1["lane"] = lane(model_list)
    return model_1


# 模块二
def model2(model_list):
    model_1 = {}
    stall = []
    # 上方三个模块坐标
    stall_x = model_list[1][0] + left_column
    stall_y = model_list[1][1]

    stall_0 = []
    # 左下 减去车长
    stall_left_down_x_0 = stall_x
    stall_left_down_y_0 = stall_y - car_length
    stall_left_down_0 = [stall_left_down_x_0, stall_left_down_y_0]
    stall_0.append(stall_left_down_0)
    # 左上
    stall_left_up_x_0 = stall_x
    stall_left_up_y_0 = stall_y
    stall_left_up_0 = [stall_left_up_x_0, stall_left_up_y_0]
    stall_0.append(stall_left_up_0)
    # 右上 加上车宽
    stall_right_up_x_0 = stall_x + car_width
    stall_right_up_y_0 = stall_y
    stall_right_up_0 = [stall_right_up_x_0, stall_right_up_y_0]
    stall_0.append(stall_right_up_0)
    # 右下 左下的y 右上的x
    stall_right_down_x_0 = stall_x + car_width
    stall_right_down_y_0 = stall_y - car_length
    stall_right_down_0 = [stall_right_down_x_0, stall_right_down_y_0]
    stall_0.append(stall_right_down_0)
    # 第二个车位
    # 左下 上一个右下的坐标
    stall_1 = []
    stall_left_down_x_1 = stall_x + car_width
    stall_left_down_y_1 = stall_y - car_length
    stall_left_down_1 = [stall_left_down_x_1, stall_left_down_y_1]
    stall_1.append(stall_left_down_1)
    # 左上 上一个右上的坐标
    stall_left_up_x_1 = stall_x + car_width
    stall_left_up_y_1 = stall_y
    stall_left_up_1 = [stall_left_up_x_1, stall_left_up_y_1]
    stall_1.append(stall_left_up_1)
    # 右上 x加两个车宽
    stall_right_up_x_1 = stall_x + 2 * car_width
    stall_right_up_y_1 = stall_y
    stall_right_up_1 = [stall_right_up_x_1, stall_right_up_y_1]
    stall_1.append(stall_right_up_1)
    # 右下 左下的y 右上的x
    stall_right_down_x_1 = stall_x + 2 * car_width
    stall_right_down_y_1 = stall_y - car_length
    stall_right_down_1 = [stall_right_down_x_1, stall_right_down_y_1]
    stall_1.append(stall_right_down_1)

    # 第三个车位
    # 左下 上一个右下坐标
    stall_2 = []
    stall_left_down_x_2 = stall_x + 2 * car_width
    stall_left_down_y_2 = stall_y - car_length
    stall_left_down_2 = [stall_left_down_x_2, stall_left_down_y_2]
    stall_2.append(stall_left_down_2)
    # 左上 上一个右上坐标
    stall_left_up_x_2 = stall_x + 2 * car_width
    stall_left_up_y_2 = stall_y
    stall_left_up_2 = [stall_left_up_x_2, stall_left_up_y_2]
    stall_2.append(stall_left_up_2)
    # 右上
    stall_right_up_x_2 = stall_x + 3 * car_width
    stall_right_up_y_2 = stall_y
    stall_right_up_2 = [stall_right_up_x_2, stall_right_up_y_2]
    stall_2.append(stall_right_up_2)
    # 右下  左下的y 右上的x
    stall_right_down_x_2 = stall_x + 3 * car_width
    stall_right_down_y_2 = stall_y - car_length
    stall_right_down_2 = [stall_right_down_x_2, stall_right_down_y_2]
    stall_2.append(stall_right_down_2)

    # 下方一个车位
    stall_3 = []
    stall_down_x = model_list[0][0] + left_column
    stall_down_y = model_list[0][1]
    # 左下 y加车宽
    stall_left_down_x_3 = stall_down_x
    stall_left_down_y_3 = stall_down_y
    stall_left_down_3 = [stall_left_down_x_3, stall_left_down_y_3]
    stall_3.append(stall_left_down_3)
    # 左上
    stall_left_up_x_3 = stall_down_x
    stall_left_up_y_3 = stall_down_y + car_width
    stall_left_up_3 = [stall_left_up_x_3, stall_left_up_y_3]
    stall_3.append(stall_left_up_3)
    # 右上
    stall_right_up_x_3 = stall_down_x + car_length
    stall_right_up_y_3 = stall_down_y + car_width
    stall_right_up_3 = [stall_right_up_x_3, stall_right_up_y_3]
    stall_3.append(stall_right_up_3)
    # 右下
    stall_right_down_x_3 = stall_down_x + car_length
    stall_right_down_y_3 = stall_down_y
    stall_right_down_3 = [stall_right_down_x_3, stall_right_down_y_3]
    stall_3.append(stall_right_down_3)

    stall.append(stall_0)
    stall.append(stall_1)
    stall.append(stall_2)
    stall.append(stall_3)
    model_1["stall"] = stall
    model_1["lane"] = lane(model_list)
    return model_1


def model3(model_list):
    model_1 = {}
    stall = []
    # 上方三个模块坐标
    stall_x = model_list[1][0] + left_column
    stall_y = model_list[1][1]
    stall_0 = []
    # 左下 减去车长
    stall_left_down_x_0 = stall_x
    stall_left_down_y_0 = stall_y - car_width
    stall_left_down_0 = [stall_left_down_x_0, stall_left_down_y_0]
    stall_0.append(stall_left_down_0)
    # 左上
    stall_left_up_x_0 = stall_x
    stall_left_up_y_0 = stall_y
    stall_left_up_0 = [stall_left_up_x_0, stall_left_up_y_0]
    stall_0.append(stall_left_up_0)
    # 右上 加上车宽
    stall_right_up_x_0 = stall_x + car_length
    stall_right_up_y_0 = stall_y
    stall_right_up_0 = [stall_right_up_x_0, stall_right_up_y_0]
    stall_0.append(stall_right_up_0)
    # 右下 左下的y 右上的x
    stall_right_down_x_0 = stall_x + car_length
    stall_right_down_y_0 = stall_y - car_width
    stall_right_down_0 = [stall_right_down_x_0, stall_right_down_y_0]
    stall_0.append(stall_right_down_0)

    # 下方一个车位
    stall_3 = []
    stall_down_x = model_list[0][0] + left_column
    stall_down_y = model_list[0][1]
    # 左下 y加车宽
    stall_left_down_x_3 = stall_down_x
    stall_left_down_y_3 = stall_down_y
    stall_left_down_3 = [stall_left_down_x_3, stall_left_down_y_3]
    stall_3.append(stall_left_down_3)
    # 左上
    stall_left_up_x_3 = stall_down_x
    stall_left_up_y_3 = stall_down_y + car_width
    stall_left_up_3 = [stall_left_up_x_3, stall_left_up_y_3]
    stall_3.append(stall_left_up_3)
    # 右上
    stall_right_up_x_3 = stall_down_x + car_length
    stall_right_up_y_3 = stall_down_y + car_width
    stall_right_up_3 = [stall_right_up_x_3, stall_right_up_y_3]
    stall_3.append(stall_right_up_3)
    # 右下
    stall_right_down_x_3 = stall_down_x + car_length
    stall_right_down_y_3 = stall_down_y
    stall_right_down_3 = [stall_right_down_x_3, stall_right_down_y_3]
    stall_3.append(stall_right_down_3)
    stall.append(stall_0)
    stall.append(stall_3)
    model_1["stall"] = stall
    model_1["lane"] = lane(model_list)
    return model_1


def model4(model_list):
    model_1 = {}
    stall = []
    # 上方三个模块坐标
    stall_x = model_list[1][0] + left_column
    stall_y = model_list[1][1]

    stall_0 = []
    # 左下 减去车长
    stall_left_down_x_0 = stall_x
    stall_left_down_y_0 = stall_y - car_length
    stall_left_down_0 = [stall_left_down_x_0, stall_left_down_y_0]
    stall_0.append(stall_left_down_0)
    # 左上
    stall_left_up_x_0 = stall_x
    stall_left_up_y_0 = stall_y
    stall_left_up_0 = [stall_left_up_x_0, stall_left_up_y_0]
    stall_0.append(stall_left_up_0)
    # 右上 加上车宽
    stall_right_up_x_0 = stall_x + car_width
    stall_right_up_y_0 = stall_y
    stall_right_up_0 = [stall_right_up_x_0, stall_right_up_y_0]
    stall_0.append(stall_right_up_0)
    # 右下 左下的y 右上的x
    stall_right_down_x_0 = stall_x + car_width
    stall_right_down_y_0 = stall_y - car_length
    stall_right_down_0 = [stall_right_down_x_0, stall_right_down_y_0]
    stall_0.append(stall_right_down_0)
    # 第二个车位
    # 左下 上一个右下的坐标
    stall_1 = []
    stall_left_down_x_1 = stall_x + car_width
    stall_left_down_y_1 = stall_y - car_length
    stall_left_down_1 = [stall_left_down_x_1, stall_left_down_y_1]
    stall_1.append(stall_left_down_1)
    # 左上 上一个右上的坐标
    stall_left_up_x_1 = stall_x + car_width
    stall_left_up_y_1 = stall_y
    stall_left_up_1 = [stall_left_up_x_1, stall_left_up_y_1]
    stall_1.append(stall_left_up_1)
    # 右上 x加两个车宽
    stall_right_up_x_1 = stall_x + 2 * car_width
    stall_right_up_y_1 = stall_y
    stall_right_up_1 = [stall_right_up_x_1, stall_right_up_y_1]
    stall_1.append(stall_right_up_1)
    # 右下 左下的y 右上的x
    stall_right_down_x_1 = stall_x + 2 * car_width
    stall_right_down_y_1 = stall_y - car_length
    stall_right_down_1 = [stall_right_down_x_1, stall_right_down_y_1]
    stall_1.append(stall_right_down_1)

    # 第三个车位
    # 左下 上一个右下坐标
    stall_2 = []
    stall_left_down_x_2 = stall_x + 2 * car_width
    stall_left_down_y_2 = stall_y - car_length
    stall_left_down_2 = [stall_left_down_x_2, stall_left_down_y_2]
    stall_2.append(stall_left_down_2)
    # 左上 上一个右上坐标
    stall_left_up_x_2 = stall_x + 2 * car_width
    stall_left_up_y_2 = stall_y
    stall_left_up_2 = [stall_left_up_x_2, stall_left_up_y_2]
    stall_2.append(stall_left_up_2)
    # 右上
    stall_right_up_x_2 = stall_x + 3 * car_width
    stall_right_up_y_2 = stall_y
    stall_right_up_2 = [stall_right_up_x_2, stall_right_up_y_2]
    stall_2.append(stall_right_up_2)
    # 右下  左下的y 右上的x
    stall_right_down_x_2 = stall_x + 3 * car_width
    stall_right_down_y_2 = stall_y - car_length
    stall_right_down_2 = [stall_right_down_x_2, stall_right_down_y_2]
    stall_2.append(stall_right_down_2)
    stall.append(stall_0)
    stall.append(stall_1)
    stall.append(stall_2)
    model_1["stall"] = stall
    model_1["lane"] = lane(model_list)
    return model_1


def model5(model_list):
    model_1 = {}
    stall = []
    # 上方三个模块坐标
    stall_x = model_list[1][0] + left_column
    stall_y = model_list[1][1]

    stall_0 = []
    # 左下 减去车长
    stall_left_down_x_0 = stall_x
    stall_left_down_y_0 = stall_y - car_length
    stall_left_down_0 = [stall_left_down_x_0, stall_left_down_y_0]
    stall_0.append(stall_left_down_0)
    # 左上
    stall_left_up_x_0 = stall_x
    stall_left_up_y_0 = stall_y
    stall_left_up_0 = [stall_left_up_x_0, stall_left_up_y_0]
    stall_0.append(stall_left_up_0)
    # 右上 加上车宽
    stall_right_up_x_0 = stall_x + car_width
    stall_right_up_y_0 = stall_y
    stall_right_up_0 = [stall_right_up_x_0, stall_right_up_y_0]
    stall_0.append(stall_right_up_0)
    # 右下 左下的y 右上的x
    stall_right_down_x_0 = stall_x + car_width
    stall_right_down_y_0 = stall_y - car_length
    stall_right_down_0 = [stall_right_down_x_0, stall_right_down_y_0]
    stall_0.append(stall_right_down_0)
    # 第二个车位
    # 左下 上一个右下的坐标
    stall_1 = []
    stall_left_down_x_1 = stall_x + car_width
    stall_left_down_y_1 = stall_y - car_length
    stall_left_down_1 = [stall_left_down_x_1, stall_left_down_y_1]
    stall_1.append(stall_left_down_1)
    # 左上 上一个右上的坐标
    stall_left_up_x_1 = stall_x + car_width
    stall_left_up_y_1 = stall_y
    stall_left_up_1 = [stall_left_up_x_1, stall_left_up_y_1]
    stall_1.append(stall_left_up_1)
    # 右上 x加两个车宽
    stall_right_up_x_1 = stall_x + 2 * car_width
    stall_right_up_y_1 = stall_y
    stall_right_up_1 = [stall_right_up_x_1, stall_right_up_y_1]
    stall_1.append(stall_right_up_1)
    # 右下 左下的y 右上的x
    stall_right_down_x_1 = stall_x + 2 * car_width
    stall_right_down_y_1 = stall_y - car_length
    stall_right_down_1 = [stall_right_down_x_1, stall_right_down_y_1]
    stall_1.append(stall_right_down_1)

    # 模块1下方的车位
    stall_down_x = model_list[0][0] + left_column
    stall_down_y = model_list[0][1]
    stall_3 = []
    # 左下
    stall_left_down_x_3 = stall_down_x
    stall_left_down_y_3 = stall_down_y
    stall_left_down_3 = [stall_left_down_x_3, stall_left_down_y_3]
    stall_3.append(stall_left_down_3)
    # 左上
    stall_left_up_x_3 = stall_down_x
    stall_left_up_y_3 = stall_down_y + car_length
    stall_left_up_3 = [stall_left_up_x_3, stall_left_up_y_3]
    stall_3.append(stall_left_up_3)
    # 右上
    stall_right_up_x_3 = stall_down_x + car_width
    stall_right_up_y_3 = stall_down_y + car_length
    stall_right_up_3 = [stall_right_up_x_3, stall_right_up_y_3]
    stall_3.append(stall_right_up_3)
    # 右下
    stall_right_down_x_3 = stall_down_x + car_width
    stall_right_down_y_3 = stall_down_y
    stall_right_down_3 = [stall_right_down_x_3, stall_right_down_y_3]
    stall_3.append(stall_right_down_3)

    # 下方车位2
    # 左下 上一个车位右下
    stall_4 = []
    stall_left_down_x_4 = stall_down_x + car_width
    stall_left_down_y_4 = stall_down_y
    stall_left_down_4 = [stall_left_down_x_4, stall_left_down_y_4]
    stall_4.append(stall_left_down_4)
    # 左上 上一个车位右上
    stall_left_up_x_4 = stall_down_x + car_width
    stall_left_up_y_4 = stall_down_y + car_length
    stall_left_up_4 = [stall_left_up_x_4, stall_left_up_y_4]
    stall_4.append(stall_left_up_4)
    # 右上
    stall_right_up_x_4 = stall_down_x + 2 * car_width
    stall_right_up_y_4 = stall_down_y + car_length
    stall_right_up_4 = [stall_right_up_x_4, stall_right_up_y_4]
    stall_4.append(stall_right_up_4)
    # 右下
    stall_right_down_x_4 = stall_down_x + 2 * car_width
    stall_right_down_y_4 = stall_down_y
    stall_right_down_4 = [stall_right_down_x_4, stall_right_down_y_4]
    stall_4.append(stall_right_down_4)

    stall.append(stall_0)
    stall.append(stall_1)
    stall.append(stall_3)
    stall.append(stall_4)
    model_1["stall"] = stall
    model_1["lane"] = lane(model_list)
    return model_1


def model6(model_list):
    model_1 = {}
    stall = []
    # 上方三个模块坐标
    stall_x = model_list[1][0] + left_column
    stall_y = model_list[1][1]

    stall_0 = []
    # 左下 减去车长
    stall_left_down_x_0 = stall_x
    stall_left_down_y_0 = stall_y - car_length
    stall_left_down_0 = [stall_left_down_x_0, stall_left_down_y_0]
    stall_0.append(stall_left_down_0)
    # 左上
    stall_left_up_x_0 = stall_x
    stall_left_up_y_0 = stall_y
    stall_left_up_0 = [stall_left_up_x_0, stall_left_up_y_0]
    stall_0.append(stall_left_up_0)
    # 右上 加上车宽
    stall_right_up_x_0 = stall_x + car_width
    stall_right_up_y_0 = stall_y
    stall_right_up_0 = [stall_right_up_x_0, stall_right_up_y_0]
    stall_0.append(stall_right_up_0)
    # 右下 左下的y 右上的x
    stall_right_down_x_0 = stall_x + car_width
    stall_right_down_y_0 = stall_y - car_length
    stall_right_down_0 = [stall_right_down_x_0, stall_right_down_y_0]
    stall_0.append(stall_right_down_0)
    # 第二个车位
    # 左下 上一个右下的坐标
    stall_1 = []
    stall_left_down_x_1 = stall_x + car_width
    stall_left_down_y_1 = stall_y - car_length
    stall_left_down_1 = [stall_left_down_x_1, stall_left_down_y_1]
    stall_1.append(stall_left_down_1)
    # 左上 上一个右上的坐标
    stall_left_up_x_1 = stall_x + car_width
    stall_left_up_y_1 = stall_y
    stall_left_up_1 = [stall_left_up_x_1, stall_left_up_y_1]
    stall_1.append(stall_left_up_1)
    # 右上 x加两个车宽
    stall_right_up_x_1 = stall_x + 2 * car_width
    stall_right_up_y_1 = stall_y
    stall_right_up_1 = [stall_right_up_x_1, stall_right_up_y_1]
    stall_1.append(stall_right_up_1)
    # 右下 左下的y 右上的x
    stall_right_down_x_1 = stall_x + 2 * car_width
    stall_right_down_y_1 = stall_y - car_length
    stall_right_down_1 = [stall_right_down_x_1, stall_right_down_y_1]
    stall_1.append(stall_right_down_1)

    stall_3 = []
    stall_down_x = model_list[0][0] + left_column
    stall_down_y = model_list[0][1]
    # 左下 y加车宽
    stall_left_down_x_3 = stall_down_x
    stall_left_down_y_3 = stall_down_y
    stall_left_down_3 = [stall_left_down_x_3, stall_left_down_y_3]
    stall_3.append(stall_left_down_3)
    # 左上
    stall_left_up_x_3 = stall_down_x
    stall_left_up_y_3 = stall_down_y + car_width
    stall_left_up_3 = [stall_left_up_x_3, stall_left_up_y_3]
    stall_3.append(stall_left_up_3)
    # 右上
    stall_right_up_x_3 = stall_down_x + car_length
    stall_right_up_y_3 = stall_down_y + car_width
    stall_right_up_3 = [stall_right_up_x_3, stall_right_up_y_3]
    stall_3.append(stall_right_up_3)
    # 右下
    stall_right_down_x_3 = stall_down_x + car_length
    stall_right_down_y_3 = stall_down_y
    stall_right_down_3 = [stall_right_down_x_3, stall_right_down_y_3]
    stall_3.append(stall_right_down_3)

    stall.append(stall_0)
    stall.append(stall_1)
    stall.append(stall_3)
    model_1["stall"] = stall
    model_1["lane"] = lane(model_list)
    return model_1


def model7(model_list):
    model_1 = {}
    stall = []
    # 上方三个模块坐标
    stall_x = model_list[1][0] + left_column
    stall_y = model_list[1][1]

    stall_0 = []
    # 左下 减去车长
    stall_left_down_x_0 = stall_x
    stall_left_down_y_0 = stall_y - car_length
    stall_left_down_0 = [stall_left_down_x_0, stall_left_down_y_0]
    stall_0.append(stall_left_down_0)
    # 左上
    stall_left_up_x_0 = stall_x
    stall_left_up_y_0 = stall_y
    stall_left_up_0 = [stall_left_up_x_0, stall_left_up_y_0]
    stall_0.append(stall_left_up_0)
    # 右上 加上车宽
    stall_right_up_x_0 = stall_x + car_width
    stall_right_up_y_0 = stall_y
    stall_right_up_0 = [stall_right_up_x_0, stall_right_up_y_0]
    stall_0.append(stall_right_up_0)
    # 右下 左下的y 右上的x
    stall_right_down_x_0 = stall_x + car_width
    stall_right_down_y_0 = stall_y - car_length
    stall_right_down_0 = [stall_right_down_x_0, stall_right_down_y_0]
    stall_0.append(stall_right_down_0)
    # 模块1下方的车位
    stall_down_x = model_list[0][0] + left_column
    stall_down_y = model_list[0][1]
    stall_3 = []
    # 左下
    stall_left_down_x_3 = stall_down_x
    stall_left_down_y_3 = stall_down_y
    stall_left_down_3 = [stall_left_down_x_3, stall_left_down_y_3]
    stall_3.append(stall_left_down_3)
    # 左上
    stall_left_up_x_3 = stall_down_x
    stall_left_up_y_3 = stall_down_y + car_length
    stall_left_up_3 = [stall_left_up_x_3, stall_left_up_y_3]
    stall_3.append(stall_left_up_3)
    # 右上
    stall_right_up_x_3 = stall_down_x + car_width
    stall_right_up_y_3 = stall_down_y + car_length
    stall_right_up_3 = [stall_right_up_x_3, stall_right_up_y_3]
    stall_3.append(stall_right_up_3)
    # 右下
    stall_right_down_x_3 = stall_down_x + car_width
    stall_right_down_y_3 = stall_down_y
    stall_right_down_3 = [stall_right_down_x_3, stall_right_down_y_3]
    stall_3.append(stall_right_down_3)
    stall.append(stall_0)
    stall.append(stall_3)
    model_1["stall"] = stall
    model_1["lane"] = lane(model_list)
    return model_1


def model8(model_list):
    model_1 = {}
    stall = []
    # 上方三个模块坐标
    stall_x = model_list[1][0] + left_column
    stall_y = model_list[1][1]

    stall_0 = []
    # 左下 减去车长
    stall_left_down_x_0 = stall_x
    stall_left_down_y_0 = stall_y - car_length
    stall_left_down_0 = [stall_left_down_x_0, stall_left_down_y_0]
    stall_0.append(stall_left_down_0)
    # 左上
    stall_left_up_x_0 = stall_x
    stall_left_up_y_0 = stall_y
    stall_left_up_0 = [stall_left_up_x_0, stall_left_up_y_0]
    stall_0.append(stall_left_up_0)
    # 右上 加上车宽
    stall_right_up_x_0 = stall_x + car_width
    stall_right_up_y_0 = stall_y
    stall_right_up_0 = [stall_right_up_x_0, stall_right_up_y_0]
    stall_0.append(stall_right_up_0)
    # 右下 左下的y 右上的x
    stall_right_down_x_0 = stall_x + car_width
    stall_right_down_y_0 = stall_y - car_length
    stall_right_down_0 = [stall_right_down_x_0, stall_right_down_y_0]
    stall_0.append(stall_right_down_0)
    # 第二个车位
    # 左下 上一个右下的坐标
    stall_1 = []
    stall_left_down_x_1 = stall_x + car_width
    stall_left_down_y_1 = stall_y - car_length
    stall_left_down_1 = [stall_left_down_x_1, stall_left_down_y_1]
    stall_1.append(stall_left_down_1)
    # 左上 上一个右上的坐标
    stall_left_up_x_1 = stall_x + car_width
    stall_left_up_y_1 = stall_y
    stall_left_up_1 = [stall_left_up_x_1, stall_left_up_y_1]
    stall_1.append(stall_left_up_1)
    # 右上 x加两个车宽
    stall_right_up_x_1 = stall_x + 2 * car_width
    stall_right_up_y_1 = stall_y
    stall_right_up_1 = [stall_right_up_x_1, stall_right_up_y_1]
    stall_1.append(stall_right_up_1)
    # 右下 左下的y 右上的x
    stall_right_down_x_1 = stall_x + 2 * car_width
    stall_right_down_y_1 = stall_y - car_length
    stall_right_down_1 = [stall_right_down_x_1, stall_right_down_y_1]
    stall_1.append(stall_right_down_1)
    stall.append(stall_0)
    stall.append(stall_1)
    model_1["stall"] = stall
    return model_1


def model9(model_list):
    model_1 = {}
    stall = []
    # 上方三个模块坐标
    stall_x = model_list[1][0] + left_column
    stall_y = model_list[1][1]

    stall_0 = []
    # 左下 减去车长
    stall_left_down_x_0 = stall_x
    stall_left_down_y_0 = stall_y - car_length
    stall_left_down_0 = [stall_left_down_x_0, stall_left_down_y_0]
    stall_0.append(stall_left_down_0)
    # 左上
    stall_left_up_x_0 = stall_x
    stall_left_up_y_0 = stall_y
    stall_left_up_0 = [stall_left_up_x_0, stall_left_up_y_0]
    stall_0.append(stall_left_up_0)
    # 右上 加上车宽
    stall_right_up_x_0 = stall_x + car_width
    stall_right_up_y_0 = stall_y
    stall_right_up_0 = [stall_right_up_x_0, stall_right_up_y_0]
    stall_0.append(stall_right_up_0)
    # 右下 左下的y 右上的x
    stall_right_down_x_0 = stall_x + car_width
    stall_right_down_y_0 = stall_y - car_length
    stall_right_down_0 = [stall_right_down_x_0, stall_right_down_y_0]
    stall_0.append(stall_right_down_0)
    stall.append(stall_0)
    model_1["stall"] = stall
    model_1["lane"] = lane(model_list)
    return model_1


def model10(model_list):
    model_1 = {}
    stall = []
    # 上方三个模块坐标
    stall_x = model_list[1][0] + left_column
    stall_y = model_list[1][1]
    stall_0 = []
    # 左下 减去车长
    stall_left_down_x_0 = stall_x
    stall_left_down_y_0 = stall_y - car_width
    stall_left_down_0 = [stall_left_down_x_0, stall_left_down_y_0]
    stall_0.append(stall_left_down_0)
    # 左上
    stall_left_up_x_0 = stall_x
    stall_left_up_y_0 = stall_y
    stall_left_up_0 = [stall_left_up_x_0, stall_left_up_y_0]
    stall_0.append(stall_left_up_0)
    # 右上 加上车宽
    stall_right_up_x_0 = stall_x + car_length
    stall_right_up_y_0 = stall_y
    stall_right_up_0 = [stall_right_up_x_0, stall_right_up_y_0]
    stall_0.append(stall_right_up_0)
    # 右下 左下的y 右上的x
    stall_right_down_x_0 = stall_x + car_length
    stall_right_down_y_0 = stall_y - car_width
    stall_right_down_0 = [stall_right_down_x_0, stall_right_down_y_0]
    stall_0.append(stall_right_down_0)
    stall.append(stall_0)
    model_1["stall"] = stall
    model_1["lane"] = lane(model_list)
    return model_1


print(model10(model))
