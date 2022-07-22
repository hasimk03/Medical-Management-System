import sqlite3
import Classes as C
import schedule as s 

#create doctor objects using classes file -> store doctors into doctors DB
def create_doctor_object():
    id = int(input("ID: "))
    name = str(input("Name: "))
    speciality = str(input("Speciality:"))
    addy = str(input("Addy: "))
    schedule = s

    #name,availability,speciality, addy,num
    doctor_object = C.doctor(id,name,schedule,speciality,addy,0)
    return doctor_object

def create_static_doctor_objects():
    #speciality types = Cardiology, Respiratory,Gastro, Neurology,Psychiatry, Infection disease *5 doctors
    
#Cardiology
    d1 = C.doctor(1001,"Dr. Ajay Agarwala",s,"Cardiology","906 Oak Tree Ave Ste J South Plainfield, NJ 07080",0)
    d2 = C.doctor(1002,"Dr. Rajendra Patel",s,"Cardiology","1804 Oak Tree Rd Edison, NJ 08820",0)
    d3 = C.doctor(1003,"Dr.Bhudev Sharma",s,"Cardiology","622 Georges Rd North Brunswick, NJ 08902",0)
    d4 = C.doctor(1004,"Dr. Sheila Sahni",s,"Cardiology","408 New Brunswick Ave Ford, NJ 08863",0)
    d5 = C.doctor(1005,"Dr. Subhashini Gowda",s,"Cardiology","75 Veronica Ave Ste 101 Somerset, NJ 8873",0)
#Respiratory
    d6 = C.doctor(2001,"Dr. Haritha Potluri",s,"Respiratory","489 Union Ave Bridgewater, NJ 08807",0)
    d7 = C.doctor(2002,"Dr. Aesha Jobanputra",s,"Respiratory","125 Paterson Street Meb 568 New Brunswick, NJ 8901",0)
    d8 = C.doctor(2003,"Dr. Prashant Patel",s,"Respiratory","489 Union Ave Bridgewater, NJ 08807",0)
#Gastro
    d9 = C.doctor(3001,"Dr. Richard Medina",s,"Gastro","doctor_addy",0)
    d10 = C.doctor(3002,"Dr. Gary Ciambotti",s,"Gastro","doctor_addy",0)
    d11 = C.doctor(3003,"Dr. Mark Greaves",s,"Gastro","doctor_addy",0)
#Neurology
    d12 = C.doctor(4001,"Dr. Brad Kamitaki",s,"Neurology","125 Paterson St Ste 6100 New Brunswick, NJ 08901",0)
    d13 = C.doctor(4002,"Dr. Ram Mani,",s,"Neurology","125 Paterson St New Brunswick, NJ 08901",0)
    d14 = C.doctor(4003,"Dr. William Hu",s,"Neurology","125 Paterson St Ste 6100 New Brunswick, NJ 08901",0)
    d15 = C.doctor(4004,"Dr. John Wittenborn",s,"Neurology","103 OMNI DR Hillsborough, NJ 08844",0)
#Psychiatry
    d16 = C.doctor(5001,"Dr. Kenneth Lichtman",s,"Psychiatry","1109 Amboy Ave Edison, NJ 08837",0)
    d17 = C.doctor(5002,"Dr. Kenneth Burns",s,"Psychiatry","320 Raritan Ave Ste 305a Highland Park, NJ 08904",0)
    d18 = C.doctor(5003,"Dr. Mary Swigar",s,"Psychiatry","1 Robert Wood Johnson Pl New Brunswick, NJ 08901",0)
#Infectious disease
    d19 = C.doctor(6001,"Dr. Ronald Nahass",s,"Infectious Disease","49 Veronica Ave Ste 102 Somerset, NJ 8873",0)
    d20 = C.doctor(6002,"Dr. Juan Baez",s,"Infectious Disease","10 MOUNTAIN BLVD Warren, NJ 07059",0)
    d21 = C.doctor(6003,"Dr. Lisa Pittarelli",s,"Infectious Disease","81 Veronica Ave Ste 203 Somerset, NJ 08873",0)
    d22 = C.doctor(6004,"Dr. John Middleton",s,"Infectious Disease","3 Hospital Plz Ste 208 Old Bridge, NJ 8857",0)
#Endocrinology
    d23 = C.doctor(7001,"Dr. Nina Ramessar",s,"Endocrinology","125 Paterson st New Brunswick,NJ 8901 ",0)
    d24 = C.doctor(7002,"Dr. Maris Davis",s,"Endocrinology","311 Bay Ave Glen Ridge, NJ 7028 ",0)
#GP/Family Medicine
    d25 = C.doctor(8001,"Dr. Beth Balinski",s,"GP","2107 County Rd 516 Ste A Old Bridge, NJ 8857",0)
    

    list_of_doctors = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25]
    return list_of_doctors

def loop_through_day(work_day,time):
    count=0
    for hour in work_day.list:                                                       #run thru all work hours
        #time.append(str(work_day.day)+":"+str(count+8))                          #add date:time in 24hr
        time.append(hour)   
        count +=1

#open doctor object to get doctor schedule
def get_doctor_schedule(doctor):
    time = []                                                                   #date:time wheen doc is not available
    loop_through_day(doctor.schedule.Monday(),time)
    loop_through_day(doctor.schedule.Tuesday(),time)
    loop_through_day(doctor.schedule.Wednesday(),time)
    loop_through_day(doctor.schedule.Thursday(),time)
    loop_through_day(doctor.schedule.Friday(),time)
    loop_through_day(doctor.schedule.Saturday(),time)

    print("Length of time =",len(time))

    return time

def create_doctor_db(doc,delete_table = False,time=[]):
    conn = sqlite3.connect("doctor_database.db")
    cursor = conn.cursor()

    #check whether input requests table to be deleted
    if delete_table == True:
        cursor.execute("DROP TABLE Doctor_Table")
        print("Delete: ",delete_table)
        exit()

    
    #SQL Query to create table if !exist and create it -> 6(10) + 4 = 64 columns
    cursor.executescript('''CREATE TABLE IF NOT EXISTS Doctor_Table             
        (id,name,speciality,address,
        M8,M9,M10,M11,M12,M13,M14,M15,M16,M17,
        T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,
        W8,W9,W10,W11,W12,W13,W14,W15,W16,W17,
        Th8,Th9,Th10,Th11,Th12,Th13,Th14,Th15,Th16,Th17,
        F8,F9,F10,F11,F12,F13,F14,F15,F16,F17,
        S8,S9,S10,S11,S12,S13,S14,S15,S16,S17)''')       #XN, where X = day_of_week and N = hour_of_day [24Format]

  
    cursor.execute('''INSERT INTO Doctor_Table (id,name,speciality,address,M8,M9,M10,M11,M12,M13,M14,M15,M16,M17,
        T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,W8,W9,W10,W11,W12,W13,W14,W15,W16,W17,Th8,Th9,Th10,Th11,Th12,Th13,Th14,Th15,Th16,Th17,
        F8,F9,F10,F11,F12,F13,F14,F15,F16,F17,S8,S9,S10,S11,S12,S13,S14,S15,S16,S17) 
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
        (doc.get_id(),doc.get_name(),doc.get_speciality(),
        doc.get_office_address(),time[0],time[1],time[2],time[3],time[4],time[5],time[6],time[7],time[8],time[9],time[10],time[11],time[12],time[13],time[14],time[15],time[16],time[17],time[18],time[19],
        time[20],time[21],time[22],time[23],time[24],time[25],time[26],time[27],time[28],time[29],time[30],time[31],time[32],time[33],time[34],time[35],time[36],time[37],time[38],time[39],
        time[40],time[41],time[42],time[43],time[44],time[45],time[46],time[47],time[48],time[49],time[50],time[51],time[52],time[53],time[54],time[55],time[56],time[57],time[58],time[59]))

    cursor.execute('SELECT * FROM Doctor_Table')
    #print(cursor.fetchall())

    #close this shit
    conn.commit()
    cursor.close()
    conn.close()

def update_db():                                                    #add cols or change something in DB
    pass

def print_doctor_information(doctor):
    
    boolean = doctor.schedule.Monday().hour5
    #print("Doctor is {} available on Wednesday @10am".format("" if boolean==True else "not" ))
    print("------New Doctor------")
    print("Name: ",doctor.get_name())
    print("ID: ",doctor.get_id())
    print("Addy: ",doctor.get_office_address())
    print("Speciality: ",doctor.get_speciality())
    print("isAvailable Mon@12pm?: ","Yes" if boolean==True else "No")


def main():
    print("Starting up....")
    #doc = create_doctor_object()
    
    inp = input("Delete table? ")
    if inp=="Yes" or inp=="yes" or inp=="y" or inp=="Y":
        doc = C.doctor(0000,"Dr.John Smith",s,"GP","123 fake lane,candyLand",0)
        create_doctor_db(doc,True)


    list_of_doctors = create_static_doctor_objects()

    for doctor in list_of_doctors:
        time_list = get_doctor_schedule(doctor)
        create_doctor_db(doctor,time=time_list)
        print_doctor_information(doctor)

    
if __name__ == "__main__":
    main()


#doctor 1-----
#0001
#Igor Priven
#Endocrinology
#345 US Highway 9 Ste 8 Englishtown, NJ 7726