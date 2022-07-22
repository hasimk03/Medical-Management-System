
import illnesses_dictionary as illness_dict

class patient:
    def __init__(self,name,age,illness,is_emergency,symptoms):
        self.name = name 
        self.age = age
        self.illness = illness
        self.is_emergency = is_emergency
        self.symptoms = symptoms
        self.priority = 0
        self.category = ""
        self.appointment = ""

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_illness(self):
        return self.illness

    def get_is_emergency(self):
        return self.is_emergency

    def get_symptoms(self):
        return self.symptoms

    def set_priority(self,input):
        self.priority = input
    
    def get_priority(self):
        return self.priority
    
    def get_category(self):
        if self.age < 12:
            self.category = 'pediatrics'
            return 'pediatrics'
        elif self.age > 64:
            self.category = 'Geriatrics'
            return 'Geriatrics'

        if self.illness in illness_dict.illness_classification_dict:
            self.category = illness_dict.illness_classification_dict[self.illness]
            return illness_dict.illness_classification_dict[self.illness]
        self.category = 'GP'
        return 'GP'

class doctor:
    #we have to choose a collection of doctors and store everything ourself in the DB
    #we will create n objects for n doctors hard programmed into the system
    #this class will be used to get  availability and make updates to it in DB
    def __init__(self,id,name,schedule,speciality, addy,num=0):
        self.id = id
        self.name = name
        self.schedule = schedule  #call get_avail()
        self.speciality = speciality
        self.office_address = addy

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_speciality(self):
        return self.speciality
    
    def get_office_address(self):
        return self.office_address
    

class illness:
    def __init__(self,category="None",symptoms = "",severity=0):
        self.category = category
        self.typical_symptoms = symptoms
        self.severity = severity

class appointment:
    def __init__(self,doctor,ID,speciality,addy,patient,date,time):
        self.doctor = doctor
        self.doctor_ID = ID
        self.doctor_speciality = speciality
        self.office_address = addy
        self.patient = patient 
        self.date = date
        self.time = time

#ignore these two classes for now -> focus on these in sprint two
class treatment:
    def __init__(self):
        #this shit has to be populated by sending requests to APIs ect
        self.type = ""
        self.illness_associated = ""
        self.direction = ""
        self.dosage = ""
        self.freq = ""
class medication:
    #same shit
    def __init__(self):
        self.type = ""
        self.illnesses_associated = ""
        self.directios = ""
        self.freq = ""
        self.importance = ""



def main():
    print("\nStart")

if __name__ == "__main__":
    main()