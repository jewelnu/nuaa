from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import Regi_form
from .models import Degsif18Y3010919

def check_registration(request):
    form = Regi_form()  # Initialize form at the start
    student = None  # Initialize student to None
    if request.method == 'POST':
        form = Regi_form(request.POST)
        if form.is_valid():
            regi_temp= form.cleaned_data['reg_no']
            try:
                student = Degsif18Y3010919.objects.get(reg_no=regi_temp)
            except Degsif18Y3010919.DoesNotExist:
                student = None  # Handle case where student does not exist
    return render(request, 'dashboard/data_exist.html',{'form':form,'student':student})
            
                




'''def check_registration(request):
    if request.method == 'POST':
        form = Regi_form(request.POST)
        if form.is_valid():
            reg_no_tem = form.cleaned_data['reg_no']
            try:
                student = Degsif18Y3010919.objects.get(reg_no=reg_no_tem)
                
                if 'save' in request.POST:
                    user = request.user
                    # Assuming you have a model UserProfile to link users with the student data
                    UserProfile.objects.create(user=user, student=student)
                    return redirect('success_page')  # Redirect to a success page

                return render(request, 'registration_check.html', {
                    'form': form,
                    'student': student,
                })
            except Student.DoesNotExist:
                return render(request, 'registration_check.html', {
                    'form': form,
                    'no_match': True,
                })
    else:
        form = RegNoForm()
    return render(request, 'registration_check.html', {'form': form})'''

