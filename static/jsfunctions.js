function hello(id) 
{
    window.alert('hello world ' + id);
  }

function getchart(id)
{ 
    const myRequest = new Request('/data/' + id);
    
    fetch(myRequest)
  .then((response) => {
      console.log(response)
});
}