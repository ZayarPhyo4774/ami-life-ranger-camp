from django.conf import settings
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import redirect, render

from .forms import QuoteRequestForm

COMPANY_NAME = 'AMI Life Insurance'

def home(request):
    return render(request, 'home.html', {
        'company': COMPANY_NAME,
        'show_back_button': False
    })

def know_insurance(request):
    return render(request, 'knowyourinsurance.html', {
        'company': COMPANY_NAME,
        'show_back_button': True
    })


def file_claim(request):
    return render(request, 'fileclaims.html', {
        'company': COMPANY_NAME,
        'show_back_button': True
    })  

def get_quote(request):
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            customer_message = form.cleaned_data['message'] or 'No message provided.'
            subject = f'New quote request from {full_name}'
            message = (
                'A new quote request was submitted.\n\n'
                f'Name: {full_name}\n'
                f'Email: {email}\n'
                f'Phone: {phone_number}\n\n'
                f'Message:\n{customer_message}\n'
            )

            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.COMPANY_QUOTE_EMAIL],
                    fail_silently=False,
                    # reply_to=[email],
                )
            except BadHeaderError:
                messages.error(request, 'Invalid form submission. Please try again.')
            else:
                messages.success(request, 'Your quote request has been sent.')
                return redirect('get_quote')
    else:
        form = QuoteRequestForm()

    return render(request, 'getquote.html', {
        'company': COMPANY_NAME,
        'show_back_button': True,
        'form': form,
    })

def coverage_details(request):
    return render(request, 'coveragedetails.html', {
        'company': COMPANY_NAME,
        'show_back_button': True
    })

def ourCommitment(request):
    return render(request, 'ourcommitment.html', {
        'company': COMPANY_NAME,
        'show_back_button': True
    })

def policydocs(request):
    return render(request, 'policydocs.html', {
        'company': COMPANY_NAME,
        'show_back_button': True
    })
