class Templates:
    DEFAULT = "[파일명: {file} | 함수명: {func} | 라인: {line}]"
    SIMPLE = "[{file}:{line}]"
    FUNCTION_ONLY = "[함수: {func}]"
    FILE_ONLY = "[파일: {file}]"
    LINE_ONLY = "[라인: {line}]"
    COMPACT = "{file}:{line}"
    DETAILED = "파일: {file} | 함수: {func} | 라인: {line}" 