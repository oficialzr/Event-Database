$(function() {

    // COUNTER

    counter = $('#counter')
    updateCounter()
    
    function updateCounter(count=null) {
        if (count) {
            counter.text(count)
            return
        }
        const currentData = $('tr:visible:not(.header-table)').length
        counter.text(currentData)
    }


    // PAGINATE




    function paginate() {
        let current_page = 1
        const count_data = 30

        
        if (document.getElementById('pages')) {
            document.getElementById('pages').remove()
        }
        
        let placeholder = document.getElementById('previous')
        placeholder.insertAdjacentHTML('afterend', '<div id="pages"></div>')
        placeholder = document.getElementById('pages')
        
        let table_paginate = $('tr:visible:not(.header-table)');
        let main_count = table_paginate.length;
        let main_count_pages = parseInt(main_count / 30) + 1
        
        updateCounter(main_count)
        hide_page(0, main_count, table_paginate)
        show_page(0, count_data, table_paginate)

        for (i=main_count_pages; i!=0; i--) {
            placeholder.insertAdjacentHTML('afterbegin', `<li name='number-page'><a>${i}</a></li>`)
        }

        document.getElementsByName('number-page').forEach(function(elem){
            elem.addEventListener('click', ()=>{go_to_the_page(parseInt(elem.querySelector('a').textContent), table_paginate);})
        });

        const first = document.getElementById('first')
        const previous = document.getElementById('previous')
        const next = document.getElementById('next')
        const last = document.getElementById('last')

        first.addEventListener('click', ()=>go_to_the_page(1, table_paginate))
        previous.addEventListener('click', ()=>go_to_the_page(current_page-1, table_paginate))
        next.addEventListener('click', ()=>go_to_the_page(current_page+1, table_paginate))
        last.addEventListener('click', ()=>go_to_the_page(main_count_pages, table_paginate))

        colorize(1)
        block_buttons(current_page)
    
        function colorize(page) {
            pages = document.getElementsByName('number-page')
            for (i of pages) {
                if (i.textContent == page) {
                    i.style.backgroundColor = 'gainsboro'
                } else {
                    i.style.backgroundColor = 'white'
                }
            }
        }

        function go_to_the_page(page, data) {
            current_from = count_data * (current_page - 1)
            current_to = count_data * current_page
            from = count_data * (page - 1)
            to = count_data * page

            hide_page(current_from, current_to, data)
            show_page(from, to, data)
            colorize(page)
            block_buttons(page)
            
            current_page = page
        }



        function block_buttons(page) {
            if (main_count_pages == 1) {
                next.style.pointerEvents = 'none'
                last.style.pointerEvents = 'none'
                first.style.pointerEvents = 'none'
                previous.style.pointerEvents = 'none'
            } else {
                if (page == main_count_pages) {
                    next.style.pointerEvents = 'none'
                    last.style.pointerEvents = 'none'
                    first.style.pointerEvents = 'auto'
                    previous.style.pointerEvents = 'auto'
                } else if (page == 1) {
                    first.style.pointerEvents = 'none'
                    previous.style.pointerEvents = 'none'
                    next.style.pointerEvents = 'auto'
                    last.style.pointerEvents = 'auto'
                } else {
                    next.style.pointerEvents = 'auto'
                    last.style.pointerEvents = 'auto'
                    first.style.pointerEvents = 'auto'
                    previous.style.pointerEvents = 'auto'
                }
            }
        }

        function hide_page(from, to, data){
            for (i of data.slice(from, to)) {
                $(i).hide()
            };
        };

        function show_page(from, to, data) {
            for (i of data.slice(from, to)) {
                $(i).show()
            };
        };
    }

    paginate()
    

    // SORT

    const tbody = $('#tbodyTable')

    const dataList = tbody.find('tr')

    document.getElementById('sortId').addEventListener('change', sortIt)
    function sortIt() {
        header = document.getElementsByClassName('header-page')[0].textContent

        const sort = $('#sortId').find('option:selected').attr('name')
    
        sortById()

        if (sort == 'byNameUp') {
            if (header == 'События') {
                showAllData()
                sortByName(true, 1)
            } else {
                showAllData()
                sortByName(true)
            }
        } else if (sort == 'byNameDown') {
            if (header == 'События') {
                showAllData()
                sortByName(false, 1)
            } else {
                showAllData()
                sortByName(false)
            }
        } else if (sort == 'byDateUp') {
            if (header == 'События') {
                showAllData()
                sortByDate(true, 1)
            } else {
                showAllData()
                sortByDate(true)
            }
        } else if (sort == 'byDateDown') {
            if (header == 'События') {
                showAllData()
                sortByDate(false, 1)
            } else {
                showAllData()
                sortByDate(false)
            }
        } else {
            showAllData()
            $(sortById()).appendTo(tbody)
        };
        paginate()
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
    document.getElementById('filter-delete').addEventListener('click', (event)=>{
        for (i of document.getElementsByClassName('filter-content')[0].querySelectorAll('select')) {
            i.selectedIndex = 0
        };
        document.getElementById('id_search_input').value = ''
    })


    const data_all = $('tr:not(.header-table)');
    const inputSearch = document.getElementById('id_search_input')
    const delSpan = document.getElementById('delete-search');

    if (inputSearch.value != '') {
        delSpan.style.display = 'block'
    }

    document.getElementById('filter-button').addEventListener('click', ()=>{
        const filterContent = document.getElementById('filter')
        $(filterContent).toggle()
    });


    
    delSpan.addEventListener('click', ()=>{
        inputSearch.value = ''
    });

    inputSearch.addEventListener('input', (value)=>{
        if (value.target.value != '') {
            delSpan.style.display = 'block'
        } else {
            delSpan.style.display = 'none'
        }
    })


    function showAllData() {
        for (line of data_all) {
            $(line).show()
        }
    }

}());