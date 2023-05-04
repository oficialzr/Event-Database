$(function() {

    const table = $('#tableMain')
    const tbody = $('#tbodyTable')

    const dataList = tbody.find('tr')

    document.getElementById('sortId').addEventListener('change', sortIt)
    function sortIt(value) {
        header = document.getElementsByClassName('header-page')[0].textContent

        const sort = $('#sortId').find('option:selected').attr('name')
    
        sortById()

        if (sort == 'byNameUp') {
            if (header == 'События') {
                sortByName(true, 1)
            } else {
                sortByName(true)
            }
        } else if (sort == 'byNameDown') {
            if (header == 'События') {
                sortByName(false, 1)
            } else {
                sortByName(false)
            }
        } else if (sort == 'byDateUp') {
            if (header == 'События') {
                sortByDate(true, 1)
            } else {
                sortByDate(true)
            }
        } else if (sort == 'byDateDown') {
            if (header == 'События') {
                sortByDate(false, 1)
            } else {
                sortByDate(false)
            }
        } else {
            $(sortById()).appendTo(tbody)
        };  
    }

    function sortByName(asc, role=false) {
        dataList.sort(function(a, b) {
            if (!asc) {
                let x = a
                a = b
                b = x
            }
            if (role) {
                return $(a['cells'][5]).text().localeCompare($(b['cells'][5]).text())
            }else{
                return $(a['cells'][2]).text().localeCompare($(b['cells'][2]).text())
            }
        }).appendTo(tbody);
    }

    function sortByDate(asc, role=false) {
        function get_list() {
            return dataList.sort(function(a, b) {
                if (role) {
                    if (new Date($(a['cells'][2]).text()) < new Date($(b['cells'][2]).text())) {
                        return 1
                    } else if (new Date($(a['cells'][2]).text()) > new Date($(b['cells'][2]).text())) {
                        return -1
                    }
                } else {
                    if (new Date($(a['cells'][0]).text()) < new Date($(b['cells'][0]).text())) {
                        return 1
                    } else if (new Date($(a['cells'][0]).text()) > new Date($(b['cells'][0]).text())) {
                        return -1
                    }
                }
            })
        }
        if (!asc) {
            $(get_list().get().reverse()).appendTo(tbody)
        } else {
            $(get_list()).appendTo(tbody)
        }
    }

    function sortById() {
        return dataList.sort(function(a, b) {
            if (Number($(b['cells'][1]).text()) > Number($(a['cells'][1]).text())) {
                return 1
            } else {
                return -1
            }
        });
    }



    // FILTER


    const data = $('tr:not(.header-table)');
    const filters = document.getElementsByName('filterOption')

    function showAllData() {
        for (line of data) {
            $(line).show()
        }
        updateCounter()
    }

    function getFiltred(tag, text, data) {
        for (line of data) {
            if ($(line).find(`#${tag}`).text() == text) {

            } else {
                $(line).hide()
            }
        }
    }

    document.getElementById('filter-delete').addEventListener('click', ()=> {
        showAllData()
        for (filter of filters) {
            $(filter).val('')
        }
        updateCounter()
    });

    document.getElementById('filter-button').addEventListener('click', ()=>{
        const filterContent = document.getElementById('filter')
        $(filterContent).toggle('slide', {'direction': 'up'}, 1000)
    })


    // FILTER EVENTS
    if ($('#head').text() == 'События') {
    
        document.getElementById('filter-accept').addEventListener('click', ()=> {
            showAllData()
    
            const typeText = $('#typeFilter').find('option:selected').text();
            if (typeText != 'Нет') {
                getFiltred('type', typeText, data)
            }
    
            const divisText = $('#divisionFilter').find('option:selected').text();
            if (divisText != 'Нет') {
                getFiltred('division', divisText, data)
            }
    
            const filialText = $('#filialFilter').find('option:selected').text();
            if (filialText != 'Нет') {
                getFiltred('filial', filialText, data)
            }
            updateCounter()
        });
    } else {
        document.getElementById('filter-accept').addEventListener('click', ()=> {
            showAllData()
    
            const sexText = $('#sexFilter').find('option:selected').text();
            if (sexText != 'Нет') {
                getFiltred('sex', sexText, data)
            }

            const countryText = $('#countryFilter').find('option:selected').text();
            if (countryText != 'Нет') {
                getFiltred('country', countryText, data)
            }
    
            const regionText = $('#regionFilter').find('option:selected').text();
            if (regionText != 'Нет') {
                getFiltred('region', regionText, data)
            }

            updateCounter()
        });
    }


    // COUNTER

    counter = $('#counter')
    updateCounter()
    
    function updateCounter() {
        const currentData = $('tr:visible:not(.header-table)').length
        counter.text(currentData)
    }


    // SEARCH
    
    const searchInput = document.getElementById('search-input')
    document.getElementById('search-button').addEventListener('click', ()=>{
        showAllData()
        searchBy(searchInput.value, data)
    })

    function searchBy(text, data) {
        if (text == '') {
            showAllData()
            return 
        }
        for (line of data) {
            if ($(line).find(`#fio`).text().search(text) >= 0) {
                
            } else {
                $(line).hide()
            }
        }
        updateCounter()
    }
    

}());