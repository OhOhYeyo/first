from django.shortcuts import render

# from django.http import HttpResponse


# 화면에 글씨를 출력하는 코드
# Create your views here.


def home(request):
    # HttpResponse(): 괄호 안에 있는 문장을 화면으로 출력하는 라이브러리
    # return HttpResponse("")
    context = {
        "name1": "오승건",
        "name2": "가나다",
        "name3": "abc",
    }

    # render(html파일을 연결시켜주는 라이브러리)
    return render(request, "first_html/home.html", context)
