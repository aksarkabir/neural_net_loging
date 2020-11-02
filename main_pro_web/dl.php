<?php
    $q = $_REQUEST["q"];
    $myfile = fopen("data_extra.txt", "r") or die("Unable to open file!");
    $str=fread($myfile,filesize("data_extra.txt"));
    fclose($myfile);
    $arr = json_decode($str,false);
    $myfile = fopen("data_extra.txt", "w") or die("Unable to open file!");
    $arr->name = $q;
    $arr->active = 1;
    $str = json_encode($arr);
    fwrite($myfile, $str);
    fclose($myfile);
?>
