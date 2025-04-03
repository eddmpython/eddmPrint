import builtins
import inspect
import os
import sys
from .colors import Colors

class EddmPrint:
    def __init__(self, color=None, prefixTemplate=None):
        self.originalPrint = print
        self.color = color or Colors.MAGENTA
        self.prefixTemplate = prefixTemplate or "[파일명: {file} | 함수명: {func} | 라인: {line}]"
        self.reset = Colors.RESET
        self.isActive = False

    def start(self):
        if not self.isActive:
            builtins.print = self._wrappedPrint
            self.isActive = True
        return self  

    def restore(self):
        if self.isActive:
            builtins.print = self.originalPrint
            self.isActive = False
        return self 

    def setColor(self, colorCode):
        self.color = colorCode
        return self 

    def setPrefixTemplate(self, template):
        self.prefixTemplate = template
        return self  

    def _wrappedPrint(self, *args, **kwargs):
        frame = inspect.stack()[1]
        file = os.path.basename(frame.filename)
        func = frame.function
        line = frame.lineno
        prefix = f"{self.color}{self.prefixTemplate.format(file=file, func=func, line=line)}{self.reset}"

        self.originalPrint(prefix, *args, **kwargs) 