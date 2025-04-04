# 릴리스 노트

## v0.1.5
- print 함수의 color와 template 파라미터 처리 방식 개선
- 불필요한 상태 변경 코드 제거로 성능 향상
- 기본 print 함수에서 직접 color와 template 설정 가능

## v0.1.4
- EddmPrint 클래스에 print, println, error, success, warning, info 메서드 추가
- 색상과 템플릿을 임시로 변경할 수 있는 기능 추가
- 메서드 호출 시 원래 설정 자동 복원 기능 추가

## v0.1.3
- 사용법 개선: 편의 함수들 직접 노출 (print, println, error, success, warning, info)
- import 시 자동 초기화 기능 안정성 개선
- 에러 처리 및 초기화 상태 확인 기능 추가

## v0.1.2
- 라이브러리 임포트 시 자동으로 시작되는 기능 추가
- 기본 인스턴스(printer) 제공으로 즉시 사용 가능

## v0.1.1
- PyPI 배포 자동화 설정
- 워크플로우 개선
- GitHub 릴리스 생성 자동화

## v0.1.0
- 초기 릴리스
- EddmPrint 클래스 구현
- print_message, change_color, reset_color 함수 구현 