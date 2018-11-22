# NOTE:
    class CustomUserAdmin(UserAdmin):
        add_form = UserCreationForm # should be add_form and UserCreationForm
        change_form = UserChangeForm # should be change_form and UserChangeForm
        model = CustomUser
        list_display = ['username', 'id', 'email']

# NOTE:
    class ChangePassword(forms.Form):
        password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
        password2 = forms.CharField(label="Password confirmation",
                    widget=forms.PasswordInput,
                    help_text="Enter the same password as above, for verification.")

# NOTE:
    1# when using file upload the form is set like that
    <form method="post" enctype="multipart/form-data">
    2# You will need to set MEDIA_URL and MEDIA_ROOT in your project’s settings.py.
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
    3# in urls.py
    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    4#To access the MEDIA_URL in template you must add
    "django.template.context_processors.media" # to your context_processeors inside the TEMPLATES config.
    5# Disply image
    <img src="{{ user.image_field.url }}" class="img-responsive"/>
