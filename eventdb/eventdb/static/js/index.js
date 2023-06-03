(function () {

const listView = document.getElementById('view')
listView.addEventListener('click', openViewList)

function openViewList() {
    const list = document.getElementById('list-values')
    $(list).toggle()
}

const listViewEdit = document.getElementById('view-edit')
listViewEdit.addEventListener('click', openViewListEdit)

function openViewListEdit() {
    const list = document.getElementById('list-values-edit')
    $(list).toggle()
}




const logoLink = document.querySelector('#logoLink')
logoLink.addEventListener('click', goToMainMenu)

function goToMainMenu() {
    window.location.replace('/')
}

}());