let comment_form = document.getElementById("comment_form")
comment_form.addEventListener('submit',
    function (e) {
        e.preventDefault()
        let comment_form_data = new FormData(this)
        fetch('/comment', {
            method: "POST",
            body: comment_form_data
        }).then(response => {
            if (response.ok) {
                let comments_set = document.getElementById("comments_set")
                let new_comment = document.createElement("div")
                let textarea = document.getElementById("commentText")
                let username = document.getElementById("username").value
                let text = textarea.value
                new_comment.innerHTML =
                    `<h5 class="mt-0">${username}</h5>
                        ${text}
                    <hr>`
                comments_set.append(new_comment)
                textarea.value = ""
                textarea.disabled = "disabled"
                textarea.placeholder = "Подождите. В целях безопасности частота отправки комментариев ограничена."
                setTimeout(function () {
                    textarea = document.getElementById("commentText")
                    textarea.disabled = ""
                    textarea.placeholder = ""
                }, 5000)
            } else {
                alert("Не удалось оставить комментарий. Попробуйте позже или свяжитесь с системным администратором.")
            }
        })
    }
)

let drop_video_form = document.querySelector('form[id=drop-video-form]')
drop_video_form.addEventListener("submit", function (e) {
    e.preventDefault()
    let form_data = new FormData(this)
    fetch('/drop-video', {
        method: 'POST',
        body: form_data
    }).then(response => {
        if (response.ok) {
            alert("Видео успешно удалёно.")
            document.location.replace('/')
        } else {
            alert("Ошибка при удалении видео. Повторите попытку позже.")
        }
    })
})

function like(type_of_operation) {
    let form_data = new FormData()
    form_data.append('name', document.getElementById('hidden-name').value)
    form_data.append('type', type_of_operation)
    form_data.append('csrfmiddlewaretoken', document.querySelector('input[name=csrfmiddlewaretoken]').value)
    fetch('/like', {
        method: 'POST',
        body: form_data
    }).then(response => {
        if (response.ok) {
            if (response.status === 200) {
                let counter = document.getElementById(`${type_of_operation}-counter`)
                let num = Number(counter.innerHTML)
                num += 1
                counter.innerHTML = String(num)
            } else if (response.status === 201) {
                alert("Вы уже поставили оценку этому видео. Вы не можете поставить ещё одну.")
            } else {
                alert("error")
            }
        } else {
            alert("Ошибка")
        }
    })
}