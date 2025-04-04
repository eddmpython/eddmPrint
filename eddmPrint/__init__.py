from .printer import EddmPrint
from .colors import Colors
from .templates import Templates

__version__ = "0.1.3"
__all__ = ["EddmPrint", "Colors", "Templates", "print", "println", "error", "success", "warning", "info"]

# 기본 인스턴스 생성 및 시작
try:
    printer = EddmPrint()
    printer.start()
    _is_initialized = True
    
    # 편의 함수들
    def print(*args, **kwargs):
        """기본 프린트 함수"""
        return printer.print(*args, **kwargs)
        
    def println(*args, **kwargs):
        """줄바꿈이 포함된 프린트 함수"""
        return printer.println(*args, **kwargs)
        
    def error(*args, **kwargs):
        """에러 메시지 출력"""
        return printer.error(*args, **kwargs)
        
    def success(*args, **kwargs):
        """성공 메시지 출력"""
        return printer.success(*args, **kwargs)
        
    def warning(*args, **kwargs):
        """경고 메시지 출력"""
        return printer.warning(*args, **kwargs)
        
    def info(*args, **kwargs):
        """정보 메시지 출력"""
        return printer.info(*args, **kwargs)
        
except Exception as e:
    _is_initialized = False
    print(f"eddmPrint 초기화 실패: {str(e)}")

def is_initialized():
    """eddmPrint가 성공적으로 초기화되었는지 확인"""
    return _is_initialized