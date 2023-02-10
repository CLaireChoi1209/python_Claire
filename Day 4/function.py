"""
함수
- 반복적인 작업을 할때 유용하게 사용함. 
- 특징) 만드는 과정과 사용하는 절차로 구분됨.
- 여러번 재사용 가능함.

<문법 1>
def 함수이름():
    함수 내용 작성
함수이름()

<문법 2>
def 함수이름(입력):
    함수 내용 작성(입력이 포함해야 함)
함수이름(입력내용)

- 함수 만들 때 입력은 변수로 해야함
- 함수를 사용할 때 입력내용은 값을 적어야 함.
- 여러 개의 입력도 가능함.
- 여러개를 입력으로 사용할 때는 쉼표로 구분
- ex) 입력1, 입력2

<문법 3>
def 함수이름(입력):
    함수 내용 작성(입력이 포함해야 함)
returm 출력

- 함수 만들 때 출출력은 변수로 해야함
- 함수를 사용할 때 출력내용은 값을 적어야 함.
"""


"""def 웅수():
    print("웅수 출두요~")


웅수()
웅수()
웅수()


def 써웅(숫자):
    for i in range(숫자):
        print("써웅양농장")


써웅(1)


def 삼각형넓이(밑변, 높이):
    결과 = 밑변 * 높이 / 2
    return 결과


넓이 = 삼각형넓이(6, 4)
print(넓이)

print(삼각형넓이(3, 2))"""


"""# 1번     나머지 나오는 함수
def 나머지(a, b):
    결과 = a % b
    return 결과


print(나머지(100, 2))
print(나머지(200, 3))"""


"""# 2번     사칙연산
def 합차곱나(a, b):
    결과 = a + b, a - b, a * b, a / b
    return 결과


print(합차곱나(10, 2))
print(합차곱나(9, 3))"""


# 3번     구구단
def 구구단(a):
    결과 = a * 1, a * 2, a * 3, a * 4, a * 5, a * 6, a * 7, a * 8, a * 9
    return 결과


print(구구단(4))
print(구구단(6))