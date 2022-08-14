class StudentInfo:
    def __init__(self, id, name, address, subject):
        self.id = id
        self.name = name
        self.address = address
        self.subject = subject   
        
class Address:
    def __init__(self, no, street, city, code):
        self.no = no
        self.street = street
        self.city = city
        self.postalCode = code
        
        
add1 =  Address(15, 'Binh Loi', 'HCMC', 70000)
sub_math = {"math" : 10}
student_1 = StudentInfo(12345, 'Hung', add1, sub_math)

print(student_1.subject["math"])