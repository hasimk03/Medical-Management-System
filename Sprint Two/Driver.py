#Developed by Hasim Khawaja 

import sqlite3
import os
import illnesses_dictionary as illness_dict
import Classes as C
import re
import names
import doctor as D
import Yelp_Fussion_Interface as API 

def set_mode():
    #set mode to patient or doctor -> create patient or doctor obj
    inp = input("Are you a doctor\n>>>")
    mode = (True if inp == "yes" or inp == "Yes" else False)                    #False = Patient mode -> def: Patient mode
    print("***Patient Mode***" if mode==False else "***Doctor Mode***")
    return mode


#Gather all inputs from user -> fix input parsing -> make it more reliable
def user_input():
    name = input("What is your name?\n>>>")                                     #store user name -> can be anything
    doctor_ID = 0
    curr_illness = ""
    symptoms = []
    num_symptoms = 0
    age = 0

    while True:
        try:
            age = int(input("How old are you?\n>>>"))
            break
        except:
            print("Your age must be an integer. Please re-enter your age")



    curr_illness = input("What illness are you facing?\n>>>")   

    if curr_illness not in illness_dict.illness_classification_dict.keys():
        curr_illness = "Other"
    
    print("Illness = ",curr_illness)


    is_urgent = (input("Is it an emergency?\n>>>"))

    if re.match("y",is_urgent.lower()):
        is_emergency = True
    else:
        is_emergency= False

    while True:
        try:
            num_symptoms = int(input("How many symptoms do you have?\n>>>"))
            break
        except:
            print("The number of symptoms you entered is invalid. Please re-enter the number of symptoms you are experiencing")

    #symptoms = [] * num_symptoms
    for i in range(num_symptoms):
        if i==0:
            val = "1st"
        elif i==1:
            val = "2nd"
        elif i==2:
            val = "3rd"
        else:
            val = str(i+1)+"th"
        symptoms.append(input("What is your {} symptom\n>>>".format(val)))
    #register patient = create patient object -> store into the DB
    patient_ob = C.patient(name,age,curr_illness,is_emergency,symptoms)                      #create patient object to store inputs
    
    return patient_ob

#def check_db_exists(filename):
    #return os.path.exists('filename')

def display_doctor_schedule(ID=0):
    print(ID)
    while True and ID==0:
        try:
            ID = int(input("what is your ID?\n>>>"))
            break
        except:
            print("The ID you entered is invalid. Please re-enter your age\n>>>")

    valid_ID = [1001,1002,1003,1004,2001,2002,2003,3001,3002,3003,4001,4002,4003,4004,5001,5002,5003,6001,6002,6003,6004,7001,7002,1010]
    while ID not in valid_ID:
        ID = int(input("The ID you entered could not be found in the database.Please re-enter your ID\n>>>"))

    #else -> use ID from user
    connection = sqlite3.connect("doctor_database.db")
    cursor = connection.cursor()

    query = """SELECT  
        M8,M9,M10,M11,M12,M13,M14,M15,M16,M17,
        T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,
        W8,W9,W10,W11,W12,W13,W14,W15,W16,W17,
        Th8,Th9,Th10,Th11,Th12,Th13,Th14,Th15,Th16,Th17,
        F8,F9,F10,F11,F12,F13,F14,F15,F16,F17,
        S8,S9,S10,S11,S12,S13,S14,S15,S16,S17
        
        FROM Doctor_Table WHERE id={}""".format(ID)

    cursor.execute(query)
    scheddy = cursor.fetchall()
    cursor.execute("SELECT name FROM Doctor_Table Where id = {}".format(ID))
    doc_name = cursor.fetchall()

    counter=0
    index=0
    days_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    
    print("Hello {}, Here is your schedule for this week :)".format(doc_name[0]))
    #print("Monday:")

    num =0
    for k in range(len(scheddy[0])):
        print("Monday") if k==0 else None
        if counter == 10:                           #9hours per day -> reset to new day if hour==10
            counter = 0
            index += 1
            print("----------------------")
        if scheddy[0][k] == 0:               #if hour j+8 is available
            #query to get patient_name -> select name based on date and time from appointments table and r
            day = days_of_week[index]
            #cursor.execute("SELECT patient_name FROM Appointments WHERE date={0} AND time]{1}".format(day,time))  #########FIX THIS -> ADD PATIENT NAME TO DOCTOR SCHEDULE
            #if counter == 4:
                #print("Lunch",day+", at 12pm")
            if counter > 4:
                print("Appointment with parent on",day+", at "+str(counter-4)+"pm")
                num +=1
            elif counter < 4:
                print("Appointment with patient on",day+", at "+str(counter+8)+"am")
                num +=1
        counter += 1
    if num==0:
        print("No patients this week!")
    #save and close DB
    connection.commit()
    cursor.close()
    connection.close()

def create_priority(patient):
    count =0                                                            #priority index
    age = patient.get_age()
    symptoms = patient.get_symptoms()
    category = patient.get_category()
    emergency = patient.get_is_emergency()

#add x to priority index (count) - based upon the risk of the patients age -> high/low age = highest risk
    if (age <2):                                            #Baby patient -> highest risk
        count += 10
    elif age < 4:                                           #toddler patient
        count += 9
    elif age < 12:                                          #child patient
        count += 6
    elif age < 17:                                          #adolescent patient
        count += 4
    elif age < 22:                                          #young adult 
        count += 3
    elif age < 32:                                          #young patient - 20s -> lowest risk
        count += 1
    elif age <40:                                           #early middle ages - 30s
        count += 2
    elif age < 55:                                          #middle aged 40s-mid 50s
        count += 5
    elif age < 65:                                          #early old age
        count += 7
    elif age < 85:                                          #old age 65-85
        count += 8
    elif age > 84:                                          #extreme old age - 85+ -> highest risk
        count += 10
#classification of difference in priority of different illness categories
    category_list_one = ['Neurosurgery','Cardiology','Respiratory','Neurology']
    category_list_two = ['Infectious Disease','Immunology','Gastro','Vascular','Rheumatology','Ophthalmology']
    category_list_three = ['Pediatrics','Geriatrics','Haematology','Endocrinology','Urology','Renal','Orthopaedics']
    category_list_four = ['GP','ENT','OB/GYN','Psychiatry']
    category_list_five = ['Sexual Health','Genetics','Dermatology']

#vary amt to increase priority index by - dependent on classification of patient's illness
    if (emergency==True):                                       #emergency situation 
        count += 40
    elif category in category_list_one:                         #highest priority categories
        count += 38
    elif category in category_list_two:                         #2nd highest priority categories
        count += 30
    elif category in category_list_three:                       #3rd highest priority categories
        count += 20
    elif category in category_list_four:                        #4th highest priority categories
        count +=15
    elif category in category_list_five:                        #5th highest priority catgories
        count += 5
        
    #print("AFTER CATEGORY COUNT===",count)         ###############################
#classification of severity of symptoms by keyword strings
    symptoms_1 = ["chocking","coughing up blood","vomiting blood","heart palpitation"]
    symptoms_2 = ["Bleeding wont stop","difficulty breathing","confusion","chest pain","loss of consciousness",
    "fainting","severe vomiting", "severe pain","severe abdominal pain","sudden dizziness","blood in stool"]
    symptoms_3 = ["high fever","weight loss","weight gain","fecal incontinence","urinary incontinence","cant pee","cant pass stool",
    "fatigue","vomitting",]

    n = len(symptoms)
    control = 0
#Increase priority index by x, depending on severity of symptoms  ####NEEDS TO BE FIXED
    for x in symptoms:                                                                                  #run thru all input symptoms
        r = re.compile(x)
        for word in symptoms_1:                                                                         #if symptom is contained in list_1
            if re.search(word,x):
                count +=50/n
                control += 1
                break
        if control ==1:
            control = 0
            continue
        for word in symptoms_2:                                                                         #if symptom is containeed in list_2
            if re.search(word,x):
                count += 42/n
                control += 1
                break
        if control ==1:
            control = 0
            continue
        for word in symptoms_3:                                                                         #if symptom is contained in list_3    
            if re.search(word,x):
                count += 25/n
                control += 1
                break
        if control ==1:
            control = 0
            continue
        count += 12/n

    patient.set_priority(count)                                                                         #update priority for patient object


def register_patient(patient,delete_table=False):                                               #register patient in sql table
    connection =sqlite3.connect("patient_database.db")                                    #create connection to sql server via filename
    cursor = connection.cursor()                                                    #points to diff blocks of sql table

    cursor.execute('CREATE TABLE IF NOT EXISTS TEST3 (name,illness,category,priority)')      #SQL Query to create table if !exist
    if delete_table == True:
        cursor.execute("DROP TABLE TEST3")
        return

    cursor.execute("INSERT INTO TEST3 (name,illness,category,priority) VALUES (?,?,?,?)",(patient.get_name(),patient.get_illness(),patient.get_category(),patient.get_priority()))     #insert new user_input into DB
    connection.commit()                                                             #commit changes to DB
    
    #methods ends by giving us table of names of patients and illnesses for now -> age, symptoms,ect... to be added later
    
    cursor.close()                                                                      #close cursor
    connection.close()                                                                  #end connection


def update_table():
    connection =sqlite3.connect("patient_database.db")                                    #create connection to sql server via filename
    cursor = connection.cursor()                                                    #points to diff blocks of sql table
    #cursor.execute('ALTER TABLE TEST3 ADD priority_index ')
    cursor.close()
    connection.close()

def gather_available_appointments(patient):
    category = patient.get_category()
    doctor_list = D.create_static_doctor_objects()
    apt = C.appointment("Fake",0,"None","DNE","Faker","Mon","0:00")

    #open up the DB


    counter=0
    index=0
    days_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]


    #Monday    = [0:9]
    #Tuesday   = [10:19]
    #Wednesday = [20:29]
    #Thursday  = [30:39]
    #Friday    = [40:49]
    #Saturday  = [50:59]

#For now use the created objects
    for doctor in doctor_list:
        if re.search(doctor.get_speciality(),category):
            conn = sqlite3.connect("doctor_database.db")
            cursor = conn.cursor()
            #Grab schedule for Table
            cursor.execute("""SELECT  
            M8,M9,M10,M11,M12,M13,M14,M15,M16,M17,
            T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,
            W8,W9,W10,W11,W12,W13,W14,W15,W16,W17,
            Th8,Th9,Th10,Th11,Th12,Th13,Th14,Th15,Th16,Th17,
            F8,F9,F10,F11,F12,F13,F14,F15,F16,F17,
            S8,S9,S10,S11,S12,S13,S14,S15,S16,S17
            FROM Doctor_Table WHERE id = {}""".format(doctor.get_id()))

            sched = cursor.fetchall()                   #grab list of hours
            scheddy = sched[0]                          
            num = group_patient(patient.get_priority()) #get priority of patient
            #close this shit
            conn.commit()
            cursor.close()
            conn.close()
            #For monday
            if num in range(1,3):
                for j in range(0,9):                                        #run thru all hours of doctors work day
                    if (scheddy[j] == True):                     #if doctor has free times during the inputted time
                        #doctor.schedule.Monday().list[j] = False                       #update doctor availability
                        patient.appointment = "Mon, "+str(j+8)+":00, "+"With"+doctor.get_name()
                        apt = C.appointment(doctor.get_name(),doctor.get_id(),doctor.get_speciality(),doctor.get_office_address(),patient.get_name(),date="Monday",time = str(j+8)+":00")
                        #create_appointment(apt,format="24hr")
                        return apt

            elif num in range(3,6):
                for j in range(0,9):
                    if scheddy[j] ==True:
                        #if doctor.schedule.Monday().list[j] ==True:
                        #doctor.schedule.Monday().list[j] = False
                        patient.appointment = "Mon, "+str(j+8)+":00, "+"With"+doctor.get_name()
                        apt = C.appointment(doctor.get_name(),doctor.get_id(),doctor.get_speciality(),doctor.get_office_address(),patient.get_name(),date="Monday",time = str(j+8)+":00")
                        #create_appointment(apt,format="24hr")
                        return apt

                for j in range(10,19):
                    if scheddy[j]==True:       
                        #doctor.schedule.Tuesday().list[j] = False
                        patient.appointment = "Tues, "+str(j-2)+":00, "+"With"+doctor.get_name()
                        apt = C.appointment(doctor.get_name(),doctor.get_id(),doctor.get_speciality(),doctor.get_office_address(),patient.get_name(),date="Tuesday",time = str(j-2)+":00")
                        #create_appointment(apt,format="24hr")
                        return apt


            elif num in range(6,8):                
                for j in range(10,19):
                    if scheddy[j] ==True:
                        #doctor.schedule.Tuesday().list[j] = False
                        patient.appointment = "Tues, "+str(j-2)+":00, "+"With"+doctor.get_name()
                        apt = C.appointment(doctor.get_name(),doctor.get_id(),doctor.get_speciality(),doctor.get_office_address(),patient.get_name(),date="Tuesday",time = str(j-2)+":00")
                        #create_appointment(apt,format="24hr")
                        return apt


                for j in range(20,29):
                    if scheddy[j]==True:
                        #doctor.schedule.Wednesday().list[j] = False
                        patient.appointment = "Wed, "+str(j-12)+":00, "+"With"+doctor.get_name()
                        apt = C.appointment(doctor.get_name(),doctor.get_id(),doctor.get_speciality(),doctor.get_office_address(),patient.get_name(),date="Wednesday",time = str(j-12)+":00")
                        #create_appointment(apt,format="24hr")
                        return apt

            elif num in range(8,10):
                for j in range(30,39):
                    if scheddy[j]==True:
                        #doctor.schedule.Thursday().list[j] = False
                        patient.appointment = "Thurs, "+str(j-22)+":00, "+"With"+doctor.get_name()
                        apt = C.appointment(doctor.get_name(),doctor.get_id(),doctor.get_speciality(),doctor.get_office_address(),patient.get_name(),date="Thursday",time = str(j-22)+":00")
                        #create_appointment(apt,format="24hr")
                        return apt


                for j in range(40,49):
                    if scheddy[j]==True:
                        #doctor.schedule.Friday().list[j] = False             
                        patient.appointment = "Fri, "+str(j-32)+":00, "+"With"+doctor.get_name()
                        apt = C.appointment(doctor.get_name(),doctor.get_id(),doctor.get_speciality(),doctor.get_office_address(),patient.get_name(),date="Friday",time = str(j-32)+":00")
                        #create_appointment(apt,format="24hr")
                        return apt

            else:
                for j in range(50,59):
                    if scheddy[j] ==True:
                        #doctor.schedule.Saturday().list[j] = False                        
                        patient.appointment = "Sat, "+str(j-42)+":00, "+"With"+doctor.get_name()
                        apt = C.appointment(doctor.get_name(),doctor.get_id(),doctor.get_speciality(),doctor.get_office_address(),patient.get_name(),date="Saturday",time = str(j-42)+":00")
                        #create_appointment(apt,format="24hr")
                        return apt
    return apt

    #For now use the created objects

    #use category of ilness and find all doctors in that speciality
    #grab each doctors schedule -> add them together and store all available appointments/times over next x num days

def group_patient(priority):
    if priority >= 90:
        if priority >= 95:
            return 1
        elif priority >=90:
            return 2
    elif priority >=65:
        if priority >=82:
            return 3
        elif priority >=72:
            return 4
        else:
            return 5
    elif priority >=40:
        if priority >=55:
            return 6
        return 7
    elif priority >=20:
        if priority >=30:
            return 8
        return 9
    return 10


def display_suggested_appointment(patient,apt):                      #display all available apointments -> will grab data from gather_available_appointments()
    #cant call apt.doctor -> have to pull this information from the database
    
    print("Suggested Appointment:")
    print("  Doctor: ",apt.doctor)
    print("  Doctor ID: ",apt.doctor_ID)
    print("  Speciality: ",apt.doctor_speciality)
    print("  Date: ",apt.date)
    print("  Time: ",apt.time)
    print("  Location: ",apt.office_address)

    return apt

def display_all_appointments(apt):
    doctor_id = apt.doctor_ID                          #grab ID from inputted doctor object 
    
    conn = sqlite3.connect("doctor_database.db")
    cursor = conn.cursor()

    #cursor.execute("SELECT id from Doctor_Table")
    
    #cursor.execute("SELECT * FROM Doctor_Table WHERE id=7001")
    cursor.execute("""SELECT  
    M8,M9,M10,M11,M12,M13,M14,M15,M16,M17,
    T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,
    W8,W9,W10,W11,W12,W13,W14,W15,W16,W17,
    Th8,Th9,Th10,Th11,Th12,Th13,Th14,Th15,Th16,Th17,
    F8,F9,F10,F11,F12,F13,F14,F15,F16,F17,
    S8,S9,S10,S11,S12,S13,S14,S15,S16,S17
    
    FROM Doctor_Table WHERE id = {}""".format(doctor_id))
    #cursor.execute("SELECT M9 FROM Doctor_Table WHERE id = {}".format(doctor_id))
    
    schedule_tuple = cursor.fetchall()
    
    counter=0
    index=0
    days_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    
    print(apt.doctor + "is available at the following days and times:")
    print("Monday:")
    for k in range(len(schedule_tuple[0])):
        if counter == 10:                           #9hours per day -> reset to new day if hour==10
            counter = 0
            index += 1
            print("----------------------")
            #print(days_of_week[index])
        if schedule_tuple[0][k] == 1:               #if hour j+8 is available
            #print("VAL=1")
            if counter == 4:
                print(days_of_week[index]+", 12pm")
            elif counter > 4:
                print(days_of_week[index]+", "+str(counter-4)+"pm")
            else:
                print(days_of_week[index]+", "+str(counter+8)+"am")
        counter += 1

    #close this shit
    conn.commit()
    cursor.close()
    conn.close()
    return schedule_tuple[0]

def set_new_appointment(apt,doc_sched):                       #sets the new appointment - done by calling set appointment method
    selected_day = input("What day would you like to schedule your appointment for?\n>>>")
    valid_days = ["mon","tue","wed","thur","fri","sat"]
   
    while selected_day[0:3].lower() not in valid_days:        #check if inputted day = valid
        selected_day = input("The day you entered is invalid. Please re-enter the day you would like to schedule the appointment for\n>>>")


    selected_time = input("What time would you like to schedule your appointment for?\n>>>")
    valid_times = ["8am","9am","10a","11a","12p","1pm","2pm","3pm","4pm","5pm"]
    
    while selected_time[0:3].lower() not in valid_times:      #check if inputted time = valid
        selected_time = input("The time you entered is invalid. Please re-enter the time you would like to schedule the appointent for\n>>>")

    j = 0
    const = 0
    for i in range(len(valid_days)):
        if selected_day[0:3] == valid_days[i]:
            j = i
            break
    
    #mon = [0,9] and sat = [50,59]
    if len(selected_time)==3:
        if "am" in selected_time:
            const = int(selected_time[0])-8
        elif "pm" in selected_time:
            const = int(selected_time[0]) + 4
    else:                                   #10am,11am,12pm or invalid input
        const = int(selected_time[0:2]) - 8

    index = (j*10) + const

    if doc_sched[index] == 0:               #already scheduled
        print("The appointment you selected is unavailable. Please select a new day and time")
        return -1

    #update appointment object
    selected_appointment = apt
    selected_appointment.date = selected_day
    selected_appointment.time = selected_time

    print("Appointment has been set. Uploading into Database...")
    create_appointment(apt)
    return 0

def create_appointment(apt,delete_table=False,format=""):                         #add decided on appointment into database 
    #create appointment database with patient Name
    conn = sqlite3.connect("doctor_database.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Appointments (
    patient_name,
    doctor_name,
    doctor_id,
    doctor_speciality,
    doctor_address,
    date,
    time
    )""")

    #print("Appointments table created")###########
    cursor.execute("INSERT INTO Appointments (patient_name,doctor_name,doctor_id,doctor_speciality,doctor_address,date,time) VALUES (?,?,?,?,?,?,?)",(apt.patient,apt.doctor,apt.doctor_ID,apt.doctor_speciality,apt.office_address,apt.date,apt.time))


    s = apt.time
    num=0

    if format == "24hr":                    #creating appointment from suggested appointment -> in 24hr format
        if len(s) == 4:
            num = s[0]
        else:
            num = s[0:2]
    else:                                   #Creating appointment from selected appointment
        #convert am pm to 24hr
        if s.__contains__("p" or "P"):      #PM
            if len(s)==3:                   #0-9pm
                num = int(s[0])             #get first char -> convert to int
            else:                           #10-12pm
                num = int(s[0:2])        #get first two  chars -> convert to int
            num += 12
        else:                               #AM
            if len(s)==3:                   #8-9am
                num = int(s[0])
            else:
                try:
                    num = int(s[0:2])
                except ValueError:
                    print("s=",s)

    if apt.date[0:2].lower() == "th":                   #edge case -> thursday input
        day = apt.date[0].upper()+apt.date[1].lower()   #Th
    else:                                               #Normal case -> any day except Thurs
        day = apt.date[0].upper()


    column = day+str(num)
    update = '''
    UPDATE Doctor_Table 
    SET {0} = False
    WHERE id = {1}
    '''.format(column,apt.doctor_ID)

    cursor.execute(update)    #update correct column with new appointment
    
    
    #cursor.execute("INSERT INTO Appointments (patient_name,doctor_name) VALUES (?,?)",apt.patient,apt.doctor)

    if delete_table == True:
        cursor.execute("DROP TABLE TEST3")
        print("Appointments table deleted!")
        return

    #methods ends by giving us table of names of patients and illnesses for now -> age, symptoms,ect... to be added later
    #cursor.execute("SELECT * from Appointments")
    #print(cursor.fetchall())  

    #close this shit
    conn.commit()
    cursor.close()
    conn.close()

    display_appt_info(apt)

def display_appt_info(apt):                                #grab all info about appointment from appointment object -> display relevant info to user
    #display all this shit to the user
    #use object to display this stuff
    #print("ee{0}".format("f"))

    print("""\nAppointment Information:
    Patient Name: {0}
    Doctor Name: {1}
    Doctor ID: {2}
    Doctor's Specialization: {3}
    Office Address: {4}
    Day of appointment: {5}
    Appointment Time: {6}
    """.format(apt.patient,apt.doctor,apt.doctor_ID,
    apt.doctor_speciality,apt.office_address,apt.date,apt.time))


def testing_mode():
    patient = C.patient(names.get_full_name(),30,"Diabetes",False,["weight loss","tired"])
    create_priority(patient)
    delete_table = bool(input("Delete Table? Enter 1 for yes\n>>>"))

    if delete_table ==1:
        register_patient(patient,True)
        return

    register_patient(patient)
    appoint = gather_available_appointments(patient)
    suggested_apt = display_suggested_appointment(patient,appoint)

    select = input("Would you like to select this appointment\n>>>")
    if re.match("n",select.lower()):                                        #if user decides to accept/reject appointment
        accept = False
        doc_schedule = display_all_appointments(appoint)                #display all possible appointments with that doctor over a week
        while (set_new_appointment(appoint,doc_schedule) == -1):
            print("Running again")
            continue
    else:
        accept = True
        create_appointment(suggested_apt,format="24hr")
        #create appointment -> store in DB

def display_local_doctors_list(patient, test_mode=False,disp=""):
    if test_mode == False:
        disp = input("Would you like to see a list of available out of system doctors?\n>>>")

    if re.match("y",disp.lower()):
        category = patient.get_category()
        doctor_dict = API.access_API(category)

        print("----------------List of out of system Doctors-----------------")
        for i in range(len(doctor_dict['businesses'])):
            print("Doctor {}".format(i+1))
            print("   Office: ",doctor_dict['businesses'][i]['name'])
            print("   Phone-Number: ",doctor_dict['businesses'][i]['phone'])
            print("   Address: ",doctor_dict['businesses'][i]['location']['address1'],"",doctor_dict['businesses'][i]['location']['city'],"",doctor_dict['businesses'][i]['location']['state'])


def main():
    print("\nStarting up...")

    test = bool(input("Enter 1 for Testing mode\n>>>"))
    if test == 1:
        testing_mode()
        exit(0)

    #doctor mode
    if set_mode() == True:
        display_doctor_schedule()
        exit()

    #patient mode
    patient = user_input()
    create_priority(patient)
    appointment = gather_available_appointments(patient)
    suggested_apt = display_suggested_appointment(patient,appointment)

    select = input("Would you like to select this appointment\n>>>")                    #only denies selection if input 1st char == N or n


    if re.match("n",select.lower()):                                        #if user decides to reject appointment
        display_local_doctors_list(patient)
        if re.match("n",input("Would you like to schedule an appointment with an in-system doctor?\n>>>").lower()):
            exit("System has been terminated")
        doc_schedule = display_all_appointments(appointment)                #display all possible appointments with that doctor over a week
        while (set_new_appointment(appointment,doc_schedule) == -1):
            print("Running again")
            continue
        #take input from user and create new apt object
        #create appointmeent -> store in DB
    else:
        create_appointment(suggested_apt,format="24hr")
        #create appointment -> store in DB

if __name__ == "__main__":
    main()