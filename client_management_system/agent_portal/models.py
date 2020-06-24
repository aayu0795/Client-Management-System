from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):
    pass


GENDER = {
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others')
}


class Customer(models.Model):
    agent = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(
        _('Name'), max_length=100, blank=False)
    age = models.IntegerField(
        _('Age'), blank=False)
    gender = models.CharField(
        _('Gender'), choices=GENDER, max_length=1, blank=False)
    contact = models.CharField(
        _('Contact'), max_length=10, blank=False)

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _('Customers')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("customer_detail", kwargs={"pk": self.pk})


class HomepageHeading(models.Model):
    main_heading = models.CharField(
        _('Main Heading'), max_length=50, blank=False)
    sub_heading = models.TextField(
        _('Sub Heading'), max_length=500, blank=True)

    class Meta:
        verbose_name = _("Homepage Heading")
        verbose_name_plural = _("Homepage Heading")


class HomepageBody(models.Model):
    description = models.TextField(
        _('Description'), max_length=500, blank=False)
    thumbnail = models.ImageField(_('Thumbnail'), upload_to='Homepage')

    class Meta:
        verbose_name = _("Homepage Body")
        verbose_name_plural = _("Homepage Body")


class AboutpageHeading(models.Model):
    main_heading = models.CharField(
        _('Main Heading'), max_length=50, blank=False)
    sub_heading = models.TextField(
        _('Sub Heading'), max_length=500, blank=True)

    class Meta:
        verbose_name = _("Aboutpage Heading")
        verbose_name_plural = _("Aboutpage Heading")


class AboutpageBody(models.Model):
    description = models.TextField(
        _('Description'), max_length=500, blank=False)
    thumbnail = models.ImageField(_('Thumbnail'), upload_to='About')

    class Meta:
        verbose_name = _("Aboutpage Body")
        verbose_name_plural = _("Aboutpage Body")


class CsvFile(models.Model):
    agent_id = models.IntegerField(_('Agent Id'))
    csv_file = models.FileField(_('Csv Files'), upload_to='Csv_files')
    completed = models.BooleanField(_('Completed'), default=False)
