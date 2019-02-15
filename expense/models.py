from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )
    value =models.CharField(
        max_length=255, 
        blank=False, 
        null=False,
        help_text = "Value of Expense")
    reason = models.CharField(max_length=255,help_text="Reasons Expense Was Made")
    date_expense_was_made = models.DateField(
        help_text = "Enter Date Expense Was Made in this format YYYY-MM-DD",
        blank = True,
        null=True,
    )
    date_expense_created = models.DateField(
        auto_now=True
    )
    date_expense_updated =models.DateField(
        auto_now_add=True
    )
    def __str__(self):
        return "Expenses: %s" % (self.value)

    def get_absolute_url(self):
        return reverse("expense:expense_detail",args=[self.id])
    



# 400be4effc19143042cb295e0010f256





    