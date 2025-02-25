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
    print("\n#################################################")
    print("###                                           ###")
    print("###  Welcome to the Loan Payment Calculator!  ###")
    print("###                                           ###")
    print("#################################################")

    principal = get_principal()
    annual_rate = get_interest_rate()
    years = get_loan_term()
    monthly_payment = calculate_monthly_payment(principal, annual_rate, years)

    display_results(principal, annual_rate, years, monthly_payment)

def get_principal():
    principal = float(input("Enter the loan principal amount($): "))
    if principal > 0:
        return principal
    else:
        print("Error: Please Enter a Valid Input")

def get_interest_rate():
    annual_rate = float(input("Enter the annual interest rate (in %, e.g. 5.0 for 5%, or 6.5 for 6.5%): "))
    if annual_rate > 0:
        return annual_rate
    else:
        print("Error: Please Enter a Valid Input")

def get_loan_term():
    years = int(input("Enter the loan term in years: "))
    if years > 0:
        return years
    else:
        print("Error: Please Enter a Valid Input")

def calculate_monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    number_of_payments = years * 12
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** (-number_of_payments))
    return monthly_payment

def display_results(principal, annual_rate, years, monthly_payment):
    total_payments = years * 12
    total_amount = monthly_payment * total_payments
    print("\n--- Loan Payment Summary ---")
    print(f"Loan principal:    ${principal:.2f}")
    print(f"Annual Interest:    {annual_rate:.2f}%")
    print("Loan Term:         ", years, "years")
    print(f"Monthly Payment:   ${monthly_payment:.2f}")
    print(f"Total Payment:     ${total_amount:.2f}")

main()