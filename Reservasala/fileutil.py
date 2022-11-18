
def read_room_file(url):
    file = open(url)
    data = file.read()
    data = data.replace("\n",'') #Remove as quebras de linha do texto
    rooms = []
    #Separa as salas
    rooms_raw = data.split(";")
    for room in rooms_raw:
        #Separa em tres seções
        split_data = room.split(":")
        name = split_data[0] #Nome da sala
        appointments = []
        appointments_raw = split_data[1].split('f') #Dias da semana reservados
        #Separa as reservas
        for appointment in appointments_raw:
            day = appointment.split(",")
            day_data = {
                "morning": day[0],
                "evening" : day[1],
                "night" : day[2]
            }
            appointments.append(day_data)
        new_room = {
            "name": name,
            "appointments": appointments
        }
        rooms.append(new_room)
    return rooms

def write_room_file(data,destiny):
    data_str = ""
    file = open(destiny)
    for room in data:
        #Adiciona o nome a string
        data_str = data_str + room["name"]
        for appointment in room["appointments"]:
            data_str = data_str + appointment["morning"] + "," +appointment["evening"] + "," + appointment["night"]
        data_str = data_str + ";"
    print("Aruivo escrilto eba!")
    file.write(data_str)


