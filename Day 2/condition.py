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

for i in range(2, 11, 2):
    print(i)
