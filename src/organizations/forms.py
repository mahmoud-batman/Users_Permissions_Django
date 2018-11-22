from django import forms
from users.forms import CustomUserCreateForm
from users.models import CustomUser
from .models import Organization

class DateInput(forms.DateInput):
    input_type = 'date'
class OrganizationUserCreateForm(CustomUserCreateForm):
    class Meta:
        model = CustomUser
        fields = [
            # "organization",
            'username',
            'email',
            'profile_picture',
            'birth_date',
            'bio',
        ]
        widgets = {
                    'birth_date': DateInput()
                }

class OrganizationCreateForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = [
        # "owner_id",
        "name",
        "bio",
        "location",
        "auth_image",
        "logo"
        ]
class OrganizationUpdateForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = [
        # "owner_id",
        "name",
        "bio",
        "location",
        "logo"
        # "auth_image",
        ]
