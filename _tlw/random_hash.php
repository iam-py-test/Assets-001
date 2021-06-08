<?php
echo "<!DOCTYPE html>";
echo "<title>Random test (try 2)</title>";
#get the random
$random = $_GET["random"];
echo "<p>Random: $random</p>";
$options = [ 
'cost' => 12, 
]; 
#hash the random number					
$hashed = password_hash($random,PASSWORD_BCRYPT,$options);
echo "<p>Hashed: $hashed</p>";
# display if it worked
$verified = password_verify($random,$hashed);
echo "<p>Verified: $verified</p>";
?>
