function displayoutput(textaftertranslation) {
  document.getElementById("outputarea").style.display = "block"; //now display the output area
  document.getElementById("resetbutton").style.display = "block"; //display the translate another text button also
  document.getElementById("output_text_sentence").value = textaftertranslation;
}
function translatethetext(event) {
  event.preventDefault();
  var req = new XMLHttpRequest();
  var inputtext = document.getElementById("input_text_sentence").value;
  req.open("POST", "/translate", true);
  req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  req.onreadystatechange = function () {
    if (this.status == 200) {
      displayoutput(req.responseText);
    }
  };
  req.send("input_text=" + encodeURIComponent(inputtext));
}

function resetscreen() {
  document.getElementById("inputform").reset(); //reset the whole input form
  document.getElementById("inputarea").style.display = "block"; //display the input area
  document.getElementById("resetbutton").style.display = "none"; //hide the translate another text button
  document.getElementById("outputarea").style.display = "none"; //hide the output area
}
