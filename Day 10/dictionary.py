"""
딕셔너리(dictionary)
- python에서 사용하는 자료구조 중 하나
- Key와 value 쌍으로 존재함.
- 중괄호와:를 이용해 작성
- indexing 하는 방법
1.딕셔너리[key]를 이용(딕셔너리에서 순서=중요하지X)
2.get method 사용
-value를 수정하는 방법
1. indexing 이용함
2. update method 이용
-key&value를 추가하는 방법
1. indexing 이용함
2. update method 이용
-삭제하는 밤법
del 딕셔너리[key]
-key를 확인하는 문법
: key in 딕셔너리
"""
리스트 = [1, 2, 3]
튜플 = (1, 2, 3)
딕셔너리 = {"축구": "손흥민", "야구": "이대호"}
딕셔너리["야구"] = "류현진"
print(딕셔너리.get("축구"))
print(딕셔너리["축구"])
print(딕셔너리["야구"])
a = [10, 20, 30]
딕셔너리.update({"야구": "추신수"})
print(딕셔너리)
딕셔너리["피겨"] = "김연아"
딕셔너리.update({"배구": "김연경"})
print(딕셔너리)
del 딕셔너리["축구"]
del 딕셔너리["피겨"]
print(딕셔너리)
print("야구" in 딕셔너리)
print("농구" in 딕셔너리)

fruits = {"orange": 50, "apple": 100, "banana": 200}
fruit = input("This is fruit store. What do you want?:")
if fruit in fruits:
    print(f"we have {fruit}. {fruits[fruit]} left!")
else:
    print(f"Sorry, we don't have {fruit}")
