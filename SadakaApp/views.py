from django.shortcuts import render, redirect
from .models import Sadaka, DeletionLog
from .forms import SadakaForm
from django.db.models import Sum
from django.utils import timezone
from django.contrib import messages


# Create your views here.

def sadaka_create(request):
    if request.method == 'POST':
        form = SadakaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sadaka-list')
    else:
        form = SadakaForm()
    return render(request, 'sadaka_create.html', {'form':form})

def sadaka_list(request):
    sadaka_zote = Sadaka.objects.all().order_by('-id')
    # Calculate the totals
    total_sadaka1 = Sadaka.objects.aggregate(total_sadaka1=Sum('sadaka1'))['total_sadaka1'] or 0
    total_shukrani = Sadaka.objects.aggregate(total_shukrani=Sum('shukrani'))['total_shukrani'] or 0

    return render(request, 'sadaka_list.html', {'sadaka_zote': sadaka_zote, 'total_sadaka1': total_sadaka1, 'total_shukrani': total_shukrani})

def sadaka_update(request, pk):
    sadaka = Sadaka.objects.get(pk=pk)
    if request.method == 'POST':
        form = SadakaForm(request.POST, instance=sadaka)
        if form.is_valid():
            form.save()
            return redirect('sadaka-list')
    else:
        form = SadakaForm(instance=sadaka)
    return render(request, 'sadaka_update.html', {'form':form})

def sadaka_delete(request, pk):
    sadaka = Sadaka.objects.get(pk=pk)
    if request.method == 'POST':
        sadaka.delete()
        return redirect('sadaka-list')
    return render(request, 'sadaka_delete.html', {'sadaka': sadaka})

def sadaka_delete(request, pk):
    sadaka = Sadaka.objects.get(pk=pk)
    deleted_by = request.user  # Assuming you are using Django's authentication system

    if request.method == 'POST':
        # Create a deletion log entry
        DeletionLog.objects.create(
            deleted_by=deleted_by,
            deletion_timestamp=timezone.now(),
            date=sadaka.date,
            sadaka1=sadaka.sadaka1,
            shukrani=sadaka.shukrani
        )

        # Delete the Sadaka instance
        sadaka.delete()

        # Add a success message
        messages.success(request, 'Sadaka deleted successfully and deletion log is stored.')

        return redirect('sadaka-list')

    return render(request, 'sadaka_delete.html', {'sadaka': sadaka})

def mapato(request):
    sadaka_zote = Sadaka.objects.all().order_by('-id')
    rowspan_value = len(sadaka_zote) * 2  # Double the length of sadaka_zote
    total_sadaka1 = Sadaka.objects.aggregate(total_sadaka1=Sum('sadaka1'))['total_sadaka1'] or 0
    total_shukrani = Sadaka.objects.aggregate(total_shukrani=Sum('shukrani'))['total_shukrani'] or 0
    overal_total_sadaka_na_shukrani = total_sadaka1 + total_shukrani
    return render(request, 'mapato.html', {'sadaka_zote': sadaka_zote, 'rowspan_value': rowspan_value, 'total_sadaka1': total_sadaka1, 'total_shukrani': total_shukrani, 'overal_total_sadaka_na_shukrani': overal_total_sadaka_na_shukrani})


def mapatodemo(request):
    return render(request, 'mapatodemo.html')