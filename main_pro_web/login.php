<?php
  $id =$_POST["id"];
  $p = $_POST["pass"];
  $myfile = fopen("pass.txt", "r") or die("Unable to open file!");
  $a = fread($myfile,filesize("pass.txt"));
  fclose($myfile);
  $obj = json_decode($a,false);
  $nm = $obj->name;
  $cn = 0;
  $pass = $obj->login;
  for ($z=0;$z<count($nm);$z++){
    if($nm[$z]==$id){
      if($pass->{$nm[$z]}==$p){
        echo '<h1>Welcome</h1>';
        $cn = 1;
        header('Location: '.'update.html');
        die();
        break;
      }
    }
  }
  if($cn == 0){
    echo '<h1>id or password not match</h1>';
  }
 ?>
