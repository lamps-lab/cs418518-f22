<html>
	<form action="process_comment.php"  method="post">
		<table border=0>
		<tr> 
			<td> Name: </td>
		    <td> <input type = "text" name="username" value = ""/> </td>
		</tr>
		<tr>
			<td> Do you like this page? </td>
			<td> <input type="radio" name="like" value="TRUE"> Yes <input type="radio" name="like" value="FALSE"> No </td>
		</tr>
		<tr> 
			<td> Comment: </td>
			<td> <textarea rows="5" cols="80" name="comment"> </textarea> </td>
		</tr>
		<tr>
			<td> Rating: </td>
			<td> 
				<select name="rating">
				<option value="1"> 1 </option>
				<option value="2"> 2 </option>
				<option value="3"> 3 </option>
				<option value="4"> 4 </option>
				<option value="5"> 5 </option>
				</select>
			</td>
		</tr>
	    </table> 
		<input type="submit" value ="go" />
	</form>
</html>
