

def clean(amount):
    amount = amount.replace('$','')
    amount = amount.replace('.','')
    int_amount = int(amount)
    return int_amount

def change(amount):
    cash_register = {'benjamins': 100, 'grants': 0, 'jacksons': 100, 'hamiltons': 0, 'lincolns': 100,
                     'washingtons': 100, 'quarters': 100, 'dimes': 100, 'nickles': 100}
    benjamins = 0
    grants = 0
    jacksons = 0
    hamiltons = 0
    lincolns = 0
    washingtons = 0
    quarters = 0
    dimes = 0
    nickles = 0
    while amount >= 10000 and cash_register['benjamins'] > 0:
        benjamins += 1
        cash_register['benjamins'] -= 1
        amount = amount - 10000
    while amount >= 5000 and cash_register['grants'] > 0:
        grants += 1
        cash_register['grants'] -= 1
        amount = amount - 5000
    while amount >= 2000 and cash_register['jacksons'] > 0:
        jacksons += 1
        cash_register['jacksons'] -= 1
        amount = amount - 2000
    while amount >= 1000 and cash_register['hamiltons'] > 0:
        hamiltons += 1
        cash_register['hamiltons'] -= 1
        amount = amount - 1000
    while amount >= 500 and cash_register['lincolns'] > 0:
        lincolns += 1
        cash_register['lincolns'] -= 1
        amount = amount - 500
    while amount >= 100 and cash_register['washingtons'] > 0:
        washingtons += 1
        cash_register['washingtons'] -= 1
        amount = amount - 100
    while amount >= 25 and cash_register['quarters'] > 0:
        quarters += 1
        cash_register['quarters'] -= 1
        amount = amount - 25
    while amount >= 10 and cash_register['dimes'] > 0:
        dimes += 1
        cash_register['dimes'] -= 1
        amount = amount - 10
    while amount >= 5 and cash_register['nickles'] > 0:
        nickles += 1
        cash_register['nickles'] -= 1
        amount = amount - 5
    print('The least amount of change is:\n{} Hundids\n{} Fiddies\n{} Twennies\n{} Tenners\n{} Fiver\n{} '
          'Dolla Bills\n{} quarters\n{} dimes\n{} nickles\n{} pennies'.format(benjamins,grants,jacksons,hamiltons,
            lincolns,washingtons,quarters, dimes, nickles, amount))

def go():
    amount = input('How much money are we talking about?')
    clean_amount = clean(amount)
    change(clean_amount)

go()