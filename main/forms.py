from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import AdvUser, DocsFile, SendedDocs


class RegisterUserForm(forms.ModelForm):
    midl_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    dateBorn = forms.CharField()
    job = forms.CharField()

    def clean_password1(self):
        password = self.cleaned_data['password']
        if password:
            password_validation.validate_password(password)
        return password

    def clean(self):
        super().clean()
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        errors = {}
        if password and password2 and password != password2:
            errors['password2'] = ValidationError(
                'Введенные пароли не совпадают', code='password_mismatch'
            )
        if errors != '':
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.date = datetime.now()
        user.set_password(self.cleaned_data['password'])
        # newdate = utilities.encode(user)
        if commit:
            user.save()
        return user

    class Meta:
        model = AdvUser
        fields = ('username', 'password', 'password2', 'first_name', 'email', 'last_name', 'midl_name',
                  'dateBorn', 'job', 'is_staff')


class ChangeUserForm(forms.ModelForm):
    midl_name = forms.CharField()
    phone = forms.CharField()
    dateBorn = forms.CharField()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.date = datetime.now()
        # newdate = utilities.encode(user)
        if commit:
            user.save()
        return user

    class Meta:
        model = AdvUser
        fields = ('username', 'first_name', 'email', 'last_name', 'midl_name', 'dateBorn', 'phone')


class DocsAddForm(forms.ModelForm):
    class Meta:
        model = DocsFile
        fields = '__all__'


class ChangeDocsForm(forms.ModelForm):
    class Meta:
        model = DocsFile
        fields = ('name', 'status', 'comments')


class SendDocs(forms.ModelForm):
    class Meta:
        model = SendedDocs
        fields = '__all__'
