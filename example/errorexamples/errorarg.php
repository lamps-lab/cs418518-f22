<?php
if (empty($var1)) {
  $errors .= "$var1 should not be empty";
}
if (!is_numeric($var2)) {
  $errors .= "$var2 should be a number";
} 
// check all anticipated error conditions
if (empty($errors)) {
   echo "I am error free!";
} else {
  $errors = urlencode($errors);
  header("Location: https://www.google.com");
}
?>
