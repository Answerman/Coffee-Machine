# 0 — 15,527: 0% tax
# 15,528 — 42,707: 15% tax
# 42,708 — 132,406: 25% tax
# 132,407 + : 28% tax

taxable_income = int(input())
tax = 0.00

if taxable_income < 15528:
    tax = 0.00
elif 15528 <= taxable_income <= 42707:
    tax = 0.15
elif 42708 <= taxable_income <= 132406:
    tax = 0.25
else:
    tax = 0.28

tax_payable = tax * float(taxable_income)
print(f"The tax for {taxable_income} is {tax * 100:.0f}%. That is {tax_payable:.0f} dollars!")
