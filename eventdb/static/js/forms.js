(function () {

$.ajaxSetup({
    headers: {
        'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
    }
});

// SEARCH FUNCTIONS

if (document.getElementById('search-intruder')) {
    let input = document.getElementById('search-intruder')
    input.addEventListener('input', () => {
        document.getElementById('add-btn-int').style.display='block';
        document.getElementById('add-btn-int').addEventListener('click', searchExist)
        if (document.getElementById('search-intruder').value == '') {
            document.getElementById('add-btn-int').style.display='none';
        }
    }, false)

    $(function () {
        $('#search-intruder').autocomplete({
            source: '../search/'
        });
    });

    let input_witness = document.getElementById('search-witness')
    input_witness.addEventListener('input', () => {
        document.getElementById('add-btn-wit').style.display='block';
        document.getElementById('add-btn-wit').addEventListener('click', searchExist)
        if (document.getElementById('search-witness').value == '') {
            document.getElementById('add-btn-wit').style.display='none';
        }
    }, false)

    $(function () {
        $('#search-witness').autocomplete({
            source: '../search/'
        });
    });

    let input_injured = document.getElementById('search-injured')
    document.getElementById('add-btn-inj').addEventListener('click', searchExist)
    input_injured.addEventListener('input', () => {
        document.getElementById('add-btn-inj').style.display='block';
        if (document.getElementById('search-injured').value == '') {
            document.getElementById('add-btn-inj').style.display='none';
        }
    }, false)

    $(function () {
        $('#search-injured').autocomplete({
            source: '../search/'
        });
    });
}


// SEARCH BUTTONS EVENTS IN FORM

function searchExist() {
    value = this.previousElementSibling.value;
    input = this.previousElementSibling
    const that = this
    $.post({
        url: `../check-person/${id}`,
        data: {'csrfmiddlewaretoken': $('meta[name="csrf-token"]').attr('content'), 'person': value},
        success: function(data) {
            if (data.warning) {
                that.parentElement.append(document.createElement('a'))
                that.parentElement.lastChild.insertAdjacentHTML('afterbegin' , `<p class=warning-note>${data.warning}</p>`)
                setTimeout(() => {
                    that.parentElement.lastChild.remove()
                }, 2000)
            }
            input.value = ''
            that.style.display = 'none'
            that.parentNode.style.display = 'none'
            that.parentNode.previousElementSibling.textContent = 'Добавить существующего'
            const new_person = that.parentNode.parentNode.querySelector('.list-persons-form');
            new_person.append(document.createElement('div'));

            const blockWithContent = new_person.lastChild;
            blockWithContent.id = value;
            blockWithContent.append(document.createElement('a'));
            blockWithContent.append(document.createElement('span'));

            const textBlock = blockWithContent.firstChild;
            const button = blockWithContent.lastChild;

            textBlock.insertAdjacentText('afterbegin', value);
            button.insertAdjacentHTML('afterbegin', '&times;')
            button.classList.add('close-button')

            button.addEventListener('click', ()=>{
                blockWithContent.remove()
            })
        }
    })

}



// FORMS 


// FORM INTRUDER

document.getElementById('btn-intruder').addEventListener('click', () => {
    if (document.getElementById('intruder').style.display == 'flex') {
        document.getElementById('btn-intruder').textContent = 'Добавить новое лицо'
        document.getElementById('intruder').style.display = 'none'
    } else {
        document.getElementById('btn-intruder').textContent = 'Отменить'
        document.getElementById('intruder').style.display = 'flex'
    }
})
document.getElementById('btn-intruder-first').addEventListener('click', () => {
    if (document.getElementById('intruder-first').style.display == 'flex') {
        document.getElementById('btn-intruder-first').textContent = 'Добавить существующего'
        document.getElementById('intruder-first').style.display = 'none'
    } else {
        document.getElementById('intruder-first').style.display = 'flex'
        document.getElementById('btn-intruder-first').textContent = 'Отменить'
    }
})

$('#intruder-form').submit(function(e){
    $.post(`../add-person-on-event/${id}`, $(this).serialize(), function(data){
        $('#intruder-form')[0].reset()
        if (data.warning) {
            document.getElementById('submit-intruder').insertAdjacentHTML('beforebegin', `<p id='warning-intruder' class=warning-note>${data.warning}</p>`)
            return
        }

        const new_person = document.getElementById('intruder-list')
        new_person.append(document.createElement('div'))

        const blockWithContent = new_person.lastChild
        blockWithContent.id = data.message
        blockWithContent.append(document.createElement('a'))
        blockWithContent.append(document.createElement('span'))

        const textBlock = blockWithContent.firstChild
        const button = blockWithContent.lastChild

        textBlock.insertAdjacentText('afterbegin', data.message)

        button.insertAdjacentHTML('afterbegin', '&times;')
        button.classList.add('close-button')
        button.addEventListener('click', () => {
            $.post({
                url: `../delete-person/${id}`,
                data: {'csrfmiddlewaretoken': $('meta[name="csrf-token"]').attr('content'), 'person': data.message}
            })
            button.parentElement.remove()
        })

        document.getElementById('intruder').style.display = 'none'
        document.getElementById('btn-intruder').textContent = 'Добавить новое лицо'
        document.getElementById('warning-intruder').remove()
    });
    e.preventDefault();
});

// FORM WITNESS

document.getElementById('btn-witness').addEventListener('click', () => {
    if (document.getElementById('witness').style.display == 'flex') {
        document.getElementById('btn-witness').textContent = 'Добавить новое лицо'
        document.getElementById('witness').style.display = 'none'
    } else {
        document.getElementById('btn-witness').textContent = 'Отменить'
        document.getElementById('witness').style.display = 'flex'
    }
})
document.getElementById('btn-witness-first').addEventListener('click', () => {
    if (document.getElementById('witness-first').style.display == 'flex') {
        document.getElementById('btn-witness-first').textContent = 'Добавить существующего'
        document.getElementById('witness-first').style.display = 'none'
    } else {
        document.getElementById('witness-first').style.display = 'flex'
        document.getElementById('btn-witness-first').textContent = 'Отменить'
    }
})


$('#witness-form').submit(function(e){
    $.post(`../add-person-on-event/${id}`, $(this).serialize(), function(data){
        $('#witness-form')[0].reset()
        if (data.warning) {
            document.getElementById('submit-witness').insertAdjacentHTML('beforebegin', `<p id='warning-witness' class=warning-note>${data.warning}</p>`)
            return
        }
        const new_person = document.getElementById('witness-list')
        new_person.append(document.createElement('div'))

        const blockWithContent = new_person.lastChild
        blockWithContent.id = data.message
        blockWithContent.append(document.createElement('a'))
        blockWithContent.append(document.createElement('span'))

        const textBlock = blockWithContent.firstChild
        const button = blockWithContent.lastChild

        textBlock.insertAdjacentText('afterbegin', data.message)

        button.insertAdjacentHTML('afterbegin', '&times;')
        button.classList.add('close-button')
        button.addEventListener('click', () => {
            $.post({
                url: `../delete-person/${id}`,
                data: {'csrfmiddlewaretoken': $('meta[name="csrf-token"]').attr('content'), 'person': data.message}
            })
            button.parentElement.remove()
        })

        document.getElementById('witness').style.display = 'none'
        document.getElementById('btn-witness').textContent = 'Добавить новое лицо'
        document.getElementById('warning-witness').remove()
    });
    e.preventDefault();
});


// FORM INJURED

document.getElementById('btn-injured').addEventListener('click', () => {
    if (document.getElementById('injured').style.display == 'flex') {
        document.getElementById('btn-injured').textContent = 'Добавить новое лицо'
        document.getElementById('injured').style.display = 'none'
    } else {
        document.getElementById('btn-injured').textContent = 'Отменить'
        document.getElementById('injured').style.display = 'flex'
    }
})
document.getElementById('btn-injured-first').addEventListener('click', () => {
    if (document.getElementById('injured-first').style.display == 'flex') {
        document.getElementById('btn-injured-first').textContent = 'Добавить существующего'
        document.getElementById('injured-first').style.display = 'none'
    } else {
        document.getElementById('injured-first').style.display = 'flex'
        document.getElementById('btn-injured-first').textContent = 'Отменить'
    }
})


$('#injured-form').submit(function(e){
    $.post(`../add-person-on-event/${id}`, $(this).serialize(), function(data){
        $('#injured-form')[0].reset()
        if (data.warning) {
            document.getElementById('submit-injured').insertAdjacentHTML('beforebegin', `<p id='warning-injured' class=warning-note>${data.warning}</p>`)
            return
        }
        const new_person = document.getElementById('injured-list')
        new_person.append(document.createElement('div'))

        const blockWithContent = new_person.lastChild
        blockWithContent.id = data.message
        blockWithContent.append(document.createElement('a'))
        blockWithContent.append(document.createElement('span'))

        const textBlock = blockWithContent.firstChild
        const button = blockWithContent.lastChild

        textBlock.insertAdjacentText('afterbegin', data.message)

        button.insertAdjacentHTML('afterbegin', '&times;')
        button.classList.add('close-button')
        button.addEventListener('click', () => {
            $.post({
                url: `../delete-person/${id}`,
                data: {'csrfmiddlewaretoken': $('meta[name="csrf-token"]').attr('content'), 'person': data.message}
            })
            button.parentElement.remove()
        })

        document.getElementById('injured').style.display = 'none'
        document.getElementById('btn-injured').textContent = 'Добавить новое лицо'
        document.getElementById('warning-injured').remove()
    });
    e.preventDefault();
});

function makeid(length) {
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const charactersLength = characters.length;
    let counter = 0;
    while (counter < length) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
      counter += 1;
    }
    return result;
}








}());



