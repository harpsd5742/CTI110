# CTI 110
# P1T2 - Salary Calculator
# Name
# Date

# Start

# Input the hours worked
hoursWorked = float(input ("How many hours did you work this week? "))
#hoursWorked = int (hoursWorked) # convert to interger
                   
# Input the hourly pay rate
hourlyPay = float (input ("What's your hourly pay rate?")) # get and convert

# Calculatae gross pay (hours worked times pay rate)
grossPay = hoursWorked * hourlyPay
                   
# Display the gross pay
print ("Your gross pay for the week is:$", grossPay)
                   
# End
