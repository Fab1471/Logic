# Write a program that returns the hourly pay of a worker considering his base monthly salary and the number of hours worked per month. .

# salary/number of hours = pay rate per hour

# What is the necessary data input?
# What do I have to do with that data?
# What are the problem constraints?
# What is the expected result?
# What is the step sequence necessary to get the expected result?

from time import sleep


print('Welcome to the Hourly Program Salary\n')
sleep(0.7)
print('This program is going to calculate how much you get per hour. .')

monthly_salary = float(input('What is your salary: '))
hours_per_day = float(input('How many hours do you work per day? '))
qtd_days_per_week = int(input ('How many days per week do you work? '))

hours_per_week = hours_per_day * qtd_days_per_week

hours_per_month = hours_per_week * 4

pay_rate_hour = monthly_salary / hours_per_month

print(f'Your pay rate per hour, considering that you work {qtd_days_per_week} days per week and your salary is {monthly_salary:.2f} is {pay_rate_hour:.2f} per hour.\n Besides that, you work a total of {hours_per_month} hours per month.')
