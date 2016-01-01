from django import forms
from .models import UserProfile

PRICE_CHOISES = (
    ('50', '50%'),
    ('60', '60%'),
    ('70', '70%'),
    ('80', '80%'),
    ('90', '90%')
)

class UserProfileForm(forms.ModelForm):

    api_key = forms.CharField()
    api_key.widget.attrs['class'] = 'form-control'
    api_key.widget.attrs['placeholder'] = 'AKLSFKAHFSHKSAKLJAKSF'

    abs_min_price = forms.ChoiceField(choices=PRICE_CHOISES, initial="70", widget=forms.Select(attrs={
        'class': 'selectpicker form-control',
        'data-style': 'btn-select',
    }))

    steam_username = forms.CharField()
    steam_username.widget.attrs['class'] = 'form-control'
    steam_username.widget.attrs['placeholder'] = '49385896754637549'

    max_price = forms.IntegerField()
    max_price.widget.attrs['class'] = 'form-control'
    max_price.widget.attrs['placeholder'] = '200'

    debug_mode = forms.BooleanField(
        label='myLabel',
        required=True,
        initial=True)

    class Meta:
        model = UserProfile
        fields = ('api_key', 'abs_min_price', 'steam_username', 'max_price', 'debug_mode')
