var daySelect = $("#dayselect")
var periodSelect = $("#periodselect");
var roomSelect = $("#roomselect");

function submit(){

}

//Coloca os dados no select
var f = function(response){
    console.log(response);
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