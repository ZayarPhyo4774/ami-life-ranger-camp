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
            # Process form data and send email...
            messages.success(request, "မက်ဆေ့ချ် ပို့ဆောင်ပြီးပါပြီ။")
            return redirect('get_quote')
    else:
        form = QuoteRequestForm()

    return render(request, 'amiapp/getquote.html', {'form': form})

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
