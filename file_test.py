import sys
sys.path.append('src')

from eddmPrint.printer import EddmPrint
from eddmPrint.colors import Colors

# 로그 파일 생성
with open('test_log.txt', 'w') as f:
    f.write("--- 테스트 시작 ---\n")
    f.write("1. 일반 출력 테스트\n")
    
    # 색상 테스트
    f.write(f"2. 색상 테스트 (콘솔에서만 보임)\n")
    
    # EddmPrint 인스턴스 생성
    f.write("3. EddmPrint 초기화\n")
    printer = EddmPrint()
    
    # 프린트 래핑
    f.write("4. print 함수 래핑\n")
    original_print = print
    def log_print(*args, **kwargs):
        text = ' '.join(str(arg) for arg in args)
        f.write(f"출력: {text}\n")
        original_print(*args, **kwargs)
    
    print = log_print
    
    # EddmPrint 테스트
    f.write("5. EddmPrint 테스트\n")
    printer.start()
    print("EddmPrint 테스트 메시지")
    printer.restore()
    
    # 테스트 완료
    f.write("--- 테스트 완료 ---\n")

# 원래 print 함수로 복원
print = __builtins__.print
print("파일 테스트가 완료되었습니다. test_log.txt 파일을 확인하세요.") 