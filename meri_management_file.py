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

    def set_employee_(self, value):
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


def main():  # sets up a new employee
    # penelope_0990 = Production_Worker('Penelope', '0990', 1, '$19.25')
    # print(penelope_0990) this and value for penelope were for testing my formatting and it worked
    employee_num = '23455'  # priming the whiles
    employee_shift = 3
    try:
        employee_name = input(
            "What is the employee's name? ").title()
        while len(str(employee_num)) != 4:
            employee_num = int(
                input("Please enter their 4 digit employee number "))
            if len(str(employee_num)) != 4:
                print("Invalid employee number")

        while employee_shift != 1 and employee_shift != 2:
            employee_shift = int(
                input("Enter the employee's shift number 1 or 2 "))
            if (employee_shift == 1 or employee_shift == 2):
                continue
            else:
                print("Please enter shift 1 or 2. 1 for day 2 for night")

        employee_pay = float(input("Please enter their hourly rate "))
        # https://pythonguides.com/python-print-2-decimal-places/ for formatting
        formated_employee_pay = "{:.2f}".format(employee_pay)

    except Exception as e:
        print(e)

    new_production_employee = Production_Worker(
        employee_name, employee_num, employee_shift, formated_employee_pay)

    print(new_production_employee)


main()
# I ended up using https://pythonguides.com/python-print-2-decimal-places/ for formatting
# and fixed the original as well. I didn't know if i should upload this one or the original
# i can simplify that one up and submit it instead if that is preferable
