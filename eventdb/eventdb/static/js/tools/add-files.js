$(function(){
    if (document.getElementById('id_image')) {
        document.getElementById('id_image').addEventListener('change', (e)=>{
            $(e.target.parentElement).submit();
        })
    }

    document.getElementById('id_file').addEventListener('change', (e)=>{
        $(e.target.parentElement).submit();
    })
}());