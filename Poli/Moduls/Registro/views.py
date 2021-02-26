from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def vistaFormularioContacto(request):  # una vista recive una peticion
    # el render me avisa la respuestas a mi petición
    return render(request, "formularioContacto.html")


# para resivir los valores que hemos indicado en el formulario
def contactar(request):
    if request.method == "POST":  # CAPTURAR el asusto el mesaje y el email
        asunto = request.POST["txtAsunto"]
       # +  "/Email:" + request.POST["txtEmail"]
        mensaje = request.POST["txtMensaje"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["epnfis2018@gmail.com"]
        send_mail(asunto, mensaje, email_desde,
                  email_para, fail_silently=False, auth_password="@Renat0Jav1")
        return render(request, "contactoExitoso.html")
    return render(request, "formularioContacto.html")
