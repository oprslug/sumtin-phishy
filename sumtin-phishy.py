#!/usr/bin/python3

import smtplib

print("sumtin-phishy by opr_slug IG")
print("must have gmail account!")
victim = input("victims email : ")
yo_email = input("yo gmail : ")
yo_pass = input ("yo pass : ")
phishingsubj = input ("yo phishing subj : ")
phishingmsg = input ("yo phishing message : ")
                                                                           
victimsemail = (victim)
hackeremail = (yo_email)
hackerspassword = (yo_pass)
phishingsubject = (phishingsubj)
phishingmessage = (phishingmsg)
message = 'Subject: {}\n\n{}'.format(phishingsubj, phishingmsg)

server = smtplib.SMTP("smtp.gmail.com" , 587)
server.ehlo()
server.starttls()
server.login(hackeremail,hackerspassword)
server.sendmail(hackeremail , victimsemail , message)
print("PHISHING EMAIL SENT!")
print("OPR GANG 2K20")
print("MADE BY OPR_SLUG")
