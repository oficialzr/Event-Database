$(function(){
    let role = ''
    if (document.getElementById('workForm')) {
        role = 'workForm'
    } else {
        role = 'event'
    }

    const selections = Array.from(document.getElementById(role).querySelectorAll('select'))

    document.getElementById(role)
    .querySelectorAll('select')
    .forEach((value)=>{
        if (value.name != 'entity') {
            value.disabled = true
        }
        value.addEventListener('change', (e)=>{
            const name = e.target.name
            const value = e.target.value

            let key = e.target
            for (i of selections.slice(selections.indexOf(key))) {
                key.nextElementSibling.disabled = true
                key.nextElementSibling.value = ''
                key = i
            }

            $.get('../set-adaptive', {'name': name, 'value': value}, function(data){
                if (data['data'] == '500') {
                    e.target.nextElementSibling.disabled = true
                } else {
                    e.target.nextElementSibling.disabled = false
                }
                try {
                    key = e.target.nextElementSibling;
                    for (i of Array.from(key.children).slice(1)) {
                        if (data['data'].includes(i.value)) {
                            $(i).show()
                        } else {
                            $(i).hide()
                        }
                    }
                } catch (error) {
                    
                }
            })
        })
    })
}());