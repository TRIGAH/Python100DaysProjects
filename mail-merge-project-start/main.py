invited_names = []
invited_letters = []

def get_letter():            
    with open("mail-merge-project-start\\Input\\Letters\\starting_letter.txt") as letters:
        letter = letters.read()
    return letter    

def get_invited_names():
    with open("mail-merge-project-start\\Input\\Names\\invited_names.txt") as names:
        for name in names.readlines():
            invited_name=name.replace("\n","")
            invited_names.append(invited_name)
    return invited_names        
          
def print_invitation_letter(names,letter):          
    for name in names:
        invitation = letter.replace("[name]",f"{name}")
        with open(f"mail-merge-project-start\\Output\\ReadyToSend\\letter_for_{name}.txt",'w') as invite:
            invite.write(invitation)
            
print_invitation_letter(get_invited_names(),get_letter())
