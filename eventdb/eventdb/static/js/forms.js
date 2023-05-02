(function () {

const id = makeid(30)

$.ajaxSetup({
    headers: {
        'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
    }
});

// SEARCH FUNCTIONS

if (document.getElementById('search-intruder')) {

    const inputs = document.getElementsByName('search')

    for (const input of inputs) {
        input.addEventListener('input', () => {
            input.nextElementSibling.style.display='block';
            input.nextElementSibling.addEventListener('click', searchExist)
            if (input.value == '') {
                input.nextElementSibling.style.display='none';
            }
        }, false)

        $(function () {
            $(input).autocomplete({
                source: '../search/'
            });
        });
    }

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
                return
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


// FORMS EVENTS


document.getElementById('btn-intruder-first').addEventListener('click', addPersonExist)
document.getElementById('btn-witness-first').addEventListener('click', addPersonExist)
document.getElementById('btn-injured-first').addEventListener('click', addPersonExist)

document.getElementById('btn-intruder').addEventListener('click', addPerson)
document.getElementById('btn-witness').addEventListener('click', addPerson)
document.getElementById('btn-injured').addEventListener('click', addPerson)


// FORMS FUNCTIONS

function addPerson() {
    if (this.nextElementSibling.style.display == 'flex') {
        this.textContent = 'Добавить новое лицо'
        this.nextElementSibling.style.display = 'none'
    } else {
        this.textContent = 'Отменить'
        this.nextElementSibling.style.display = 'flex'
    }
}

function addPersonExist() {
    // document.getElementById('a').next
    if (this.nextElementSibling.style.display == 'flex') {
        this.textContent = 'Добавить существующего'
        this.nextElementSibling.style.display = 'none'
    } else {
        this.nextElementSibling.style.display = 'flex'
        this.textContent = 'Отменить'
    }
}


// INTRUDER

(function () {
    const forms = document.getElementsByName('form')
    for (const form of forms) {
        $(form).submit(function(e){
            $.post(`../add-person-on-event/${id}`, $(this).serialize(), function(data){
                $(form)[0].reset()
                if (data.warning) {
                    form.firstElementChild.lastElementChild.lastElementChild.insertAdjacentHTML('beforebegin', `<p id='warning-${form.id}' class=warning-note>${data.warning}</p>`)
                    return
                }
                const mainDiv = form.firstElementChild
                const new_person = mainDiv.querySelector('div')
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
                
                

                mainDiv.lastElementChild.style.display = 'none'
                mainDiv.querySelector('a[name="addPersonNew"]').textContent = 'Добавить новое лицо'
                try {
                    document.getElementById(`warning-${form.id}`).remove()
                } catch {

                }
            });
            e.preventDefault();
        });
    }
})(); 



// MAIN FORM

$('#event').submit(function(e){
    e.preventDefault();
    $.post('../add-event/', $(this).serialize(), function(data){
        const forms = document.getElementsByName('form');
        list_int = {}
        list_wit = {}
        list_inj = {}
        let counter = 0
        for (line of forms[0].firstElementChild.querySelector('div').children) {
            list_int[counter] = line.id;
            counter += 1;
        }
        counter = 0
        for (line of forms[1].firstElementChild.querySelector('div').children) {
            list_wit[counter] = line.id;
            counter += 1
        }
        counter = 0
        for (line of forms[2].firstElementChild.querySelector('div').children) {
            list_inj[counter] = line.id;
            counter += 1
        }

        intruders = JSON.stringify(list_int)
        witnesses = JSON.stringify(list_wit)
        injureds = JSON.stringify(list_inj)

        $.post({
            url: `../create-relations/${id}`,
            data: {'csrfmiddlewaretoken': $('meta[name="csrf-token"]').attr('content'), 'intruders': intruders, 'witnesses': witnesses, 'injureds': injureds, 'event_id': data}
        });
        window.location.replace("../events/");
    });
});



// GET INFO FROM SECONDARY FORMS

function getPersons() {

}




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
