from django.shortcuts import render, redirect
from .models import MedicineInventory
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt



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

def update_stock(request, product_id):
    if request.method == 'POST':
        medicine = get_object_or_404(MedicineInventory, product_id=product_id)
        action_type = request.POST.get("action_type")
        try:
            quantity = int(request.POST.get("quantity", 0))
        except ValueError:
            quantity = 0

        if action_type == "add":
            if quantity > 0:
                medicine.stock = (medicine.stock or 0) + quantity

        elif action_type == "remove":
            if quantity > 0:
                
                medicine.pending_quantity = (medicine.pending_quantity or 0) + quantity

                if medicine.pending_quantity >= (medicine.big_box_quantity or 1):
                    deduction_boxes = medicine.pending_quantity // medicine.big_box_quantity
                    medicine.stock = max(0, (medicine.stock or 0) - deduction_boxes)

                    medicine.pending_quantity = medicine.pending_quantity % medicine.big_box_quantity
        medicine.save()

    return redirect("medicine_list")

