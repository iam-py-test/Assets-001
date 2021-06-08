<?php
echo "<!DOCTYPE html>";
echo "<title>Random test (try 2)</title>";
$random = $_GET["random"];
echo "<p>Random: $random</p>";
$options = [ 
							'cost' => 12, 
						]; 
						
$hashed = password_hash($random,PASSWORD_BCRYPT,$options);
echo "<p>Hashed: $hashed</p>";
$verified = password_verify($random,$hashed);
echo "<p>Verified: $verified</p>";
?>