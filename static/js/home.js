let dropArea = document.getElementById('drop-area');
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false)
})

function preventDefaults(e) {
    e.preventDefault()
    e.stopPropagation()
}

['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false)
})

    ;['dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, unhighlight, false)
    })

function highlight(e) {
    dropArea.classList.add('highlight')
}

function unhighlight(e) {
    dropArea.classList.remove('highlight')
}

dropArea.addEventListener('drop', handleDrop, false)

function handleDrop(e) {
    let dt = e.dataTransfer
    let files = dt.files

    uploadFile(files[0])
}


function uploadFile(file) {
    let url = '/upload/'
    let formData = new FormData()

    formData.append('file', file);
    let csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    formData.append('csrfmiddlewaretoken', csrf);
    fetch(url, {
        method: 'POST',
        body: formData
    }).then((res) => res.json()).then(data => {
        window.location.href = '/proceed/' + data.id;
    })
}
