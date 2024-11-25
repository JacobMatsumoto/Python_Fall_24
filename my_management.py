"""File 1: Write an Employee class with the following attributes:

Employee name
Employee number
Create a subclass named ProductionWorker that inherits from Employee.
This subclass should include additional attributes:
Shift number (integer: 1 for day, 2 for night)
Hourly pay rate
Implement accessor and mutator methods (getters and setters) for each class.
Assignment Part 2: Implementing and Testing
Part 2: Write a script to:
Create an instance of ProductionWorker.
Prompt the user for each attribute's data.
Store and then display the data using the object's methods."""


class Employee:
    def __init__(self, name, employee_number):
        self.name = name
        self.employee_number = employee_number

    def get_name(self):
        return self.name

    def get_employee_number(self):
        return self.employee_number

    def set_name(self, value):
        self.name = value

    def set_employee_number(self, value):
        self.employee_number = value

    def __str__(self):
        return f"Employee\nName: {self.name} \nEmployee_number: {self.employee_number}"


class Production_Worker(Employee):

    def __init__(self, name, employee_number, shift_num, hourly_pay):
        super().__init__(name, employee_number)
        self.shift_num = shift_num
        self.hourly_pay = hourly_pay

    def get_shift_num(self):
        return self.shift_num

    def get_hourly_pay(self):
        return self.hourly_pay

    def set_shift_num(self, value):
        self.shift_num = value

    def set_hourly_pay(self, value):
        self.hourly_pay = value

    def __str__(self):
        return f"{super().__str__()} \nShift Number: {self.shift_num} \nHourly Pay: {self.hourly_pay}"


def main():
    # penelope_0990 = Production_Worker('Penelope', '0990', 1, '$19.25')
    # print(penelope_0990) this and value for penelope were for testing my formatting and it worked
    new_production_employee = Production_Worker(
        'Default', 'Default', 'Default', 'Default')
    setting_name = True
    setting_num = True
    setting_shift = True
    setting_pay = True
    while setting_name:
        try:
            employee_name = input("What is the employee's name? ").title()
            new_production_employee.set_name(employee_name)
            print("Name accepted")
            setting_name = False
        except:
            print("Please enter a valid name for the employee")

    while setting_num:
        try:
            employee_num = int(
                input("Please enter their 4 digit employee number "))
            if len(str(employee_num)) != 4:
                print("Please enter a valid employee number ex 0001 ")
                continue

            else:
                new_production_employee.set_employee_number(employee_num)
                print("Number accepted")
                setting_num = False

        except ValueError:
            print("Please enter a valid employee number ex 0001 ")

    while setting_shift:
        try:
            employee_shift = int(
                input("Enter the employee's shift number 1 or 2 "))
            if (employee_shift == 1 or employee_shift == 2):
                new_production_employee.set_shift_num(employee_shift)
                print("Shift set")
                setting_shift = False
            else:
                print("Please enter shift 1 or 2. 1 for day 2 for night")

        except ValueError:
            print("Please enter a '1' for day or '2' for night shift")

    while setting_pay:
        try:
            employee_pay = float(input("Please enter their hourly rate "))
            # https://pythonguides.com/python-print-2-decimal-places/ for formatting
            employee_pay = "{:.2f}".format(employee_pay)
            new_production_employee.set_hourly_pay(employee_pay)
            setting_pay = False

        except ValueError:
            print("Please enter their hourly rate example, 23.25")

    print(new_production_employee)


main()
