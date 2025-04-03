import sys
import os

# 현재 디렉토리 기준으로 src 경로 추가
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(current_dir, 'src'))

from eddmPrint import EddmPrint, Colors, Templates

def test_function():
    print("함수 내에서 호출된 프린트입니다.")

# ===== 기본 예제 =====
print("\n===== 기본 예제 =====")
printer = EddmPrint()
printer.start()
print("Hello, World!")
test_function()
printer.restore()

# ===== 색상 예제 =====
print("\n===== 색상 예제 =====")
# 녹색
printer = EddmPrint(color=Colors.GREEN)
printer.start()
print("녹색으로 표시됩니다")
printer.restore()

# 빨간색
printer = EddmPrint(color=Colors.RED)
printer.start()
print("빨간색으로 표시됩니다")
printer.restore()

# 파란색
printer = EddmPrint(color=Colors.BLUE)
printer.start()
print("파란색으로 표시됩니다")
printer.restore()

# ===== 템플릿 예제 =====
print("\n===== 템플릿 예제 =====")
# 기본 템플릿
printer = EddmPrint()
printer.start()
print("기본 템플릿입니다")
printer.restore()

# 간단한 템플릿
printer = EddmPrint(prefixTemplate=Templates.SIMPLE)
printer.start()
print("간단한 템플릿입니다")
printer.restore()

# 함수만 표시하는 템플릿
printer = EddmPrint(prefixTemplate=Templates.FUNCTION_ONLY)
printer.start()
print("함수명만 표시하는 템플릿입니다")
printer.restore()

# 사용자 정의 템플릿
custom_template = "📍 위치: {file}의 {line}번째 줄"
printer = EddmPrint(prefixTemplate=custom_template)
printer.start()
print("사용자 정의 템플릿입니다")
printer.restore()

print("\n모든 예제가 완료되었습니다. 스크린샷을 찍어서 images 폴더에 저장하세요.") 