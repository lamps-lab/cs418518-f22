<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html>
	<head>
		<title>A Simple Website</title>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-15" />
		<link rel="stylesheet" href="styles.css" />
	</head>
	<body>
	<div id="conteneur">
	<div id="header">A Simple Website</div>
        <?php include 'navbar.php'; ?>
	<div id="centre">
	<?php
		require 'authentication.php';
		
		// connect to the server
		$conn = new mysqli($server, $sqlUsername, $sqlPassword, $databaseName);
		
		// prepare SQL query
		$query="SELECT * FROM PROJECT";
		
		// Execute SQL query
		$query_result = $conn->query($query);
		
		// Output query results: HTML table
		echo "<table border=1>";
		echo "<tr>";
		
		// fetch attribute names
                while ($fieldMetadata = $query_result->fetch_field()) {
			echo "<th>".$fieldMetadata->name."</th>";
                }
		echo "</tr>";
		
		// fetch table records
                while ($line = $query_result->fetch_assoc()) {
			echo "<tr>\n";
			foreach ($line as $cell) {
				echo "<td> $cell </td>";
			}
			echo "</tr>\n";
		}
		echo "</table>";
		
		// close the connection with database
		$conn->close();
	?>
	</div>
</div>
</body>
</html>
