(function() {

    const table = $('#tableMain')
    const tbody = $('#tbodyTable')

    document.getElementById('sortId').addEventListener('change', filterIt)
    function filterIt(value) {
        header = document.getElementsByClassName('header-page')[0].textContent

        const filter = $('#sortId').find('option:selected').attr('name')

        if (filter == 'byNameUp') {
            if (header == 'События') {
                filterByName(true, 1)
            } else {
                filterByName(true)
            }
        } else if (filter == 'byNameDown') {
            if (header == 'События') {
                filterByName(false, 1)
            } else {
                filterByName(false)
            }
        } else if (filter == 'byDateUp') {
            filterByDate(true)
        } else if (filter == 'byDateDown') {
            filterByDate(false)
        } else {
            $(filterById()).appendTo(tbody)
        };  
    }

    function filterByName(asc, role=false) {
        tbody.find('tr').sort(function(a, b) {
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

    function filterByDate(asc) {
        function get_list() {
            return filterById().sort(function(a, b) {
                if (new Date($(a['cells'][0]).text()) < new Date($(b['cells'][0]).text())) {
                    return 1
                } else if (new Date($(a['cells'][0]).text()) > new Date($(b['cells'][0]).text())) {
                    return -1
                }
            })
        }
        if (!asc) {
            $(get_list().get().reverse()).appendTo(tbody)
        } else {
            $(get_list()).appendTo(tbody)
        }
    }

    function filterById() {
        return tbody.find('tr').sort(function(a, b) {
            if (Number($(b['cells'][1]).text()) > Number($(a['cells'][1]).text())) {
                return 1
            } else {
                return -1
            }
        });
    }


}());