
function onDelete(button){
    //console.log('event', e);
    var todoId = button.dataset['id'];
    fetch('/todos/deleted', {
        method: 'DELETE',
        body: JSON.stringify({
            'id': todoId
            }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(jsonResponse => {
        // TODO delete li item
        console.log('response', jsonResponse);
        if(jsonResponse['success']){
            var liItem = button.parentElement;
            liItem.remove();
            document.getElementById('error').className = 'hidden';
        }else{
            document.getElementById('error').className = '';
        }
    })
    .catch(function() {
          document.getElementById('error').className = '';
        })
}

function onDeleteList(button){
    //console.log('event', e);
    var listId = button.dataset['id'];
    fetch('/list/deleted', {
        method: 'DELETE',
        body: JSON.stringify({
            'id': listId
            }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(jsonResponse => {
        // TODO delete li item
        console.log('response', jsonResponse);
        if(jsonResponse['success']){
            var liItem = button.parentElement;
            liItem.remove();
            document.getElementById('error-list').className = 'hidden';
        }else{
            document.getElementById('error-list').className = '';
        }
    })
    .catch(function() {
          document.getElementById('error-list').className = '';
        })
}