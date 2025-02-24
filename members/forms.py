import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django_countries.widgets import CountrySelectWidget

from members.models import GsmpMember
from django.utils.translation import gettext_lazy as _



country_list = [_('Georgia'), _('United Kingdom'), _('Armenia'), _('Azerbaijan'), _('Bolivia'), _('Germany'), ]



class LoginMemberForm(AuthenticationForm):
    username = forms.CharField(label=_('ელ-ფოსტა'), widget=forms.TextInput(attrs={'placeholder': _('შეიყვანე ელ-ფოსტა'), 'class': 'form-control'}))
    password = forms.CharField(label=_('პაროლი'), widget=forms.PasswordInput(attrs={'placeholder': _('შეიყვანე პაროლი'), 'class': 'form-control'}))


    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class RegisterMemberForm(UserCreationForm):
    # username = forms.CharField(label='მომხმარებლის სახელი', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label=_('პაროლი'), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label=_('გაიმეორე პაროლი'), widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    class Meta:
        model = get_user_model()
        this_year = datetime.date.today().year
        date_birth = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year - 100, this_year - 5))),
                                     label='დაბადების თარიღი')


        fields = ['photo', 'first_name', 'last_name', 'email',
                  'password1', 'password2', 'date_birth', 'country', 'city',
                   'address', 'postal_code', 'workplace', 'academic_degree',
                  'academic_position', 'workplace_activity', 'Gender',]
        labels = {
            'email': 'E-mail',
            'first_name': _('სახელი'),
            'last_name': _('გვარი'),
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': CountrySelectWidget(attrs={'class': 'form-control', 'style': 'max-width:200px'}),
            # 'date_birth': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'address':  forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'workplace': forms.TextInput(attrs={'class': 'form-control'}),
            'academic_degree': forms.Select(attrs={'class': 'form-select', 'style': 'width:200px'}),
            'academic_position': forms.Select(attrs={'class': 'form-select', 'style': 'width:200px'}),
            'workplace_activity': forms.Select(attrs={'class': 'form-select', 'style': 'width:200px'}),
            'Gender': forms.Select(attrs={'class': 'form-select', 'style': 'width:40px'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if GsmpMember.objects.filter(email=email).exists():
            raise forms.ValidationError(_("ასეთი ფოსტა არის"))
        return email


class ProfileMemberForm(forms.ModelForm):
    # username = forms.CharField(disabled=True, label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control'}))
    this_year = datetime.date.today().year
    date_birth = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year-100, this_year-5))), label='დაბადების თარიღი')


    class Meta:
        model = get_user_model()
        fields = ['photo', 'first_name', 'last_name', 'email',
                   'date_birth', 'country', 'city',
                   'address', 'postal_code', 'workplace', 'academic_degree',
                  'academic_position', 'workplace_activity', 'Gender',]

        labels = {
            'first_name': _('სახელი'),
            'last_name': _('გვარი'),
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),

        }


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("ძველი პაროლი"), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label=_("ახალი პაროლი"), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label=_("გაიმეორეთ პაროლი"), widget=forms.PasswordInput(attrs={'class': 'form-control'}))