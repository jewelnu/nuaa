from django.shortcuts import render
from exam.contact_us.forms import ContactModelForm


# Create your views here.


def home(request):
    return render(request, 'alumni/home.html')


def about(request):
    return render(request, 'alumni/about.html')


def alumni_members(request):
    return render(request, 'alumni/alumni_members.html')


def committee_members(request):
    return render(request, 'alumni/committee_members.html')


def notice(request):
    return render(request, 'alumni/notice_board.html')


def downloads(request):
    return render(request, 'alumni/downloads.html')


def gallery(request):
    return render(request, 'alumni/gallery.html')


def message(request):
    return render(request, 'alumni/message.html')


def faq(request):
    return render(request, 'alumni/faq.html')
