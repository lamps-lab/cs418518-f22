<html>
<head>
<title> PHP SQL Example </title>
</head>

<body>
<h3> Query </h3>

<?php
	//$_POST=NULL;
?>
<form action="" method="post">
	Which table to query: <input type="text" name="table" /> <br> <br>
	<input type="submit" />
</form>

<?php
	$server = "localhost";
	$sqlUsername = "root";
	$sqlPassword = "BBQSundaymorning@8pm";
	$databaseName = "xschool";

	$conn = new mysqli($server, $sqlUsername, $sqlPassword, $databaseName);

  	// check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	} 

	if (!empty($_POST['table'])) {
		// get the table name
		$table = $_POST['table'];
			
		// prepare SQL query
		$sql = "SELECT * FROM $table";
			
		// print the query
		echo "Query: ".$sql."<br>";
			
		// Execute SQL query
	        $result = $conn->query($sql)
			or die( "ERROR: Query is wrong");
			
		echo "<table border=1>";
		echo "<tr>";
			
		// fetch attribute names
                while ($fieldMetadata = $result->fetch_field() ) {
		    echo "<th>".$fieldMetadata->name."</th>";
		}

		echo "</tr>";
			
		// fetch rows in the table
		while( $row = $result->fetch_assoc() ) {
			echo "<tr>\n";
			foreach ($row as $cell) {
				echo "<td> $cell </td>";
			}
			echo "</tr>\n";
		}
			
		echo "</table>";
    	}
	// close the connection with database
	$conn->close();
?>
</body>
</html>
