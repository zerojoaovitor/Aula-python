import smtplib
server = smtplib.SMTP(host='host_address',port=your_port)


temperatura = float(input("Informar a temperatura"))

if temperatura > 40:
