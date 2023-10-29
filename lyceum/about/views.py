from django.shortcuts import render
import django.http

# Create your views here.
def item_list(request):
    return django.http.HttpResponse('<html>Список элементов<html>')

def item_detail(request, pk):
    return django.http.HttpResponse('<html>Подробно элэмент</html>')