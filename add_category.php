<?php
include "db.php";

$name = $_POST["name"];
$sql = "INSERT INTO categories(name) VALUES ('$name')";

echo $conn->query($sql) ? "success" : "error";
?>
