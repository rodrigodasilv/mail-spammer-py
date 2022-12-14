import smtplib
from getpass import getpass

remetente = input("Informe o e-mail do remetente (seu e-mail): ")
senha_remetente = getpass("Informe a senha do e-mail do remetente (sua senha): ")
destinatario = input("Informe o e-mail do destinatário: ")
assunto = input("Informe o assunto e-mail: ")
texto = input("Informe o texto do corpo e-mail: ")
repeticoes = int(input("Informe a quantidade de repetições de envio do e-mail: "))

#Faz o login no gmail
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(remetente, senha_remetente)

for vezes in range(repeticoes):
    assunto = assunto + str(vezes) #Assunto do email
    mensagem = 'Subject: {}\n\n{}'.format(assunto, texto)
    server.sendmail(remetente, destinatario, mensagem.encode('utf-8'))
    print("Iteração " + str(vezes))
    assunto = ""
server.quit()
print("Email enviado " + str(repeticoes) + " vezes.")