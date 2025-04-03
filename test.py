"""
eddmPrint 라이브러리 사용 예제
"""
from eddmPrint import printer, Colors, Templates

# 이미 printer가 자동으로 시작되어 있음 (start() 호출 필요 없음)
print("안녕하세요! 기본 설정으로 출력")

# 색상 변경 예제
printer.setColor(Colors.RED)
print("빨간색으로 출력")

printer.setColor(Colors.GREEN)
print("초록색으로 출력")

printer.setColor(Colors.BLUE)
print("파란색으로 출력")

# 템플릿 변경 예제
printer.setPrefixTemplate(Templates.SIMPLE)
print("간단한 템플릿으로 출력")

printer.setPrefixTemplate(Templates.DETAILED)
print("상세한 템플릿으로 출력")

# 일반 출력으로 복원
printer.restore()
print("일반 출력 (프린터 비활성화)")

# 다시 활성화
printer.start()
print("다시 활성화된 출력")

