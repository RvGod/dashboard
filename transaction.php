<header>
    <h1>Expense Tracker</h1>
</header>

<section id="transaction-form">
    <h2>Add Transaction</h2>
    <form id="form">
        <input type="number" id="amount" placeholder="Amount" required>
        <select id="type">
            <option value="income">Income</option>
            <option value="expense">Expense</option>
        </select>
        <select id="category"></select>
        <input type="date" id="date" required>
        <input type="text" id="description" placeholder="Description">
        <button type="button" onclick="saveTransaction(document.getElementById('form'))">Add</button>
    </form>
</section>

