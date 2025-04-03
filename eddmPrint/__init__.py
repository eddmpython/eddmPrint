from .printer import EddmPrint
from .colors import Colors
from .templates import Templates

__version__ = "0.1.2"
__all__ = ["EddmPrint", "Colors", "Templates", "printer"]

# 기본 인스턴스 생성 및 시작
printer = EddmPrint()
printer.start()