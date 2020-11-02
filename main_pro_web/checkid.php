<?php
    $myfile = fopen("data.txt", "r") or die("Unable to open file!");
    $str= fread($myfile,filesize("data.txt"));
    fclose($myfile);
    $arr = json_decode($str,false);
    if($arr->pass == $_POST['password']){
      echo '<h1>welcome</h1><br>';
      echo '<h1>'.$arr->name.'</h1>';
      $arr->active = 0;
      $str = json_encode($arr);
      $myfile = fopen("data.txt", "w") or die("Unable to open file!");
      fwrite($myfile, $str);
      fclose($myfile);
      header("Location: light.html");
      die();
    }else{
      $arr->active = 0;
      $str = json_encode($arr);
      $myfile = fopen("data.txt", "w") or die("Unable to open file!");
      fwrite($myfile, $str);
      fclose($myfile);
      echo "<h1> sms code doesn't match</h1>";
    }
 ?>
 <script type="text/javascript">
 setTimeout(red, 3000);
 function red(){
   location.replace("index.html");
 }
 </script>
