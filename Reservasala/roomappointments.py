from flask import Flask
from flask import request
from fileutil import read_room_file, write_room_file
import json
global_url = "salas.txt"
app = Flask(__name__)


@app.route('/checkavailable',methods = ['POST'])
def check_available():
    data = read_room_file(global_url)
    #Dados com o nome da sala, e o dia que se deseja checar a disponibilidade
    query_data = request.form['querydata']
    query = json.loads(query_data)

    #Verifica se a sala está disponivel retorna 3 se sala não encontrada, 2 se indisponivel, 1 se ocupada e 0 se disponivel
    for room in data:
        if(room.name == query["name"]):
            appointment = room.appointments[int(query["day"])]
            if(appointment[query["period"]]==0):
                return 0
            elif(appointment[query["period"]]==2):
                return 2
            return 1
    return 3

# retorna 3 caso não encontre a sala
@app.route('/getavailabledays',methods=['POST'])
def get_available_days():
    data = read_room_file(global_url)
    room_name = request.form["name"]
    found_room = None
    for room in data:
        if(room.name==room_name):
            found_room = room
            break
    if(found_room==None):
        return 3
    return json.dumps(room)

#Obtem um vetor com todas as salas disponiveis nos dias enviados
@app.route("/getavailablerooms",methods=['POST'])
def get_available_rooms():
    data = read_room_file(global_url)
    days_raw = request.form["days"]
    days = json.load(days_raw)
    rooms = []
    for room in data:
        #Verifica se a sala está disponivel em algum desses dias
        for day in days:
            appointment = room[int(day["day"])]
            #Verifica se a sala está disponivel em algum dos periodos
            if(appointment["morning"]==0 or appointment["evening"]==0 or appointment==0):
                rooms.append(room)
                break
    return json.dumps(rooms)

#Obtem uma lista com todas as salas
@app.route("/getroomnames",methods=['POST'])
def get_room_names():
    data = read_room_file(global_url)
    names = []
    for room in data:
        names.append(room["name"])
    return json.dumps(names)

#Retorna reservas de uma sala x
@app.route("/getreservation")
def get_reservations():
    data = read_room_file(global_url)
    name = request.form["name"]
    for room in data:
        if(room["name"]==name):
            return json.dumps(room)

#Reserva uma sala, retorna 0 em sucesso, 1 em caso de sala reservada, e 2 em caso de sala ocupada, retorna 3 caso nome da sala seja inexistente
@app.route("/reserveroom")
def reserve_room():
    data = read_room_file(global_url)
    query_raw = request.form["query"]
    query = json.load(query_raw)
    for room in data:
        if(room.name == query["name"]):
            appointment = room.appointments[int(query["day"])]
            if(appointment[query["period"]]==0):
                appointment[query["period"]] =1
                write_room_file(data,global_url)
                return 0
            elif(appointment[query["period"]]==2):
                return 2
            return 1
    return 3 

#Retorna 0 caso cancele a reserva com sucesso, 1 caso a sala não tenha sido reservada, e 2 caso a sala não esteja indisponivel, e 3 caso a sala não tenha sido encontrada
@app.route("/unreserveroom")
def cancel_room_reservation():
    data = read_room_file(global_url)
    query_raw = request.form["query"]
    query = json.load(query_raw)
    for room in data:
        if(room.name == query["name"]):
            appointment = room.appointments[int(query["day"])]
            if(appointment[query["period"]]==0):
                return 1
            elif(appointment[query["period"]]==2):
                return 2
            appointment[query["period"]] =0
            write_room_file(data,global_url)
            return 0
    return 3 

