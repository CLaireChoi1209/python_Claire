"""
클래스(class)
-객체(object)를 생성하기 위한 설계도(class)
-생성된 객체를 인스턴스(instance)라고 함.
-문법
class 클래스이름:
->프로퍼티(property)
->메소드(method)
클래스 내 멤버변수를 '프로퍼티'라고 함
클래스 내 멤버함수를 '메소드'라고 함
"""


class 수학:
    원주율 = 3.14

    def 더하기(self, a, b):
        결과 = a + b
        return 결과

    def 빼기(self, a, b):
        결과 = a - b
        return 결과

    def 곱하기(self, a, b):
        결과 = a * b
        return 결과

    def 나누기(self, a, b):
        결과 = a / b
        return 결과


유치원수학 = 수학()
print(유치원수학.더하기(3, 4))
유치원수학 = 수학()
print(유치원수학.빼기(10, 5))
초등수학 = 수학()
print(초등수학.원주율)
초등수학 = 수학()
print(초등수학.곱하기(7, 7))
print(초등수학.나누기(77, 11))
중등수학 = 수학()
중등수학 = 수학()
print(중등수학.원주율)
고등수학 = 수학()
print(고등수학.원주율)
대학수학 = 수학()
print(대학수학.원주율)


첫번째수 = input("첫번째수는:")
두번째수 = input("두번째수는:")
print(f"첫번째수가 11{첫번째수}이고, 두번째수가 {두번째수}이면 두수의 합은~?! {초등수학.더하기(int(첫번째수),int(두번째수))}")
