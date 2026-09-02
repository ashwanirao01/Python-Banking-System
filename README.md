# 🏦 Python Banking System

A simple **console-based banking management system built with Python**.
This project allows users to create a bank account, deposit and withdraw money, view account details, update their information, and delete their account.

Account data is stored locally in a **JSON file (`data.json`)**, so the information remains available after restarting the program.

## ✨ Features

* 🆕 Create a new bank account
* 🔐 Account authentication using Account Number and PIN
* 💰 Deposit money
* 💸 Withdraw money
* 📄 View account details
* ✏️ Update account name, email, and PIN
* 🗑️ Delete an account
* 💾 Persistent data storage using JSON
* 🔢 Automatically generated account numbers

## 🛠️ Technologies Used

* **Python 3**
* **JSON** — for storing account data
* **Pathlib** — for file handling
* **Random & String** — for generating account numbers

## 📁 Project Structure

```text
Banking-System/
│
├── bank.py
├── data.json
└── README.md
```

## ⚙️ Requirements

Make sure Python 3 is installed on your system.

Check your Python version:

```bash
python --version
```

No external Python packages are required.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Move into the project directory

```bash
cd Banking-System
```

### 3. Run the program

```bash
python bank.py
```

If `data.json` does not exist, create an empty file containing:

```json
[]
```

## 📌 How to Use

After running the program, you will see the following menu:

```text
Press 1 for creating an account
Press 2 for Deposititing the money
Press 3 for withdrawing the money
Press 4 for details
Press 5 for updating the details
Press 6 for deleting your account
```

### 1️⃣ Create Account

Enter:

* Name
* Age
* Email
* 4-digit PIN

The program automatically generates an account number.

Example:

```text
Account_no: aB7#91x
Balance: 0
```

The account will only be created if the user is **18 or older** and provides a 4-digit PIN.

### 2️⃣ Deposit Money

Provide:

* Account Number
* PIN
* Deposit amount

The current balance will be updated and saved to `data.json`.

### 3️⃣ Withdraw Money

Provide:

* Account Number
* PIN
* Withdrawal amount

The program checks whether the account has sufficient balance before completing the withdrawal.

### 4️⃣ Show Details

Enter your Account Number and PIN to view your stored account information.

### 5️⃣ Update Details

Users can update:

* Name
* Email
* PIN

The following information cannot be changed:

* Age
* Account Number
* Balance

### 6️⃣ Delete Account

Enter your Account Number and PIN, then confirm the deletion.

## 💾 Data Storage

The project uses `data.json` to store account information.

Example:

```json
[
    {
        "name": "John",
        "age": 21,
        "email": "john@example.com",
        "pin": 1234,
        "Account_no": "aB7#91x",
        "Balance": 5000
    }
]
```

## ⚠️ Important Note

This project is created for **learning and practice purposes**. It is not suitable for handling real banking or financial data.

The PIN is stored as plain text in the JSON file. A production banking application should use secure authentication, password/PIN hashing, input validation, database storage, transaction logging, and proper authorization.

## 🔮 Future Improvements

Some possible improvements:

* [ ] Add a continuous menu loop
* [ ] Improve input validation
* [ ] Prevent duplicate account numbers
* [ ] Hash PINs instead of storing them directly
* [ ] Add transaction history
* [ ] Add transfer-money functionality
* [ ] Add interest calculation
* [ ] Replace JSON storage with SQLite/MySQL
* [ ] Add better error handling
* [ ] Create a GUI version
* [ ] Add unit tests

## 🤝 Contributing

Contributions and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push the branch
6. Open a Pull Request

## 📜 License

This project is intended for educational purposes. You can add a license such as **MIT License** if you want to make the project open-source.
