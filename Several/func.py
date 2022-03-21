    #The transaction amount should not be above the account limit
    if   transaction.amount > accountData.av ailableLimit:
        rejectedReasonList.append("CODE: DEscription")