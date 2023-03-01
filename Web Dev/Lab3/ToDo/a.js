function newElement(){
    var li =  document.createElement("li");
    var inputValue = document.getElementById("inputting").value;
    var text =  document.createTextNode(inputValue);
    li.append(text);

    if (inputValue === '') {
        alert("Бірбәле жаз!");
      } else {
        document.getElementById("tasks").appendChild(li);
      }
    document.getElementById("inputting").value = "";

    var span = document.createElement("span");
    var trash  = document.createTextNode("Delete");
    span.className = "close";
    span.append(trash);
    li.append(span);

    

    for (i = 0; i < close.length; i++) {
        close[i].onclick = function() {
          var div = this.parentElement;
          div.style.display = "none";
        }
      }
  
}




// Delete element of list
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";
  }
}


// Checked mark

var list = document.querySelector('ul');
list.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'LI') {
    ev.target.classList.toggle('checked');
  }
}, false);