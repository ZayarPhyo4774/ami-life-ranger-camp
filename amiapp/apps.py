from django import forms


class QuoteRequestForm(forms.Form):
    full_name = forms.CharField(
        label='အမည်',
        max_length=100,
        required=True,
        error_messages={
            'required': 'ကျေးဇူးပြု၍ သင့်အမည်ကို ထည့်သွင်းပေးပါ။',
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'သင့်အမည်',  # Required for Bootstrap floating labels
            'autocomplete': 'name',
        }),
    )

    phone_number = forms.CharField(
        label='ဖုန်းနံပါတ်',
        max_length=30,
        required=True,
        error_messages={
            'required': 'ကျေးဇူးပြု၍ သင့်ဖုန်းနံပါတ်ကို ထည့်သွင်းပေးပါ။',
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '၀၉ ၁၂၃ ၄၅၆ ၇၈၉',
            'autocomplete': 'tel',
            'type': 'tel',
        }),
    )

    email = forms.EmailField(
        label='အီးမေးလ်',
        required=False,
        error_messages={
            'invalid': 'မှန်ကန်သော အီးမေးလ်လိပ်စာကို ထည့်သွင်းပေးပါ။',
        },
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'you@example.com',
            'autocomplete': 'email',
        }),
    )

    message = forms.CharField(
        label='အကြောင်းအရာ',
        max_length=1000,
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'မေးမြန်းလိုသည်များကို ရေးသားပါ',
            'style': 'height: 120px;',  # Explicit height required for form-floating textareas
        }),
    )