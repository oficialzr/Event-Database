(function() {

    $('#event').submit(function(e){
        const that = this
        $.post('../add-person/', $(this).serialize(), function(data){
            if (data['message']) {
                that.insertAdjacentHTML('beforeend', `<p id='bad-add' class=warning-note>${data.message}</p>`)
                setTimeout(()=>{
                    document.getElementById('bad-add').remove()
                }, 2000);
            } else {
                window.location.replace("../persons/");
            }
        });
        e.preventDefault();
    });

}());