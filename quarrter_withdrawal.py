INVESTMENTS = [
    {"principal":500000,"returns":20000,"principal_returns":520000,"status":"Mature"},
]

# Set Netwoth
def set_networth():
    NETWORTH = 0
    for invest in INVESTMENTS:
        NETWORTH += invest["principal_returns"]
    return NETWORTH    

# Check Amount
def check_amount(amount):
    if amount == 0:
        return True

# Check Status of Account    
def check_status(invest):
    if invest["principal_returns"] == 0:
        invest["status"] = "Closed"
    elif invest["principal"] == 0:
        invest["status"] = "Inactive"    
    else:
        invest["status"] = "Active"

# Check Investments
def check_investments(amount):
    global account,count 
    account = 0
    count = 0
    account = amount
    if account > set_networth():
       print("Insufficient Funds")
    else:
        for invest in INVESTMENTS:
                if invest["status"] == "Mature":
                    if check_amount(account):
                        break
                    if account >= invest["principal_returns"]:
                        account -= invest["principal_returns"]
                        invest["principal"]=0
                        invest["returns"]=0
                        invest["principal_returns"]=0
                        check_status(invest)
                        print(account)
                        print("Account Closed")
            
                    else:
                        if check_amount(account):
                            break
                        elif account <= invest["returns"]:
                            invest["returns"] -= account
                            invest["principal_returns"] = invest["principal"] + invest["returns"]
                            check_status(invest)
                            print(account)
                        elif account > invest["returns"] and account < invest["principal"]:
                            invest["principal"] -= account
                            invest["principal_returns"] = invest["principal"] + invest["returns"]
                            check_status(invest)
                            print(account)
                        else:
                            account -= invest["principal"]   
                            invest["principal"] = 0
                            invest["principal_returns"] = invest["principal"] + invest["returns"]
                            check_status(invest)
                        
                        # if check_amount(account):
                        #     break  
                        # elif account >= invest["principal"]:
                        #     account -= invest["principal"]
                        #     invest["principal"]=0
                        #     invest["principal_returns"] = invest["principal"] + invest["returns"]
                        #     check_status(invest)
                        #     print(account)
                        # else: 
                        #     invest["principal"] -= account 
                        #     account = 0
                        #     invest["principal_returns"] = invest["principal"] + invest["returns"]
                        #     check_status(invest)
                        #     print(f'{account}p...')     
                        # elif account > invest["returns"] and account > invest["principal"]:
                        #     account -= invest["principal"]
                        #     invest["principal_returns"] = invest["principal"] + invest["returns"]
                        #     invest["status"]="Inactive"
                        #     print(account)
     
                        # else:
                        #     invest["returns"] -= account
                        #     account = 0
                        #     invest["principal_returns"] = invest["principal"] + invest["returns"]
                        #     check_status(invest)
                        #     print(f'{account}r....') 
  
                count+=1
        print(f'{count} Accounts Checked')    
        print(INVESTMENTS)                 


# Withdrawal Logic
def withdraw(amount):
        check_investments(amount)            
withdraw(521000)   