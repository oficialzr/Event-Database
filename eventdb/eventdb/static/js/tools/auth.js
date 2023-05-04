$(function(){
    $(document.getElementById('auth-form')).submit(function(e){
        $.post('../login/', $(this).serialize(), function(data){
            if (data.status == '500') {
                document.getElementById('auth-form').insertAdjacentHTML('beforeend', `<p class="warning-auth">${data.warning}</p>`)
            } else {
                window.location.replace('/')
            }
        });
        e.preventDefault();
    });
}());