<?php
session_start();
include "db.php";

if(isset($_POST["login"])) {
    $email = $_POST["email"];
    $password = $_POST["password"];

    $result = $conn->query("SELECT * FROM users WHERE email='$email'");

    if ($result->num_rows === 1) {
        $user = $result->fetch_assoc();

        if (password_verify($password, $user["password"])) {
            $_SESSION["user_id"] = $user["id"];
            $_SESSION["fullname"] = $user["fullname"];
            header("Location: index.php");
            exit();
        }
    }

    $_SESSION["error"] = "Invalid email or password.";
    header("Location: login_page.php");
}
?>
