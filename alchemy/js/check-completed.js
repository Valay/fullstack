
function onChange(cb){
    //console.log('event', e);
    var newCompleted = cb.checked;
    var todoId = cb.dataset['id'];
    fetch('/todos/completed', {
        method: 'POST',
        body: JSON.stringify({
            'completed': newCompleted,
            'id': todoId
            }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(jsonResponse => {
        console.log('response', jsonResponse);
        var liItem = cb.parentElement;
        if(newCompleted){
            liItem.className = 'complete';
        }else{
            liItem.className = '';
        }
        document.getElementById('error').className = 'hidden';
    })
    .catch(function() {
          document.getElementById('error').className = '';
        })
}