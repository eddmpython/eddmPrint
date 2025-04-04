# EddmPrint

콘솔 출력에 색상과 메타데이터(파일명, 함수명, 라인번호)를 추가하는 Python 라이브러리입니다.

## 설치

```bash
pip install eddmPrint
```

## 사용법

### 기본 사용법 (v0.1.3 이상)

라이브러리를 임포트하면 자동으로 시작됩니다:

```python
import eddmPrint

# 기본 프린트
eddmPrint.print("테스트 메시지")  # 자동으로 파일명, 함수명, 라인 정보가 출력됨

# 줄바꿈 포함
eddmPrint.println("줄바꿈이 포함된 메시지")

# 다양한 메시지 타입
eddmPrint.error("에러 메시지")
eddmPrint.success("성공 메시지")
eddmPrint.warning("경고 메시지")
eddmPrint.info("정보 메시지")
```

### 색상 상수 사용

```python
from eddmPrint import Colors

# 색상 직접 설정
eddmPrint.print("빨간색 메시지", color=Colors.RED)
eddmPrint.print("초록색 메시지", color=Colors.GREEN)
eddmPrint.print("파란색 메시지", color=Colors.BLUE)
```

### 템플릿 형식 변경

```python
from eddmPrint import Templates

# 템플릿 설정
eddmPrint.print("간단한 템플릿", template=Templates.SIMPLE)
eddmPrint.print("상세한 템플릿", template=Templates.DETAILED)
eddmPrint.print("함수명만 표시", template=Templates.FUNCTION_ONLY)
```

### 커스텀 프린터 사용

```python
from eddmPrint import EddmPrint

# 새로운 인스턴스 생성
my_printer = EddmPrint(color="\033[36m", prefixTemplate="[DEBUG {file}:{line}]")
my_printer.start()
my_printer.print("커스텀 프린터 테스트")
```

## 색상 목록

다음과 같은 색상 상수를 사용할 수 있습니다:

- `Colors.BLACK`
- `Colors.RED`
- `Colors.GREEN` 
- `Colors.YELLOW`
- `Colors.BLUE`
- `Colors.MAGENTA`
- `Colors.CYAN`
- `Colors.WHITE`
- `Colors.BRIGHT_RED`
- `Colors.BRIGHT_GREEN`
- 등등...

## 템플릿 목록

다음과 같은 템플릿 상수를 사용할 수 있습니다:

- `Templates.DEFAULT`: "[파일명: {file} | 함수명: {func} | 라인: {line}]"
- `Templates.SIMPLE`: "[{file}:{line}]"
- `Templates.FUNCTION_ONLY`: "[함수: {func}]"
- `Templates.FILE_ONLY`: "[파일: {file}]"
- `Templates.LINE_ONLY`: "[라인: {line}]"
- `Templates.COMPACT`: "{file}:{line}"
- `Templates.DETAILED`: "파일: {file} | 함수: {func} | 라인: {line}"

## 개발자 정보

### 새 버전 릴리스하기

이 프로젝트는 GitHub Actions를 사용하여 자동으로 릴리스를 생성하고 PyPI에 배포합니다.
새 버전을 릴리스하려면 다음 단계를 따르세요:

1. 코드를 수정하고 커밋합니다.
2. 버전 태그를 생성합니다:
   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   ```
3. GitHub Actions가 자동으로 릴리스를 생성하고 PyPI에 배포합니다.

## 라이센스

이 프로젝트는 MIT 라이센스를 따릅니다. 자세한 내용은 [LICENSE](LICENSE)를 참조하세요. 