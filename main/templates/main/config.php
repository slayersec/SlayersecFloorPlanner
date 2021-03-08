<?php
$servername = "slayersec.mysql.pythonanywhere-services.com"; // no change
$username = "slayersec"; // change
$password = "13146@Data";				

$dbname = "testslayersecdatabase";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);

// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}
//echo "Connected successfully";

?>