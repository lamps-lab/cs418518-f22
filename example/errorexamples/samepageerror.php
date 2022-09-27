<?php
if (empty($var1)) {
    $errors .= "var1 should not be empty<br>";
}
if (!is_numeric($var2)) {
    $errors .= "var2 should be a number<br>";
} 
// check all anticipated error conditions ...
if (empty($errors)){
    echo "No errors found!";
} else {
    internal_error_function($errors);
}

function internal_error_function ($errors) {
    echo "Errors found: ". $errors;
    // provide link to start over
}
?>
