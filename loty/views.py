from django.shortcuts import render, redirect
from .models import Loty, Linie, Kraje
from .forms import LotyForm

# def lot(request):
#     return render(request, 'lot.html')
def index(request):
    template = "index.html"
    context = {}
    return render(request, template, context)

def index2(request):
    template = "index2.html"
    context = {}
    return render(request, template, context)

def lot(request):
    template = "lot.html"
    context = {}
    context['form'] = LotyForm()
    if request.method == "GET":
        loty = Loty.objects.all()
        context['loty'] = loty
        return render(request, template, context)
    if request.method == "POST":
        form = LotyForm(request.POST)
        if form.is_valid():
            lotnisko_wylot = form.cleaned_data["lotnisko_wylot"]
            lotnisko_przylot = form.cleaned_data['lotnisko_przylot']
            data_lotu = form.cleaned_data["data_lotu"]
            lot = Loty(lotnisko_wylot=lotnisko_wylot, lotnisko_przylot=lotnisko_przylot, data_lotu=data_lotu)
            lot.save()
            return redirect('lot')
        else:
            context['form'] = form
            return render(request, template, context)

def lot_detail(request, pk):
    template="lot_detail.html"
    context={}
    context["form"] = LotyForm()
    if request.method == "GET":
        lot = Loty.objects.get(id=pk)
        context["lot"] = lot
        return render(request, template, context)
    if request.method == "POST":
        form = LotyForm(request.POST)
        # if form.is_valid():
        if form.is_valid():
            lotnisko_wylot = form.cleaned_data["lotnisko_wylot"]
            lotnisko_przylot = form.cleaned_data['lotnisko_przylot']
            data_lotu = form.cleaned_data["data_lotu"]
            lot = Loty(lotnisko_wylot=lotnisko_wylot, lotnisko_przylot=lotnisko_przylot, data_lotu=data_lotu)
            lot.save()
            return redirect('lot')
        else:
            context['form'] = form
            return render(request, template, context)



def lot_delete(request, pk):
    if request.method == "POST":
        lot = Loty.objects.get(id=pk)
        lot.delete()
        return redirect('lot')

