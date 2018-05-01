from django.db import models
from django.contrib.auth.models import User


class CreditCard(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    name = models.CharField(max_length=500, db_column='Name')
    login_page = models.URLField(db_column='LoginPage')

    class Meta:
        db_table = 'CreditCard'


class UserCard(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    user = models.ForeignKey(User, db_column='UserId')
    credit_card = models.ForeignKey(CreditCard, db_column='CreditCardId')
    name = models.CharField(max_length=500, db_column='Name')
    last_paid_at = models.DateTimeField(blank=True, db_column='LastPaidAt')
    amount_paid = models.FloatField(blank=True, db_column='AmountPaid')
    goal = models.FloatField(blank=True, db_column='Goal')
    cancel_by = models.DateField(blank=True, db_column='CancelBy')
    is_cancelled = models.BooleanField(default=False, db_column='IsCancelled')

    class Meta:
        db_table = 'UserCard'


