var daySelect = document.getElementById("dayselect")
var periodSelect = document.getElementById("periodselect");
var roomSelect = document.getElementById("roomselect");

//Coloca os dados no select
var f = function(response){
    response = JSON.parse(response);
    console.log(roomSelect);
    response.forEach(function(option){
       let opt = document.createElement('option');
       opt.value = option;
       opt.innerHTML = option;
       roomSelect.appendChild(opt);
    });
}
//Requisicao ajax para obter os dados de sala
$.ajax({
    type: 'POST',
    url: 'http://127.0.0.1:5000/getroomnames',
    contentType: 'application/json; charset=utf-8',
    cache: false,
    crossDomain: true,
    success: f,
    error: function(response){
        console.log("dk rap");
        console.log(response);
    }
});


const whichPokemon = function(response){
    $.notify("Você pode encontrar nesse dia um "+response.name,"info")
}

const notifyAvailable = function(response){
    switch(response){
        case '0':
            $.notify("Sala disponivel","success");
            break;
        case '1':
            $.notify("Sala ocupada","warn");
            break;
        case '2':
            $.notify("Sala não disponivel nesse horario","warn");
            break;
        case '3':
            $.notify("Sala não encontrada");
        default:
            console.log("bruh")
    }
    let url ='https://pokeapi.co/api/v2/pokemon/'+(daySelect.selectedIndex+1)+""+(periodSelect.selectedIndex+1)+(response);
    console.log(url);
    //Pokemon sei la
    $.ajax({
        type: 'GET',
        url:url,
        //contentType: 'application/json; charset=utf-8',
        cache: false,
        crossDomain: true,
        success: whichPokemon,
        error: function(response){
        }
    });
}

function submit(){
    //Obtem os dados dos formularios
    let room = roomSelect.options[roomSelect.selectedIndex].value;
    let period = periodSelect.options[periodSelect.selectedIndex].value;
    let day = daySelect.options[daySelect.selectedIndex].value;
    let data = {
        "name":room,
        "period":period,
        "day":day
    }
    data = JSON.stringify(data);
    //Manda o request
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:5000/checkavailable',
        //contentType: 'application/json; charset=utf-8',
        data: {
          "querydata": data
        },
        cache: false,
        crossDomain: true,
        success: notifyAvailable,
        error: function(response){
          $.notify("Erro ao checar os dados","error");
        }
    });
}