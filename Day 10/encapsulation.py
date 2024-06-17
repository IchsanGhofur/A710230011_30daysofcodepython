class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
    def set_salary(self, salary):
        self.__salary = salary
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_salary(self):
        return self.__salary
    
karyawan = Employee("Parmin", 24, 5000000)
print(karyawan.get_name())
print(karyawan.get_age())
print(karyawan.get_salary())
karyawan.set_name("Fatih")
karyawan.set_salary(5500000)
print(karyawan.get_name())
print(karyawan.get_salary())