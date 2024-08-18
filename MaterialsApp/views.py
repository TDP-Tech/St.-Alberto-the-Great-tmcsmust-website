from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .models import StudyMaterial
from .forms import StudyMaterialForm

def all_materials(request):
    materials_list = StudyMaterial.objects.all()
    paginator = Paginator(materials_list, 10)  # Show 10 materials per page

    page = request.GET.get('page')
    try:
        materials = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        materials = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        if paginator.num_pages > 0:
            materials = paginator.page(paginator.num_pages)
        else:
            materials = None

    return render(request, 'study_materials.html', {'materials': materials})

def filter_materials(request, level):
    if level == 'ALL':
        materials_list = StudyMaterial.objects.all()
    else:
        materials_list = StudyMaterial.objects.filter(level=level)

    paginator = Paginator(materials_list, 15)

    page = request.GET.get('page')
    try:
        materials = paginator.page(page)
    except PageNotAnInteger:
        materials = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        if paginator.num_pages > 0:
            materials = paginator.page(paginator.num_pages)
        else:
            materials = None

    context = {
        'materials': materials,
        'selected_level': level,
    }
    return render(request, 'filter_materials.html', context)


def add_material(request):
    if request.method == 'POST':
        form = StudyMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all-materials')
    else:
        form = StudyMaterialForm()
    return render(request, 'add_materials.html', {'form': form})

def edit_material(request, material_id):
    material = get_object_or_404(StudyMaterial, pk=material_id)
    if request.method == 'POST':
        form = StudyMaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            return redirect('all-materials')
    else:
        form = StudyMaterialForm(instance=material)
    return render(request, 'edit_materials.html', {'form': form})

def delete_material(request, material_id):
    material = get_object_or_404(StudyMaterial, pk=material_id)
    if request.method == 'POST':
        material.delete()
        return redirect('all-materials')
    return render(request, 'delete_materials.html', {'material': material})
