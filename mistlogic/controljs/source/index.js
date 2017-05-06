
class Peticion {
    constructor(url){
        this.url = url;
        this.request = new XMLHttpRequest();
    }

    send(){
        return new Promise((resolve, reject) => {
            let req = this.request;
            req.onload = () => {
                resolve(req.response);
            }

            req.onerror = function(){
                reject("Error externo");
            }
            req.open('GET', this.url);
            req.send();
        });
    }

}

async function manualToggle(state){
    peticion = new Peticion('manual');

    respuesta = await peticion.send().then((value) => {
        console.log(value);
    }).catch((reason) => {
        console.log(reason);
    });

}

$("#myswitch").click(function(event){
    manualToggle($(event.target).prop("checked"));
});
