<?php
	$str = "";
	$myfile = fopen("data.txt", "r") or die("Unable to open file!");
	$a= fread($myfile,filesize("data.txt"));
	$b = json_decode($a,false);
	fclose($myfile);
	if ($b->active==1){
		$str = $str.$b->num.','.$b->pass;
		echo $str;
		$b->active = 2;
		$str = json_encode($b);
		$myfile = fopen("data.txt", "w") or die("Unable to open file!");
		fwrite($myfile, $str);
		fclose($myfile);
	}else{
		echo 'not';
	}
?>
