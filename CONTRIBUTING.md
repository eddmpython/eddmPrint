# 기여 가이드

## 개발 환경 설정

1. 저장소를 클론합니다:
   ```bash
   git clone https://github.com/eddmpython/eddmPrint.git
   cd eddmPrint
   ```

2. (선택 사항) 가상 환경을 생성하고 활성화합니다:
   ```bash
   python -m venv venv
   source venv/bin/activate  # 또는 Windows의 경우: venv\Scripts\activate
   ```

3. 개발 모드로 패키지를 설치합니다:
   ```bash
   pip install -e .
   ```

## 자동 릴리스 및 PyPI 배포 설정

이 프로젝트는 GitHub Actions를 사용하여 태그를 푸시할 때 자동으로 릴리스를 생성하고 PyPI에 배포합니다.

### PyPI API 토큰 설정

1. [PyPI](https://pypi.org/)에 로그인합니다.
2. 계정 설정에서 API 토큰을 생성합니다.
3. GitHub 저장소의 Settings > Secrets > Actions로 이동합니다.
4. "New repository secret" 버튼을 클릭합니다.
5. 이름을 `PYPI_API_TOKEN`으로 설정하고, 값에 PyPI API 토큰을 입력합니다.
6. "Add secret" 버튼을 클릭합니다.

### 새 버전 릴리스하기

1. 코드를 수정하고 커밋합니다.
2. `setup.py` 파일에서 버전 번호를 업데이트합니다.
3. 변경 사항을 커밋하고 푸시합니다.
4. 태그를 생성하고 푸시합니다:
   ```bash
   git tag v0.1.0  # 버전 번호에 맞게 변경하세요
   git push origin v0.1.0
   ```
5. GitHub Actions가 자동으로 실행되어 릴리스를 생성하고 PyPI에 배포합니다.

## 이미지 관리

프로젝트에서 사용되는 스크린샷은 `images` 디렉토리에 저장됩니다. 새로운 스크린샷을 추가하려면:

1. `examples/screenshot_example.py` 스크립트를 실행합니다.
2. 결과 화면을 캡처합니다.
3. 이미지 파일을 `images` 디렉토리에 저장합니다.
4. 저장한 이미지를 README.md 파일에서 참조합니다. 