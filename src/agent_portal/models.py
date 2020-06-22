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
    contact = models.IntegerField(
        _('Contact'), blank=False)

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _('Customers')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("customer_detail", kwargs={"pk": self.pk})
