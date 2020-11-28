from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.de

# VISTA DE NOMBRE  formularioContacto


def formularioContacto(request):
    # el render es una funcion y me va a dar la respuesta a partir de la Peticion,Y VOY A DEVOLVER UN FORMULARIO
    return render(request, "formularioContacto.html")


def contactar(request):
    if request.method == "POST":  # CAPTURAR el asusto el mesaje y el email
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"]
        #+ "/Email:" + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["epnfis2018@gmail.com"]
        send_mail(asunto, mensaje, email_desde, [
                  email_para], fail_silently=False, auth_password="@Renat0Jav1")
        return render(request, "contactar.html")
    return render(request, "formularioContacto.html")
