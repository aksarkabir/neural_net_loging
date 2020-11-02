<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="w3.css">
    <title>delet user</title>
  </head>
  <body>
    <div class="w3-container">
      <a href="update.html" class="w3-button w3-left w3-text-blue">back</a>
      <h1 id="jk" class="w3-center w3-text-red">delete the selected user</h1>
      <?php
        $myfile = fopen("/home/kabir/codes/python/face/main_pro/data/data.txt", "r") or die("Unable to open file!");
        $str=fread($myfile,filesize("/home/kabir/codes/python/face/main_pro/data/data.txt"));
        fclose($myfile);
        $arr = json_decode($str,false);
        $brr = $arr->name;
        for($z=0;$z<count($brr);$z++){
          echo '<a id="'.$z.'" class="w3-button w3-left w3-text-blue" href="#" onclick = "hi(this)">'.$brr[$z].'</a>';
        }
      ?>
    </div>
  </body>
  <script type="text/javascript">
    function hi(a){
      var b = a.innerHTML;
      var c = a.id;
      document.getElementById("jk").innerHTML=b;
      document.getElementById(c).style.display = "none"
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          var g = this.responseText;
        }
      };
      xhttp.open("GET", "dl.php?q="+b, true);
      xhttp.send();
    }
  </script>
</html>
