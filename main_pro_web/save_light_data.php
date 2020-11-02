<?php
  $str = $_REQUEST["q"];

  $myfile = fopen("light_data.txt", "r") or die("Unable to open file!");
  $str2=fread($myfile,filesize("light_data.txt"));
  fclose($myfile);

  $arr = json_decode($str2,false);
  $brr = json_decode($str,false);

  if($brr->light==1){
    $arr->light_1=$brr->active;
  }else if($brr->light==2){
    $arr->light_2=$brr->active;
  }else if($brr->light==3){
    $arr->light_3=$brr->active;
  }
  $str2 = json_encode($arr);
  $myfile = fopen("light_data.txt", "w") or die("Unable to open file!");
  fwrite($myfile, $str2);
  fclose($myfile);
  echo 'done';
 ?>
