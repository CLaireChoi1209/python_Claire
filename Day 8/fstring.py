"""
fstring
- 변수와 문자를 같이 사용하는 문법
-f"문자"=>문법
-f" "안에 변수는 중괄호 {} 이용
"""
str = "나는 13살이고, 이름은 말랑밀랑이에요"
print(str)

age = 19
name = "오노"
str2 = f"나는 {age}살 이고, 이름은 {name}이에요"
print(str2)

season = "겨울"
month = 12
day = 25
str3 = f"오늘은 {season}이고, 날짜는 {month}월 {day}일 입니다. "
print(str3)
