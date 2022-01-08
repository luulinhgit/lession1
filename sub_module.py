def emailProcess(email):
    email_username=email[0:email.index("@")]
   # print(f"username is {email_username}")
    email_domain=email[email.index("@")+1:]
    #print(f"domain is {email_domain}")
    return [email_username,email_domain]
def printMsg(email_username,email_domain):
    print(f"username is {email_username}\ndomainname is {email_domain}")
def main():
  email=  input("please enter your email address:").strip()
  email_username,email_domain=emailProcess(email)
  printMsg(email_username,email_domain)
if __name__ == '__main__':

    main()