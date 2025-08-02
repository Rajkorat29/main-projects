echo "# 🧾 Inventory Management System

A complete inventory & billing system built using **Python Tkinter** and **MySQL**, with support for employee/supplier management, product tracking, and secure login.

---

## 💡 Features

- 🔐 Role-based Login (Admin, Employee)
- 📦 Product Management (Add, Update, Delete, Stock)
- 🧾 Billing System with live calculation
- 👨‍💼 Employee & Supplier Management
- 🗂️ Category-wise product listing
- 🧮 Tax calculation support
- 🖨️ Printable Bills with QR code
- 📤 Email Integration (Invoices/Notifications)

---

## 🛠 Technologies Used

| Layer              | Tools                        |
|--------------------|------------------------------|
| Programming        | Python 3.x                   |
| GUI                | Tkinter                      |
| Database           | MySQL 8                      |
| Local Server       | XAMPP                        |
| DB Management      | MySQL Workbench              |
| QR Code Generator  | \`qrcode\` Python library      |
| Email Sending      | \`smtplib\`, \`email\` modules   |
| Image Handling     | \`Pillow (PIL)\`               |
| Others             | \`os\`, \`tempfile\`, \`threading\`|

---

## 📂 Folder Structure

\`\`\`
Inventory_Management_System/
├── login.py
├── dashboard.py
├── employee.py
├── supplier.py
├── category.py
├── product.py
├── billing.py
├── config/
│   └── db_config.py
├── database/
│   └── inventory_schema.sql
├── assets/
│   └── icons, logos, etc.
├── README.md
└── main.py
\`\`\`

---

## ⚙️ Setup Instructions

### ✅ 1. Clone Repository
\`\`\`bash
git clone https://github.com/Rajkorat29/main-projects.git
cd main-projects/Inventory_Management_System
\`\`\`

### ✅ 2. Install Required Packages
\`\`\`bash
pip install pillow qrcode mysql-connector-python
\`\`\`

### ✅ 3. Configure MySQL
- Import the SQL file from \`/database/inventory_schema.sql\`
- Update \`db_config.py\` with your MySQL user/password

### ✅ 4. Run the Application
\`\`\`bash
python main.py
\`\`\`

---

## 👤 Default Roles for Testing

| Role     | Username | Password |
|----------|----------|----------|
| Admin    | admin    | 1234     |
| Employee | employee | 5678     |

---

## 📈 Future Enhancements

- 📊 Sales reporting with charts
- 📲 Mobile App (Android/iOS)
- 📩 Low-stock email alerts
- ☁️ Cloud database support
- 🔐 Multi-factor authentication

---

## 📚 References

- [Python Tkinter Docs](https://docs.python.org/3/library/tkinter.html)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [Pillow Docs](https://pillow.readthedocs.io/)
- [QR Code Library](https://pypi.org/project/qrcode/)
- [GitHub Help](https://docs.github.com/)

---

## 👨‍💻 Author

**Raj Korat**  
[GitHub: Rajkorat29](https://github.com/Rajkorat29)

---
