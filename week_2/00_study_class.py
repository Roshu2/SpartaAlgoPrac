class Person:
    def __init__(self, param_name): # self는 파이썬이 자기자신을 인자로 넘겨준다.
        print("i am created!", self)
        self.name = param_name

    def talk(self):
        print("안녕하세요, 제 이름은", self.name, "입니다.")


person_1 = Person("유재석") # constructor 생성자
print(person_1.name)
person_1.talk()
person_2 = Person("박명수")
print(person_2)