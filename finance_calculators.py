# import mathematical function
import math


# print statement to explain to the user what investment option does.
print("\nInvestment - to calculate the amount of interest you'll earn on your investment")

# print statement to explain to the user what bond option does
print("\nBond - to calculate the amount you'll have to pay on a home loan")

# Input for the user to calculate their investment or or bond.
menu = input("\nEnter either 'Investment' or 'Bond' from the menu above to proceed: ").upper()

# if user enters investment.
if menu == "investment".upper():
 
    # user inputs how much they would like to invest.
    amount_invested = float(input("\nHow much money are you investing? "))

    # user inputs their current interest rate
    interest_rate = float(input("\nWhat is the interest rate? " ))/100
 
    # user inputs how many years they would like to invest for.
    time_period = float(input("\nHow many years will you be investing? "))

    # user inout whether they would like simple or compound interest
    interest = input("\nWould you like simple or compound interest? ").lower()

  # calculate simple interest and print.
    if interest == "simple".lower():
        simple_interest = amount_invested *(1+ interest_rate * time_period)
        print (f"\nYour final amount after {float(time_period)} years  will be {simple_interest}")

    # calculate compound interest and print.
    elif interest == "compound".lower(): 
        compound_interest = amount_invested * math.pow((1+ interest_rate),time_period)
        print(f"\nYour final amount after {float(time_period)} years will be {compound_interest}")
     
     # if incorrect entry prompt correct entry
    else: 
        print("\nplease enter 'simple' or 'compound'")   

# if user enters bond in the menu
elif menu == "bond".upper():
    
    # user inputs the current value of their house.
    house_value = float(input("\n What is the present value of the house? "))
    
    # user inputs their annual interest rate
    annual_interest = float(input("\nWhat is your annual interest rate? "))
    
    # variable storing annual interest rate equation
    monthly_interest = (annual_interest/100)/12
    
    # user input time period they will repay over (months)
    repayment_timeframe = float(input("\nOver how many months will the bond be repaid? "))
    
    # variable storing bond repayment equation
    repayment = (monthly_interest * house_value)/(1-(1+monthly_interest)**(- repayment_timeframe))

    # print how much they will have to pay over how many months
    print(f"\nEvery month you will have to repay {repayment} over {int(repayment_timeframe)} months ")

# prompt the user to enter a valid option from the menu
else:
    print("\nPlease enter a valid option")


