from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import PricingConfig
from .forms import PricingConfigForm


def pricingConfig_list(request):
    pricingConfig = PricingConfig.objects.all()
    context = {
        'pC': pricingConfig,
    }
    return render(request, 'admin/dashboard.html', context)


def create_pricingModule(request):
    form = PricingConfigForm()

    if request.method == 'POST':
        form = PricingConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pricingconfig-list')

    context = {
        'form': form,
    }
    return render(request, 'admin/create.html', context)



def edit_pricingModule(request, pk):
    pricingConfig = PricingConfig.objects.get(id=pk)
    form = PricingConfigForm(instance=pricingConfig)

    if request.method == 'POST':
        form = PricingConfigForm(request.POST, instance=pricingConfig)
        if form.is_valid():
            form.save()
            return redirect('pricingconfig-list')

    context = {
        'pC': pricingConfig,
        'form': form,
    }
    return render(request, 'admin/edit.html', context)

def delete_pricingModule(request, pk):
    pricingConfig = PricingConfig.objects.get(id=pk)

    if request.method == 'POST':
        pricingConfig.delete()
        return redirect('pricingconfig-list')

    context = {
        'pC': pricingConfig,
    }
    return render(request, 'admin/delete.html', context)

def results(request):

    DBP = request.POST['distanceBasePrice']
    DAP = request.POST['distanceAdditionalPrice']
    D = request.POST['distance']
    TMF = request.POST['timeMultiplierFactor']

    if DBP.isdigit() and DAP.isdigit() and D.isdigit() and TMF.isdigit():
        price = (DBP+(D*DAP))*TMF
        return render(request, "admin/dashboard.html", {"result": price})
    else:
        res = "Only digits are allowed"
        return render(request, "admin/dashboard.html", {"result": price})
    