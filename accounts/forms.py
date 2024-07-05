from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()


class RegisterForm(UserCreationForm):
    maps = forms.JSONField(required=False, widget=forms.Textarea, help_text='Введите JSON в формате {"maps": []}')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        print(kwargs)
        if 'initial' not in kwargs or 'maps' not in kwargs['initial']:
            print(self.initial)
            self.initial['maps'] = ["", ]
            print(self.initial)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
