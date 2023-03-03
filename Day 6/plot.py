"""
o 모듈 설치

terminal 창에서
>>pip install 모듈이름

o 모듈 가져오기
import 모듈이름
"""
import matplotlib.pyplot as p

"""fruits = ["apple", "orange", "watermelon", "banana", "cherry"]
counts = [5, 2, 10, 7, 20]
barcolor = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
]
창, 내용 = p.subplots(2, 1)
내용[0].barh(fruits, counts, color=barcolor)
내용[1].bar(fruits, counts, color=barcolor)
p.show()
"""
heights = ["130", "140", "150", "160"]
counts = [3, 10, 7, 3]
barcolor = ["rosybrown", "olivedrab", "steelblue", "slateblue"]
창, 내용 = p.subplots(1, 1)
내용.bar(heights, counts, color=barcolor)
p.show()
