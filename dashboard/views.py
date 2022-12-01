from django.shortcuts import render, redirect
from .models import CountryData
from .forms import CountryDataForm

# Create your views here.
def dashboard(request):
    # if request method == post
    #   valid하다면
    #   폼에 입력 데이터를 저장
    # else
    #   폼객체를 생성
    #   폼객체 랜더링
    if request.method == 'POST':
        form = CountryDataForm(request.POST)
        #print(form)
        if form.is_valid():
            '''
            폼에 입력 값을 개별로 변수 대입
            나라이름(country) DB 값이 있는 확인
            입력한 나라 이름이 있으면, 업데이트하고
            없으면 저장 
            '''
            # 폼에 입력 값을 개별로 변수 대입
            input_country = form.data.get('country', None)
            input_num = form.data.get('population', None)

            #
            CountryData.objects.update_or_create(
                #filter 
                country = input_country,
                #new value
                defaults = {
                    'country': input_country,
                    'population': input_num          
                }
            )
            # form.save()
            # return redirect('/dashboard')
            return redirect('.')
    else:
        form = CountryDataForm()
    # 나라별 인구 데이터를 DB에서 가져오기
    country_datas = CountryData.objects.all()
    # print(country_datas)
    context = {
        'form': form,
        'country_datas': country_datas
    }
    return render(request, 'dashboard/dashboard.html', context)
