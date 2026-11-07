# Email sender program
import smtplib as s

ob = s.SMTP("smtp.gmail.com", 587)
ob.ehlo()
ob.starttls()
ob.login("dharmikzanzmera8@gmail.com", "superm@n.7818")
subject = "Test Email"
body = "This is a test email sent from Python."
massage = f"Subject: {subject}\n\n{body}"
# massage = "Subject: {}\n\n{}".format(subject, body)
listadd = ['dharmikzanzmera18@outlook.com']
ob.sendmail("dharmikzanzmera8@gmail.com", listadd, massage)
print("Email sent successfully!")
ob.quit()