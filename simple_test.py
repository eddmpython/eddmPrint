import sys
sys.path.append('src')

# 기본 프린트
print("1. 기본 프린트 테스트")

# 색상 코드 임포트 및 테스트
from eddmPrint.colors import Colors
print(f"{Colors.RED}2. 빨간색 텍스트{Colors.RESET}")

# 완료 메시지
print("테스트 완료") 