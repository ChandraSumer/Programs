a=0
while a<50:
    import smtplib
    a=a+1
    text = "Egmore Nungabakkam"
     
    ml = smtplib.SMTP ('smtp.gmail.com',587)
     
    ml.ehlo()
     
    ml.starttls()
     
    ml.login('johndoeappleseed2@gmail.com','tarana1969')
     
    #Now here comes the fun part.
    #Let's say you want your boss
    #to think he got the mail from CIA.
    #Type in like nobody@cia.com in place of 
    #foremail and your boss's email in place
    #of receiver.
     
    ml.sendmail('nobody@cia.com','500061047@stu.upes.ac.in',text)
     
    ml.close()
