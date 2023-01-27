"""
조건문
<if/else>
js
var 오늘날씨=맑음;
if(오늘날씨==비){
    console.log("우산쓰셈");
    }else{
        console.log("그냥가셈")
        
}
py
오늘날씨="맑음"
if 오늘날씨=="비"
    print("우산쓰셈")
else:
    print("그냥가셈")

    {-> = 들여쓰기(tab 또는 space)}

    if 조건:
        참일때 실행할 코드
        else:
            거짓일때 실행한 코드

 - 조건=true or false로 답할수 있는 질문
 <For>
 js
 for(var i=0;i<3;i++){
    console("서우야");
 }
 py
 for i in range(3):
    print("서우야")
1번방법
for 변수 in range(숫자):
    실행할 코드

2번방법
for 변수 in range (시작,끝)
    실행할 코드
시작수=이상
끝수=미만

3번 방법
for 변수 in range(시작,끝,증감):
    실행할 코드

<☆☆☆중요한 부분>
아래는 모두 같은 코드임
1번 for i ing range(5):
    print("파이썬)

2번 for i ing range(0,5):
    print("파이썬)    

3번 for i ing range(0,5,1):
    print("파이썬)
"""
# 오늘날씨 = "비"
# if 오늘날씨 == "비":
#     print("우산쓰셈")
# else:
#     print("그냥가셈")

# for i in range(3):
#     print("서우야")

# for i in range(1, 11):
#     print(i)

# for i in range(25, 36):
#     print(i)

# for i in range(2, 11, 2):
#     print(i)


for i in range(7):  # =7번반복 1번
    print("내일은 토요일")

for i in range(3, 11, 3):  # =1~10중에 3배수 2번번
    print(i)

sum = 0  # =1~20 4배수 아닌수
for i in range(1, 21, 1):
    if i % 4 != 0:
        sum += i

print(sum)

for i in range(50, 101): #50~100까지 3,4 공배수
    if i % 3 == 0:
        if i % 4 == 0:
            print(i)

sum = 0
mul = 1
for i in range(1, 101): #1~100까지수중 짝수의 합 - 홀수의 합
    if i % 2 == 0:
        mul += i
    if i % 2 == 1:
        sum += i
print(mul - sum)
