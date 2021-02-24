<?php
$servername = "localhost"; // no change
$username = "testroot"; // change
$password = "toor";				

$dbname = "testslayersecdatabase";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);

// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}
//echo "Connected successfully";

?>