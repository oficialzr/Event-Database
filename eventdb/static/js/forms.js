(function () {

$.ajaxSetup({
    headers: {
        'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
    }
});

// MAIN FORM

$('#event').submit(function(e){
    const date = document.getElementById('id_date_incedent')
    if (new Date(date.value) <= new Date() & new Date(date.value) > new Date('1900-01-01')){

    } else {
        e.preventDefault()
        const place = document.getElementById('main-form-submit')

        date.style.borderColor = 'red'
        date.style.borderStyle = 'solid'
        date.style.borderWidth = '1px'

        place.insertAdjacentHTML('beforebegin', `<p id='bad-add' class='warning-note-person'>Неверная дата!</p>`)
        setTimeout(()=>{
            document.getElementById('bad-add').remove()
        }, 2000);
    }
});

}());
