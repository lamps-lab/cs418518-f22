<html>
	<form method ="post" >
		Pick a student (1-5)! 
		<input type="text" name="studentID" /> <br>
		<input type="submit" value = "go"/>
	</form>
	<?php 
		$lastname = array ('Smith', 'Kim', 'Davis', 'Miller', 'Taylor');
		$firstname = array('John', 'Anthony', 'Richard', 'Thomas', 'Jessica');
		if (!empty($_POST['studentID'])){
			$v = $_POST['studentID'];
			echo "Today's Winner is: ".$firstname[$v-1]." ".$lastname[$v-1];
		}	
	?>
</html>
