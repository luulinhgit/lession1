from sub_module import emailProcess,printMsg

def main():
    emails = ['qyd@gmail.com', 'youtube@luulinh.com', 'manchestercity@winner.com']
    for email in emails:
        email_username, email_domain=emailProcess(email)
        printMsg( email_username, email_domain)
if __name__ == '__main__':
    main()