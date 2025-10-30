window.onload = function () {

    let selector = document.querySelector("#country");
    selector.addEventListener('change', function () {

        let country_id = selector.value;
        console.log(country_id)
        if (country_id == "no_country") {
            removeChilds(document.getElementById('table'));
        } else {
            ajax_request(country_id);
        }

    });


    function ajax_request(id) {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                console.log(this.responseText);
                res = JSON.parse(this.responseText)
                reservation = res.reservation;
                removeChilds(document.getElementById('table'));
                for (const prop in reservation) {
                    add_option(prop, reservation[prop]);
                }
            }
        };
        xhttp.open("GET", `/ajax_handler/${id}`, true);
        xhttp.send();
    }


    function add_option(val, text) {
        var sel = document.getElementById('table');

// create new option element
        var opt = document.createElement('option');

// create text node to add to option element (opt)
        opt.appendChild(document.createTextNode(text));

// set value property of opt
        opt.value = val;

// add opt to end of select box (sel)
        sel.appendChild(opt);
    }

}

var removeChilds = function (node) {
    var last;
    while (last = node.lastChild) node.removeChild(last);
};