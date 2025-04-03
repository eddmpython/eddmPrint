import sys
sys.path.append('src')

# 일반 프린트 테스트
print("1. 일반 프린트 테스트")

# EddmPrint 임포트
from eddmPrint.printer import EddmPrint
from eddmPrint.colors import Colors

# 색상 테스트
print(f"{Colors.RED}2. 빨간색 테스트{Colors.RESET}")

# EddmPrint 인스턴스 생성 및 사용
printer = EddmPrint()
printer.start()

# 프린트 테스트
print("3. EddmPrint 테스트")

# 원래 프린트로 복원
printer.restore()

print("4. 테스트 완료") 