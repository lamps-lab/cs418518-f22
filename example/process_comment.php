<?php 
	$userName=$_POST["username"];
	$like=$_POST["like"];
	$comment=$_POST["comment"];
	$rating=$_POST["rating"];
	echo "Hello <b>$userName</b>!<br>";
	if($like == "TRUE") {
		echo "I am happy that you <strong>like</strong> this page :) <br/>";
	} else {
		echo "I am sorry that you <strong>do not like</strong> this page :( <br/>";
	}
	echo "Thanks for your comment <strong>[$comment]</strong> <br/>";
	echo "You rate my page as Rating <strong>$rating</strong>!";
?>

