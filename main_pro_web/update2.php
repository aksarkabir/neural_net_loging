<?php
    $myfile = fopen("upload/data.txt", "r") or die("Unable to open file!");
    $str =fread($myfile,filesize("upload/data.txt"));
    fclose($myfile);
    $arr = json_decode($str,false);
    $arr->active=1;
    $arr->name = $_POST['nn'];
    $arr->number = $_POST['nnn'];
    $str = json_encode($arr);
    $myfile = fopen("upload/data.txt", "w") or die("Unable to open file!");
    fwrite($myfile, $str);
    fclose($myfile);
    echo '<h1>upload complete</h1>';
 ?>
 <!DOCTYPE html>
 <html lang="en" dir="ltr">
   <head>
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <link rel="stylesheet" href="w3.css">
     <title>processing....</title>
   </head>
   <body>
     <div class="w3-container">
       <h1 class="w3-center w3-text-blue">processing.....please wait</h1>
       <div class="w3-container w3-center">
         <div id = "notmatch" class="w3-card-4" style="display:none;">
           <h1 class="w3-center w3-text-red">Not found any image please insert a new image</h1>
         </div>
         <div id = "match" class="w3-card-4" style="display:none;">
           <h1 id = "mid" class="w3-center w3-text-red">data save to the database successfully</h1>
         </div>
       </div>
     </div>
     <p id="txtHint"></p>
   </body>
   <script type="text/javascript">
     function check() {
       var xmlhttp = new XMLHttpRequest();
       xmlhttp.onreadystatechange = function() {
         if (this.readyState == 4 && this.status == 200) {
           var str = this.responseText;
           var arr = JSON.parse(str);
           if(arr.active==2){
             document.getElementById("match").style.display = "block";
             change();
             setTimeout(red, 3000);
           }else if(arr.active == 3){
             document.getElementById("notmatch").style.display ="block" ;
             change();
             setTimeout(red, 3000);
           }
         }
       };
       xmlhttp.open("POST", "upload/data.txt", true);
       xmlhttp.send();
     }
     window.setInterval(function(){
       check();
   /// call your function here
   }, 500);
   function red(){
     location.replace("update.html");
   }
   function change() {
     var xhttp = new XMLHttpRequest();
     xhttp.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
         var g = this.responseText;
       }
     };
     xhttp.open("GET", "changeupload.php", true);
     xhttp.send();
   }
   </script>
 </html>
