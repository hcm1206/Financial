# 슬랙으로 알림 메시지 보내기

# 슬랙 워크스페이스와 앱 생성 후 채팅 봇 생성 후 인증 토큰 발급
# 슬랙 API를 이용해 메시지 보내는 코드 구현

# 기존에는 Slacker 객체를 이용하여 메시지를 보냈으나 슬랙 정책 변경으로 슬랙 API에 request 요청을 통해 메시지를 전달

import requests

# 슬랙 토큰, 채널명, 보낼 텍스트를 입력받는 슬랙 메시지 전송 함수 정의
def post_message(token, channel, text):
    # 슬랙 메시지 전송 API 주소에 채널명과 보낼 텍스트를 입력하여 POST 요청
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text})
    # POST 요청에 대한 응답을 수신받아 출력
    print(response)

# 슬랙 토큰 설정(직접 입력)
myToken = "dlrjtdmstmfforxhzmsdlaudkanehdkftndjqtek"
# 슬랙 토큰과 채널명, 메시지를 입력하여 슬랙에 메시지 전송
post_message(myToken, "#financial", 'Hello, my friend!')


# 슬랙 토큰, 채널명, 보낼 텍스트와 첨부내용을 입력받는 슬랙 메시지 전송 함수 정의
def post_format_message(token, channel, text, attachments):
    # 슬랙 메시지 전송 API 주소에 채널명과 보낼 텍스트, 첨부 내용을 입력하여 POST 요청
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             json={"channel": channel, "text": text, "attachments": attachments})
    # POST 요청에 대한 응답을 수신받아 출력
    print(response)

# 마크다운 문법으로 작성된 텍스트 설정
markdown_text = '''
This message is plain.
*This message is bold.*
'This message is code.'
_This message is italic._
~This message is strike.~
'''

# 첨부 내용으로 사용할 딕셔너리 설정
attach_dict = {
    'color'         :'#ff0000', # 첨부내용 테두리 색 설정
    'author_name'   :'INVESTAR', # 첨부 내용 저자명 설정
    'author_link'   :'github.com/hcm1206', # 첨부 내용 저자명의 링크 URL 설정
    'title'         :'오늘의 증시 KOSPI', # 첨부 내용 제목 설정
    'title_link'    :'http://finance.naver.com/sise/sise_index.nhn?code=KOSPI', # 첨부 내용 제목 링크 설정
    'text'          :'2,326.13 △11.89 (+0.51%)', # 첨부내용 텍스트 설정
    'image_url'     :'https://ssl.pstatic.net/imgstock/chart3/day/KOSPI.png' # 첨부내용의 이미지 경로 URL 설정
}

# 첨부 내용 딕셔너리를 리스트에 담아서 저장
attach_list = [attach_dict]
# 슬랙 토큰과 채널명, 메시지(마크다운), 첨부 내용을 입력하여 슬랙에 메시지 전송
post_format_message(myToken, channel="#financial", text=markdown_text, attachments=attach_list)