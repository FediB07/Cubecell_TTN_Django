from django.shortcuts import render

from .mqtt_client import send_to_web

def ma_vue(request):
    context={'data':send_to_web()}
    return render(request, "website/index.html",context=context)
