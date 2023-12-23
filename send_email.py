# УНИВЕРСАЛЬНЫЙ МОДУЛЬ ДЛЯ ОТПРАВКИ НА ПОЧТУ СООБЩЕНИЙ И ФАЙЛОВ

#библиотеки для работы с почтой
import smtplib
from os.path import basename
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


from_address = "alax.alax.91@mail.ru"
to_address = "alax.alax.91@mail.ru"
my_password = "5hYMz1bXtdp6z6MTAesx"  #пароль для почты для подключения внешнего приложения от mail
reportname = 'report.xml'

msg = MIMEMultipart()           # экземпляр объекта письма
msg['From'] = from_address      # поля почты
msg['To'] = to_address           # поля почты
msg['Subject'] = "Привет от Питона"      # поля почты в заголовке

# чтение байтов файла
with open(reportname, "rb") as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(reportname)        #создаем файл для объекта письма msg
    msg.attach(part)                                            # добавляем файл в наш экземпляр объекта письма msg

body = "Это пробное сообщение"   # текст письма в теле сообщения
msg.attach(MIMEText(body, 'plain'))     # присоединение body к объекту msg

server = smtplib.SMTP_SSL('smtp.mail.ru', 465)          # подключение к порту mail 465 , у каждого почтового сервера свой порт
server.login(from_address, my_password)                 # авторизация в почтоывом сервере
text = msg.as_string()                                  # перевод всех полей объекта msg в string
server.sendmail(from_address, to_address, text)         # отправляем сообщение msg
server.quit()



