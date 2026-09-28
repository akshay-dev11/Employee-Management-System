from database import get_connection

def add_employees():
    name = input("Enter a name: ")
    email = input("Enter an email: ")
    phone = int(input("Enter a phone number: "))
    department = input("Enter a department: ")
    salary = int(input("Enter salary: "))

    connection = get_connection()
    pen = connection.cursor()

    pen.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            name VARCHAR(150),
            email VARCHAR(120),
            phone VARCHAR(15),
            department VARCHAR(150),
            salary INT
        )
    """)

    query = """
        INSERT INTO employee (name, email, phone, department, salary)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (name, email, phone, department, salary)

    pen.execute(query, values)
    connection.commit()

    print("Employee successfully added")

    pen.close()
    connection.close()

def view_employee():
    connection =get_connection()
    pen = connection.cursor()

    query ="SELECT * from employee" 
    pen.execute(query)

    employees=pen.fetchall()

    if len(employees) == 0:
        print("No employees in the table")
    else :
        for employee in employees:
            print(employee)
    pen.close()
    connection.close()

def search_name():
    connection =get_connection()
    pen = connection.cursor()

    choice =input("Search by name :")

    if choice == "1":
        name = input("Enter an name :")

        query ="SELECT  * from employee where name like %s"
        values =(name,)
        pen.execute(query,values)
        employees=pen.fetchall()
        if len(employees) == 0:
            print("Employees not found")
        else :
            for employee in employees:
                print(employee)
    pen.close()
    connection.close()

def search_department():
    connection =get_connection()
    pen = connection.cursor()

    choice = input("Search the department :")

    if choice == "1":
        department = input("Enter an department :")

        query ="SELECT * from employee where department like %s"
        value =(department,)
        pen.execute(query,value)

        employees =pen.fetchall()
        if len(employees) == 0:
            print("department cannot be found")
        else :
            for employee in employees:
                print(employee)
    else :
        print("Invalid choice")
    pen.close()
    connection.close()

def update_salary():
    connection =get_connection()
    pen =connection.cursor()

    name = input("Enter an employee name :")
    salary = int(input("Enter an salary :"))

    query ="""
    UPDATE employee SET salary = %s WHERE name = %s 
    """
    values=(salary,name)
    pen.execute(query,values)
    connection.commit()
    if pen.rowcount == 0:
        print("Employee not found")
    else :
        print("Salary will be updated")
    pen.close()
    connection.close()

def update_department():
    connection =get_connection()
    pen=connection.cursor()

    name = input("Enter an name :")
    department =input("enter an department :")

    query ="""
    UPDATE  employee SET department = %s where name =%s
    """
    values =(department,name)
    pen.execute(query,values)
    connection.commit()
    if pen.rowcount == 0:
        print("Employee not found")
    else :
        print("Department will be updatedd")
    pen.close()
    connection.close()

def delete_employee():
    connection =get_connection()
    pen=connection.cursor()

    name = input("Enter an name :")
    query ="""
    DELETE from employee where name = %s
    """
    value =(name,)
    pen.execute(query,value)
    connection.commit()
    if pen.rowcount == 0:
        print("employee not found")
    else :
        print("Employee can be deleted")
    pen.close()
    connection.close()

def highest_salary():
    connection =get_connection()
    pen =connection.cursor()

    query ="""
    SELECT  max(salary) FROM employee
    """
    pen.execute(query)

    result = pen.fetchone()
    if result[0] is None:
        print("No employees found ")
    else :
        print("Heighest salary :",result[0])
    pen.close()
    connection.close()

def lowest_salary():
    connection =get_connection()
    pen = connection.cursor()

    query ="""
    SELECT min(salary) from employee
    """
    pen.execute(query)

    result=pen.fetchone()
    if result[0] is None:
        print("Employee not found")
    else :
        print("Lowest salary :",result[0])
    pen.close()
    connection.close()