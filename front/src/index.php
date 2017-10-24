<?php
$docker_localhost = "proxy:8080";

$backends = array(
"http://$docker_localhost/boardgames/plays/latestgames",
"http://$docker_localhost/boardgames/plays/statistics",
"http://$docker_localhost/antell/",
"http://$docker_localhost/abc/",
"http://$docker_localhost/now-listening/",
"http://$docker_localhost/rss/");

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
// using file() function to get content
$content=file_get_contents($backends[$_GET["index"]]);

// Remove control characters which make JSON parser fail.
$regFrom = array("/\n/", "/\t/");
$regTo = array("", "    ");
$content = preg_replace($regFrom, $regTo, $content);
// Convert string to JSON object
$contentAsJson = json_decode($content);

?>
<html>
<head>
<meta http-equiv="refresh" content="10;URL='?index=<?php echo $nextindex ?>'">
<title><?=$contentAsJson->title;?></title>
</head>
    <body>
<?php

if ($contentAsJson == null) {
    echo "<h1>Error parsing JSON</h1>";
    echo "<pre>";
    print_r($content);
    var_dump($contentAsJson);
    echo "</pre>";
} else {
    echo $contentAsJson->content;
}
echo "<!--";
print_r($content);
var_dump($contentAsJson);
echo "-->";
?>
</body>
</html>
