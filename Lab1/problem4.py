# Hospital Admission Managemnt System by Raju Nekadi


# Defing various classes like Hospital, Patient , Doctors , Staff, Procedure one by one along with there functionality


# Hospital Class with name and address public data attribute


class Hospital:

    def __init__(self, n, a):
        self.hname = n

        self.haddress = a


# Dental Procedure class with procedure name , procedure code , procedure fee detailes


class Procedure:

    def __init__(self, pcode, pname, pfee):
        self.procedure_name = pname

        self.procedure_code = pcode

        self.procedure_fee = pfee


# Patient class with name, address, gender and dental procedure details extended from class procedure and hospital


class Patient(Hospital, Procedure):  # Multiple inheritance

    total_patient = 0  # class attribute for counting number of in hospital

    def __init__(self, pid, pname, page, phname, paddress, pcode, pcname, pfee):
        super(Patient, self).__init__(phname, paddress)  # Super class Hospital call for Patient Class

        Procedure.__init__(self, pcode, pcname, pfee)  # Call for __int__ Procedure

        self.__patient_id = pid  # Defining patient ID as private

        self.patient_name = pname

        self.patient_age = page

        self.__class__.total_patient += 1  # Incrementing Patient Class by 1

    def patient_display(self):
        print('Patient Name:', self.patient_name, 'Denatl Procedure Undergone:',

              self.procedure_name, 'Fee paid of $', self.procedure_fee)

    def getpatient_id(self):  # Function to return Private Patient ID
        return self.__patient_id


# Hospital Staff Class with Staff ID and Staff Type


class Staff(Hospital):

    def __init__(self, scode, stype, hname, haddress):
        super(Staff, self).__init__(hname, haddress)

        self.staff_code = scode

        self.staff_type = stype


# Doctor Class


class Doctor(Staff):  # Multilevel Inheritance logic implemented here

    total_doctor = 0  # Class attribute for counting number of doctors

    def __init__(self, did, name, qual, city, spec, scode, stype, hname, haddress):

        super(Doctor, self).__init__(scode, stype, hname, haddress)  # Call to base class Staff using supre method

        self.__doc_id = did  # Defining Doctor ID as Private data member

        self.doc_name = name

        self.doc_qual = qual

        self.doc_city = city

        self.doc_specaility = spec

        self.__class__.total_doctor += 1  # Incrementing Doctor Count by 1

    def doctor_display(self):
        print('Doctor Name :', self.doc_name, 'Qualification:', self.doc_qual,

              'Specaility:', self.doc_specaility, 'Hospital', self.hname)

    def getdoctor_id(self):  # Function to return private Doctor ID
        return self.__doc_id


# Nurse Class


class Nurse(Staff):
    total_nurse = 0  # Class attribute for counting number of Nurses

    def __init__(self, nid, name, age, qual, city, scode, stype, hname, haddress):
        super(Nurse, self).__init__(scode, stype, hname, haddress) # Call to base class using super method

        self.__nurse_id = nid

        self.nurse_name = name

        self.nurse_qual = qual

        self.nurse_city = city

        self.nurse_age = age

        self.__class__.total_nurse += 1  # incrmenting nurse Count by one

    def display_nurse(self):
        print('Nurse Name: ', self.nurse_name, 'Nurse Qualification :', self.nurse_qual,
              'Hospital:', self.hname)

    def getnurse_id(self):
        return self.__nurse_id


# Driver Program

if __name__ == "__main__":

    # Creating patient Class Object
    p1 = Patient(1, 'Raju Nekadi', 30, 'ABC', '6100 fsoter St', 'D5992',

                 'Tooth Cleansing', 200)

    p1.patient_display()  # Patient Display method call

    print('Patient ID:', p1.getpatient_id())

    # Creating Doctor Class object
    d1 = Doctor(1, 'Swati Singh', 'Dental M.D', 'Kansas City', 'Dentist', 100, 'Doctors', 'ABC', '6100 fsoter St')

    d1.doctor_display()  # Doctor Display Method Call

    print('Doctor ID:', d1.getdoctor_id())

    # Creating nurse Class Object
    n1 = Nurse(1, 'Mary Jane', '28', 'Health Science', 'Kansas City', 200, 'Nurse', 'ABC', '6100 Foster St')

    n1.display_nurse()  # Nurse Display Method Call

    print('Nurse ID:', n1.getnurse_id())


