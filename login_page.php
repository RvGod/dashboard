<?php session_start(); ?>
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        body {
            font-family: Arial;
            background: #1F2544;
            color: #FFD0EC;
            display: flex;
            height: 100vh;
            justify-content: center;
            align-items: center;
        }
        .card {
            width: 350px;
            background: #474F7A;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            text-align: center;
        }
        input {
            width: 93%;
            padding: 12px;
            margin: 10px 0px;
            border-radius: 6px;
            background-color: #1F2544;
            border: 1px solid #53629E;
            color: #FFD0EC;
        }
        button {
            width: 100%;
            padding: 12px;
            border-radius: 6px;
            cursor: pointer;
            background-color: #473472;
            border: 1px solid #53629E;
            color: #FFD0EC;
        }
        button:hover { background: #81689D; }
        .link { margin-top: 10px; display: block; }
        .error { color: red; }
        .success { color: green; }

        a {
            color: #FFD0EC;
        }

        a:hover {
            color: #1F2544;
        }
    </style>
</head>
<body>

<div class="card">
    <h2>Login</h2>

    <?php if(isset($_SESSION["error"])) { ?>
        <p class="error"><?= $_SESSION["error"]; unset($_SESSION["error"]); ?></p>
    <?php } ?>

    <?php if(isset($_SESSION["success"])) { ?>
        <p class="success"><?= $_SESSION["success"]; unset($_SESSION["success"]); ?></p>
    <?php } ?>

    <form action="login.php" method="POST">
        <input type="email" name="email" placeholder="Email" required>
        <input type="password" name="password" placeholder="Password" required>

        <button name="login">Login</button>
    </form>

    <a class="link" href="register_page.php">Create an account</a>
</div>

</body>
</html>
