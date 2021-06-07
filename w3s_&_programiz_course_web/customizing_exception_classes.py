class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)


# Enter salary amount: 2000
# Traceback (most recent call last):
#   File "<string>", line 17, in <module>
#     raise SalaryNotInRangeError(salary)
# __main__.SalaryNotInRangeError: Salary is not in (5000, 15000) range

#https://www.programiz.com/python-programming/user-defined-exception