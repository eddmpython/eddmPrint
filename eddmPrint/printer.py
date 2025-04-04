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

    def _wrappedPrint(self, *args, **kwargs):
        frame = inspect.stack()[1]
        file = os.path.basename(frame.filename)
        func = frame.function
        line = frame.lineno
        prefix = f"{self.color}{self.prefixTemplate.format(file=file, func=func, line=line)}{self.reset}"
        self.originalPrint(prefix, *args, **kwargs)

    def print(self, *args, **kwargs):
        """기본 프린트 함수"""
        color = kwargs.pop('color', self.color)
        template = kwargs.pop('template', self.prefixTemplate)
        original_color = self.color
        original_template = self.prefixTemplate
        
        self.color = color
        self.prefixTemplate = template
        self._wrappedPrint(*args, **kwargs)
        
        self.color = original_color
        self.prefixTemplate = original_template

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
