import sys
sys.path.append('src')

from eddmPrint import EddmPrint, Colors, Templates

# 기본 테스트
printer = EddmPrint()
printer.start()
print("기본 출력 테스트")
printer.restore()

# 색상 테스트
printer = EddmPrint(color=Colors.GREEN)
printer.start()
print("녹색 출력 테스트")
printer.restore()

# 템플릿 테스트
printer = EddmPrint(prefixTemplate=Templates.SIMPLE)
printer.start()
print("간단한 템플릿 테스트")
printer.restore()

print("모든 테스트 완료!") 