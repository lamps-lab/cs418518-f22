<?php
   if(!file_exists("test.txt")) {
      die("File not found");
   } else {
      $file = fopen("test.txt","r");
      print "Opend file sucessfully";
      fclose( $file );     
   }
   // Test of the code here.
?>
