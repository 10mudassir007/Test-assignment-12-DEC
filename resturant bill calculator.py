no_of_people = int(input('Enter number of people : '))
cost_meal = int(input('Enter cost of each meal : '))
sales_tax = float(input('Enter sales tax percentage : '))
tip = float(input('Enter tip percentage : '))

total_cost = no_of_people * cost_meal 
total_salesTax = (total_cost/100) * sales_tax
total_tip = (total_cost/100) * tip
total_bill = total_cost + total_salesTax + total_tip
print(f'Total cost of food is : {total_cost}')
print(f'Sales tax : {total_salesTax}')
print(f'Tip : {total_tip}')
print(f'Total bill per person is : {total_bill/no_of_people}') # 1400/100 x 3 3%