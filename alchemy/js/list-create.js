const nameInput = document.getElementById('name');
      document.getElementById('list-form').onsubmit = function(e) {
        e.preventDefault();
        const name = nameInput.value;
        name.value = '';
        fetch('/lists/create', {
          method: 'POST',
          body: JSON.stringify({
            'name': name,
          }),
          headers: {
            'Content-Type': 'application/json',
          }
        })
        .catch(function() {
          document.getElementById('error-list').className = '';
        })
      }