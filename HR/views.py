from django.shortcuts import render
from HR.forms import EmployeeForm
from django.http import HttpResponse
import mission

def create_profile(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            form.save_m2m()
            return mission.views.index(request)
        else:
            print form.errors
    else:
        form = EmployeeForm()

    return render(request, 'HR/create_profile.html', {'form': form})
