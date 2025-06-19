from django.http import HttpResponse

def index(request):
    return HttpResponse("Selamat datang di simple Application Polling!")

def address_view(request):
    return HttpResponse("Jl. Pondok Halimun RT.01/RW.07, Kel. Perbawati, Kec. Sukabumi, Kab. Sukabumi, Jawa Barat 43151")

def phone_view(request):
    return HttpResponse("085724562959")
