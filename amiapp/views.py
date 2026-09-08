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
            form = QuoteForm(request.POST)
            if form.is_valid():
                # Extract cleaned data
                full_name = form.cleaned_data['full_name']
                phone_number = form.cleaned_data['phone_number']
                email = form.cleaned_data['email']
                message_text = form.cleaned_data['message']

                try:
                    send_mail(
                        subject=f"New Quote Request from {full_name}",
                        message=f"Name: {full_name}\nPhone: {phone_number}\nEmail: {email}\n\nMessage:\n{message_text}",
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[settings.COMPANY_QUOTE_EMAIL],
                        fail_silently=False,
                    )
                    messages.success(request, "မက်ဆေ့ချ် ပို့ဆောင်ပြီးပါပြီ။ မကြာမီ ပြန်လည်ဆက်သွယ်ပါမည်။")
                    return redirect('get_quote')

                except Exception as e:
                    logger.error(f"Email delivery failed: {e}")
                    messages.error(
                        request, 
                        "စနစ်ပိုင်းဆိုင်ရာ လိုအပ်ချက်ကြောင့် မက်ဆေ့ချ် မပို့ဆောင်နိုင်ပါ။ ကျေးဇူးပြု၍ ဖုန်းဖြင့် တိုက်ရိုက် ဆက်သွယ်ပေးပါရန်။"
                    )
        else:
            form = QuoteForm()

        return render(request, 'getquote.html', {'form': form})

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
