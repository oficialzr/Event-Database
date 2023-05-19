$(function(){
    $(document.getElementById('auth-form')).submit(function(e){
        $('#loadingauth').show()
        $.post('../login/', $(this).serialize(), function(data){
            $('#loadingauth').hide()
            if (data.status == '500') {
                document.getElementById('auth-form').insertAdjacentHTML('beforeend', `<p class="warning-auth">${data.warning}</p>`)
            } else {
                window.location.replace('/')
            }
        });
        e.preventDefault();
    });
}());