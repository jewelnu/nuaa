from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views.generic import TemplateView, FormView
from django.shortcuts import render
from .forms import ContactModelForm
from .forms import ContactForm


# Create your views here.


def contact_us(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            # need to sent mail from here
            return render(request, 'contact_us/success_contact.html')
        else:
            return render(request, 'contact_us/error_contact.html')
    form = ContactModelForm()
    context = {'form': form}
    return render(request, 'contact_us/contact_us.html', context)


class SuccessView(TemplateView):
    template_name = "contact_us/success.html"


class ContactView(FormView):
    form_class = ContactForm
    template_name = "contact_us/contact.html"

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        full_message = f"""
            Received message below from {email}, {subject}
            ________________________


            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )
        return super(ContactView, self).form_valid(form)
