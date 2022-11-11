function fn_createGuid()
{
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random()*16|0, v = c === 'x' ? r : (r&0x3|0x8);
        return v.toString(16);
    });
}

fn_populate = (container_id, list) => {

    const app = document.getElementById(container_id)

    // Create markup
    app.innerHTML = '<ul>' + list.map(function (element) {
        return '<li>' + element.id + '</li>';
    }).join('') + '</ul>';
}

async function getCars(){
    fetch("http://localhost:3005/cars", {

        // Adding method type
        method: "GET",

        // Adding headers to the request
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })

    // Converting to JSON
    .then(response => response.json())

    // Displaying results to console
    .then(json => {
        console.log(json);
        fn_populate('id_cars', json )

    })
    .catch(
        err => console.log(err)
    )

}

async function postCar(){
    // d = new Date().getTime();
    id = fn_createGuid()
    fetch("http://localhost:3005/cars", {

        // Adding method type
        method: "POST",

        // Adding body or contents to send
        body: JSON.stringify({
            "id": id,
            "year": 1979,
            "make": "cheyy",
            "model": "pinto",
            "owner_id": 1
        }),

        // Adding headers to the request
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
        .then(response => response.json())
        .then(
            json => {
                console.log(json);
                changeStatus('added new car !!!');
            })
        .catch(
            err => console.log(err)
        )
}

const changeStatus = (msg) => {
  document.getElementById("status").innerHTML = msg;
}


// postCar();
