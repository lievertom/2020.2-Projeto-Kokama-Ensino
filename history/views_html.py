from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .forms import AddNewHistory
from .models import KokamaHistory

base_url = '/historia'

@require_http_methods(["GET"])
def list_history (request):
    if(request.method == 'GET'):
        history_title = KokamaHistory.objects.all() 
        return render(request, 'list_history.html',{'object':history_title})
    else:
        return HttpResponse('<h1>Erro interno do servidor</h1>', status=500)

@require_http_methods(["GET", "POST"])
def add_history(request):
    if(request.method == 'GET'):
        form = AddNewHistory()
        return render(request, 'add_history.html', {'form': form})
    elif(request.method == 'POST'):
        form = AddNewHistory(request.POST)
        
        if form.is_valid():
            history_title = request.POST.get('history_title')
            history_text = request.POST.get('history_text')
            history = KokamaHistory(history_title=history_title, history_text=history_text)
            history.save()
            return redirect(base_url)

@require_http_methods(["GET"])
def views_history(request, id):
    if(request.method == 'GET'):
        kokama = get_object_or_404(KokamaHistory, pk=id)
        title = kokama.history_title
        text = kokama.history_text
        print(text)

        context = {
            'kokama': kokama,
            'title': title,
            'text': text,
            }
        return render(request, 'views_history.html', context)
    else:
        return HttpResponse('<h1>Erro interno do servidor</h1>', status=500)

@require_http_methods(["GET"])
def del_history(request, id):
    if(request.method == 'GET'):
        emp = KokamaHistory.objects.get(pk = id)
        emp.delete()
        return redirect(base_url)

    return HttpResponse('Erro ao deletar', status=500)

@require_http_methods(["GET", "POST"])
def edit_history(request, id):
    if(request.method == 'GET'):
        kokama = get_object_or_404(KokamaHistory, pk=id)
        title = kokama.history_title
        text = kokama.history_text

        form = AddNewHistory(
            initial={
                "history_title":title,
                "history_text":text,
            })

        return render(request, 'add_history.html', {'form': form})
    elif(request.method == 'POST'):
        form = AddNewHistory(request.POST)
        
        if form.is_valid():
            history = KokamaHistory.objects.get(pk = id)
            history.history_title = request.POST.get('history_title')
            history.history_text = request.POST.get('history_text')
            history.save()
            return redirect(base_url)

    return redirect(base_url)