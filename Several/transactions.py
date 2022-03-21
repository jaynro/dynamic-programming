

from curses import ALL_MOUSE_EVENTS

def calculateFirstTransactionPercentage(listOfApprovedTransactions):
    # TODO
    if len(listOfApprovedTransactions ) ==0:
        # calc not exceed limit
        return 

    # TODO Calculate transaction percentage ; listOfApprovedTransactions[0]
    # Case 1 -> limit 100; ta =20;  listOfApprovedTransactions [0] - true
    # Case 2 -> limit 100; ta =20;  listOfApprovedTransactions[20] - true
    # Case 3 -> limit 100; ta =20;  listOfApprovedTransactions[71,] - true
    # Case 3 -> limit 100; 91 ; listOfApprovedTransactions[ 91] - 

    return

def isTransactionAuthorized(accountData, transaction, listOfApprovedTransactions):
    
    rejectedReasonList=[]

    #The transaction amount should not be above the account limit
    if   transaction.amount > accountData.av ailableLimit:
        rejectedReasonList.append("CODE: DEscription")

    #2. No transaction should be approved when the card is blocked
    if accountData.cardStatus == "blocked":
        rejectedReasonList.append("CODE: DEscription")

    # 3. 3. The first transaction shouldn't be above 90% of the limit
    limitPercentage = calculateFirstTransactionPercentage(transaction, listOfApprovedTransactions)
    if limitPercentage > 90 :
        rejectedReasonList.append("CODE: DEscription")



    # TRUE or FALSE : if transaction meets the rules
    # Updated available Limit
    # If false -> Reasons
    return authorizationResult


transaction;
    merchant
    amount
    date

accountData:
    cardStatus
    availableLimit

authorizationResult:
    trasactionId
    Boolean authorizationStatus:
    accountData 
    rejectedReasons = []

