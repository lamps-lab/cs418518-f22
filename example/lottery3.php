<?php 
echo "<h1>Lottery Game 2</h1>";

/* initialization */
$lastname=array('Smith','Kim','Davis','Miller','Taylor');
$firstname=array('John','Anthony','Richard','Thomas','Jessica');
$major=array('IST','CSE','EE','PHYS','ACCT');

/* create table */
echo "<table border=1>";
echo "<tr>";
echo "<th>LastName</th>";
echo "<th>FirstName</th>";
echo "<th>Major</th>";
echo "</tr>";
for($i=0;$i<sizeof($lastname);$i++){
	echo "<tr>";
	echo "<td>$lastname[$i]</td>";
	echo "<td>$firstname[$i]</td>";
	echo "<td>$major[$i]</td>";
	echo "</tr>";
}
echo "</table>";

/* output results -*/
$v=rand(0,4);
echo "<p><span style=font-size:200%;color:red>Today's winner is $firstname[$v] $lastname[$v]</span></p>";
?>
