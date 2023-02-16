import os
continue_program=True
new_data=[]
highest_bid=0
while continue_program:
    name = input("What is your name?: ")
    bid = input("Whats your bid?: ")

    data={}
    data["name"]=name
    data["bid"]=bid
    new_data.append(data)
    option=input("Are there any other bidders? Type yes or no: ")
    if option == "yes":
        os.system('cls')
    else:
        for i in new_data:
            score = int(i["bid"])
            if score > highest_bid:
                highest_bid = score
                score_name=i["name"]
        continue_program=False
        print(new_data)
        print(score_name + f" is the highest biddder with {highest_bid}")
    

# os.system('cls')