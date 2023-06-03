$(function() {
    const edit = document.getElementById('is_edit')
    if (edit) {
        sex = $('#sex_from_form #id_sex').get(0).value
        for (option of document.getElementById('sex')) {
            if (option.textContent == sex) {
                option.selected = 'selected'
            }
        }
        
    }
    $('#event').submit(function(e){
        const that = this
        const edit = document.getElementById('is_edit')
        
        if (edit) {

        } else {
            const date = document.getElementById('id_birthday')
            if (new Date(date.value) <= new Date() & new Date(date.value) > new Date('1900-01-01')) {
                $.post('../add-person/', $(this).serialize(), function(data){
                    if (data['message']) {
                        that.insertAdjacentHTML('beforeend', `<p id='bad-add' class='warning-note-person'>${data.message}</p>`)
                        setTimeout(()=>{
                            document.getElementById('bad-add').remove()
                        }, 2000);
                    } else {
                        if (data.redirect) {
                            history.back();
                            return
                        }
                        window.location.replace(`../person/${data['id']}`);
                    }
                });
                e.preventDefault();
            } else {
                date.style.borderColor = 'red'
                date.style.borderStyle = 'solid'
                date.style.borderWidth = '1px'
                that.insertAdjacentHTML('beforeend', `<p id='bad-add' class='warning-note-person'>Неверная дата!</p>`)
                setTimeout(()=>{
                    document.getElementById('bad-add').remove()
                }, 2000);
                e.preventDefault();
            }
        } 
    });
}());