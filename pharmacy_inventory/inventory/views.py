from django.shortcuts import render, redirect
from .models import MedicineInventory
from django.db.models import Q
from django.shortcuts import get_object_or_404

def medicine_list(request):
    query = request.GET.get('q', '')
    if query:
        medicines = MedicineInventory.objects.filter(
            Q(product_name__icontains=query) |
            Q(product_id__iexact=query))
    else:
        medicines = MedicineInventory.objects.all()

    return render(request, 'inventory/medicine_list.html', 
                  {'medicines' :medicines,
                   'query' : query,})

def add_medicine(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        unit_type = request.POST['unit_type']
        unit = int(request.POST['unit'])
        big_box_quantity = int(request.POST['big_box_quantity'])
        stock = int(request.POST['number_of_boxes'])
        Manufacturer = request.POST['Manufacturer']
        Bill = float(request.POST['Bill'])

        MedicineInventory.objects.create(
            product_name = product_name,
            unit_type = unit_type,
            unit = unit,
            big_box_quantity = big_box_quantity,
            stock = stock,
            Manufacturer = Manufacturer,
            product_price = (Bill/stock)/big_box_quantity,
        )
        return redirect('medicine_list')
    return render(request, 'inventory/add_medicine.html')

def medicine_info(request, product_id):
    medicine = get_object_or_404(MedicineInventory,product_id = product_id)
    return render(request, 'inventory/medicine_info.html', {'medicine':medicine})


#def add_quantity(request):
    #if request.method == 'POST':

        # Create your views here.
