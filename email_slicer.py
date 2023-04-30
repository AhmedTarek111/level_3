email="ahmedtarekalsaudi@gmail.com@gmail.com"

def email_slicer(email):
    email=email.split("@")
    username=email[0];domain=email[1]
    return(f' username = {username}\n domain = {domain} ')
print(email_slicer(email))