from django.shortcuts import render, redirect
from .models import Mauzo, MauzoDeletionLog, Matumizi, MatumiziDeletionLog
from .forms import MauzoForm, MatumiziForm
from django.db.models import Sum
from django.utils import timezone
from django.contrib import messages


def mauzo_create(request):
    if request.method == 'POST':
        form = MauzoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mauzo-list')
    else:
        form = MauzoForm()
    return render(request, 'mauzo_create.html', {'form': form})


def mauzo_list(request):
    mauzo_zote = Mauzo.objects.all().order_by('-id')
    total_mauzo_tshirt = Mauzo.objects.aggregate(total_mauzo_tshirt=Sum('mauzo_tshirt'))['total_mauzo_tshirt'] or 0
    total_mauzo_visakramenti = Mauzo.objects.aggregate(total_mauzo_visakramenti=Sum('mauzo_visakramenti'))['total_mauzo_visakramenti'] or 0
    total_mauzo_vipeperushi = Mauzo.objects.aggregate(total_mauzo_vipeperushi=Sum('mauzo_vipeperushi'))['total_mauzo_vipeperushi'] or 0
    total_mapato_saloon = Mauzo.objects.aggregate(total_mapato_saloon=Sum('mapato_saloon'))['total_mapato_saloon'] or 0

    return render(request, 'mauzo_list.html', {'mauzo_zote': mauzo_zote, 'total_mauzo_tshirt': total_mauzo_tshirt, 'total_mauzo_visakramenti': total_mauzo_visakramenti,'total_mauzo_vipeperushi': total_mauzo_vipeperushi,'total_mapato_saloon': total_mapato_saloon})


def mauzo_update(request, pk):
    mauzo = Mauzo.objects.get(pk=pk)
    if request.method == 'POST':
        form = MauzoForm(request.POST, instance=mauzo)
        if form.is_valid():
            form.save()
            return redirect('mauzo-list')
    else:
        form = MauzoForm(instance=mauzo)
    return render(request, 'mauzo_update.html', {'form': form})

def mauzo_delete(request, pk):
    mauzo = Mauzo.objects.get(pk=pk)
    deleted_by = request.user
    if request.method == 'POST':
        MauzoDeletionLog.objects.create(
            deleted_by=deleted_by,
            deletion_timestamp=timezone.now(),
            date=mauzo.date,
            mauzo_tshirt=mauzo.mauzo_tshirt,
            mauzo_visakramenti=mauzo.mauzo_visakramenti,
            mauzo_vipeperushi=mauzo.mauzo_vipeperushi,
            mapato_saloon=mauzo.mapato_saloon
        )
        mauzo.delete()
        messages.success(request, 'Mauzo deleted successfully and deletion log is stored.')
        return redirect('mauzo-list')
    return render(request, 'mauzo_delete.html', {'mauzo': mauzo})

def report_mapato(request):
    # Retrieve data from the database
    mauzo_data = Mauzo.objects.all()
    rowspan_value = len(mauzo_data) * 3
    rowspan_value_saloon = len(mauzo_data)
    rowspan_value_date = len(mauzo_data)
    # Calculate totals
    total_mauzo_tshirt = mauzo_data.aggregate(total=Sum('mauzo_tshirt'))['total'] or 0
    total_mauzo_visakramenti = mauzo_data.aggregate(total=Sum('mauzo_visakramenti'))['total'] or 0
    total_mauzo_vipeperushi = mauzo_data.aggregate(total=Sum('mauzo_vipeperushi'))['total'] or 0
    total_mapato_saloon = mauzo_data.aggregate(total=Sum('mapato_saloon'))['total'] or 0
    jumla_ya_mauzo_yote = total_mauzo_tshirt + total_mauzo_visakramenti + total_mauzo_vipeperushi
    # Pass the totals and data to the template
    return render(request, 'mipango.html', {'mauzo_data': mauzo_data, 'jumla_ya_mauzo_yote': jumla_ya_mauzo_yote, 'total_mauzo_tshirt': total_mauzo_tshirt,'total_mauzo_visakramenti': total_mauzo_visakramenti,'total_mauzo_vipeperushi': total_mauzo_vipeperushi,'total_mapato_saloon': total_mapato_saloon, 'rowspan_value':rowspan_value, 'rowspan_value_saloon':rowspan_value_saloon, 'rowspan_value_date':rowspan_value_date})

##################################
##################################
def matumizi_create(request):
    if request.method == 'POST':
        form = MatumiziForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matumizi-list')
    else:
        form = MatumiziForm()
    return render(request, 'matumizi_create.html', {'form': form})

def matumizi_list(request):
    matumizi_zote = Matumizi.objects.all().order_by('-id')
    total_matumizi_tshirt = Matumizi.objects.aggregate(total_matumizi_tshirt=Sum('matumizi_tshirt'))['total_matumizi_tshirt'] or 0
    total_matumizi_visakramenti = Matumizi.objects.aggregate(total_matumizi_visakramenti=Sum('matumizi_visakramenti'))['total_matumizi_visakramenti'] or 0
    total_matumizi_vipeperushi = Matumizi.objects.aggregate(total_matumizi_vipeperushi=Sum('matumizi_vipeperushi'))['total_matumizi_vipeperushi'] or 0
    total_matumizi_saloon = Matumizi.objects.aggregate(total_matumizi_saloon=Sum('matumizi_saloon'))['total_matumizi_saloon'] or 0

    return render(request, 'matumizi_list.html', {'matumizi_zote': matumizi_zote, 'total_matumizi_tshirt': total_matumizi_tshirt, 'total_matumizi_visakramenti': total_matumizi_visakramenti,'total_matumizi_vipeperushi': total_matumizi_vipeperushi,'total_matumizi_saloon': total_matumizi_saloon})

def matumizi_update(request, pk):
    matumizi = Matumizi.objects.get(pk=pk)
    if request.method == 'POST':
        form = MatumiziForm(request.POST, instance=matumizi)
        if form.is_valid():
            form.save()
            return redirect('matumizi-list')
    else:
        form = MatumiziForm(instance=matumizi)
    return render(request, 'matumizi_update.html', {'form': form})

def matumizi_delete(request, pk):
    matumizi = Matumizi.objects.get(pk=pk)
    deleted_by = request.user
    if request.method == 'POST':
        MatumiziDeletionLog.objects.create(
            deleted_by=deleted_by,
            deletion_timestamp=timezone.now(),
            date=matumizi.date,
            matumizi_tshirt=matumizi.matumizi_tshirt,
            matumizi_visakramenti=matumizi.matumizi_visakramenti,
            matumizi_vipeperushi=matumizi.matumizi_vipeperushi,
            matumizi_saloon=matumizi.matumizi_saloon
        )
        matumizi.delete()
        messages.success(request, 'Matumizi deleted successfully and deletion log is stored.')
        return redirect('matumizi-list')
    return render(request, 'matumizi_delete.html', {'matumizi': matumizi})

def report_matumizi(request):
    # Retrieve data from the database
    matumizi_data = Matumizi.objects.all()
    rowspan_value = len(matumizi_data) * 3
    rowspan_value_saloon = len(matumizi_data)
    rowspan_value_date = len(matumizi_data)
    # Calculate totals
    total_matumizi_tshirt = matumizi_data.aggregate(total=Sum('matumizi_tshirt'))['total'] or 0
    total_matumizi_visakramenti = matumizi_data.aggregate(total=Sum('matumizi_visakramenti'))['total'] or 0
    total_matumizi_vipeperushi = matumizi_data.aggregate(total=Sum('matumizi_vipeperushi'))['total'] or 0
    total_matumizi_saloon = matumizi_data.aggregate(total=Sum('matumizi_saloon'))['total'] or 0
    jumla_ya_matumizi_yote = total_matumizi_tshirt + total_matumizi_visakramenti + total_matumizi_vipeperushi
    # Pass the totals and data to the template
    return render(request, 'matumizi.html', {'matumizi_data': matumizi_data, 'jumla_ya_matumizi_yote': jumla_ya_matumizi_yote, 'total_matumizi_tshirt': total_matumizi_tshirt,'total_matumizi_visakramenti': total_matumizi_visakramenti,'total_matumizi_vipeperushi': total_matumizi_vipeperushi,'total_matumizi_saloon': total_matumizi_saloon, 'rowspan_value':rowspan_value, 'rowspan_value_saloon':rowspan_value_saloon, 'rowspan_value_date':rowspan_value_date})

###################################
###################################
# home section of mipango


def mapato_na_matumizi_report(request):
    # Fetching income data
    mauzo_data = Mauzo.objects.all()
    total_mauzo_visakramenti = mauzo_data.aggregate(Sum('mauzo_visakramenti'))['mauzo_visakramenti__sum'] or 0
    total_mauzo_vipeperushi = mauzo_data.aggregate(Sum('mauzo_vipeperushi'))['mauzo_vipeperushi__sum'] or 0
    total_mauzo_tshirt = mauzo_data.aggregate(Sum('mauzo_tshirt'))['mauzo_tshirt__sum'] or 0
    jumla_ya_mauzo_yote = total_mauzo_visakramenti + total_mauzo_vipeperushi + total_mauzo_tshirt
    total_mapato_saloon = mauzo_data.aggregate(Sum('mapato_saloon'))['mapato_saloon__sum'] or 0
    
    # Filter out rows with zero values
    mauzo_data = mauzo_data.exclude(mauzo_visakramenti=0, mauzo_vipeperushi=0, mauzo_tshirt=0, mapato_saloon=0)
    
    # Fetching expense data
    matumizi_data = Matumizi.objects.all()
    total_matumizi_visakramenti = matumizi_data.aggregate(Sum('matumizi_visakramenti'))['matumizi_visakramenti__sum'] or 0
    total_matumizi_vipeperushi = matumizi_data.aggregate(Sum('matumizi_vipeperushi'))['matumizi_vipeperushi__sum'] or 0
    total_matumizi_tshirt = matumizi_data.aggregate(Sum('matumizi_tshirt'))['matumizi_tshirt__sum'] or 0
    jumla_ya_matumizi_yote = total_matumizi_visakramenti + total_matumizi_vipeperushi + total_matumizi_tshirt
    total_matumizi_saloon = matumizi_data.aggregate(Sum('matumizi_saloon'))['matumizi_saloon__sum'] or 0

    # Filter out rows with zero values
    matumizi_data = matumizi_data.exclude(matumizi_visakramenti=0, matumizi_vipeperushi=0, matumizi_tshirt=0, matumizi_saloon=0)

    # Calculating rowspan values separately
    rowspan_value_income = len(mauzo_data) * 3  # For VISAKAMENTI, VIPEPERUSHI, T-SHIRT
    rowspan_value_saloon_income = len(mauzo_data)
    rowspan_value_expenses = len(matumizi_data) * 3  # For VISAKAMENTI, VIPEPERUSHI, T-SHIRT
    rowspan_value_saloon_expenses = len(matumizi_data)

    context = {
        'mauzo_data': mauzo_data,
        'total_mauzo_visakramenti': total_mauzo_visakramenti,
        'total_mauzo_vipeperushi': total_mauzo_vipeperushi,
        'total_mauzo_tshirt': total_mauzo_tshirt,
        'jumla_ya_mauzo_yote': jumla_ya_mauzo_yote,
        'total_mapato_saloon': total_mapato_saloon,
        'matumizi_data': matumizi_data,
        'total_matumizi_visakramenti': total_matumizi_visakramenti,
        'total_matumizi_vipeperushi': total_matumizi_vipeperushi,
        'total_matumizi_tshirt': total_matumizi_tshirt,
        'jumla_ya_matumizi_yote': jumla_ya_matumizi_yote,
        'total_matumizi_saloon': total_matumizi_saloon,
        'rowspan_value_income': rowspan_value_income,
        'rowspan_value_saloon_income': rowspan_value_saloon_income,
        'rowspan_value_expenses': rowspan_value_expenses,
        'rowspan_value_saloon_expenses': rowspan_value_saloon_expenses,
    }

    return render(request, 'mapato_na_matumizi.html', context)




def mipangodemo3(request):
    return render(request, 'mipangodemo3.html')

def mipangonafedhahomepage(request):
    return render(request, 'mipangonafedhahome.html')

def saloon(request):
    return render(request, 'saloon.html')

def itservices(request):
    return render(request, 'itservices.html')

def architecture(request):
    return render(request, 'architecture.html')

def keki(request):
    return render(request, 'keki.html')

def mapambonasherehe(request):
    return render(request, 'mapambonasherehe.html')
