from django.test import TestCase
from expense.models import Expense
from django.contrib.auth.models import User
from django.urls import reverse

class ExpenseListViewTest(TestCase):
    # @classmethod
    def setUp(self):
        # create 10 expense for pagination test
        number_of_expense = 10
        test_user1 = User.objects.create_user(
            username="testuser1",
            password = "secret"
        )
        test_user2 = User.objects.create_user(
            username = "testuser2",
            password ="secret"
        )
        test_user1.save()  # saves the user
        test_user2.save() # saves the user

        for expense_id in range(number_of_expense):
            Expense.objects.create(
                user = test_user1,
                value = "Made Expense",
                reason = "Hade to made some expenses"
            )
    
    
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('expense:expenses_list'))
        self.assertRedirects(response, "/account/login/?next=/expenses/list")

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(
            username="testuser1",
            password="secret"
        )
        response = self.client.get(reverse("expense:expenses_list"))

        #check our user is logged in 
        self.assertEqual(str(response.context['user']), 'testuser1')
        #check that we got a response "success"
        self.assertEqual(response.status_code, 200)


        # check we used correct templates
        self.assertTemplateUsed(response, "expenses/list.html")
        

    # def test_view_url_exists_at_desired_location(self):
    #     response = self.client.get("expense/list")
    #     self.assertEqual(response.status_code, 200)
    
