from django.db import models
from django.conf import settings

class Bank(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PaymentDate(models.Model):
     emission_date = models.DateField()
     at_date = models.DateField()
     post_date = models.DateField()


class PayCheck(models.Model):
    bank = models.ForeignKey(Bank, null=False, blank=False, related_name='bank', on_delete=models.DO_NOTHING)
    #pay_date = models.ForeignKey(PaymentDate, null=False, blank=False, on_delete=models.CASCADE, related_name='pay_date')
    check_number = models.IntegerField(unique=True, null=True)
    beneficiary = models.CharField(max_length=100, null=True)
    #money_value = models.DecimalField(max_digits=6, decimal_places=2)
    concept = models.CharField(max_length=200, null=True)
    notes = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    emission_date = models.DateField(blank=True, null=True)
    at_date = models.DateField(blank=True, null=True)
    post_date = models.DateField(blank=True, null=True)
