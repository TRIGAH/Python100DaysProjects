import smtplib


my_email = "imaps@pristincapital.com"
my_email_pass = "zohoWhizx1?"

with smtplib.SMTP_SSL('smtp.zoho.com',465) as smtp:
    smtp.login(my_email,my_email_pass)
    subject = "Quarrter"
    boby= "Welcome To Quarrter"
    msg= f"Subject:{subject}\n\n{boby}"

    smtp.sendmail(my_email,"togunniyi@pristincapital.com",msg="Subject:Quarrter\n\n Welcome To Quarrter")


# connection = smtplib.SMTP_SSL("smtp.zoho.com",465)
# connection.login(user=my_email,password=my_email_pass)
# connection.sendmail(from_addr=my_email,to_addrs="ijenrandy2@gmail.com",msg="Welcome To Quarrter")
# connection.quit()