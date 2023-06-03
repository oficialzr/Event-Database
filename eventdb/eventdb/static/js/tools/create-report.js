$(function() {


    const type = document.getElementById('type_rep')
    const hiddenBlock = document.getElementById('hidden-block')

    type.addEventListener('change', (e)=>{
        if (e.target.value == 'event') {
            $(hiddenBlock).hide()
        } else {
            $(hiddenBlock).show()
        }
    })


    document.getElementById('form-rep').addEventListener('submit', (e)=>{
        const start = document.getElementById('start-date').value
        const end = document.getElementById('end-date').value
        const sex = document.getElementById('sex_rep').value
        const role = document.getElementById('role_rep').value

        const entity = document.getElementById('entity_rep').value
        const division = document.getElementById('division_rep').value
        const filial = document.getElementById('filial_rep').value

        $.get('../create-report', {'start': start, 'end': end, 'entity': entity, 'division': division, 'filial': filial, 'sex': sex, 'role': role}, function(data){
            if (data['status'] == '500') {
                document.getElementById('form-rep').insertAdjacentHTML('afterend', 
                `<b id="f1" style="color: red; text-align: center; font-size: 18px; position: absolute; bottom: 15px; left: 35%";>Отчет пуст</b>`)
                setTimeout(()=>{
                    document.getElementById('f1').remove()
                }, 2000)
            }
        })

        e.preventDefault()
    })
}());