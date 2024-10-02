from django.db import models
from django.db.models import FileField
from django.utils.translation import gettext_lazy as _

class WhyUs(models.Model):
    image = models.ImageField(_('image'), upload_to='images/')
    desc = models.TextField(_('description'))

    class Meta:
        verbose_name = _('WhyUs')
        verbose_name_plural = _('WhyUs')

    def __str__(self):
        return self.desc


class StudentComments(models.Model):
    name = models.CharField(_('name'), max_length=100)
    image = models.ImageField(upload_to='student_comments/', verbose_name=_('image'))
    profession = models.CharField( max_length=100, verbose_name=_('profession'))
    desc = models.TextField( verbose_name=_('description'))

    class Meta:
        verbose_name = _('StudentComments')
        verbose_name_plural = _('StudentComments')

    def __str__(self):
        return self.name


class FutureProfession(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Profession name'))
    desc = models.TextField(verbose_name=_('description'))
    image_icon = FileField(upload_to='future_professions/', verbose_name=_('Icon'))

    class Meta:
        verbose_name = _('FutureProfession')
        verbose_name_plural = _('FutureProfession')

    def __str__(self):
        return self.name


class ProfessionPartner(models.Model):
    image = models.FileField(upload_to='profession_partner/', verbose_name=_('Icon'))

    class Meta:
        verbose_name = _('ProfessionPartner')
        verbose_name_plural = _('ProfessionPartner')

    def __str__(self):
        return 'Trading partner'


class Teachers(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Teacher's name"))
    profession = models.CharField(max_length=100, verbose_name=_('profession'))
    position = models.CharField(max_length=100, verbose_name=_('position'))

    class Meta:
        verbose_name = _('Teachers')
        verbose_name_plural = _('Teachers')

    def __str__(self):
        return self.name


class ExtraDesc(models.Model):
    number = models.PositiveIntegerField(_('number'))
    desc = models.TextField(verbose_name=_('description'))

    class Meta:
        verbose_name = _('ExtraDesc')
        verbose_name_plural = _('ExtraDesc')

    def __str__(self):
        return f"{self.number}: {self.desc}"


class Profession(models.Model):
    image = models.ImageField(upload_to='profession/', verbose_name=_('image'))
    name = models.CharField( max_length=100, verbose_name=_('name'))
    desc = models.TextField(verbose_name=_('description'))
    extra_desc = models.ForeignKey(ExtraDesc, on_delete=models.CASCADE, verbose_name=_('extra_desc'), null=True, blank=True)

    class Meta:
        verbose_name = _('Profession')
        verbose_name_plural = _('Profession')

    def __str__(self):
        return self.name


