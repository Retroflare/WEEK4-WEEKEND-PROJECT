import re

class RentalProperty:
    def __init__(self, name):
        self.name = name
        self.property_income = 0
        self.property_expenses = 0
        self.property_cash_flow = 0
        self.property_roi = 0
        self.total_investment = 0
        self.roi = 0

    def validate_input(self, question):
        pattern = re.compile(r'^[0-9]+(\.[0-9]+)?$')
        while True:
            user_input = input(question)
            is_valid = pattern.match(user_input)
            if is_valid:
                return user_input
            else:
                print("That is not a valid input. Please try again.")

    def property_income_calc(self):
        rental_income = self.validate_input("What is your total monthly property rental income?: ")
        parking_income = self.validate_input("What is your total monthly property parking income?: ")
        laundry_income = self.validate_input("What is your total monthly property laundry income?: ")
        storage_income = self.validate_input("What is your total monthly property storage income?: ")
        misc_income = self.validate_input("What is your total monthly property income from all other sources?: ")

        self.property_income = float(rental_income) + float(parking_income) + float(laundry_income) + float(storage_income) + float(misc_income)
        print(f"\nThe total monthly income for this property is ${format(self.property_income, '.2f')}\n")

    def property_expenses_calc(self):
        tax_expenses = self.validate_input("What is your total monthly property tax expense?: ")
        insurance_expenses = self.validate_input("What is your total monthly property insurance expense?: ")
        utilities_expenses = self.validate_input("What is your total monthly property utilities expense?: ")
        hoa_expenses = self.validate_input("What is your total monthly property HOA expense?: ")
        lawn_snow_expenses = self.validate_input("What is your total monthly property lawn/snow expense?: ")
        vacancy_expenses_calc = self.validate_input("What percentage of total monthly income do you want to set aside for vacancy?: ")
        vacancy_expenses = (float(vacancy_expenses_calc) / 100) * self.property_income
        repairs_expenses = self.validate_input("What is your total monthly property repairs expense?: ")
        cap_ex_expenses = self.validate_input("What is your total monthly property capital expenditures expense?: ")
        management_expenses = self.validate_input("What is your total monthly property management expense?: ")
        mortgage_expenses = self.validate_input("What is your total monthly property mortgage expense?: ")

        self.property_expenses = float(tax_expenses) + float(insurance_expenses) + float(utilities_expenses) + float(hoa_expenses) + float(lawn_snow_expenses) + vacancy_expenses + float(repairs_expenses) + float(cap_ex_expenses) + float(management_expenses) + float(mortgage_expenses)
        print(f"\nThe total monthly expense for this property is ${format(self.property_expenses, '.2f')}\n")

    def property_cash_flow_calc(self):
        self.property_cash_flow = self.property_income - self.property_expenses
        print(f"\nThe total monthly cash flow for this property is ${format(self.property_cash_flow, '.2f')}\n")

    def property_roi_calc(self):
        down_payment = self.validate_input("What was your total down payment on this property?: ")
        closing_costs = self.validate_input("What were your total closing costs on this property?: ")
        rehab_budget = self.validate_input("What was your total rehab budget for the property (separate from your repairs and your capital expenditures)?: ")
        misc_other = self.validate_input("What was your total for money down for any other items not included above?: ")

        self.total_investment = float(down_payment) + float(closing_costs) + float(rehab_budget) + float(misc_other)
        self.roi = ((self.property_cash_flow * 12) / self.total_investment) * 100

        print(f"\nThe return on investment (ROI) for this property is {format(self.roi, '.2f')}%")

    def run_program(self):
        print("Welcome to the Rental Income ROI Calculator! This program will prompt you to provide input on various aspects, including property income and expenses. Please make sure to respond using numerical values only, without any special characters such as dollar signs, commas, or percentage signs. Decimal points are allowed.")
        print("After you have entered all the required information, the program will calculate and present the return on investment (ROI) for the property as a percentage (%).")
        print("\nCommence!")
        self.property_income_calc()
        self.property_expenses_calc()
        self.property_cash_flow_calc()
        self.property_roi_calc()

first_property = RentalProperty("First Property")
first_property.run_program()


