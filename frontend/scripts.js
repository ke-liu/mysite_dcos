var root = document.getElementById('root');
root.innerHTML = '';
root.innerHTML += '<ul>'

var request = new XMLHttpRequest()
request.open('GET', '/mymovies/', true)

request.onload = function() {
  // Begin accessing JSON data here
  var data = JSON.parse(this.response)

  if (request.status >= 200 && request.status < 400) {
    data.forEach(movie => {
      console.log(movie.title);
      root.innerHTML += '<li>' + movie.title + '</li>';
      root.innerHTML +=  `Description: ${movie.description}  `; 
    })
  } else {
    console.log('error')
  }
}
root.innerHTML += '</ul>'
request.send()