<?php
$docker_localhost = "proxy:8080";

$backends = array( 
"http://$docker_localhost/first/", 
"http://$docker_localhost/gotest/satiaisia",
"http://$docker_localhost/second/page");

if(!isset($_GET["index"]) || $_GET["index"] === "") {
    header( 'Location: /?index=0');
    exit();
} else {
  $index = $_GET["index"];
  $nextindex = $index+1;
  if($nextindex >= sizeof($backends)) {
      $nextindex = 0;
  }
}
?>
<html>
<head>
<meta http-equiv="refresh" content="10;URL='?index=<?php echo $nextindex ?>'">
</head>
    <body>
<?php
// using file() function to get content
$lines_array=file($backends[$_GET["index"]]);
// turn array into one variable
$lines_string=implode('',$lines_array);
//output, you can also save it locally on the server
echo $lines_string;
?>
</body>
</html>
