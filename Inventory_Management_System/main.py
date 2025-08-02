import os
from tkinter import *
from tkinter import messagebox
import pymysql
import time
import category
import employee
import product
import sales
import supplier
from tkinter import ttk


# Example function to save tax to the database
def enter_tax():
    tax_window = Toplevel()
    tax_window.grab_set()
    tax_window.geometry('300x200')
    tax_window.title("Enter Tax Percentage")

    # Define colors for the theme
    bg_color = "#f0f0f0"  # Light gray background
    fg_color = "#333333"  # Dark text color
    btn_color = "#4caf50"  # Green button
    btn_fg_color = "#ffffff"  # White button text

    tax_window.configure(bg=bg_color)

    def save_tax_to_database():
        tax_value = tax_spinbox.get()
        try:

            # Convert the tax value to a float
            tax_percentage = float(tax_value)

            # Save tax to the database
            mycursor.execute("SELECT id FROM settings WHERE id = 1")
            result = mycursor.fetchone()

            if result:
                # Update existing entry
                mycursor.execute("UPDATE settings SET tax_percentage = %s WHERE id = 1", (tax_percentage,))
            else:
                # Insert new entry
                mycursor.execute("INSERT INTO settings (id, tax_percentage) VALUES (1, %s)", (tax_percentage,))

            # Commit the changes to the database
            conn.commit()

            messagebox.showinfo("Success", f"Tax percentage set to {tax_percentage}% and saved successfully.")
        except Exception as e:
            print(f"Error saving tax to database: {e}")
            messagebox.showerror("Database Error", "Failed to save tax percentage.")

    # Create a label and spinbox for entering tax
    tax_label = Label(tax_window, text="Enter Tax Percentage (%):", font=("Arial", 12), bg=bg_color, fg=fg_color)
    tax_label.pack(pady=10)

    tax_spinbox = Spinbox(tax_window, from_=0, to=100, font=("Arial", 12), bg="#ffffff", fg=fg_color, width=10)
    tax_spinbox.pack(pady=10)

    # Create a save button
    save_button = Button(tax_window, text="Save", font=("Arial", 12), bg=btn_color, fg=btn_fg_color,
                         command=save_tax_to_database)
    save_button.pack(pady=10)

    tax_window.mainloop()


def connection():
    global mycursor, conn, emp_name
    try:
        conn = pymysql.connect(host='localhost', user='root', password='1247', database='inventory_data')
        mycursor = conn.cursor()
    except:
        messagebox.showerror('Error', 'Something went wrong, Please open MySQL app before running again')

    try:
        emp_id = os.getenv('EMP_ID')
        mycursor.execute('SELECT name from emp_data WHERE empid=%s', (emp_id))
        emp_name = mycursor.fetchone()
        if len(emp_name) > 0:
            emp_name = emp_name[0]
    except:
        emp_name = 'Admin'


def update_content():
    global mycursor

    try:
        mycursor.execute('SELECT * from product_data')
        product = mycursor.fetchall()
        totalProductscountLabel.config(text=f'{len(product)}')
    except:
        totalProductscountLabel.config(text='0')

    try:
        mycursor.execute('SELECT * from sup_data')
        suppliers = mycursor.fetchall()
        totalSuppliercountLabel.config(text=f'{len(suppliers)}')
    except:
        totalSuppliercountLabel.config(text='0')

    try:
        mycursor.execute('SELECT * from emp_data')
        employees = mycursor.fetchall()
        totalEmployeescountLabel.config(text=f'{len(employees)}')
    except:
        totalEmployeescountLabel.config(text='0')

    try:
        mycursor.execute('SELECT * from category_data')
        categories = mycursor.fetchall()
        totalCategorycountLabel.config(text=f'{len(categories)}')
    except:
        totalCategorycountLabel.config(text='0')

    try:
        totalSalescountLabel.config(text=f'{len(os.listdir("bills"))}')
    except:
        totalSalescountLabel.config(text='0')

    time_ = time.strftime('%I:%M:%S %p')
    date_ = time.strftime('%d/%m/%Y')
    subtitleLabel.config(text=f'Welcome {emp_name}\t\t Date: {date_}\t\t Time: {time_}')
    subtitleLabel.after(500, update_content)


# Functionality Part
current_window = None


def close_current_window():
    global current_window
    if current_window is not None:
        current_window.destroy()
        current_window = None


def employee_form():
    global current_window, mycursor

    close_current_window()

    current_window, mycursor = employee.employee_page(window, mycursor, conn)


def supplier_form():
    global current_window, mycursor
    close_current_window()

    current_window, mycursor = supplier.supplier_page(window, mycursor, conn)


def category_form():
    global current_window, mycursor

    close_current_window()

    current_window, mycursor = category.category_page(window, mycursor, conn)


def product_form():
    global current_window, mycursor
    close_current_window()
    urrent_window, mycursor = product.product_page(window, mycursor, conn)


def sales_form():
    global current_window
    close_current_window()

    current_window = sales.sales_page(window, mycursor, conn)


def exit():
    result = messagebox.askyesno('Confirm', 'Do you want to really exit?')
    if result:
        window.destroy()


def logout():
    window.destroy()
    os.system('python login.py')


# GUI Part
window = Tk()
window.title('Inventory Management System')
window.geometry('1525x755+0+0')
window.config(bg='#E4E0E1')
icon = PhotoImage(file='P1logo.png')

# text of title
titleLabel = Label(window, text='  Inventory Management System', image=icon, compound=LEFT,font=('times new roman', 30, 'bold'), bg='#E4E0E1', fg='#493628', anchor='w', padx=20)
titleLabel.place(x=0, y=0, relwidth=1, height=70)

#logout button
logoutButton = Button(window, text='Logout', font=('times new roman', 20, 'bold'), bg='#493628', fg='#E4E0E1',cursor='hand2', command=logout)
logoutButton.place(x=1350, y=10)

#time lable
subtitleLabel = Label(window, text='Welcome to Inventory Management System\t\t Date:DD-MM-YYYY\t\t Time: HH:MM:SS',font=('times new roman', 15), bg='#D6C0B3', fg='black')
subtitleLabel.place(x=0, y=70, relwidth=1)

# Frame of left menu
leftFrame = Frame(window, bd=2, relief=RIDGE, bg='#493628')
leftFrame.place(x=-1, y=99, width=200, height=755)

leftLogo = PhotoImage(file='P1Task-rafiki(2).png')
leftLabel = Label(leftFrame, image=leftLogo)
leftLabel.pack()



employeeLogo = PhotoImage(file='P1employee.png')
employeeButton = Button(leftFrame, text='Employee', image=employeeLogo, compound=LEFT,height=55,font=('times new roman', 19,), bg='#AB886B', cursor='hand2', pady=2, anchor='w', padx=10,command=employee_form)
employeeButton.pack(fill=X)

supplierLogo = PhotoImage(file='P1agreement.png')
supplierButton = Button(leftFrame, text='Supplier', image=supplierLogo, compound=LEFT,height=55,font=('times new roman', 19), bg='#AB886B', cursor='hand2', pady=2, anchor='w', padx=10,command=supplier_form)
supplierButton.pack(fill=X)

categoryLogo = PhotoImage(file='P1categorization.png')
categoryButton = Button(leftFrame, text='Category', image=categoryLogo, compound=LEFT,height=55, font=('times new roman', 19), bg='#AB886B', cursor='hand2', pady=2, anchor='w', padx=10,command=category_form)
categoryButton.pack(fill=X)

productLogo = PhotoImage(file='P1product.png')
productButton = Button(leftFrame, text='Product', image=productLogo, compound=LEFT,height=55,font=('times new roman', 19), bg='#AB886B', cursor='hand2', pady=2, anchor='w', padx=10,command=product_form)
productButton.pack(fill=X)

salesLogo = PhotoImage(file='P1growth.png')
salesButton = Button(leftFrame, text='Sales', image=salesLogo, compound=LEFT,height=55, font=('times new roman', 19),bg='#AB886B', cursor='hand2', pady=2, anchor='w', padx=10, command=sales_form)
salesButton.pack(fill=X)

taxLogo = PhotoImage(file='tax.png')
taxButton = Button(leftFrame, text='Tax', image=taxLogo, compound=LEFT,height=55,font=('times new roman', 19), bg='#AB886B', cursor='hand2', pady=2, anchor='w', padx=10,command=enter_tax)
taxButton.pack(fill=X)

exitLogo = PhotoImage(file='P1exit.png')
exitButton = Button(leftFrame, text='Exit', image=exitLogo, compound=LEFT,height=55, font=('times new roman', 19),bg='#AB886B', cursor='hand2', pady=2, anchor='w', padx=10, command=exit)
exitButton.pack(fill=X)

# sections
# Total Employees Frame
emp_frame = Frame(window, bg='#F5F5F5', bd=3, relief=RIDGE)
emp_frame.place(x=400, y=175, height=170, width=280)

total_emp_image = PhotoImage(file='P1inside_icon_employee.png')
totalEmpImageLabel = Label(emp_frame, image=total_emp_image)
totalEmpImageLabel.pack()

totalEmployeesLabel = Label(emp_frame, text='Total Employees', font=('times new roman', 15, 'bold'), bg='#F5F5F5', fg='#3E3232')
totalEmployeesLabel.pack()

totalEmployeescountLabel = Label(emp_frame, text='0', font=('times new roman', 30, 'bold'), bg='#F5F5F5', fg='#3E3232')
totalEmployeescountLabel.pack()

# Total Suppliers Frame
sup_frame = Frame(window, bg='#F5F5F5', bd=3, relief=RIDGE)
sup_frame.place(x=700, y=175, height=170, width=280)

total_sup_image = PhotoImage(file='P1suppliers.png')
totalSupImageLabel = Label(sup_frame, image=total_sup_image)
totalSupImageLabel.pack()

totalSupplierLabel = Label(sup_frame, text='Total Suppliers', font=('times new roman', 15, 'bold'), bg='#F5F5F5', fg='#3E3232')
totalSupplierLabel.pack()

totalSuppliercountLabel = Label(sup_frame, text='0', font=('times new roman', 25, 'bold'),bg='#F5F5F5', fg='#3E3232')
totalSuppliercountLabel.pack()

# Total Categories Frame
cat_frame = Frame(window, bg='#F5F5F5', bd=3, relief=RIDGE)
cat_frame.place(x=1000, y=175, height=170, width=280)

total_cat_image = PhotoImage(file='P1cat.png')
totalCatImageLabel = Label(cat_frame, image=total_cat_image)
totalCatImageLabel.pack()

totalCategoryLabel = Label(cat_frame, text='Total Categories', font=('times new roman', 15, 'bold'), bg='#F5F5F5', fg='#3E3232')
totalCategoryLabel.pack()

totalCategorycountLabel = Label(cat_frame, text='0', font=('times new roman', 30, 'bold'),  bg='#F5F5F5', fg='#3E3232')
totalCategorycountLabel.pack()

# Total Products Frame
prod_frame = Frame(window, bg='#F5F5F5', bd=3, relief=RIDGE)
prod_frame.place(x=1000, y=360, height=170, width=280)

total_prod_image = PhotoImage(file='P1products.png')
totalProdImageLabel = Label(prod_frame, image=total_prod_image)
totalProdImageLabel.pack()

totalProductsLabel = Label(prod_frame, text='Total Products', font=('times new roman', 15, 'bold'),  bg='#F5F5F5', fg='#3E3232')
totalProductsLabel.pack()

totalProductscountLabel = Label(prod_frame, text='0', font=('times new roman', 30, 'bold'),  bg='#F5F5F5', fg='#3E3232')
totalProductscountLabel.pack()

# Total Sales Frame
sales_frame = Frame(window, bg='#F5F5F5', bd=3, relief=RIDGE)
sales_frame.place(x=400, y=360, height=170, width=280)

total_sales_image = PhotoImage(file='P1sales.png')
totalSalesImageLabel = Label(sales_frame, image=total_sales_image)
totalSalesImageLabel.pack()

totalSalesLabel = Label(sales_frame, text='Total Sales', font=('times new roman', 15, 'bold'),  bg='#F5F5F5', fg='#3E3232')
totalSalesLabel.pack()

totalSalescountLabel = Label(sales_frame, text='0', font=('times new roman', 30, 'bold'), bg='#F5F5F5', fg='#3E3232')
totalSalescountLabel.pack()

connection()
update_content()

window.mainloop()
