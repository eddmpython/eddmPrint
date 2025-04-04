import builtins
import inspect
import os
from .colors import Colors

class EddmPrint:
    def __init__(self, color=None, prefixTemplate=None):
        self.originalPrint = print
        self.color = color or "\033[35m"
        self.prefixTemplate = prefixTemplate or "[파일명: {file} | 함수명: {func} | 라인: {line}]"
        self.reset = "\033[0m"
        self.isActive = False

    def start(self):
        if not self.isActive:
            builtins.print = self._wrappedPrint
            self.isActive = True

    def restore(self):
        if self.isActive:
            builtins.print = self.originalPrint
            self.isActive = False

    def setColor(self, colorCode):
        self.color = colorCode

    def setPrefixTemplate(self, template):
        self.prefixTemplate = template

    def _get_caller_info(self):
        """호출자의 파일, 함수, 라인 정보를 반환"""
        stack = inspect.stack()
        # 라이브러리 내부 파일들을 건너뛰고 실제 호출 파일을 찾음
        for frame in stack[2:]:  # [0]은 _get_caller_info, [1]은 _wrappedPrint
            if not frame.filename.endswith('printer.py'):
                return {
                    'file': os.path.basename(frame.filename),
                    'func': frame.function,
                    'line': frame.lineno
                }
        return {'file': 'unknown', 'func': 'unknown', 'line': 0}

    def _wrappedPrint(self, *args, **kwargs):
        # color와 template 파라미터 추출
        color = kwargs.pop('color', self.color)
        template = kwargs.pop('template', self.prefixTemplate)
        
        # 호출자 정보 가져오기
        caller = self._get_caller_info()
        prefix = f"{color}{template.format(**caller)}{self.reset}"
        self.originalPrint(prefix, *args, **kwargs)

    def print(self, *args, **kwargs):
        """기본 프린트 함수"""
        self._wrappedPrint(*args, **kwargs)

    def println(self, *args, **kwargs):
        """줄바꿈이 포함된 프린트 함수"""
        kwargs['end'] = '\n\n'
        self.print(*args, **kwargs)

    def error(self, *args, **kwargs):
        """에러 메시지 출력"""
        kwargs['color'] = Colors.RED
        self.print(*args, **kwargs)

    def success(self, *args, **kwargs):
        """성공 메시지 출력"""
        kwargs['color'] = Colors.GREEN
        self.print(*args, **kwargs)

    def warning(self, *args, **kwargs):
        """경고 메시지 출력"""
        kwargs['color'] = Colors.YELLOW
        self.print(*args, **kwargs)

    def info(self, *args, **kwargs):
        """정보 메시지 출력"""
        kwargs['color'] = Colors.CYAN
        self.print(*args, **kwargs)
