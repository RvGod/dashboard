<?php
include "db.php";

$sql = "SELECT value FROM budget WHERE id = 1";
$result = $conn->query($sql);

if ($row = $result->fetch_assoc()) {
    echo $row['value'];
} else {
    echo 0; // default if not found
}
?>
