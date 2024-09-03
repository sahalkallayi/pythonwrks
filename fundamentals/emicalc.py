#write a program to calculate monthly emi

#emi=loan_amount*intrest_rate(1+intrest_rate)**tenure/((1+intrest_rate)**tenure-1)

loan_amount=int(input("enter loan amount:" ))
tenure=int(input("enter tenure:" ))
intrest_rate=int(input("enter intrest rate:" ))

print(f"loan_amount={loan_amount}")
print(f"tenure={tenure}")
print(f"intrest_rate={intrest_rate}")

intrest_per_month=intrest_rate/(12*100)

emi=loan_amount*intrest_per_month*((1+intrest_per_month)**tenure)/((1+intrest_per_month)**tenure-1)

print(f"monthly emi={emi}")

#totalintrestpayable

total_intrest_payable=tenure*emi

print(f"total_intrest_payable={total_intrest_payable}")

#total amount payable

total_amount=loan_amount*intrest_rate

print(f"total amount{total_amount}:")





