
<?php
$target_dir = "";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if($check !== false) {
        echo "File is an image - " . $check["mime"] . ".";
        $uploadOk = 1;
    } else {
        echo "File is not an image.";
        $uploadOk = 0;
    }
}
// Check if file already exists
// Check file size

// Allow certain file formats
// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.";
// if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
}
?>
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
          <h1 class="w3-center w3-text-red">Not matched with any id</h1>
        </div>
        <div id = "match" class="w3-card-4" style="display:none;">
          <h1 id = "mid" class="w3-center w3-text-red">matched with shihab</h1>
        </div>
        <div id = "noface" class="w3-card-4" style="display:none;">
          <h1 id = "" class="w3-center w3-text-red">NO Face found</h1>
        </div>
      </div>
      <form id ="pf" class="w3-container w3-card-4 w3-light-grey w3-text-blue" action="checkid.php" method="post" style="display:none;">
        enter pass
        <input class="w3-input" type="text" name="password" value="" required>
        <br>
        <input class="w3-button w3-blue" type="submit" name="" value="enter the pass">
      </form>
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
            var t = "matched with "+arr.name;
            document.getElementById("match").style.display = "block";
            document.getElementById("mid").innerHTML =t;
            document.getElementById("pf").style.display = "block";
          }else if(arr.active == 3){
            document.getElementById("notmatch").style.display ="block" ;
            change();
            setTimeout(red, 3000);
          }else if(arr.active == 4){
            document.getElementById("noface").style.display ="block" ;
            change();
            setTimeout(red, 3000);
          }
        }
      };
      xmlhttp.open("POST", "data.txt", true);
      xmlhttp.send();
    }
    window.setInterval(function(){
      check();
  /// call your function here
  }, 500);
  function red(){
    location.replace("index.html");
  }
  function change() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var g = this.responseText;
      }
    };
    xhttp.open("GET", "change.php", true);
    xhttp.send();
  }
  </script>
</html>
