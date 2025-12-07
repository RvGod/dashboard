<?php
include "db.php";

$amount = $_POST["amount"];
$type = $_POST["type"];
$category = $_POST["category"];
$date = $_POST["date"];
$description = $_POST["description"];

$sql = "INSERT INTO transactions(amount, type, category, date, description)
        VALUES ('$amount', '$type', '$category', '$date', '$description')";

echo $conn->query($sql) ? "success" : "error";
?>
