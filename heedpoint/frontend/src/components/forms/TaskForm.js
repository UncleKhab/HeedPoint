import React from 'react'

function TaskForm() {

    function getCookie(name) {
        if (!document.cookie) {
          return null;
        }
      
        const xsrfCookies = document.cookie.split(';')
          .map(c => c.trim())
          .filter(c => c.startsWith(name + '='));
      
        if (xsrfCookies.length === 0) {
          return null;
        }
        return decodeURIComponent(xsrfCookies[0].split('=')[1]);
    }
    

    const handleSubmit = (e) => {
        e.preventDefault()
        console.log(e.target)
        const myForm = e.target
        const csrfToken = getCookie('csrftoken');
        const headers = new Headers({
            'X-CSRFToken': csrfToken
        });
        const myFormSend = new FormData(myForm)
        fetch('api/tasks/', {
            method: 'POST',
            credentials: "same-origin",
            headers,
            body: myFormSend
        })
        .then(response => response.json())
        .then(result => {
            myForm.reset()
            console.log(result)
        }) 
    }

    

    return (
        <div>
            <form onSubmit={handleSubmit}>
                
                <input type="text" name="title"/>
                <input type="text" name="description"/>
                <select name="status" id="status">
                    <option value="h">Holding</option>
                    <option value="p">Prioritized</option>
                    <option value="s">Started</option>
                    <option value="f">Finished</option>
                </select>
                <select name="priority" id="priority">
                    <option value="f">Important and Urgent</option>
                    <option value="l">Important not Urgent</option>
                    <option value="d">Delegate</option>
                    <option value="e">Eliminate</option>
                    <option value="n">Not Set</option>
                </select>
                <select name="project">
                    <option value="1">1</option>
                </select>
                <select name="user">
                    <option value="1">1</option>
                </select>
                <button>submit</button>
            </form>
        </div>
    )
}

export default TaskForm
