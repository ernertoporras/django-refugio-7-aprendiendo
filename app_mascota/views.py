from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_mascota.form import MascotaForm
from app_mascota.models import Mascota
# Create your views here.


# -------------muestra en html lo que esta en HttpRespnse------
def index(request):
    return render(request,'mascota/index.html')



def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ('mascota:index')

    else:
        form = MascotaForm()
    return render(request,'mascota/mascota_form.html',{'form':form})



def mascota_list(requets):
    mascota=Mascota.objects.all()
    contexto = {'mascotas':mascota}
    return render(requets, 'mascota/mascota_list.html',contexto)











