from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm , AuthenticationForm

class DateInput(forms.DateInput):
    input_type = 'date'
class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
        # 'organization',
            'username',
            'email',
            'profile_picture',
            'birth_date',
            'bio',
        ]
        widgets = {
                    'birth_date': DateInput()
                }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            'username' ,
            'first_name',
            'last_name',
            'email',
            'user_permissions',
            'groups',
        ]

class UserPermissionsForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        fields = [
            'user_permissions',
        ]
        ordering = sorted(["-user_permissions"])
