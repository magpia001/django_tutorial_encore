from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import Form
# Create your views here.

def write(request):
    # if(request의 post true이면)
    # 사용자가 입력한 form 데이터를 변수에 저장하고
    # ORM으로 DB에 저장하기
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()
    return render(request, 'write.html', {'form':form})

    # else
    form = Form()

    #return render(request, 'html템플릿 파일.html', data)
    return render(request, 'write.html', {'form':form})