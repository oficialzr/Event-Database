$(function(){
    
    change_from = document.getElementById('from')
    change_to = document.getElementById('to')

    for (line=4; line<change_from.children.length; line++) {
        if (change_from.children[line].textContent != change_to.children[line].textContent) {
            change_to.children[line].style.color = 'red'
            change_to.children[line].style.fontWeight = '600'
        }
    }

}());