window.onload = function() {
	var okButton = document.getElementById("ok");
	okButton.onclick = okayClick;
};
function okayClick() {
	this.innerHTML = "booyah"; 
}
