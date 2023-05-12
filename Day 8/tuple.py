"""
튜플(tuple)
- python에서 사용하는 자료구조중 하나
- list와 비슷하며, 여러 값들을 모아두는 형태
- 소괄호를 이용해 표현함. ex. ()
# List와 Tuple의 차이점
- List는 mutable 값
- Tuple은 immutable 값
- indexing 가능
"""
a = [1, 2, 3]
a[2] = 100
print(a)
b = (1, 2, 3)
b[2] = 100
print(b)
