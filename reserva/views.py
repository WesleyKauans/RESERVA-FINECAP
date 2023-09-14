from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect
from .models import reserva
from .forms import reservaForm


def index(request):
    total_reserva = reserva.objects.count()
    
    context = {
        'total_reserva' : total_reserva,
    }
    return render(request,"reserva/index.html",context)

def reserva_cadastrar(request):
    if request.method == 'POST':
        form = reservaForm(request.POST)
        if form.is_valid():
            print("salvando")
            form.save()
            form = reservaForm()
    else:
        
        print('entrou primeiro aqui')
        form = reservaForm()

    return render(request,'reserva/form.html',{'form':form})

def reserva_editar(request,id):
    produto = get_object_or_404(reserva,id=id)
   
    if request.method == 'POST':
        form = reservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos_listar')
    else:
        form = reservaForm(instance=produto)

    return render(request,'reserva/form.html',{'form':form})


def reserva_editar(request,id):
    produto = get_object_or_404(reserva,id=id)
   
    if request.method == 'POST':
        form = reservaForm(request.POST,request.FILES,instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produtos_listar')
    else:
        form =reservaForm(instance=produto)

    return render(request,'area_administrativa/form.html',{'form':form})


def reserva_remover(request, id):
    reserva = get_object_or_404(reserva, id=id)
    reserva.delete()
    return redirect('reserva_listar') # procure um url com o nome 'produtos_listar'

def reserva_listar(request):
    reserva = reserva.objects.all()
    context ={
        'reservas':reserva
    }
    return render(request, "reserva/reservas.html",context)


def detalhar_reserva(request, id):
    produtos = get_object_or_404(reserva, id=id)
    context={'reserva' : reserva}
    
    return render(request,'reserva/detalhar.html', context)
