from employee import(
    add_employees,
    view_employee,
    search_name,
    search_department,
    update_salary,
    update_department,
    delete_employee,
    highest_salary,
    lowest_salary,
)

while True:
    print("\n========= Employees management system =========\n")
    print("1.add_employees")
    print("2.view_employee")
    print("3.search_name")
    print("4.search_department")
    print("5.update_salary")
    print("6.update_department")
    print("7.delete_employee")
    print("8.highest_salary")
    print("9.lowest_salary")
    print("10.exit")
    choice = input("Enter an choice :")

    if choice =="1":
        add_employees()
    elif choice == "2":
        view_employee()
    elif choice == "3":
        search_name() 
    elif choice=="4":
        search_department()
    elif choice =="5":
        update_salary()
    elif choice =="6":
        update_department()
    elif choice =="7":
        delete_employee()
    elif choice =="8":
        highest_salary()
    elif choice =="9":
        lowest_salary()
    elif choice == 10:
        print("Program ended.")
        break
    else :
        print("Invalid choice.")