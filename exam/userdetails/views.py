from django.shortcuts import render

def project_stage_view(request):
    stages = ['basic_info', 'educational_info', 'company_info', 'payment_info']
    context = {
        'stages': stages,
        'current_stage': request.GET.get('stage', 'basic_info')  # Get current stage from query params
    }
    return render(request, 'userdetails/project_stage.html', context)
