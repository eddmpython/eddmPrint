from eddmPrint import EddmPrint

# 기본 설정으로 시작
printer = EddmPrint()
printer.start()

# 이제 print는 자동으로 위치 정보를 포함합니다
print("Hello, World!")

# 원래 print 함수로 복원
printer.restore()

# 메서드 체이닝 사용 예시
EddmPrint().start()
print("메서드 체이닝 예시") 