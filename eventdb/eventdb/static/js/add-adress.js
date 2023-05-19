$(function() {

    const button = document.getElementById('form-choice')

    const birthForm = document.getElementById('birthForm')
    const otherForm = document.getElementById('defaultForm')

    place = $('#place')
    entity = $('#entity')
    role = document.getElementById('role')

    button.addEventListener('change', ()=>{
        birthForm.reset()
        otherForm.reset()
        place.hide()
        entity.hide()
        const selected = button.options[button.selectedIndex].value

        if (selected == '1') {
            otherForm.style.display = 'none'
            birthForm.style.display = 'flex'
        } else if (selected == '4') {
            place.show()
            role.value = '4'
            birthForm.style.display = 'none'
            otherForm.style.display = 'flex'
        } else if (selected == '2') {
            entity.show()
            role.value = '2'
            birthForm.style.display = 'none'
            otherForm.style.display = 'flex'
        } else if (selected == '3') {
            role.value = '3'
            birthForm.style.display = 'none'
            otherForm.style.display = 'flex'
        }

    })



    $('#birthForm').submit(function(e){
        const id = document.getElementById('id').textContent
        $.post(`/add-adress/${id}`, $(this).serialize(), function(data){
            addOnPageBirth(JSON.parse(data.data)[0].fields)
            birthForm.reset()
        })
        e.preventDefault();
    });

    $('#defaultForm').submit(function(e){
        const id = document.getElementById('id').textContent
        $.post(`/add-adress/${id}`, $(this).serialize(), function(data){
            const role = JSON.parse(data.data)[0].model
            addOnPageOther(JSON.parse(data.data)[0].fields, role)
            otherForm.reset()
        })
        e.preventDefault();
    });
    
    const placeholder_for_data = document.getElementById('placeholder_for_data')
    placeholder_for_data.insertAdjacentHTML('afterend', `<div id="added-data" class="added-data"></div>`)
    place_for_data = document.getElementById('added-data')

    function addOnPageBirth(data) {
        place_for_data.insertAdjacentHTML('beforeend', `<table class="collapse-border" style="width: 50%">
            <th colspan=2><h2>Место рождения</h2></th>
            <tr><td class="td-border">Страна</td><td class="td-border">${data['country']}</td></tr>
            <tr><td class="td-border">Область</td><td class="td-border">${data['region']}</td></tr>
            <tr><td class="td-border">Адрес</td><td class="td-border">${data['adress']}</td></tr>
        </table><br>`);
    }

    function addOnPageOther(data, role) {
        let desc = ''
        let header = ''
        if (role == 'main.adressesplacesofwork') {
            header = 'Место работы'
            desc = `<tr><td class="td-border">Юридическое лицо</td><td class="td-border">${data['entity']}</td></tr>`
        } else if (role == 'main.adressesplacesoflive') {
            header = 'Адрес регистрации'
        } else {
            header = 'Другой адрес'
            desc = `<tr><td class="td-border">Описание адреса</td><td class="td-border">${data['description']}</td></tr>`
        }
        place_for_data.insertAdjacentHTML('beforeend', `<table class="collapse-border" style="width: 50%">
            <th colspan=2><h2>${header}</h2></th>
            ${desc}
            <tr><td class="td-border">Страна</td><td class="td-border">${data['country']}</td></tr>
            <tr><td class="td-border">Область</td><td class="td-border">${data['region']}</td></tr>
            <tr><td class="td-border">Район</td><td class="td-border">${data['area']}</td></tr>
            <tr><td class="td-border">Населенный пункт</td><td class="td-border">${data['locality']}</td></tr>
            <tr><td class="td-border">Улица</td><td class="td-border">${data['street']}</td></tr>
            <tr><td class="td-border">Дом</td><td class="td-border">${data['house']}</td></tr>
            <tr><td class="td-border">Корпус</td><td class="td-border">${data['frame']}</td></tr>
            <tr><td class="td-border">Квартира</td><td class="td-border">${data['apartment']}</td></tr>

        </table><br>`);
    }
    

}());