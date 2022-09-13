<?php
	$server = "localhost";
	$sqlUsername = "user";
	$sqlPassword = "password";
	$databaseName = "php";

     	$conn = new mysqli($server, $sqlUsername, $sqlPassword);

  	// check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	}
	echo "Connected successfully";

        $conn->close();
?>
