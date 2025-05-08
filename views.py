from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html', {
        'project_name': 'DP_Lichman',
        'description': 'Це навчальний проєкт з використанням Django.'
    })

def resume(request):
    return render(request, 'main/resume.html')
