from sys import argv

script_param_py, profit_in_hours, rate_in_hour, premium = argv

def formula(profit_in_hours, rate_in_hour, premium):
    return (int(profit_in_hours) * int(rate_in_hour)) + int(premium)

print(formula(profit_in_hours, rate_in_hour, premium))
