from django.shortcuts import render, redirect
from .models import Audio
from django.contrib import messages
# from django.core.mail import BadHeaderError, send_mail
# from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm, PartnershipForm

# Create your views here.
def index(request):
    return render(request, 'auxano/index.html')


def sermon(request):
    audio = Audio.objects.all()
    return render(request, 'auxano/sermon.html', {'audios': audio})


def partnership(request):
    if request.method == 'POST':
        form = PartnershipForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "You have successfully partnered with us")
            return redirect('partnership')
    form = PartnershipForm()
    context = {'form': form}
    return render(request, 'auxano/partnership.html', context)


def about(request):
    return render(request, 'auxano/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Message successfully sent")
            return redirect('contact')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'auxano/contact.html', context)


# def send_email(request):
#     subject = request.POST.get('subject', '')
#     message = request.POST.get('message', '')
#     email = request.POST.get('email', '')
#     if subject and message and email:
#         try:
#             send_mail(subject, message, [email])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         messages.add_message(request, messages.SUCCESS, "Message successfully sent")
#         return redirect('/contact/')
#     else:
#         return HttpResponse('Make sure all fields are entered and valid.')