
accepted_medical_specialities = ["Cardiology","Respiratory","Gastro","Surgery","Orthopaedics","Neurology","Psychiatry",
    "Dermatology","Paediatrics","OB/GYN","Haematology","Rheumatology","Endocrinology","Renal","Urology","Vascular","ENT",
    "Neurosurgery","Genetics","Infectious Disease","Ophthalmology","Geriatrics","Emergency Medicine","Immunology","Sexual Health"]

#surgery cannot be scheduled -> must be recommended by another doctor - the diseases/illnesses cannot be classified as surgical
#peadiatrics -> no specific illnesses/diseases -> automatically go to one if child is < 4 regardless of disease
    #if GP = speciality assigned && age < 15 -> go to paediatrician
    
#data-source -> https://almostadoctor.co.uk/encyclopedia/


#change classification########
    #classify illnesses/diseases/disorders by organ/tissue = 78ish categories
    #classify doctors by specialities -> each doctor works on a few categories (3 on average)


illness_classification_dict = {
#Cardiology     #########
    "Arrhythmia" : "Cardiology", "Coronary artery disease" : "Cardiology", "Cardiomyopathy" : "Cardiology", "Pericardial disease" :"Cardiology", "Heart Value disease" : "Cardiology",
#Respiratory    #########
    "Asthma" : "Respiratory", "Covid-19" : "Respiratory", "Pneumonia" : "Respiratory", "Cystic Fibrosis" : "Respiratory", "Lung Cancer" : "Respiratory",
#Gastro         #########
    "Celiac disease" : "Gastro", "IBS" : "Gastro", "Diarrhea" : "Gastro", "Crohns disease" : "Gastro", "Gallstones" : "Gastro", "Acid Reflux" : "Gastro", "Constipation" : "Gastro",
#Orthopaedics   #########
    "Arthritis" : "Orthopaedics", "Carpal Tunnel Syndrome" : "Orthopaedics", "Torn Meniscus" : "Orthopaedics",  "Osteoporosis" : "Orthopaedics", "Scoliosis" : "Orthopaedics", "Medial Epicondylitis" : "Orthopaedics", "Low Back Pain" : "Orthopaedics",
#Neurology       #########
    "Headaches" : "Neurology", "Epilepsy" : "Neurology", "Seizures" : "Neurology", "Stroke" : "Neurology", "ALS" : "Neurology", "Alzheimers" : "Neurology", "Dementia" : "Neurology",
#Psychiatry
    "Panic disorder" : "Psychiatry", "OCD" : "Psychiatry", "Depression" : "Psychiatry", "Bipolar disorder" : "Psychiatry", "Post-traumatic stress disorder" : "Psychiatry", "Schizophrenia" : "Psychiatry",
#Dermatology        
    "Acne" : "Dermatology", "Pemphigus" : "Dermatology", "Psoriasis" : "Dermatology", "Rosacea" : "Dermatology", "Scleroderma" : "Dermatology",
#OB/GYN           #########
#Haematology      #########
#Rheumatology     #########
#Endocrinology      #########  
    "Diabetes" : "Endocrinology", "Hypothyroidism" : "Endocrinology", "PCOS" : "Endocrinology", "Crushing's Syndrome" : "Endocrinology", "Acromegaly" : "Endocrinology",
#Renal              #########
#Urology          ######### 
    "Erectile Dysfunction" : "Urology", "Prostatis" : "Urology", "Kidney Stone" : "Urology", "Prostate cancer" : "Urology", "Stomas" : "Urology", "Testicular cancer" : "Urology", "Urinary Tract Infection" : "Urology", "UTI" : "Urology",
#Vascular             #########
#ENT
#Neurosurgery         #########
    "Spinal stenosis" : "Neurosurgery", "Spondyolisthesis" : "Neurosurgery", "Cauda equina syndrome" : "Neurosurgery", "Chiari malformations" : "Neurosurgery",
#Genetics
#Infectious Disease   #########
    "Typhus" : "Infectious Disease", "Typhoid" : "Infectious Disease", "Tetanus" : "Infectious Disease", "Syphillis" : "Infectious Disease", "Mumps" : "Infectious Disease", "Lyme disease" : "Infectious Disease", "Malaria" : "Infectious Disease", "COVID-19" : "Infectious Disease", "Hepatitis A" : "Infectious Disease", "Hepatitis B" : "Infectious Disease", "Hepatitis C" : "Infectious Disease",
    "Other" : "GP"
#Ophthalmology      #########
#Geriatrics         GP for old ppl
#Emergency Medicine #########
#Immunology         #########
#Sexual Health
}