<?php
  echo $_POST['name'].'<br>';
  echo $_POST['password'];
  $myfile = fopen("pass.txt", "r") or die("Unable to open file!");
  $str =fread($myfile,filesize("pass.txt"));
  fclose($myfile);
  $arr = json_decode($str,false);
  array_push($arr->name,$_POST['name']);
  $arr->login->{$_POST['name']}=$_POST['password'];
  $str = json_encode($arr);
  $myfile = fopen("pass.txt", "w") or die("Unable to open file!");
  fwrite($myfile, $str);
  fclose($myfile);
  echo 'done';
 ?>

 <script type="text/javascript">
   setTimeout(red, 3000);
   function red(){
     location.replace("update.html");
   }
 </script>
