<?php
include "db.php";

$value = $_POST["budget"];
$sql = "UPDATE budget SET value = $value WHERE id = 1";

echo $conn->query($sql) ? "success" : "error";
?>
