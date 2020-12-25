const descInput = document.getElementById('description');
      document.getElementById('form').onsubmit = function(e) {
        e.preventDefault();
        const desc = descInput.value;
        const listId = document.getElementById('form').dataset['id'];
        descInput.value = '';
        fetch('/todos/create', {
          method: 'POST',
          body: JSON.stringify({
            'description': desc,
            'list-id' : listId
          }),
          headers: {
            'Content-Type': 'application/json',
          }
        })
        .then(response => response.json())
        .then(jsonResponse => {
          console.log('response', jsonResponse);
          id = jsonResponse['id'];
          li = document.createElement('li');
          checkbox = document.createElement('input');
          checkbox.setAttribute('type','checkbox');
          checkbox.setAttribute('class','check-completed');
          checkbox.setAttribute('data-id',id);
          checkbox.setAttribute('onclick','onChange(this)');
          li.appendChild(checkbox);
          li.appendChild(document.createTextNode(desc));
          button = document.createElement('button');
          button.setAttribute('class','delete');
          button.setAttribute('data-id',id);
          button.setAttribute('onclick','onDelete(this)');
          button.innerHTML = '&cross;';
          li.appendChild(button);
          document.getElementById('todos').appendChild(li);
          document.getElementById('error').className = 'hidden';
        })
        .catch(function() {
          document.getElementById('error').className = '';
        })
      }