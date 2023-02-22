import pickle 
def LOginning_in():


    def log_in():
        with open("dump.dat", 'rb') as dump_in:
            base = pickle.load(dump_in)

        # #сохраняем словарь в файл
        # with open('dump.dat', 'wb') as dump_out:
        #     pickle.dump(base, dump_out)
        llogin = input("Input your login: ")
        if llogin in base: #проверить наличие логина в словаре
            passww = input("Input your password: ")
            mail = input("Input your mail: ")
            if base[llogin] == passww:
                print("Well Done. Now u're in your account: ",llogin )
                from email.message import EmailMessage
                import ssl
                import smtplib
            
                email_sender = 'arseny.atnashev@gmail.com'
                email_password = "VTQXZPISYJWPRNDH"
                email_receiver = mail

                subject = 'Registration another account for <Python programming without knowing programming>'
                body = """
                Nobody should knows this secret code
                ---------------------------------
                code: 
                """
                body = body

                em = EmailMessage()
                em['From'] = email_sender
                em['To'] = email_receiver
                em['subject'] = subject
                em.set_content(body)

                context = ssl.create_default_context()


                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(email_sender, email_password)
                    smtp.sendmail(email_sender, email_receiver, em.as_string())

            else:
                print("Incorrect password")
        else:
            print("incorrect login")


        

