# 팬더스로 상장법인목록 읽기
# 한국 거래소 기업공시채널 사이트에서 제공하는 상장법인 목록 액셀 파일을 통해 종목코드 확인

import pandas as pd

# 액셀 파일 내용 확인하기

# 상장법인목록.xls 파일은 HTML 형식으로 구성되어 있어 팬더스의 read_excel() 함수로 읽기 불가
# pd.read_excel('상장법인목록.xls') # 오류 발생

print()

# HTML 형식으로 된 액셀 파일을 read_html() 함수로 로드한 후 첫번째 원소를 인덱싱하여 데이터프레임으로 출력
krx_list = pd.read_html('상장법인목록.xls')
print(krx_list[0])
# 종목코드에서 앞자리 0이 제거되어 6자리 미만의 종목코드를 가진 데이터 발생

print()

# 종목코드를 6자리 숫자 형식으로 바꾸고 앞자리가 비어있을 시 0으로 채움
krx_list[0].종목코드 = krx_list[0].종목코드.map('{:06d}'.format)
print(krx_list[0])

print()

# 상장법인목록을 로컬 드라이브로 다운로드하는 과정 없이 웹 상에서 URL을 통해 파일을 받아서 데이터프레임으로 전환
df = pd.read_html('https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13')[0]
# 종목코드를 6자리 숫자 형식으로 변경
df['종목코드'] = df['종목코드'].map('{:06d}'.format)
# 데이터프레임의 각 종목들을 종목코드 기준 오름차순하여 정렬
df = df.sort_values(by='종목코드')
print(df)

print()