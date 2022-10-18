// called when page loads; sets up event handlers
function pageLoad() {
	$("ok").onclick = okayClick;
}
function okayClick() {
	alert("booyah");
}
window.onload = pageLoad; // global code					JS
