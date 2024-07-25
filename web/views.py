from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Flan, Contact
from .forms import ContactForm
from django.contrib.auth.decorators import login_required

def index(request):
    flanes = Flan.objects.all()
    flanes_privados = Flan.objects.filter(is_private=True)
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes,
        
        'flanes_privados': flanes_privados,
        'flanes_publicos': flanes_publicos,
        })

@login_required
def welcome(request):
    flanes = Flan.objects.all()
    flanes_privados = Flan.objects.filter(is_private=True)
    flanes_publicos = Flan.objects.filter(is_private=False)
    
    # implementacion de los botones filtrado
    if request.method == 'POST':
        if 'btn_privados' in request.POST:
            flanes = flanes_privados
        elif 'btn_publicos' in request.POST:
            flanes = flanes_publicos
        else:
            flanes = Flan.objects.all()
    else:
        flanes = Flan.objects.all()

    return render(request, 'welcome.html', {'flanes': flanes,
        'flanes_privados': flanes_privados,
        'flanes_publicos': flanes_publicos,
        })

def about(request):
 return render(request, 'about.html', {})

def contacto(request):
    if request.method =='POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact_form = Contact.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito/')
    else:
        form = ContactForm()
        
    return render(request, 'contacto.html', {'form': form})

def exito(request):
    return render(request, 'exito.html', {})

def detalle_flan(request, id):
    flan = get_object_or_404(Flan, pk=id)
    return render(request, 'detalle_flan.html', {'flan': flan})

