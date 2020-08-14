function allowDrop(ev) {
    ev.preventDefault();
}
  
function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
  }


function success(data){
    console.log(data)
    window.location.replace(`http://localhost:8000/song/${data.name}/${data.genre}`)
}
  
function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.files;
    // ev.target.appendChild(document.getElementById(data));
    // var files = ev.originalEvent.dataTransfer.files;

    var formData = new FormData();
    formData.append("audio", data[0]);

    var req = {
        url: "/sendfile",
        method: "post",
        processData: false,
        contentType: false,
        data: formData,
    };

    var promise = $.ajax(req);
    promise.then(success);
}