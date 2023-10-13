balanceChecking = [0]
chChAm = [0]
balanceSavings = [0]
svChAm = [0]
trHistChe = [""]
trHistSav = [""]


def accountBalanceChecking(abc):
    balanceChecking.append(abc)

def checkingChangeAmount(deposit):
    chChAm.append(deposit)

def accountBalanceSavings(abc):
    balanceSavings.append(abc)
    
def savingsChangeAmount(withdraw):
    svChAm.append(withdraw)
    
def transactionHistoryChecking(dAndT):
    trHistChe.append(dAndT)

def transactionHistorySavings(dAndT):
    trHistSav.append(dAndT)

    

