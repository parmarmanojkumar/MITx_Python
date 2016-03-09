# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 20:58:17 2016

@author: VirKrupa
"""

balance = 126643
annualInterestRate = 0.22
monthlyPaymentRate = 0.4



min_pay = 0
unpaid = 0
paid = 0
bal_pay = balance
lower_bound = balance/12
upper_bound = ((1 + annualInterestRate/12)**12) * lower_bound

while abs(bal_pay) > 0.01:
    min_pay = (lower_bound + upper_bound) / 2
    bal_pay = balance
    month = 0
    while month < 12 :
        month += 1
        paid += min_pay
        unpaid =  bal_pay  -  min_pay
        bal_pay = unpaid * (1 + annualInterestRate/ 12)
    if (bal_pay > 0):
        lower_bound = min_pay
    else:
        upper_bound = min_pay
print 'Lowest Payment: ' + str(round(min_pay,2))


#PS1
#
#month = 0
#min_pay = 0
#unpaid = 0
#paid = 0
#bal_pay = balance
#
#while month < 12 :
#    month += 1
#    print 'Month : ' + str(month)
#    min_pay = monthlyPaymentRate * bal_pay
#    print 'Minimum monthly payment: ' + str(round(min_pay,2))
#    paid += min_pay
#    unpaid =  max(bal_pay  -  min_pay, 0)
#    bal_pay = unpaid * (1 + annualInterestRate/ 12)
#    print 'Remaining balance: ' + str(round(bal_pay,2))
#
#print 'Total paid: ' + str(round(paid,2))
#print 'Remaining balance: ' + str(round(bal_pay,2))

#PS2

#min_pay = 0
#unpaid = 0
#paid = 0
#bal_pay = balance
#
#while bal_pay > 0:
#    min_pay += 10
#    bal_pay = balance
#    month = 0
#    while month < 12 :
#        month += 1
#        paid += min_pay
#        unpaid =  bal_pay  -  min_pay
#        bal_pay = unpaid * (1 + annualInterestRate/ 12)
#    
#print 'Lowest Payment: ' + str(round(min_pay,2))




