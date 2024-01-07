# Financial
증권 데이터 분석 실습용 레포지토리

## 비고
Pandas 라이브러리는 최신 2.0 이상 버전이 아닌 1.3.2 버전을 사용 중
```
pip install pandas==1.3.2
```
  
네이버 웹 스크레이핑을 통한 일별 시세를 DB에 갱신하기 위해 /Investar/DBUpdater.py를 실행  
DB에 저장하는 데 수 시간 걸리므로 실행시켜놓고 유튜브 열심히 봐야 함  
실행이 끝났으면 /Investar/Analyzer.py 모듈을 통해 시세 조회 API 이용 가능  