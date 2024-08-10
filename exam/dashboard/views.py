from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import Regi_form
from .models import Degsif18Y3010919,Student
from django.contrib.auth.decorators import login_required

@login_required(login_url="my-log")
def check_registration(request):
    form = Regi_form()  # Initialize form at the start
    student = None  # Initialize student to None
    data_matched = False
    if request.method == 'POST':
        if 'search' in request.POST:
            form = Regi_form(request.POST)
            if form.is_valid():
                regi_temp= form.cleaned_data['reg_no']
                try:
                    student = Degsif18Y3010919.objects.get(reg_no=regi_temp)
                    
                    request.session['student_id'] = student.id  # Store the student's ID
                    print(f"Student found: {student}")  # Debugging output
                    data_matched=True
                except Degsif18Y3010919.DoesNotExist:
                    student = None  # Handle case where student does not exist
                    data_matched = False
        elif 'save' in request.POST:
            form =Regi_form(request.POST)
            if form.is_valid(): 
                student_id =request.session.get('student_id')
                if student_id:
                    student= Degsif18Y3010919.objects.get(id=student_id) 
                    new_student = Student(
                        reg_no=student.reg_no,
                        std_name=student.std_name,
                        fname=student.fname,
                        mname=student.mname,
                        gender=form.cleaned_data['gender']  # Save additional_info
                    )
                    new_student.save()  # Save the new student instance
                    return redirect('save_success')
                else:
                    print("Student variable is None, cannot save.")  # Debugging output
    return render(request, 'dashboard/dashboard.html',{'form':form,'student':student,'data_exist': data_matched})
            
def success(request):
    return render(request, 'dashboard/success.html')        

