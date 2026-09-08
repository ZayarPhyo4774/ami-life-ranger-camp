from django import forms


class QuoteRequestForm(forms.Form):
    full_name = forms.CharField(
        label='အမည်',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Jane Doe',
            'autocomplete': 'name',
        }),
    )
    email = forms.EmailField(
        label='အီးမေးလ်',
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'you@example.com',
            'autocomplete': 'email',
        }),
    )
    phone_number = forms.CharField(
        label='ဖုန်းနံပါတ်',
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '၀၉ ၁၂၃ ၄၅၆ ၇၈၉',
            'autocomplete': 'tel',
        }),
    )
    message = forms.CharField(
        label='အကြောင်းအရာ',
        max_length=1000,
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'မေးမြန်းလိုသည်များကို ရေးသားပါ',
            'rows': 4,
        }),
    )
