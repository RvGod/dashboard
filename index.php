<?php
session_start();
if(!isset($_SESSION["user_id"])) {
    header("Location: login_page.php");
    exit();
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Expense Tracker</title>
    <link rel="stylesheet" href="style.css">
    <link rel='stylesheet' href='https://cdn-uicons.flaticon.com/3.0.0/uicons-solid-straight/css/uicons-solid-straight.css'>
    <link rel='stylesheet' href='https://cdn-uicons.flaticon.com/3.0.0/uicons-regular-rounded/css/uicons-regular-rounded.css'>
    <link rel='stylesheet' href='https://cdn-uicons.flaticon.com/3.0.0/uicons-regular-rounded/css/uicons-regular-rounded.css'>
    <link rel='stylesheet' href='https://cdn-uicons.flaticon.com/3.0.0/uicons-regular-rounded/css/uicons-regular-rounded.css'>
    <link rel='stylesheet' href='https://cdn-uicons.flaticon.com/3.0.0/uicons-bold-rounded/css/uicons-bold-rounded.css'>
    <link rel='stylesheet' href='https://cdn-uicons.flaticon.com/3.0.0/uicons-solid-rounded/css/uicons-solid-rounded.css'>
</head>

<body>

<!--SIDEBAR -->
<div class="sidebar" id="sidebar">
    <div class="sidebar-toggle" onclick="toggleSidebar()">
        <div class="hamburger active" id="hamburger">
            <span></span>
            <span></span>
            <span></span>
        </div>
    </div>

    <h2></h2>

    <ul>
    <li onclick="loadPage('dashboard.php')">
        <i class="fi fi-rr-dashboard"></i><span>Dashboard</span>
    </li>

    <li onclick="loadPage('transaction.php')">
        <i class="fi fi-ss-receipt"></i><span>Add Transaction</span>
    </li>

    <li onclick="loadPage('categories.php')">
        <i class="fi fi-rr-category-alt"></i><span>Categories</span>
    </li>

    <li onclick="loadPage('budget.php')">
        <i class="fi fi-rr-budget-alt"></i><span>Budget</span>
    </li>

    <li onclick="loadPage('history.php')">
        <i class="fi fi-br-time-past"></i><span>History</span>
    </li>

    <li class="logout" onclick="location.href='logout.php'">
        <i class="fi fi-sr-user-logout"></i><span>Logout</span>
    </li>
</ul>

</div>

<!--MAIN CONTENT-->
<div class="main-content" id="main-content">

<header>
    <h1>Expense Tracker</h1>
</header>
<main>
    
</main>
</div> <!--end main-content-->

<script src="script.js"></script>

<script>
function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    const main = document.getElementById("main-content");
    const hamburger = document.getElementById("hamburger");

    const isCollapsed = sidebar.classList.toggle("collapsed");
    main.classList.toggle("collapsed");

    if (isCollapsed) {
        // Sidebar is now CLOSED → show hamburger
        hamburger.classList.remove("active");
    } else {
        // Sidebar is now OPEN → show X
        hamburger.classList.add("active");
    }
}

function loadPage(page) {
    fetch(page)
        .then(response => response.text())
        .then(html => {
            document.getElementById("main-content").innerHTML = html;

            // Re-run functions AFTER new content loads
            if (page === "dashboard.php") {
                updateDashboard();
            }
            if (page === "categories.php") {
                loadCategories();
            }
            if (page === "history.php") {
                loadHistory();
            }
            if (page === "transaction.php") {
                loadCategories(); // Category dropdown
            }
            if (page === "budget.php") {
                loadBudget();
            }
        });
}

</script>

</body>
</html>
