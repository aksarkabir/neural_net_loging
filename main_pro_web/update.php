
<?php
$target_dir = "upload/";
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
  <title>add new people</title>
</head>
<body>
  <div class="w3-container">
    <h1 class="w3-center w3-text-blue">upload new user</h1>
    <form class="w3-container w3-card-4 w3-light-grey w3-text-gray" action="update2.php" method="post">
      <h2 class="w3-center">upload info</h2>

      name:
      <input class="w3-input" type="text" name="nn" value="" required>
      phone number
      <input class="w3-input" type="text" name="nnn" value="" required>
      <br>
      <input class="w3-button w3-blue" type="submit" name="" value="enter new user">
    </form>
  </div>
</body>
</html>
