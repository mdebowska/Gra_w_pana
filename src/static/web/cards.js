function Toggle_card(id) {

    var elem = document.getElementById('card'+id);
    var input_elem = document.getElementById(id);
    var input_elem_last = document.getElementById('last'+id);
    if (elem.classList.contains("checked") == 0) {
        // elem.classList.remove("unchecked")
        elem.classList.add("checked");
        input_elem.checked = true;
        input_elem_last.checked = true;

    } else {
        elem.classList.remove("checked")
        input_elem.checked = false;
    }
}