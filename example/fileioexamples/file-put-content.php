<?php
    $file="cnn.txt";// Open the file to get existing content
    $current=file_get_contents($file);// Append a new person to the file
    echo $current."<br/>";
    $current.="John Smith\n";// Write the contents back to the file
    echo $current."<br/>";
    file_put_contents("cnn2.txt",$current);
?>

