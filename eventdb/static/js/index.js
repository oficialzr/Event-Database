(function () {

const listView = document.getElementById('view')
listView.addEventListener('click', openViewList)

function openViewList() {
    const list = document.getElementById('list-values')
    if (list.style.display === 'block') {
        list.style.display = 'none'
    } else {
        list.style.display = 'block'
    }
}

const listViewEdit = document.getElementById('view-edit')
listViewEdit.addEventListener('click', openViewListEdit)

function openViewListEdit() {
    const list = document.getElementById('list-values-edit')
    if (list.style.display === 'block') {
        list.style.display = 'none'
    } else {
        list.style.display = 'block'
    }
}

const id = makeid(30)




const logoLink = document.querySelector('#logoLink')
logoLink.addEventListener('click', goToMainMenu)

function goToMainMenu() {
    window.location.replace('/')
}

});