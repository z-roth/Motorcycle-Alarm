import smtplib # import SMTP module
carriers = {
        'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

# sends a text message to a number with a carrier, with a message (all three arguments are strings)
def send(number, carrier, message):
    to_number = number + carriers[carrier] # concatenate number and given carrier's email 
    auth = ('<your email address>', '<your email password>') 

    # initiate server connection
    server = smtplib.SMTP("<your emails SMTP server>", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    # send message
    server.sendmail(auth[0], to_number, message)
    
