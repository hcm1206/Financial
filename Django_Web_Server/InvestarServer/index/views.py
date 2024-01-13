from django.shortcuts import render

# 탬플릿 html을 넘겨주는 메인 뷰 정의
def main_view(request):
    return render(request, 'index.html')

# Create your views here.
