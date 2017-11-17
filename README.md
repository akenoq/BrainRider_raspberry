# BrainRider_raspberry
Программа для реализации обработки и передачи данных, полученных от API эцефалографа

### 1.0.0
Отправка рандомных данных с расбери POST запросом
(без сокетов) для
post_Request.py

### 1.0.1
Написан socket-сервер и socket-client на Python3
socket_Client.py, socket_Server.py

### 1.0.2
Так как работаем с websocket-сервером на Nodejs
То написан код, отпраляющий ws запросы и получающий ответы
web_socket_Client.py

### 1.0.3
`python server_keyboard.py` => работает на port 9000

В 3D-треначере его указать: `localhost:9000`
