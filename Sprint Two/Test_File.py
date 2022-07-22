#Test System using automated tests
import Driver
import Classes as C
import names
import Yelp_Fussion_Interface as API
import random


def accept_apt_calls(patient,mode="accepted",doc_list=False):
    Driver.create_priority(patient)                                                                        
    appointment = Driver.gather_available_appointments(patient)                                     
    suggested_apt = Driver.display_suggested_appointment(patient,appointment)                      

    days = ["monday","tuesday","wednesday","thursday","friday","saturday"]
    hours = ["8am","9am","10am","11am","12pm","1pm","2pm","3pm","4pm","5pm"]

    if mode == "rejected":          #rejected appointment
        if doc_list == True:            #display out of system docs
            Driver.display_local_doctors_list(patient,True,"yes")
        else:
            Driver.display_all_appointments(appointment)
            appointment.date = random.choice(days)
            appointment.time = random.choice(hours)
            Driver.create_appointment(suggested_apt)
    else:                           #accepted appointment
        Driver.create_appointment(suggested_apt,format="24hr")
    return appointment

def sched_apt_after(apt,sched=False):
    if sched == False:              #stop using system
        exit("System has been terminated")
    else:                           #print list of avail times - try to get an apt
        while (Driver.set_new_appointment(apt,Driver.display_all_appointments(apt)) == -1):
            print("Running again")
            continue

def unit_tests():
#Group 1: Mode of use
    #Test One
    print("Beginning Unit Test One...")
    patient = C.patient(names.get_full_name(),30,"Tetanus",False,"")                                 
    accept_apt_calls(patient)

    #Test 2:
    print("Beginning Unit Test Two...")
    Driver.display_doctor_schedule(6001)
    

    #Test 3: 
    print("Beginning Unit Test Three...")
    patient = C.patient(names.get_full_name(),30,"Diabetes",False,"")                                 
    accept_apt_calls(patient)


    #Test 4:
    print("Beginning Unit Test Four...")
    patient = C.patient(names.get_full_name(),22,"OCD",False,"")                                 
    accept_apt_calls(patient)


    #Test 5:
    print("Beginning Unit Test Five...")
    patient = C.patient(names.get_full_name(),40,"Coronary artery disease",False,"")                                 
    accept_apt_calls(patient)

    #Test 6:
    print("Beginning Unit Test Six...")
    patient = C.patient(names.get_full_name(),30,"Celiac disease",True,"")                                 
    accept_apt_calls(patient)

    #Test 7: 
    print("Beginning Unit Test Seven...")
    patient = C.patient(names.get_full_name(),30,"Celiac disease",False,"")                                 
    accept_apt_calls(patient)
    
    #Test 8:
    print("Beginning Unit Test Eight...")
    patient = C.patient(names.get_full_name(),30,"Celiac disease",False,"weight loss")                                 
    accept_apt_calls(patient)
    
    #Test 9:
    print("Beginning Unit Test Nine...")
    try:
        patient = C.patient(names.get_full_name(),60,"Celiac disease",False,["weight loss","severe abdominal pain"])                                 
        accept_apt_calls(patient,mode="rejected")
    except Exception as e:
        print("Unit Test Nine Failed")
        print(e)


def component_tests():              #component tests
    print("\n\n----------------Component Tests------------------")
    #Test 1
    try:
        print("Beginning Component Test One")
        #patient = C.patient(names.get_full_name(),"I dont remember","Schitzophrenia",False,["No, Im tired"])
        print("Inputs: ->  name, I dont remember, Schitzophrenia, False, No Im tired")   
        patient = Driver.user_input()                              
        accept_apt_calls(patient)
    except Exception as e:
        print("Component Test One Failed")
        print(e)

    #Test 2
    try:
        print("Beginning Component Test Two")
        patient = C.patient(names.get_full_name(),25,"Foot disorder",False,["No, Im tired"])                                 
        accept_apt_calls(patient)
    except Exception as e:
        print("Component Test Two Failed:\n Error = {}".format(e))


    #Test 3
    try:
        print("Beginning Component Test Three")
        patient = C.patient(names.get_full_name(),25,"Diabetes",False,"")             
        Driver.create_priority(patient)                                                                        
        appointment = Driver.gather_available_appointments(patient)   
        appointment.doctor_ID = 4830       
        appointment.doctor_speciality = "Family Doctor"                           
        suggested_apt = Driver.display_suggested_appointment(patient,appointment)                      
        Driver.create_appointment(suggested_apt,format="24hr")       
    except Exception as e:
        print("Component Test Three Failed: \n Error = {}".format(e))


    #Test 4
    try:
        print("Beginning Component Test Four")
        Driver.display_doctor_schedule(6001)
    except Exception as e:
        print("Component Test Four Failed: \n Error = {}".format(e))

    #Test 5
    try:
        print("Beginning Component Test Five")
        #patient = C.patient(names.get_full_name(),25,"Diabetes",False,"")  
        print("Inputs: name, 25, Diabetes, False, , -> Date:04/25/22 , Time:12:30pm ")
        patient = Driver.user_input()                               
        Driver.create_priority(patient)                                                                        
        appointment = Driver.gather_available_appointments(patient)                                     
        #appointment.date = "04/25/22"
        #appointment.time = "12:30pm"
        suggested_apt = Driver.display_suggested_appointment(patient,appointment)                      
        Driver.create_appointment(suggested_apt,format="24hr")
    except Exception as e:
        print("Component Test Five Failed: \n Error = {}".format(e))


    #Test 6 -> see list of local doctors then dont sched apt
    try:
        print("Beginning Component Test Six")
        patient = C.patient(names.get_full_name(),30,"Arrythmia",False,"")                                 
        apt = accept_apt_calls(patient,mode="rejected",doc_list=True)
        #sched_apt_after(apt,sched=False)
    except Exception as e:
        print("Component Test Six Failed: \n Error = {}".format(e))

    #Test 7 -> see list of local doctors then sched apt with in system doc
    try:
        print("Beginning Component Test Seven")
        patient = C.patient(names.get_full_name(),30,"Arrythmia",False,"")                                 
        apt = accept_apt_calls(patient,mode="rejected",doc_list=True)
        sched_apt_after(apt,sched=True)
    except Exception as e:
        print("Component Test Seven Failed: \n Error = {}".format(e))




def system_tests():                 #system tests
    print("\n\n----------------System Tests------------------")
    #Test 1
    try:
        print("Beginning System Test One")
        #patient = C.patient(names.get_full_name(),25,"Diabetes",False,"") 
        print("Inputs: name,25,Diabetes,False, -> Date=None, Time=17:00")
        patient = Driver.user_input()                                
        Driver.create_priority(patient)                                                                        
        appointment = Driver.gather_available_appointments(patient)                                     
        #appointment.date = "None"
        #appointment.time = "17:00"
        suggested_apt = Driver.display_suggested_appointment(patient,appointment)                      
        Driver.create_appointment(suggested_apt,format="24hr")
    except Exception as e:
        print("System Test One Failed: \n Error = {}".format(e))

    #Test 2
    try:
        print("Beginning System Test Two")
        #patient = C.patient(names.get_full_name(),25,"Diabetes",False,"")
        print("Inputs: name,25,Diabetes,False, -> Date=Monday, Time=None")
        patient = Driver.user_input()                                 
        Driver.create_priority(patient)                                                                        
        appointment = Driver.gather_available_appointments(patient)                                     
        #appointment.date = "Monday"
        #appointment.time = "None"
        suggested_apt = Driver.display_suggested_appointment(patient,appointment)                      
        Driver.create_appointment(suggested_apt,format="24hr")
    except Exception as e:
        print("System Test Two Failed: \n Error = {}".format(e))

    #Test 3
    try:
        print("Beginning System Test Three")
        patient = C.patient(names.get_full_name(),60,"Celiac disease",False,["weight loss","severe abdominal pain"])                                 
        Driver.create_priority(patient)                                                                        
        appointment = Driver.gather_available_appointments(patient)                                     
        appointment.date = "Monday"
        appointment.time = "10am"
        suggested_apt = Driver.display_suggested_appointment(patient,appointment)                      
        Driver.create_appointment(suggested_apt)
    except Exception as e:
        print("System Test Three Failed: \n Error = {}".format(e))

    #test 4 -> check if i can sched apt for unavailabe date/time
    try:
        print("Beginning System Test Four")
        patient = C.patient(names.get_full_name(),60,"Celiac disease",False,["weight loss","severe abdominal pain"])                                 
        Driver.create_priority(patient)                                                                        
        appointment = Driver.gather_available_appointments(patient)                                     
        appointment.date = "Friday"
        appointment.time = "10am"
        suggested_apt = Driver.display_suggested_appointment(patient,appointment)                      
        Driver.create_appointment(suggested_apt)
    except Exception as e:
        print("System Test Four Failed: \n Error = {}".format(e))

    #Test 5
    try:
        print("Beginning System Test Five")
        patient = C.patient(names.get_full_name(),60,"Celiac disease",False,"")                                 
        Driver.create_priority(patient)                                                                        
        appointment = Driver.gather_available_appointments(patient)                                     
        appointment.date = "Friday"
        appointment.time = "10am"
        suggested_apt = Driver.display_suggested_appointment(patient,appointment)                      
        Driver.create_appointment(suggested_apt)
    except Exception as e:
        print("System Test Five Failed: \n Error = {}".format(e))


    #Test 6 -> test API name input
    try:
        print("Beginning System Test Six")
        API.access_API("Invalid")
    except Exception as e:
        print("Component Test Six Failed: \n Error = {}".format(e))




def main():
    print("Beginning Tests...")
    unit_tests()
    component_tests()
    system_tests()
    print("\n\nFinished Testing System.")
if __name__ == "__main__":
    main()