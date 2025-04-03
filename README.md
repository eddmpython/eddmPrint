# eddmPrint

개선된 print 함수로 파일명, 함수명, 라인 번호를 자동으로 표시합니다.

## 설치 방법

```bash
pip install eddmPrint
```

## 기본 사용법

```python
from eddmPrint import EddmPrint

# 기본 설정으로 시작
printer = EddmPrint()
printer.start()

# 이제 print는 자동으로 위치 정보를 포함합니다
print("Hello, World!")  # [파일명: example.py | 함수명: <module> | 라인: 7] Hello, World!

# 원래 print 함수로 복원
printer.restore()
```

## 색상 사용자 지정

```python
from eddmPrint import EddmPrint, Colors

printer = EddmPrint(color=Colors.GREEN)
printer.start()

print("녹색으로 표시됩니다")

# 중간에 색상 변경
printer.setColor(Colors.RED)
print("이제 빨간색으로 표시됩니다")
```

## 템플릿 사용자 지정

```python
from eddmPrint import EddmPrint, Templates

# 간단한 템플릿 사용
printer = EddmPrint(prefixTemplate=Templates.SIMPLE)
printer.start()

print("간단한 템플릿으로 표시됩니다")  # [file.py:10] 간단한 템플릿으로 표시됩니다

# 사용자 정의 템플릿
custom_template = "위치: {file}의 {line}번째 줄"
printer.setPrefixTemplate(custom_template)
print("사용자 정의 템플릿으로 표시됩니다")  # 위치: file.py의 14번째 줄 사용자 정의 템플릿으로 표시됩니다
```

## 라이센스

이 프로젝트는 MIT 라이센스를 따릅니다. 자세한 내용은 [LICENSE](LICENSE)를 참조하세요. 