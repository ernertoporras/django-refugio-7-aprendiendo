from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# -------------muestra en html lo que esta en HttpRespnse------
def adopcion(request):
    return HttpResponse("ADOPCION ESTA ES LA PAGINA")
                # no olvides importar from django.http import HttpResponse
