from django.db import models
from django.utils.translation import gettext_lazy as _

class ForWho(models.Model):
    desc = models.TextField(_('Description'))

    class Meta:
        verbose_name = _('ForWho')
        verbose_name_plural = _('ForWhos')

    def __str__(self):
        return self.desc


class CoursePlan(models.Model):
    course_time = models.CharField(_('Course Time'), max_length=255)
    theory = models.CharField(_('Theory'), max_length=255)
    theory_desc = models.CharField(_('Theory Time'), max_length=255)
    practice = models.CharField(_('Practice'), max_length=255)
    practice_desc = models.CharField(_('Practice Time'), max_length=255)

    class Meta:
        verbose_name = _('CoursePlan')
        verbose_name_plural = _('CoursePlan')

    def __str__(self):
        return f"{self.course_time}: {self.theory} - {self.practice}"


class Lesson(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')

    def __str__(self):
        return self.name

class Modul(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=_('Lesson'))

    class Meta:
        verbose_name = _('Modul')
        verbose_name_plural = _('Moduls')

    def __str__(self):
        return self.name


class Experience(models.Model):
    place = models.TextField(_('Place'), max_length=255)

    class Meta:
        verbose_name = _('Experience')
        verbose_name_plural = _('Experience')

    def __str__(self):
        return self.place


class WorkedPlace(models.Model):
    icon = models.FileField(_('Icon'), upload_to='course/icons')

    class Meta:
        verbose_name = _('WorkedPlace')
        verbose_name_plural = _('WorkedPlace')

    def __str__(self):
        return "Icon"


class AboutTeacher(models.Model):
    image = models.ImageField(_('Image'), upload_to='course/about')
    experience = models.ManyToManyField(Experience, verbose_name=_('Experience'))
    work_place = models.ManyToManyField(WorkedPlace, verbose_name=_('Work place'))

    class Meta:
        verbose_name = _('AboutTeacher')
        verbose_name_plural = _('AboutTeacher')

    def __str__(self):
        return "teacher's information"


class Computer(models.Model):
    processor = models.CharField(_('Processor'), max_length=255)
    cpu = models.CharField(_('CPU'), max_length=255)
    vidio_card = models.CharField(_('Vidio Card'), max_length=255)
    screen = models.CharField(_('Screen'), max_length=255)

    class Meta:
        verbose_name = _('Computer')
        verbose_name_plural = _('Computer')

    def __str__(self):
        return _("Computer's information")


class Course(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    desc = models.TextField(_('Description'))
    icon = models.FileField(_('Icon'), upload_to='course/icons')
    for_who = models.ForeignKey(ForWho, on_delete=models.CASCADE, verbose_name=_('ForWho'))
    course_plan = models.ForeignKey(CoursePlan, on_delete=models.CASCADE, verbose_name=_('CoursePlan'))
    modul = models.ForeignKey(Modul, on_delete=models.CASCADE, verbose_name=_('Modul'))
    about_teacher = models.ForeignKey(AboutTeacher, on_delete=models.CASCADE, verbose_name=_('AboutTeacher'))
    about_computer = models.ForeignKey(Computer, on_delete=models.CASCADE, verbose_name=_('AboutComputer'))

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Course')

    def __str__(self):
        return self.name


