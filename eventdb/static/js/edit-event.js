$(function() {

    const form = document.getElementById('edit-form')
    const lines = ['description', 'submit', 'csrfmiddlewaretoken', 'way', 'instrument', 'relation', 'object', 'place']
    for (let line of form.children) {
        if (!lines.includes(line.name)) {
            line.disabled = true
        }
    }


}());
