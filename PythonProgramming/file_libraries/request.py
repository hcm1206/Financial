# 리퀘스트로 이미지 파일 요청

# 리퀘스트 모듈 임포트
import requests

# 인터넷 URL을 통해 GET 요청으로 이미지 파일을 다운로드
url = "http://bit.ly/3ZZyeXQ"
r = requests.get(url, stream=True).raw

print()

# 필로로 이미지 출력

# 필로 패키지의 이미지 모듈 임포트
from PIL import Image

# 이미지 파일을 필로 이미지 객체로 변환 후 화면에 출력 및 저장
img = Image.open(r)
img.show()
img.save('src.png')

# 그림 파일에 대한 정보 출력(PNG 포맷, RGB 모드, 2918×3024 크기)
print(img.get_format_mimetype)

print()

# 'with ~ as 파일 객체'로 이미지 파일 복사

BUF_SIZE = 1024
# src.png 이미지 파일을 읽기 모드로 불러와 sf 파일 객체로 생성, dst.png 파일을 쓰기 모드로 불러와 df 파일 객체로 생성
with open('src.png', 'rb') as sf, open('dst.png', 'wb') as df:
    while True:
        # sf 파일 객체로부터 1024바이트씩 읽기
        data = sf.read(BUF_SIZE)
        # 읽을 data가 없을 시 반복문 종료
        if not data:
            break
        # 읽어온 data를 df 파일 객체에 작성
        df.write(data)

print()

# SHA-256으로 파일 복사 검증

# 해시립 모듈 임포트
import hashlib

# 원본 이미지와 사본 이미지에 사용할 해시 객체 각각 생성
sha_src = hashlib.sha256()
sha_dst = hashlib.sha256()

# 원본 이미지와 사본 이미지를 로드하여 파일 객체로 생성 후 각각에 대한 해시 객체 업데이트
with open('src.png', 'rb') as sf, open('dst.png', 'rb') as df:
    sha_src.update(sf.read())
    sha_dst.update(df.read())

# 원본 이미지와 사본 이미지의 해시값을 각각 16진수로 출력
print("src.png's hash : {}".format(sha_src.hexdigest()))
print("dst.png's hash : {}".format(sha_dst.hexdigest()))
# 복사된 동일한 이미지 파일이므로 해시값이 같음

# 맷플롯립으로 이미지 가공

# 맷플롯립 패키지의 모듈 임포트
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 사본 이미지를 mpimg 객체로 불러와 출력(3차원 부동 소수점 데이터로 구성됨)
dst_img = mpimg.imread('dst.png')
print(dst_img)

# 사본 이미지 객체에서 첫 번째 RGB 채널만 불러와 의사 색상 이미지로 저장하여 출력(부동 소수점 데이터가 2차원으로 변경)
pseudo_img = dst_img[:,:,0]
print(pseudo_img)

# 서브플롯을 이미지 원본과 의사 색상 이미지를 불러와 출력
plt.suptitle('Image Processing', fontsize=18)
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(mpimg.imread('src.png'))

plt.subplot(122)
plt.title('Pseudocolor Image')
dst_img = mpimg.imread('dst.png')
pseudo_img = dst_img[:,:,0]
plt.imshow(pseudo_img)
plt.show()

print()