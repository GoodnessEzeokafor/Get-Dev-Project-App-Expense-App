#  model for expenses
    # date of the expense
    # the value of the expense
    # the reason of the expense
    # date expense was created
    # user

#  model for a user

# Expense List View
    # the date od the expense
    # the vat (20% of the expense)
    As a user, in the UI, when I write an expense, I can add the chars EUR after it (example : 12,00 EUR). When this happens, the application automatically converts the entered value into pounds and saves this new value in the database. The conversion needs to be accurate. It was decided that our application would call a public API to either realise the conversion or determine the right conversion rate, and then use it.

    As a user, I want to see the VAT calculation update in real time as I enter my expenses




Implementation
    - Home Page
    - Add Expense Page
    - List Expenses
    
    

    AUTH
    - SignUp Page - Logs u in
    - Login Page
    - Logout Page

    
