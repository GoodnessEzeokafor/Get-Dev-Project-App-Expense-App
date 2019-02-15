import datetime
from django.test import TestCase
from expense.forms import ExpenseForm



class AddExpenseFormTest(TestCase):
    def test_value_field_label(self):
        form = ExpenseForm()
        self.assertTrue(form.fields['value'].label == 'Value' or form.fields['Value'] == None)
    
    def test_value_field_help_text(self):
        form = ExpenseForm()
        self.assertTrue(form.fields['value'].help_text == "Value of Expense")

    def test_value_field_max_length(self):
        form = ExpenseForm()
        max_length = form.fields['value'].max_length
        self.assertEqual(max_length, 255)


    def test_reason_field_label(self):
        form = ExpenseForm()
        self.assertTrue(form.fields['reason'].label == 'Reason' or form.fields['reason'] == None)

    def test_reason_field_help_text(self):
        form = ExpenseForm()
        self.assertTrue(form.fields['reason'].help_text == "Reasons Expense Was Made")

    def test_date_expense_was_made(self):
        form = ExpenseForm()
        self.assertTrue(form.fields['date_expense_was_made'].help_text == "Enter Date Expense Was Made in this format YYYY-MM-DD")
