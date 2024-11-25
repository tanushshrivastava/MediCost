entriesList = [
    "HEART TRANSPLANT OR IMPLANT OF HEART ASSIST SYSTEM W MCC",
    "ECMO OR TRACH W MV 96+ HRS OR PDX EXC FACE, MOUTH & NECK W MAJ O.R.",
    "TRACH W MV 96+ HRS OR PDX EXC FACE, MOUTH & NECK W/O MAJ O.R.",
    "LIVER TRANSPLANT W MCC OR INTESTINAL TRANSPLANT",
    "LUNG TRANSPLANT",
    "SIMULTANEOUS PANCREAS/KIDNEY TRANSPLANT",
    "TRACHEOSTOMY FOR FACE,MOUTH & NECK DIAGNOSES W MCC",
    "ALLOGENEIC BONE MARROW TRANSPLANT",
    "INTRACRANIAL VASCULAR PROCEDURES W PDX HEMORRHAGE W MCC",
    "CRANIO W MAJOR DEV IMPL/ACUTE COMPLEX CNS PDX W MCC OR CHEMO IMPLANT",
    "CRANIOTOMY & ENDOVASCULAR INTRACRANIAL PROCEDURES W MCC",
    "SPINAL PROCEDURES W MCC",
    "VENTRICULAR SHUNT PROCEDURES W MCC",
    "CAROTID ARTERY STENT PROCEDURE W MCC",
    "EXTRACRANIAL PROCEDURES W MCC",
    "PERIPH/CRANIAL NERVE & OTHER NERV SYST PROC W MCC",
    "NERVOUS SYSTEM NEOPLASMS W MCC",
    "DEGENERATIVE NERVOUS SYSTEM DISORDERS W MCC",
    "ACUTE ISCHEMIC STROKE W USE OF THROMBOLYTIC AGENT W MCC",
    "INTRACRANIAL HEMORRHAGE OR CEREBRAL INFARCTION W MCC",
    "TRANSIENT ISCHEMIA",
    "NONSPECIFIC CEREBROVASCULAR DISORDERS W MCC",
    "CRANIAL & PERIPHERAL NERVE DISORDERS W MCC",
    "HYPERTENSIVE ENCEPHALOPATHY W MCC",
    "TRAUMATIC STUPOR & COMA, COMA >1 HR W MCC",
    "OTHER DISORDERS OF NERVOUS SYSTEM W MCC",
    "BACTERIAL & TUBERCULOUS INFECTIONS OF NERVOUS SYSTEM W MCC",
    "SEIZURES W MCC",
    "HEADACHES W MCC",
    "EXTRAOCULAR PROCEDURES EXCEPT ORBIT",
    "NEUROLOGICAL EYE DISORDERS",
    "SALIVARY GLAND PROCEDURES",
    "DYSEQUILIBRIUM",
    "OTITIS MEDIA & URI W MCC",
    "OTHER EAR, NOSE, MOUTH & THROAT DIAGNOSES W MCC",
    "DENTAL & ORAL DISEASES W MCC",
    "MAJOR CHEST PROCEDURES W MCC",
    "OTHER RESP SYSTEM O.R. PROCEDURES W MCC",
    "PULMONARY EMBOLISM W MCC",
    "RESPIRATORY INFECTIONS & INFLAMMATIONS W MCC",
    "RESPIRATORY NEOPLASMS W MCC",
    "MAJOR CHEST TRAUMA W MCC",
    "PLEURAL EFFUSION W MCC",
    "PULMONARY EDEMA & RESPIRATORY FAILURE",
    "CHRONIC OBSTRUCTIVE PULMONARY DISEASE W MCC",
    "SIMPLE PNEUMONIA & PLEURISY W MCC",
    "INTERSTITIAL LUNG DISEASE W MCC",
    "PNEUMOTHORAX W MCC",
    "RESPIRATORY SIGNS & SYMPTOMS",
    "OTHER RESPIRATORY SYSTEM DIAGNOSES W MCC",
    "RESPIRATORY SYSTEM DIAGNOSIS W VENTILATOR SUPPORT 96+ HOURS",
    "RESPIRATORY SYSTEM DIAGNOSIS W VENTILATOR SUPPORT <96 HOURS",
    "OTHER HEART ASSIST SYSTEM IMPLANT",
    "CARDIAC VALVE & OTH MAJ CARDIOTHORACIC PROC W CARD CATH W MCC",
    "CARDIAC VALVE & OTH MAJ CARDIOTHORACIC PROC W/O CARD CATH W MCC",
    "CARDIAC DEFIB IMPLANT W CARDIAC CATH W AMI/HF/SHOCK W MCC",
    "CARDIAC DEFIB IMPLANT W CARDIAC CATH W/O AMI/HF/SHOCK W MCC",
    "CARDIAC DEFIBRILLATOR IMPLANT W/O CARDIAC CATH W MCC",
    "OTHER CARDIOTHORACIC PROCEDURES W MCC",
    "CORONARY BYPASS W CARDIAC CATH W MCC",
    "CORONARY BYPASS W/O CARDIAC CATH W MCC",
    "MAJOR CARDIOVASC PROCEDURES W MCC",
    "AMPUTATION FOR CIRC SYS DISORDERS EXC UPPER LIMB & TOE W MCC",
    "PERMANENT CARDIAC PACEMAKER IMPLANT W MCC",
    "AICD GENERATOR PROCEDURES",
    "PERC CARDIOVASC PROC W DRUG-ELUTING STENT W MCC OR 4+ VESSELS/STENTS",
    "PERC CARDIOVASC PROC W NON-DRUG-ELUTING STENT W MCC OR 4+ VES/STENTS",
    "PERC CARDIOVASC PROC W/O CORONARY ARTERY STENT W MCC",
    "OTHER VASCULAR PROCEDURES W MCC",
    "UPPER LIMB & TOE AMPUTATION FOR CIRC SYSTEM DISORDERS W MCC",
    "CARDIAC PACEMAKER REVISION EXCEPT DEVICE REPLACEMENT W MCC",
    "OTHER CIRCULATORY SYSTEM O.R. PROCEDURES",
    "ACUTE MYOCARDIAL INFARCTION, DISCHARGED ALIVE W MCC",
    "ACUTE MYOCARDIAL INFARCTION, EXPIRED W MCC",
    "CIRCULATORY DISORDERS EXCEPT AMI, W CARD CATH W MCC",
    "HEART FAILURE & SHOCK W MCC",
    "CARDIAC ARREST, UNEXPLAINED W MCC",
    "PERIPHERAL VASCULAR DISORDERS W MCC",
    "ATHEROSCLEROSIS W MCC",
    "HYPERTENSION W MCC",
    "CARDIAC CONGENITAL & VALVULAR DISORDERS W MCC",
    "CARDIAC ARRHYTHMIA & CONDUCTION DISORDERS W MCC",
    "ANGINA PECTORIS",
    "SYNCOPE & COLLAPSE",
    "CHEST PAIN",
    "OTHER CIRCULATORY SYSTEM DIAGNOSES W MCC",
    "STOMACH, ESOPHAGEAL & DUODENAL PROC W MCC",
    "MAJOR SMALL & LARGE BOWEL PROCEDURES W MCC",
    "RECTAL RESECTION W MCC",
    "PERITONEAL ADHESIOLYSIS W MCC",
    "ANAL & STOMAL PROCEDURES W MCC",
    "HERNIA PROCEDURES EXCEPT INGUINAL & FEMORAL W MCC",
    "OTHER DIGESTIVE SYSTEM O.R. PROCEDURES W MCC",
    "MAJOR ESOPHAGEAL DISORDERS W MCC",
    "MAJOR GASTROINTESTINAL DISORDERS & PERITONEAL INFECTIONS W MCC",
    "DIGESTIVE MALIGNANCY W MCC",
    "G.I. HEMORRHAGE W MCC",
    "UNCOMPLICATED PEPTIC ULCER W MCC",
    "INFLAMMATORY BOWEL DISEASE W MCC",
    "G.I. OBSTRUCTION W MCC",
    "ESOPHAGITIS, GASTROENT & MISC DIGEST DISORDERS W MCC",
    "OTHER DIGESTIVE SYSTEM DIAGNOSES W MCC",
    "PANCREAS, LIVER & SHUNT PROCEDURES W MCC",
    "BILIARY TRACT PROC EXCEPT ONLY CHOLECYST W OR W/O C.D.E. W MCC",
    "CHOLECYSTECTOMY EXCEPT BY LAPAROSCOPE W/O C.D.E. W MCC",
    "LAPAROSCOPIC CHOLECYSTECTOMY W/O C.D.E. W MCC",
    "OTHER HEPATOBILIARY OR PANCREAS O.R. PROCEDURES W MCC",
    "CIRRHOSIS & ALCOHOLIC HEPATITIS W MCC",
    "MALIGNANCY OF HEPATOBILIARY SYSTEM OR PANCREAS W MCC",
    "DISORDERS OF PANCREAS EXCEPT MALIGNANCY W MCC",
    "DISORDERS OF LIVER EXCEPT MALIG,CIRR,ALC HEPA W MCC",
    "DISORDERS OF THE BILIARY TRACT W MCC",
    "COMBINED ANTERIOR/POSTERIOR SPINAL FUSION W MCC",
    "SPINAL FUS EXC CERV W SPINAL CURV/MALIG/INFEC OR 9+ FUS W MCC",
    "SPINAL FUSION EXCEPT CERVICAL W MCC",
    "WND DEBRID & SKN GRFT EXC HAND, FOR MUSCULO-CONN TISS DIS W MCC",
    "REVISION OF HIP OR KNEE REPLACEMENT W MCC",
    "MAJOR JOINT REPLACEMENT OR REATTACHMENT OF LOWER EXTREMITY W MCC",
    "CERVICAL SPINAL FUSION W MCC",
    "AMPUTATION FOR MUSCULOSKELETAL SYS & CONN TISSUE DIS W MCC",
    "BIOPSIES OF MUSCULOSKELETAL SYSTEM & CONNECTIVE TISSUE W MCC",
    "HIP & FEMUR PROCEDURES EXCEPT MAJOR JOINT W MCC",
    "MAJOR JOINT/LIMB REATTACHMENT PROCEDURE OF UPPER EXTREMITIES",
    "LOWER EXTREM & HUMER PROC EXCEPT HIP,FOOT,FEMUR W MCC",
    "LOCAL EXCISION & REMOVAL INT FIX DEVICES EXC HIP & FEMUR W MCC",
    "SOFT TISSUE PROCEDURES W MCC",
    "OTHER MUSCULOSKELET SYS & CONN TISS O.R. PROC W MCC",
    "FRACTURES OF HIP & PELVIS W MCC",
    "OSTEOMYELITIS W MCC",
    "PATHOLOGICAL FRACTURES & MUSCULOSKELET & CONN TISS MALIG W MCC",
    "CONNECTIVE TISSUE DISORDERS W MCC",
    "MEDICAL BACK PROBLEMS W MCC",
    "BONE DISEASES & ARTHROPATHIES W MCC",
    "SIGNS & SYMPTOMS OF MUSCULOSKELETAL SYSTEM & CONN TISSUE W MCC",
    "TENDONITIS, MYOSITIS & BURSITIS W MCC",
    "FX, SPRN, STRN & DISL EXCEPT FEMUR, HIP, PELVIS & THIGH W MCC",
    "OTHER MUSCULOSKELETAL SYS & CONNECTIVE TISSUE DIAGNOSES W MCC",
    "SKIN DEBRIDEMENT W MCC",
    "SKIN GRAFT FOR SKIN ULCER OR CELLULITIS W MCC",
    "OTHER SKIN, SUBCUT TISS & BREAST PROC W MCC",
    "SKIN ULCERS W MCC",
    "MAJOR SKIN DISORDERS W MCC",
    "CELLULITIS W MCC",
    "TRAUMA TO THE SKIN, SUBCUT TISS & BREAST W MCC",
    "MINOR SKIN DISORDERS W MCC",
    "AMPUTAT OF LOWER LIMB FOR ENDOCRINE,NUTRIT,& METABOL DIS W MCC",
    "O.R. PROCEDURES FOR OBESITY W MCC",
    "THYROID, PARATHYROID & THYROGLOSSAL PROCEDURES W MCC",
    "OTHER ENDOCRINE, NUTRIT & METAB O.R. PROC W MCC",
    "DIABETES W MCC",
    "MISC DISORDERS OF NUTRITION,METABOLISM,FLUIDS/ELECTROLYTES W MCC",
    "INBORN AND OTHER DISORDERS OF METABOLISM",
    "ENDOCRINE DISORDERS W MCC",
    "KIDNEY TRANSPLANT",
    "MAJOR BLADDER PROCEDURES W MCC",
    "KIDNEY & URETER PROCEDURES FOR NEOPLASM W MCC",
    "KIDNEY & URETER PROCEDURES FOR NON-NEOPLASM W MCC",
    "TRANSURETHRAL PROCEDURES W MCC",
    "OTHER KIDNEY & URINARY TRACT PROCEDURES W MCC",
    "RENAL FAILURE W MCC",
    "ADMIT FOR RENAL DIALYSIS",
    "KIDNEY & URINARY TRACT INFECTIONS W MCC",
    "URINARY STONES W/O ESW LITHOTRIPSY W MCC",
    "OTHER KIDNEY & URINARY TRACT DIAGNOSES W MCC",
    "FEMALE REPRODUCTIVE SYSTEM RECONSTRUCTIVE PROCEDURES",
    "VAGINAL DELIVERY W COMPLICATING DIAGNOSES",
    "VAGINAL DELIVERY W/O COMPLICATING DIAGNOSES",
    "OTHER ANTEPARTUM DIAGNOSES W MEDICAL COMPLICATIONS",
    "MAJOR HEMATOL/IMMUN DIAG EXC SICKLE CELL CRISIS & COAGUL W MCC",
    "RED BLOOD CELL DISORDERS W MCC",
    "COAGULATION DISORDERS",
    "LYMPHOMA & LEUKEMIA W MAJOR O.R. PROCEDURE W MCC",
    "LYMPHOMA & NON-ACUTE LEUKEMIA W OTHER O.R. PROC W MCC",
    "MYELOPROLIF DISORD OR POORLY DIFF NEOPL W MAJ O.R. PROC W MCC",
    "ACUTE LEUKEMIA W/O MAJOR O.R. PROCEDURE W MCC",
    "CHEMO W ACUTE LEUKEMIA AS SDX OR W HIGH DOSE CHEMO AGENT W MCC",
    "LYMPHOMA & NON-ACUTE LEUKEMIA W MCC",
    "OTHER MYELOPROLIF DIS OR POORLY DIFF NEOPL DIAG W MCC",
    "CHEMOTHERAPY W/O ACUTE LEUKEMIA AS SECONDARY DIAGNOSIS W MCC",
    "RADIOTHERAPY",
    "INFECTIOUS & PARASITIC DISEASES W O.R. PROCEDURE W MCC",
    "POSTOPERATIVE OR POST-TRAUMATIC INFECTIONS W O.R. PROC W MCC",
    "POSTOPERATIVE & POST-TRAUMATIC INFECTIONS W MCC",
    "FEVER",
    "VIRAL ILLNESS W MCC",
    "OTHER INFECTIOUS & PARASITIC DISEASES DIAGNOSES W MCC",
    "SEPTICEMIA OR SEVERE SEPSIS W MV 96+ HOURS",
    "SEPTICEMIA OR SEVERE SEPSIS W/O MV 96+ HOURS W MCC",
    "ACUTE ADJUSTMENT REACTION & PSYCHOSOCIAL DYSFUNCTION",
    "DEPRESSIVE NEUROSES",
    "NEUROSES EXCEPT DEPRESSIVE",
    "DISORDERS OF PERSONALITY & IMPULSE CONTROL",
    "ORGANIC DISTURBANCES & MENTAL RETARDATION",
    "PSYCHOSES",
    "BEHAVIORAL & DEVELOPMENTAL DISORDERS",
    "OTHER MENTAL DISORDER DIAGNOSES",
    "ALCOHOL/DRUG ABUSE OR DEPENDENCE, LEFT AMA",
    "OTHER O.R. PROCEDURES FOR INJURIES W MCC",
    "ALLERGIC REACTIONS W MCC",
    "POISONING & TOXIC EFFECTS OF DRUGS W MCC",
    "COMPLICATIONS OF TREATMENT W MCC",
    "EXTENSIVE BURNS OR FULL THICKNESS BURNS W MV 96+ HRS W SKIN GRAFT",
    "FULL THICKNESS BURN W/O SKIN GRFT OR INHAL INJ",
    "NON-EXTENSIVE BURNS",
    "SIGNS & SYMPTOMS W MCC",
    "OTHER FACTORS INFLUENCING HEALTH STATUS",
    "LIMB REATTACHMENT, HIP & FEMUR PROC FOR MULTIPLE SIGNIFICANT TRAUMA",
    "OTHER O.R. PROCEDURES FOR MULTIPLE SIGNIFICANT TRAUMA W MCC",
    "OTHER MULTIPLE SIGNIFICANT TRAUMA W MCC",
    "HIV W EXTENSIVE O.R. PROCEDURE W MCC",
    "EXTENSIVE O.R. PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS W MCC",
    "NON-EXTENSIVE O.R. PROC UNRELATED TO PRINCIPAL DIAGNOSIS W MCC",
]

state_abbreviations = {
            "Alaska": "AK", "Alabama": "AL", "Arkansas": "AR", "American Samoa": "AS",
            "Arizona": "AZ", "California": "CA", "Colorado": "CO", "Connecticut": "CT",
            "District of Columbia": "DC", "Delaware": "DE", "Florida": "FL", "Georgia": "GA",
            "Guam": "GU", "Hawaii": "HI", "Iowa": "IA", "Idaho": "ID", "Illinois": "IL",
            "Indiana": "IN", "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA",
            "Massachusetts": "MA", "Maryland": "MD", "Maine": "ME", "Michigan": "MI",
            "Minnesota": "MN", "Missouri": "MO", "Mississippi": "MS", "Montana": "MT",
            "North Carolina": "NC", "North Dakota": "ND", "Nebraska": "NE", "New Hampshire": "NH",
            "New Jersey": "NJ", "New Mexico": "NM", "Nevada": "NV", "New York": "NY",
            "Ohio": "OH", "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA",
            "Puerto Rico": "PR", "Rhode Island": "RI", "South Carolina": "SC",
            "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT",
            "Virginia": "VA", "Virgin Islands": "VI", "Vermont": "VT", "Washington": "WA",
            "Wisconsin": "WI", "West Virginia": "WV", "Wyoming": "WY"
        }