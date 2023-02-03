"""
반복문(while)
- 조건인 참인 동안에 코드를 실행
- 조건이 거짓이면 while이 종료
<문법>
while 조건:
    반복할 코드 작성

<중요>
조건을 true로 정하면 무한반복 됨. 
"""
# 예제
# while True:
#   print("지웅이바보")

# while False:
#   print("성웅항잉")
"""i = 1
while i<11:
    print(i)
    i+=1

i = 1
while i<11:
    if i%2==0
        print(i)
    i+=1
    """

"""i = 10
while i < 21:
    if i % 3 != 0:
        print(i)
    i += 1
"""
"""i = 50
while i < 101:
    if i % 3 == 0:
        if i % 4 == 0:
            print(i)
    i += 1"""

"""sum = 0
i = 20
while i < 31:
    if i % 5 != 0:
        sum += i
    i += 1
print(sum)"""

"""sum = 0
i = 20
while i < 31:
    if i % 5 != 0:
        sum += i
    i += 1
print(sum)"""
sum1 = 0
sum2 = 0
i = 1
while i < 101:
    if i % 2 == 0:
        sum1 += i
    else:
        sum2 += i
print(sum1 - sum2)
i += 1
