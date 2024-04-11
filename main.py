import lamp 
import pult 
import manip 
import socket
import time


adreses = {
    "core": "192.168.42.241",
    "lamp": "192.168.42.10",
    "pult" :"192.168.42.88",
    "manip" :"192.168.42.200",
    "conveer": "192.168.42.15",
    "camera": "192.168.42.16"
}

port = 8888

AUTO = False
START = False
conveyor = False
work = True

red_tomatoes = 0
green_tomatoes = 0

red_ball = False

point = 0
iter = 0


def parseMsg(data: bytes) -> list:
    data = data.decode()
    data = list(data.split(":"))
    
    return data


if __name__ == '__main__':
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    NanoPiServer = (adreses["core"], port)
    udp.bind(NanoPiServer)
    print("Server start")
    

    coords = manip.generate_udp_packets_to_manip()


    while True:

        while not START:
            data, addr = udp.recvfrom(1024) 
            parse = parseMsg(data)

            if parse[0] == "R" and parse[3] == "1": #зеленая кнопка для АВТОМАТИЧЕСКОГО режима
                print("Start main in <<AUTO>> mode")
                print(parse)
                lamp.send_lamp("auto")
                pult.send_pult("auto", 2, "Auto mode")
                
                manip.move_home() #двигаем манипуляятор в зону конвейера
                time.sleep(3)

                START = True
                AUTO = True

            elif parse[0] == "R" and parse[4] == "1": #нажали желтую кнопку манипулятор сработает один раз НАДО ПРОВЕРИТЬ КОД ЦВЕТА ПУЛЬТА!!!!
                print("Start main in <<MANUAL>> mode")
                print(parse)
                lamp.send_lamp("wait")
                pult.send_pult("wait", 2, "Manual mode")
                
                manip.move_home()  #двигаем манипуляятор в зону конвейера
                time.sleep(3)

                START = True
                AUTO = False
                state_but = int(parse[4])
            



        try:
            data, addr = udp.recvfrom(1024) 
            data = parseMsg(data)
            print("Received message:", data, "from:", addr)


            if data[0] == "R":    #dead mans switch
                if data[2] == "1":
                    lamp.send_lamp("error")  
                    pult.send_pult("error", 2, "ostanovka")
                    break  #прекращаем работу, похорошему надо манипулятор передвинуть на базу

                elif int(data[4]) > state_but: #если желтую кнопку нажали еще раз то исполняется следующая точка
                    point += 1
                    work = True
                    state_but = int(data[4])


            elif data[0] == "c": #сообщение от камеры
                print("Камера отправила:", data)
                if data[1] == "1":
                    red_ball = True
                
                else: red_ball = False



            elif data[0] == "V":  #сообщение от dxl-iot  ПАКЕТ ФОРМАТА   V:1# ( 0/1 сервисный робот приехал и готов получить груз -> конвейер включен)
                if data[1] == "1":
                    conveyor = True  #конвейер запущен

                    print("Start conveyor")
                    lamp.send_lamp("move")
                    pult.send_pult("move", 2, "Good tomatoes: " + str(red_tomatoes))  #так как подьезд робота и включение конвейерной ленты происходят одновременно то нет смысла управлять конвейером цбу
                    pult.send_pult("move", 3, "Conveyor is moving")

                elif data[1] == "0" and conveyor:   #конвейер остановлен, помидоры закончились и ячейка ожидает
                    lamp.send_lamp("wait")
                    pult.send_pult("wait", 2, "Tomatoes are over")
                    pult.send_pult("wait", 3, "Conveyor is stopped")



            if AUTO:
                lamp.send_lamp("move")
                pult.send_pult("move", 2, "кол-во помидор: " + str(red_tomatoes))
                

                if iter == 8: #когда манипулятор пройдет по всем позициям одной точки мы можем сменить точку
                    red_tomatoes += 1
                    pult.send_pult("move", 2, "кол-во помидор: " + str(red_tomatoes))

                    iter = 0
                    point +=1

                if point == 6: # 6 помидор перетащили
                    print("Помидоры закончились")
                    lamp.send_lamp("wait")
                    pult.send_pult("wait", 2, "кол-во помидор: " + str(red_tomatoes))
                    work = False

                if work:
                    start_time = time.time()
                    manip.move_manip(coords[point][iter]) #в цикле отправляю один пакет и меняю его индексы
                    if time.time() - start_time > 3:  #засекаю 3 секунды но программа не спит
                        iter +=1
                


            elif not AUTO:
                lamp.send_lamp("move")
                pult.send_pult("move", 2, "кол-во помидор: " + str(red_tomatoes))
                

                if iter == 8: #когда манипулятор пройдет по всем позициям одной точки мы можем сменить точку
                    red_tomatoes += 1
                    pult.send_pult("move", 2, "кол-во помидор: " + str(red_tomatoes))

                    iter = 0
                    work = False

                if work:
                    start_time = time.time()
                    manip.move_manip(coords[point][iter]) #в цикле отправляю один пакет и меняю его индексы
                    if time.time() - start_time > 3:  #засекаю 3 секунды но программа не спит
                        iter +=1
                



            
            
            # move_manip()
            
            time.sleep(0.2)


 

        except KeyboardInterrupt as e:
            print("Interrupted")
            break
    exit()