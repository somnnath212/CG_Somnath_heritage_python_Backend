# Loan eligibility — ALL conditions must be True 

age             = 30 

monthly_income  = 45000 

credit_score    = 720 

existing_loans  = 1 

 

is_eligible = (age >= 21 and age <= 60 and 

               monthly_income >= 30000  and 

               credit_score   >= 700    and 

               existing_loans <= 2) 

 

if is_eligible: 

    print('Loan Approved!') 

else: 

    print('Loan Rejected — criteria not met.') 

# Output: Loan Approved!