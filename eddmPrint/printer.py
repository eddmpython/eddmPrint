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
        stack = inspect.stack()
        for frame in stack:
            filename = frame.filename
            if not any(lib in filename for lib in ['eddmPrint', 'site-packages']):
                return {
                    'file': os.path.basename(filename),
                    'func': frame.function,
                    'line': frame.lineno
                }
        return {'file': 'unknown', 'func': 'unknown', 'line': 0}

    def _wrappedPrint(self, *args, **kwargs):
        color = kwargs.pop('color', self.color)
        template = kwargs.pop('template', self.prefixTemplate)
        caller = self._get_caller_info()
        prefix = f"{color}{template.format(**caller)}{self.reset}"
        self.originalPrint(prefix, *args, **kwargs)

    def print(self, *args, **kwargs):
        self._wrappedPrint(*args, **kwargs)

    def println(self, *args, **kwargs):
        kwargs['end'] = '\n\n'
        self.print(*args, **kwargs)

    def error(self, *args, **kwargs):
        kwargs['color'] = Colors.RED
        self.print(*args, **kwargs)

    def success(self, *args, **kwargs):
        kwargs['color'] = Colors.GREEN
        self.print(*args, **kwargs)

    def warning(self, *args, **kwargs):
        kwargs['color'] = Colors.YELLOW
        self.print(*args, **kwargs)

    def info(self, *args, **kwargs):
        kwargs['color'] = Colors.CYAN
        self.print(*args, **kwargs)
