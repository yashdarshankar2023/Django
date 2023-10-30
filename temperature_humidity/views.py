
from django.shortcuts import render, redirect
from .forms import TemperatureHumidityForm
from .models import TemperatureHumidity

def input_data(request):
    if request.method == 'POST':
        form = TemperatureHumidityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('temperature_humidity:input_data')
    else:
        form = TemperatureHumidityForm()
    
    data = TemperatureHumidity.objects.all()
    
    return render(request, 'input_data.html', {'form': form, 'data': data})

def display_data(request):
    data = TemperatureHumidity.objects.all()
    return render(request, 'display_data.html', {'data': data})


from django.http import JsonResponse

def delete_row(request):
    if request.method == "POST":
        row_id = request.POST.get("id")
        # Perform the actual row deletion here, e.g., using the ORM
        # Example: TemperatureHumidity.objects.get(id=row_id).delete()
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})



# views.py
from django.http import JsonResponse

def delete_table_data(request):
    # Delete the table data here (e.g., clear the data from the database or storage)
    # Return a JSON response indicating success or failure
    try:
        # Your code to delete the table data here
        return JsonResponse({'success': True, 'message': 'Table data deleted successfully'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})




