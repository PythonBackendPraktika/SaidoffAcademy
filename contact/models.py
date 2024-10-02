from django.db import models
from django.utils.translation import gettext_lazy as _

class Faq(models.Model):
    question = models.TextField(_('Question'))
    answer = models.TextField(_('Answer'))

    class Meta:
        verbose_name = _('Faq')
        verbose_name_plural = _('Faqs')

    def __str__(self):
        return self.question


class SocialMedia(models.Model):
    icon = models.FileField(_('Icon'), upload_to='social_media/')
    link = models.URLField(_('Link'))

    class Meta:
        verbose_name = _('Social Media')
        verbose_name_plural = _('Social Media')

    def __str__(self):
        return self.link


class CourseRegister(models.TextChoices):
    FRONTEND = 'frontend', _('Frontend')
    BACKEND = 'backend', _('Backend')
    GRAPHIC_DESIGNER = 'graphic_designer', _('Graphic Designer')
    WEB_UX_UI = 'web_ux_ui', _('Web UX UI')


class Registration(models.Model):
    full_name = models.CharField(_('Full Name'), max_length=100)
    phone_number = models.CharField(_('Phone Number'), max_length=15)
    course = models.CharField(
        _('Course'),
        max_length=100,
        choices=CourseRegister.choices,
        default=CourseRegister.FRONTEND
    )

    def __str__(self):
        return f"{self.full_name} - {self.course}"

    class Meta:
        verbose_name = _('Registration')
        verbose_name_plural = _('Registrations')


class ContactInfo(models.Model):
    icon = models.FileField(_('Icon'), upload_to='contact_info/')
    address = models.CharField(_('Address'), max_length=100)
    phone = models.CharField(_('Phone Number'), max_length=15)
    course = models.CharField(
        _('Course'),
        max_length=100,
        choices=CourseRegister.choices
    )

    class Meta:
        verbose_name = _('Contact Info')
        verbose_name_plural = _('Contact Info')

    def __str__(self):
        return f"{self.address} - {self.phone}"
