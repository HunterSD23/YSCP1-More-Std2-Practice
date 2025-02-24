"""
BEGIN (main() function)
    print Application Header

    # Get User Input
    principal = get_principal()
    annual_rate = get_interest_rate()
    years = get_loan_term()

    # calculate monthly payment using the loan formula
    monthly_payment = calculate_monthly_payment(principal, annual rate, years)

    # display the results in a formatted summary
    display_results(principal, annual_rate, years, monthly_payment)
"""

def main():
    principal = get_principal()
    annual_rate = get_interest_rate()
    years = get_loan_term()
    monthly_payment = calculate_monthly_payment(principal, annual_rate, years)

    display_results(principal, annual_rate, years, monthly_payment)

def get_principal():
    while input < 0:
        float(input("Enter the loan principal amount($): "))
        if input > 0:
            return input
        else:
            print("Error: Please Enter a Valid Input")

def get_interest_rate():
    while input < 0:
        float(input("Enter the annual interest rate (in %, e.g. 5.0 for 5%, or 6.5 for 6.5%): "))
        if input > 0:
            return input
        else:
            print("Error: Please Enter a Valid Input")

def get_loan_term():
    while input < 0:
        int(input("Enter the loan term in years: "))
        if input > 0:
            return input
        else:
            print("Error: Please Enter a Valid Input")

def calculate_monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    number_of_payments = years * 12
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ^ (-number_of_payments))
    return monthly_payment

def display_results(principal, annual_rate, years, monthly_payment):
    total_payments = years * 12
    total_amount = monthly_payment * total_payments
    print("Loan Payment Summary:")
    print("Loan principal: $" + principal)
    print("Annual Interest: " + annual_rate + "%")
    print("Loan Term: " + years + " years")
    print("Monthly Payment: $" + monthly_payment)
    print("Total Payment: $" + total_amount)

main()