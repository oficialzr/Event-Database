$(function() {
    const event_id = document.getElementById('event_id').value
    document.getElementById('backBtn').addEventListener('click', ()=>{
        window.location.replace(`../event/${event_id}`);
    })


    new Autocomplete('#autocomplete', {
        search: input =>{
            const url = `/search/?term=${input}`
            return new Promise(resolve => {
                fetch(url)
                .then(response => response.json())
                .then(data => {
                    resolve(data.data.slice(0, 10))
                })
            })
        },
    });

    const confirmButton = document.getElementById('confBtn')


    placeholder_for_data.insertAdjacentHTML('afterend', `<div id="added-data" class="added-data"></div>`)
    place_for_data = document.getElementById('added-data')

    const formChoice = document.getElementById('form-choice')
    const hiddenDesc = document.getElementById('hidden-desc')

    formChoice.addEventListener('change', ()=>{
        if (formChoice.value == '4') {
            hiddenDesc.style.display = 'flex'
        } else {
            hiddenDesc.style.display = 'none'
        }
    })


    confirmButton.addEventListener('click', ()=>{
        const inputDesc = document.getElementById('input-desc')
        const role = document.getElementById('form-choice').value
        const person = document.getElementById('auto-input').value
        let roleDesc = null
        let header = ''
        if (role == '1') {
            header = 'Нарушитель'
        } else if (role == '2') {
            header = 'Свидетель'
        } else if (role == '3') {
            header = 'Потерпевший'
        } else if (role == '4') {
            if (inputDesc.value == '') {
                inputDesc.style.borderColor = 'red'
                inputDesc.style.borderStyle = 'solid'
                return
            } else {
                inputDesc.style.borderColor = 'black'
                inputDesc.style.borderStyle = 'solid'
                inputDesc.style.borderWidth = '1px'
                roleDesc = inputDesc.value
            }
            header = 'Другой фигурант'
        }

        $.post('../../add-person/', {'data': document.getElementById('auto-input').value, 'csrfmiddlewaretoken': $('meta[name="csrf-token"]').attr('content'), 'event_id': event_id, 'role': header, 'role_desc': roleDesc}, function(data){
            if (data.status == '200') {
                
                place_for_data.insertAdjacentHTML('beforeend', `
                <div style='display: flex; flex-direction: column; align-items: center;'>
                    <h2>${header}</h2>
                    <h4 style='padding: 0; margin: 0; margin-bottom: 20px'>${person}</h4>
                </div>
                `)

                document.getElementById('auto-input').value = ''

            } else {
                confirmButton.insertAdjacentHTML('afterend', '<p class="warning-note" id="warning">Такого лица не существует!</p>')
                setTimeout(()=>{
                    document.getElementById('warning').remove()
                }, 1500)
            }
        });
    })

}());