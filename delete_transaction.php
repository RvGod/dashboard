<?php
include "db.php";

$id = $_POST["id"];
$sql = "DELETE FROM transactions WHERE id = $id";

echo $conn->query($sql) ? "success" : "error";
?>
