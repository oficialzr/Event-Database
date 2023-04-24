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




const logoLink = document.querySelector('#logoLink')
logoLink.addEventListener('click', goToMainMenu)

function goToMainMenu() {
    window.location.replace('/')
}

const autoCompleteJS = new autoComplete({
    data: {
        src: input => {
            console.log(input);
            const url = `/search/?intruder=${input}`
            return new Promise(resolve => {
                fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    resolve(data.data)
                })
            })
        },
        onSubmit : result => {
            console.log(result);
        }
    },
    resultItem: {
        highlight: true,
        },
    resultList: {
        tabSelect: true,
    }
    })

autoCompleteJS.input.addEventListener("selection", function (event) {
  const feedback = event.detail;
  // Prepare User's Selected Value
  const selection = feedback.selection.value;
  // Render selected choice to selection div
  document.querySelector("#autoComplete").setAttribute('value', selection);
  // Replace Input value with the selected value
  autoCompleteJS.input.value = selection;
  // Console log autoComplete data feedback
  console.log(feedback);
});