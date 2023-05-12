"""
슬라이싱(slicing)
-범위가 필요함
-indexing과 구별됨
-범위표현은 :을 이용함
-ㅇ:ㅁ;ㅇ이상 ㅁ미만
-시작이 0일때 생략가능
-마지막이 끝일때 생략가능
"""
a = [10, 20, 30, 40, 50]
print(a[2])
print(a[:3])
print(a[1:4])
print(a[:2])
print(a[:])

fruits = ["banana", "orange", "apple", "peach"]
fruits.pop()
fruits.sort()
fruits.append("watermelon")
print(fruits[3:])
