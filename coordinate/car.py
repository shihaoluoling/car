# ģ������
model = [[-274.920461, -188.934746], [-274.920461, -172.434746], [-266.82046099999997, -172.434746],
         [-266.82046099999997, -188.934746]]
# ����������
left_column = 0
# ����������
right_column = 0
# ����
car_length = 0
# ����
car_width = 0
# ���ӳ���
column = 0

# ����


def lane():
    lane_arr = []
    # �������½�����
    left_lane_down_x = model[0][0]
    left_lane__down_y = model[0][1] + car_length
    lane_arr.append(left_lane_down_x)
    lane_arr.append(left_lane__down_y)
    # �������Ͻ�����
    left_lane_up_x = model[1][0]
    left_lane__up_y = model[1][1] - car_length
    # �������Ͻ�����
    right_lane_down_x = model[2][0]
    right_lane_down_y = model[2][1] - car_length
    # �������½�����
    right_lane_down_x = model[3][0]
    right_lane_down_y = model[3][1] + car_length


def model1():
    for a in range(4):
        print(a)


print(model1())
