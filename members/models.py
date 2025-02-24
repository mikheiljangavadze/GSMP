from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _


GENDER_CHOICES = [( 'მამრობითი',  _('მამრ')), ('მდედრობითი', _('მდედრ'))]
acad_degrees = [
    ('ბაკალავრი', _('ბაკალავრი')),
    ('მაგისტრი', _('მაგისტრი')),
    ('მეცნიერებათა დოქტორი', _('მეცნიერებათა დოქტორი'))

]
acad_position = [
    ('ასისტენტი', _('ასისტენტი') ),
    ('ასისტენტ პროფესორი', _('ასისტ. პროფ.') ),
    ('ასოცირებული პროფესორი', _('ასოც. პროფ.') ),
    ('პროფესორი', _('პროფესორი') ),
    ('პროფესორი-ემერიტუსი', _('პროფესორი-ემერიტუსი') )
]
work_activity = [
    ('კლინიკური/სამედიცინო სერვისი', _('კლინიკური/სამედიცინო სერვისი')),
    ('კვლევა', _('კვლევა')),
    ('ორივე - კლინიკური/კვლევითი', _('ორივე - კლინიკური/კვლევითი')),
    ('ადმინისტრაციული', _('ადმინისტრაციული')),
    ('ფინანსები, მარკეტინგი, გაყიდვები', _('ფინანსები, მარკეტინგი, გაყიდვები')),
    ('საგანმანათლებო', _('საგანმანათლებო')),
    ('სხვა', _('სხვა'))

]



class GsmpMember(AbstractUser):
    USERNAME_FIELD = "email"




    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100)
    REQUIRED_FIELDS = [first_name, last_name]





    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name=_("ფოტო"))
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name=_("დაბადების თარიღი"))

    Gender = models.TextField(blank=True, choices=GENDER_CHOICES, verbose_name=_('სქესი'))
    country = CountryField(_('country'), multiple=False, blank=False)
    city = models.CharField(blank=True,  null=True, max_length=50, verbose_name=_("ქალაქი"))
    address = models.CharField(blank=True, null=True, max_length=80, verbose_name=_("მისამართი"))
    workplace = models.CharField(blank=True, null=True, max_length=100,verbose_name=_("სამუშაო ადგილი"))
    postal_code = models.CharField(blank=True, null=True, max_length=10, verbose_name=_("საფოსტო ინდექსი"))
    academic_degree = models.TextField(blank=True, choices=acad_degrees, verbose_name=_('აკადემიური ხარისხი'))
    academic_position = models.TextField(blank=True, choices=acad_position, verbose_name=_('აკადემიური პოზიცია'))
    workplace_activity = models.TextField(blank=True, choices=work_activity, verbose_name=_('სამუშაო აქტიობა'))
    email_confirmed = models.BooleanField(default=False)


    def __str__(self):
        return self.email