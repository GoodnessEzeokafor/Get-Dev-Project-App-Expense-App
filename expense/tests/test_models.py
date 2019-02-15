
from django.test import TestCase
from expense.models import Expense
from django.contrib.auth.models import User




class ExpenseModelTest(TestCase):
    def setUp(self):
        #set up non-modified objecs used by all tes methods
        self.user = User.objects.create(
            username = "test_user",
            password="secret"
        )
        self.expense =  Expense.objects.create(
            user = self.user, 
            value="Bought Apple",
            reason="To Eat" )
        
    def test_user_label(self):
        expense = self.expense
        print(expense)
        field_name = expense._meta.get_field('user').verbose_name
        self.assertEquals(field_name, 'user')

    def test_value_label(self):
        expense = self.expense
        field_name = expense._meta.get_field('value').verbose_name
        self.assertEqual(field_name,"value")
    
    def test_reason_label(self):
        expense = self.expense
        field_name = expense._meta.get_field('reason').verbose_name
        self.assertEqual(field_name,"reason")
    
    def test_date_expense_was_made_label(self):
        expense = self.expense
        field_name = expense._meta.get_field('date_expense_was_made').verbose_name
        self.assertEqual(field_name,"date expense was made")

    def test_date_expense_created_label(self):
        expense = self.expense
        field_name = expense._meta.get_field('date_expense_created').verbose_name
        self.assertEqual(field_name,"date expense created")

    def test_date_expense_updated_label(self):
        expense = self.expense
        field_name = expense._meta.get_field('date_expense_updated').verbose_name
        self.assertEqual(field_name,"date expense updated")


    def test_value_max_length(self):
        expense = self.expense
        max_length = expense._meta.get_field('value').max_length        
        self.assertEqual(max_length, 255)

    def test_reason_max_length(self):
        expense = self.expense
        max_length = expense._meta.get_field('reason').max_length        
        self.assertEqual(max_length, 255)

    
    def test_expected_string_representation(self):
        expense = self.expense
        expected_str_rep = f"Expenses: {expense.value}"
        self.assertEquals(expected_str_rep, str(expense))

