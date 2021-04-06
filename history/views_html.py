from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .forms import AddNewHistory
from .models import KokamaHistory


@require_http_methods(["GET"])
def list_history (request):
    if(request.method == 'GET'):
        history_title = KokamaHistory.objects.all() 
        return render(request, 'list_history.html',{'object':history_title})
    else:
        return HttpResponse('<h1>Erro interno do servidor</h1>', status=500)