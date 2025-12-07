<?php
session_start();
include "db.php";

if(isset($_POST["register"])) {
    $fullname = $_POST["fullname"];
    $email = $_POST["email"];
    $password = password_hash($_POST["password"], PASSWORD_DEFAULT);

    // Check if email already exists
    $check = $conn->query("SELECT * FROM users WHERE email='$email'");
    if($check->num_rows > 0){
        $_SESSION["error"] = "Email already registered.";
        header("Location: register_page.php");
        exit();
    }

    $sql = "INSERT INTO users(fullname, email, password)
            VALUES('$fullname', '$email', '$password')";

    if ($conn->query($sql)) {
        $_SESSION["success"] = "Account created. You may now log in.";
        header("Location: login_page.php");
    } else {
        $_SESSION["error"] = "Registration failed.";
        header("Location: register_page.php");
    }
}
?>
