$(function() {

    const form = document.getElementById('edit-form')
    for (line of form.children) {
        if (!(line.id == 'id_description' | line.id == 'accept-edit' | line.name == 'csrfmiddlewaretoken')) {
            line.disabled = true
        }
    }


}());
