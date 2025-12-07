// DYNAMIC PAGE LOADING 
function loadPage(page) {
    fetch(page)
        .then(res => res.text())
        .then(html => {
            document.getElementById("main-content").innerHTML = html;

            // Ensure DOM is rendered fully before running JS
            requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                    initializePage(page);
                });
            });
        });
}

function initializePage(page) {
    switch (page) {
        case "dashboard.php":
            loadBudget();
            updateDashboard();
            break;

        case "categories.php":
            loadCategories();
            break;

        case "history.php":
            loadHistory();
            break;

        case "transaction.php":
            loadCategories().then(() => initTransactionForm());
            break;

        case "budget.php":
            loadBudget();
            break;
    }
}

// Load dashboard initially
window.onload = () => loadPage("dashboard.php");

// CATEGORY FUNCTIONS
function loadCategories() {
    return fetch("load_categories.php")
        .then(res => res.json())
        .then(data => {
            const dropdown = document.getElementById("category");
            const list = document.getElementById("category-list");

            if (dropdown) dropdown.innerHTML = "";
            if (list) list.innerHTML = "";

            data.forEach(cat => {
                if (dropdown) {
                    const opt = document.createElement("option");
                    opt.value = cat.name;
                    opt.textContent = cat.name;
                    dropdown.appendChild(opt);
                }

                if (list) {
                    const li = document.createElement("li");
                    li.innerHTML = `
                        ${cat.name}
                        <button onclick="deleteCategory(${cat.id})">Delete</button>
                    `;
                    list.appendChild(li);
                }
            });
        });
}

function addCategory() {
    const field = document.getElementById("new-category");
    if (!field) return;

    const value = field.value.trim();
    if (value === "") return alert("Category cannot be empty");

    const fd = new FormData();
    fd.append("name", value);

    fetch("add_category.php", { method: "POST", body: fd })
        .then(res => res.text())
        .then(resp => {
            if (resp === "success") {
                field.value = "";
                loadCategories();
            }
        });
}

function deleteCategory(id) {
    const fd = new FormData();
    fd.append("id", id);

    fetch("delete_category.php", { method: "POST", body: fd })
        .then(res => res.text())
        .then(resp => {
            if (resp === "success") loadCategories();
        });
}

// TRANSACTION FUNCTIONS
function initTransactionForm() {
    const form = document.getElementById("form");
    if (!form) return;

    // remove old listeners
    const newForm = form.cloneNode(true);
    form.parentNode.replaceChild(newForm, form);

    newForm.addEventListener("submit", e => {
        e.preventDefault();
        saveTransaction(newForm);
    });
}

function saveTransaction(form) {
    const fields = [
        { id: "amount", required: true },
        { id: "type", required: true },
        { id: "category", required: true },
        { id: "date", required: true },
        { id: "description", required: false } // optional
    ];

    let valid = true;
    let firstEmpty = null;

    // Reset all borders
    fields.forEach(f => {
        const el = document.getElementById(f.id);
        if (el) el.style.border = "";
    });

    // Check each field
    fields.forEach(f => {
        const el = document.getElementById(f.id);
        if (!el) return;

        const value = el.value.trim();
        if (f.required && !value) {
            el.style.border = "2px solid red";
            if (!firstEmpty) firstEmpty = el;
            valid = false;
        }

        if (f.id === "amount" && value && (isNaN(value) || Number(value) <= 0)) {
            el.style.border = "2px solid red";
            if (!firstEmpty) firstEmpty = el;
            valid = false;
        }
    });

    if (!valid) {
        if (firstEmpty) firstEmpty.focus();
        return alert("Please fill in all required fields correctly.");
    }

    // Prepare data
    const fd = new FormData();
    fields.forEach(f => {
        const el = document.getElementById(f.id);
        if (el) fd.append(f.id, el.value.trim());
    });

    // Send request
    fetch("save_transaction.php", { method: "POST", body: fd })
        .then(res => res.text())
        .then(resp => {
            if (resp.trim() === "success") {
                alert("Transaction Added!");
                form.reset();
                updateDashboard();
                loadHistory();
            } else {
                alert("Error: " + resp);
            }
        });
}

// HISTORY
function loadHistory() {
    const body = document.getElementById("history-body");
    if (!body) return;

    fetch("load_transactions.php")
        .then(res => res.json())
        .then(data => {
            body.innerHTML = "";
            data.forEach(t => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td>₱${t.amount}</td>
                    <td>${t.type}</td>
                    <td>${t.category}</td>
                    <td>${t.date}</td>
                    <td>${t.description}</td>
                    <td><button onclick="deleteTransaction(${t.id})">Delete</button></td>
                `;
                body.appendChild(tr);
            });
        });
}

function deleteTransaction(id) {
    if (!confirm("Delete this transaction?")) return;

    const fd = new FormData();
    fd.append("id", id);

    fetch("delete_transaction.php", { method: "POST", body: fd })
        .then(res => res.text())
        .then(resp => {
            if (resp === "success") {
                loadHistory();
                updateDashboard();
            }
        });
}

// BUDGET
function setBudget() {
    const input = document.getElementById("budget-input");
    if (!input) return;

    const val = Number(input.value);
    if (val <= 0) return alert("Enter a valid budget");

    const fd = new FormData();
    fd.append("budget", val);

    fetch("save_budget.php", { method: "POST", body: fd })
        .then(res => res.text())
        .then(resp => {
            if (resp === "success") {
                alert("Budget Saved!");
                loadBudget();
            }
        });
}

function loadBudget() {
    fetch("load_budget.php")
        .then(res => res.text())
        .then(value => {
            const el = document.getElementById("budget-display");
            if (el) el.innerText = "₱" + value;

            window.currentBudget = Number(value);
        });
}

// DASHBOARD
function updateDashboard() {
    Promise.all([
        fetch("load_transactions.php").then(res => res.json()),
        fetch("load_budget.php").then(res => res.text())
    ]).then(([transactions, budgetValue]) => {
        let income = 0, expenses = 0;
        transactions.forEach(t => {
            if (t.type === "income") income += Number(t.amount);
            else expenses += Number(t.amount);
        });

        const balance = income - expenses;

        document.getElementById("total-income").innerText = "₱" + income;
        document.getElementById("total-expenses").innerText = "₱" + expenses;
        document.getElementById("balance").innerText = "₱" + balance;

        const budgetEl = document.getElementById("budget-display");
        if (budgetEl) budgetEl.innerText = "₱" + budgetValue;

        window.currentBudget = Number(budgetValue);
        checkBudget(expenses);
    });
}

function checkBudget(expenses) {
    const budget = window.currentBudget || 0;
    if (budget <= 0) return;

    const percent = (expenses / budget) * 100;

    if (percent >= 100) alert("⚠ Budget exceeded!");
    else if (percent >= 80) alert("⚠ You have used 80% of your budget.");
}
