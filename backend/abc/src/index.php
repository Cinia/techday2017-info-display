<?php
//header("Content-Type", "application/json");
// using file() function to get content
$content=file_get_contents("https://www.abcasemat.fi/fi/asemat/abc-keljonkangas-jyvaskyla/noutopoyta");

$regFrom = array("/\r\n/", "/\r/", "/\n/", "/\t/");
$regTo = array("", "", "", "    ");

// Remove line changes and tabs
$content = preg_replace($regFrom, $regTo, $content);

$replacement = '${1}';

// Print menu for today
$abc_content = "<h2>ABC keljonkangas</h2><div><p><strong>TÄNÄÄN</strong></p>";
$abc_content .= preg_replace("/.*\<div class=\"row station_lunch_food\"\>(.*)\<a class=\"show_lunches\" id=\"show_lunch_list\">VIIKON NOUTOPÖYDÄT &raquo;\<\/a\>\s+\<\/div\>\s+\<\/div\>.*/", $replacement, $content);
$abc_content .= "</div></div>";

// This gets the rest of the week too
// Get current day of week 
//$i = date ("N") +1 ;
//for($i; $i <= 7; $i++){
  // Menus for remaining days of week
  //$abc_content .= preg_replace("/.*(\<div class=\"lunch_day_row\" data-day=\"$i\"\>((?!<div class=\"row lunch_more_info\"\>).)*)\<div class=\"row lunch_more_info\"\>.*/", $replacement, $content);
//}


// Convert string to JSON object
header('Content-type: application/json');
echo json_encode([ "title" => "ABC Noutopöytä", "content" => $abc_content]);
?>