from django.db import models

from credit_card.models import CreditCard


class CardPage(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    credit_card = models.ForeignKey(CreditCard, db_column='CreditCardId')
    rank = models.IntegerField(db_column='Rank')
    transition_button = models.CharField(max_length=750, db_column='TransitionButton')

    class Meta:
        db_table = 'CardPage'
        unique_together = (('credit_card', 'rank'),)


class PageActionType(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    name = models.CharField(max_length=500, unique=True, db_column='Name')

    class Meta:
        db_table = 'PageActionType'


class PageAction(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    card_page = models.ForeignKey(CardPage, db_column='CardPageId')
    action_type = models.ForeignKey(PageActionType, db_column='PageActionTypeId')
    value = models.CharField(max_length=750, db_column='Value')

    class Meta:
        db_table = 'PageActionType'




