<?php
// Error handler function
function customError($errno, $errstr){
    echo "<b>custom Error:</b> [$errno] $errstr";
}

// Set error handler
set_error_handler("customError");

// Trigger error
echo($test);
?>
