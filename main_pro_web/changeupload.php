<?php
    $myfile = fopen("upload/data.txt", "r") or die("Unable to open file!");
    $str= fread($myfile,filesize("upload/data.txt"));
    fclose($myfile);
    $arr = json_decode($str,false);
    $arr->active = 0;
    $str = json_encode($arr);
    $myfile = fopen("upload/data.txt", "w") or die("Unable to open file!");
    fwrite($myfile, $str);
    fclose($myfile);
    echo 'done';
 ?>
