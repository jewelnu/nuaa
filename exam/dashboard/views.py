from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import Regi_form, AddressJobForm
from .models import Degsif18Y3010919,Student,Upozilla,District,AddressJob
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def success(request):
    return render(request, 'dashboard/success.html')  

@login_required(login_url="my-log")
def check_registration(request):
    form = Regi_form()  # Initialize form at the start
    student = None  # Initialize student to None
    data_matched = False
    if request.method == 'POST':
        form = Regi_form(request.POST, request.FILES)
        if form.is_valid():
                regi_search= form.cleaned_data['reg_no']
                try:
                    student = Degsif18Y3010919.objects.get(reg_no=regi_search)
                    print(f"Student found: {student}")  # Debugging output
                    data_matched=True
                except Degsif18Y3010919.DoesNotExist:
                    student = None  # Handle case where student does not exist
                    data_matched = False
        else:
            print(form.errors) 
    if 'save' in request.POST and student:
        if student:
            student_data = Student(
                        reg_no=student.reg_no,
                        std_name=student.std_name,
                        fname=student.fname,
                        mname=student.mname,
                        gender=form.cleaned_data['gender'],
                        user = request.user,
                        username = request.user.email,
                        date_of_birth= form.cleaned_data['date_of_birth'],
                        marital_status= form.cleaned_data['marital_status'],
                        nationality= form.cleaned_data['nationality'],
                        spouse_name = form.cleaned_data['spouse_name'],
                        number_of_children= form.cleaned_data['number_of_children'],
                        picture= form.cleaned_data['picture']
                    )
            student_data.save()
            print("student data to save.")
            return redirect('save_success')
        else:
              print("No student data to save.")
    return render(request, 'dashboard/dashboard.html',{'form':form,'student':student,'data_exist': data_matched})

def address_job_view(request):
    if request.method == "POST":
        form = AddressJobForm(request.POST)
        if form.is_valid():       
            # Create a new AddressJob instance and save it
            AddressJob.objects.create(
                present_address=form.cleaned_data['present_address'],
                present_dist=form.cleaned_data['present_dist'].district,
                present_upozilla=form.cleaned_data['present_upozilla'].upozilla,
                permanent_address=form.cleaned_data['permanent_address'],
                permanent_dist=form.cleaned_data['permanent_dist'].district,
                permanent_upozilla=form.cleaned_data['permanent_upozilla'].upozilla,
                occupation=form.cleaned_data['occupation'],
                work_address=form.cleaned_data['work_address'],
                work_dist=form.cleaned_data['work_dist'].district,
                work_upozilla=form.cleaned_data['work_upozilla'].upozilla,
                company_name= form.cleaned_data['company_name'],
                designation= form.cleaned_data['designation'],
                mobile= form.cleaned_data['mobile'],
                telephone=form.cleaned_data['telephone'],
                highest_degree_obtained=form.cleaned_data['highest_degree_obtained'],
                category_of_membership=form.cleaned_data['category_of_membership'],
                amount_payable=form.cleaned_data['amount_payable']
            )
            return redirect('save_success')  
    else:
        form = AddressJobForm()
    districts = District.objects.all()
    return render(request, 'dashboard/address.html', {'form': form,'districts': districts})

def load_upozillas(request):
    district_id = request.GET.get('district_id')
    upozillas = Upozilla.objects.filter(dist_id=district_id).order_by('upozilla')
    return JsonResponse(list(upozillas.values('id', 'upozilla')), safe=False)

