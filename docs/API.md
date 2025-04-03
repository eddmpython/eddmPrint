# eddmPrint API 문서

## EddmPrint 클래스

### `__init__(color=None, prefixTemplate=None)`

생성자입니다. 색상과 접두사 템플릿을 설정할 수 있습니다.

- `color`: 출력 텍스트의 색상 코드 (기본값: Colors.MAGENTA)
- `prefixTemplate`: 출력 형식 템플릿 (기본값: "[파일명: {file} | 함수명: {func} | 라인: {line}]")

### `start()`

print 함수를 대체하여 위치 정보를 표시하는 기능을 시작합니다.

### `restore()`

원래의 print 함수로 복원합니다.

### `setColor(colorCode)`

출력 텍스트의 색상을 변경합니다.

- `colorCode`: 변경할 색상 코드

### `setPrefixTemplate(template)`

출력 형식 템플릿을 변경합니다.

- `template`: 변경할 템플릿

## Colors 클래스

### 기본 색상

- `BLACK`: 검은색
- `RED`: 빨간색
- `GREEN`: 녹색
- `YELLOW`: 노란색
- `BLUE`: 파란색
- `MAGENTA`: 자주색
- `CYAN`: 청록색
- `WHITE`: 흰색
- `RESET`: 초기화

### 밝은 색상

- `BRIGHT_BLACK`: 밝은 검은색
- `BRIGHT_RED`: 밝은 빨간색
- `BRIGHT_GREEN`: 밝은 녹색
- `BRIGHT_YELLOW`: 밝은 노란색
- `BRIGHT_BLUE`: 밝은 파란색
- `BRIGHT_MAGENTA`: 밝은 자주색
- `BRIGHT_CYAN`: 밝은 청록색
- `BRIGHT_WHITE`: 밝은 흰색

### 배경 색상

- `BG_BLACK`: 검은색 배경
- `BG_RED`: 빨간색 배경
- `BG_GREEN`: 녹색 배경
- `BG_YELLOW`: 노란색 배경
- `BG_BLUE`: 파란색 배경
- `BG_MAGENTA`: 자주색 배경
- `BG_CYAN`: 청록색 배경
- `BG_WHITE`: 흰색 배경

## Templates 클래스

### 기본 템플릿

- `DEFAULT`: "[파일명: {file} | 함수명: {func} | 라인: {line}]"
- `SIMPLE`: "[{file}:{line}]"
- `FUNCTION_ONLY`: "[함수: {func}]"
- `FILE_ONLY`: "[파일: {file}]"
- `LINE_ONLY`: "[라인: {line}]"
- `COMPACT`: "{file}:{line}"
- `DETAILED`: "파일: {file} | 함수: {func} | 라인: {line}" 