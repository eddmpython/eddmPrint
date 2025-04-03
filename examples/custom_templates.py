from eddmPrint import EddmPrint, Colors, Templates

# 다양한 색상과 템플릿 조합 사용
printer = EddmPrint(color=Colors.GREEN, prefixTemplate=Templates.SIMPLE)
printer.start()

print("간단한 템플릿으로 표시됩니다")

# 색상 변경
printer.setColor(Colors.RED)
print("빨간색으로 표시됩니다")

# 템플릿 변경
printer.setPrefixTemplate(Templates.DETAILED)
print("자세한 템플릿으로 표시됩니다")

# 사용자 정의 템플릿
custom_template = "📍 {file}:{line}"
printer.setPrefixTemplate(custom_template)
print("이모지와 함께 표시됩니다")

# 원래 print 함수로 복원
printer.restore() 