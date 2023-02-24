"""
리스트(list)
열거형 변수를 나타내는 자료구조 중 하나
<문법>
대괄호로 묶어주고, 요소들은 쉼표로 구분
비어있는 리스트는 "[]" 표현
요소들의 값은 indexing으로 가져올수 있음
-왼쪽에서 오른쪽ㅇ으로 인덱싱 할때는 0,1,2번째 순서로 정해짐
-오른쪽에서 왼쪽으로 인덱싱 할 때는 -1,-2,-3번째 순서로  정해짐
<특징1>
요소를 추가할 떄 append 메소드를 사용
*오른쪽에 요소가 추가됨
<특징2>
요소를 삭제할 때 pop 메소드를 사용
*오른쪽에 요소가 삭제됨
<특징3>
리스트 초기화 할때 clear 메소드 사용
<특징4>
오름차순 정렬할때 sort 메소드 사용
<특징5>
거꾸로 정렬 할때 reverse 메소드 사용
<특징6>
index
값으로 자릴를 찾을 때 사용하는 메소드
<특징7>
indexing
자리로 값를 찾는 문법(6이랑 반대)

<문법>
indexing 할떄 대괄호와 숫자를 사용
<특징8>
count
값이 몇개있는지 알아보는 메소드
<특징9>
내가 원하는 위치에 값을 끼워 넣을때 insert 메소드 사용
<특징10>
내가 원하는 값을 지울떄 remove 메소드 사용
<특징11>
리스트와 리스트를 결합할떄 extend 메소드 사용
<특징12>
리스트와 리스트를 결합할떄 + 연산자 사용
<특징13>
리스트의 길이를 구하는 함수는 len 함수 사용
<특14>
for와 리스트를 결합한 문법
Q.sort()
Q.reverse()
=내림차순
print(Q)
"""
"""a = [1, 2, 3]
print(a)
b = ["사과", "바나나", "귤"]
print(b)
c = [13, "지웅", 2011, "온유"]
print(c)
d = []
print(d)
e = [13, 53, 345, 54]
print(e[3])
f = [1, 2, 3]
print([2])
g = [1, 2, 3]
print(a[-2]%a[2])
"""
# a = []
# a.append(10)
# print(a)
# a.append(20)
# print(a)
# a.append(30)
# print(a)
"""결과 = []
for i in range(1, 11):
    결과.append(i)
print(결과)

b = [1, 2, 3, 4]
b.pop()

b.pop()
print(b)

c = ["사과", "바나나", "귤"]
c.clear()
print(c)

d = [2, 4, 1, 3]
d.sort()
print(d)

e = ["banana", "cherry", "apple"]
e.sort()
print(e)

f = [2, 4, 1, 3]
f.reverse()
print(f)

g = ["banana", "cherry", "apple"]
g.reverse()
print(g)"""

"""# 1번
Q = [2, 4, 1, 3]
Q.sort()
Q.reverse()
print(Q)

# 2번
R = ["banana", "cherry", "apple"]
R.sort()
R.reverse()
print(R)

결과 = []
for i in range(1, 11):
    결과.append(i)
    결과.sort()
결과.reverse()
print(결과)

a = [100, 200, 300]

print(a.index(100))
print(a.index(200))
print(a.index(300))
print(a[0])
print(a[1])
print(a[2])

b = [1, 20, 30, 40]
print(b[-1] * b[2])
print(b[-2] % b[1])
"""
"""c = [1, 2, 3, 1, 4]
print(c.count(2))
print(c.count(1))
print(c.count(7))
print(c.index(1))

d = [1, 2, 3]
d.insert(1, 100)
print(d)
d.insert(1, 200)
print(d)"""

"""e = [100, 200, 10, 300]
e.remove(10)
print(e)
e.remove(200)
print(e)
"""
"""f = [1, 2]
g = [3, 4, 5]
f.extend(g)
print(g)
g.extend(f)
print(g)

i = [100, 200]
j = [300, 400, 500]
print(i + j)
print(j + i)"""

k = [10, 20, 30]
print(len(k))
k.append(40)
print(len(k))
k.clear()
print(len(k))

fruit = ["cherry", "apple", "banana"]
for i in range(len(fruit)):
    print(fruit[i])

for fruits in fruit:
    print(fruits)
