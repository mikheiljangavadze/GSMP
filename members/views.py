import threading

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView, UpdateView
from django.conf import settings
from .models import GsmpMember
from .tokens import account_activation_token
from .utils import generate_token
from gsmpsite import settings
from .forms import LoginMemberForm, RegisterMemberForm, ProfileMemberForm, UserPasswordChangeForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class LoginMember(LoginView):
    form_class = LoginMemberForm
    template_name = 'members/login.html'
    extra_context = {'title': "ავტორიზაცია"}


class RegisterMember(CreateView):
    form_class = RegisterMemberForm
    template_name = 'members/register.html'


    col1 = ["id_photo", 'id_first_name', 'id_last_name', 'id_email', 'id_password1', 'id_password2', 'id_date_birth', 'id_Gender', ]
    col2 = [ 'id_country', 'id_city', 'id_address', 'id_postal_code', 'id_workplace', 'id_academic_degree',
            'id_academic_position', 'id_workplace_activity', ]

    required_field_list = ['id_first_name', 'id_last_name', 'id_email', 'id_password1', 'id_password2',]

    extra_context = {'title': "რეგისტრაცია", "col1": col1, "col2": col2, "required_field_list": required_field_list}
    success_url = reverse_lazy('members:login')

    def form_valid(self, form):
        user = form.save()
        user = form.save(commit=False)
        user.is_active = False  # Deactivate the user until email confirmation
        user.save()

        # Send email confirmation
        current_site = get_current_site(self.request)
        subject = 'Activate your account'
        message = render_to_string('members/account_activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        user.email_user(subject, message)

        return redirect('members:account_activation_sent')


# @login_required
def account_activation_sent(request):
    return render(request, 'members/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = GsmpMember.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, GsmpMember.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('members:account_activation_complete')
    else:
        return HttpResponseBadRequest('Activation link is invalid!')


@login_required
def account_activation_complete(request):
    return render(request, 'members/account_activation_complete.html')


class ProfileMember(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileMemberForm
    template_name = 'members/profile.html'
    extra_context = {
        'title': _("წევრის პროფილი"),
        'default_image': settings.DEFAULT_USER_IMAGE,
    }

    def get_success_url(self):
        return reverse_lazy('members:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("members:password_change_done")
    template_name = "members/password_change_form.html"
    extra_context = {'title': "პაროლის შეცვლა"}

