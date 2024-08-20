from django.shortcuts import render

# Create your views here.


def contact_us(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            # need to sent mail from here
            return render(request, 'alumni/success_contact.html')
        else:
            return render(request, 'alumni/error_contact.html')
    form = ContactModelForm()
    context = {'form': form}
    return render(request, 'alumni/contact_us.html', context)
