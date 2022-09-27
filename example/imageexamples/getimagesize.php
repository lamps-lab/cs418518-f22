<?php
$filename="jianwu.png";
$size = getimagesize($filename);
$fp = fopen($filename, "rb");
if ($size && $fp) {
    echo "$size[0]<br>";
    echo "$size[1]<br>";
    echo "$size[2]";
    exit;
} else {
    // error
}
?>
