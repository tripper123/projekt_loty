from django.views.generic import ListView
from django.shortcuts import redirect
from .models import Loty, Linie, Kraje
from .forms import LotyForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

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
            kraj = form.cleaned_data["kraj"]
            linia = form.cleaned_data["linia"]
            lot = Loty(lotnisko_wylot=lotnisko_wylot, lotnisko_przylot=lotnisko_przylot, data_lotu=data_lotu, kraj=kraj,
                       linia=linia)
            lot.save()
            return redirect('lot')
        else:
            context['form'] = form
            return render(request, template, context)

def lot_detail(request, pk):
    template = "lot_detail.html"
    context = {}
    context["form"] = LotyForm()
    if request.method == "GET":
        lot = Loty.objects.get(id=pk)
        context["lot"] = lot
        return render(request, template, context)

def lot_delete(request, pk):
    if request.method == "POST":
        lot = Loty.objects.get(id=pk)
        lot.delete()
        return redirect('lot')

def dodaj_lot(request):
    template = "dodaj_lot.html"
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
            kraj = form.cleaned_data["kraj"]
            linia = form.cleaned_data["linia"]
            lot = Loty(lotnisko_wylot=lotnisko_wylot, lotnisko_przylot=lotnisko_przylot, data_lotu=data_lotu, kraj=kraj,
                       linia=linia)
            lot.save()
            return redirect('lot')
        else:
            context['form'] = form
            return render(request, template, context)

def detail(request):
    template = "detail.html"
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
            kraj = form.cleaned_data["kraj"]
            linia = form.cleaned_data["linia"]
            lot = Loty(lotnisko_wylot=lotnisko_wylot, lotnisko_przylot=lotnisko_przylot, data_lotu=data_lotu, kraj=kraj,
                       linia=linia)
            lot.save()
            return redirect('lot')
        else:
            context['form'] = form
            return render(request, template, context)

def pagination(request):
    template = "pagination.html"
    object_list = Loty.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(object_list, 6)  # 6 employees per page
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, template, {'page_obj': page_obj, 'form': LotyForm})

def index(request):
    template = "index.html"
    context = {}
    return render(request, template, context)

def usun_lot(request):
    template = "usun_lot.html"
    context = {}
    context['form'] = LotyForm()
    if request.method == "GET":
        loty = Loty.objects.all()
        context['loty'] = loty
        return render(request, template, context)


class PostListView(ListView):
    queryset = Loty.objects.all()
    context_object_name = 'loty'
    paginate_by = 10
    template_name = 'lot.html'


class PostListView2(ListView):
    queryset = Loty.objects.all()
    context_object_name = 'loty'
    paginate_by = 10
    template_name = 'detail.html'


class PostListView3(ListView):
    queryset = Loty.objects.all()
    context_object_name = 'loty'
    paginate_by = 10
    template_name = 'usun_lot.html'


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)

                    return HttpResponse('ZALOGOWANY')
                else:
                    return HttpResponse('BŁĄD LOGOWANIA')
            else:
                return HttpResponse('NIEPRAWIDLOWE DANE')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})



def index2(request):
    template = "index2.html"
    context = {}
    return render(request, template, context)

def index3(request):
    template = "index3.html"
    context = {}
    return render(request, template, context)




