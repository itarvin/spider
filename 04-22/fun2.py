#coding=utf-8
# 定义汽车类
# class Car:
#
#     def __init__(self):
#         self.wheelNum = 4
#         self.color = '蓝色'
#
#     def move(self):
#         print('车在跑，目标:夏威夷')
#
# # 创建对象
# BMW = Car()
#
# print('车的颜色为:%s'%BMW.color)
# print('车轮胎数量为:%d'%BMW.wheelNum)


# 定义汽车类
# class Car:
#
#     def __init__(self, newWheelNum, newColor):
#         self.wheelNum = newWheelNum
#         self.color = newColor
#
#     def move(self):
#         print('车在跑，目标:夏威夷')
#
# # 创建对象
# BMW = Car(4, 'green')
#
# print('车的颜色为:%s'%BMW.color)
# print('车轮子数量为:%d'%BMW.wheelNum)



class Car:

    def __init__(self, newWheelNum, newColor):
        self.wheelNum = newWheelNum
        self.color = newColor

    def __str__(self):
        msg = "嘿。。。我的颜色是" + self.color + "我有" + self.wheelNum + "个轮胎..."
        return msg

    def move(self):
        print('车在跑，目标:夏威夷')


BMW = Car(4, "白色")
print(BMW)
