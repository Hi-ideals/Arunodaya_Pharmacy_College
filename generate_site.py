import os
import json

workspace_dir = r"c:\Users\win10\Documents\Arunodayag_ Institutions"
os.makedirs(workspace_dir, exist_ok=True)

# Define content data dictionary
content_data = {
    "config": {
        "useLiveImageFallback": True,
        "liveBaseUrl": "https://arunodayaginstitutions.in/"
    },
    "header": {
        "phone": "+91 9483752034",
        "email": "arunodaya.pharm@gmail.com",
        "marqueeDesktop": "Welcome to Arunodaya College of pharmacy Aurad (B), affiliated to BEA",
        "marqueeMobile": "Welcome to arunodaya pharmacy College of Aurad, affiliated to BEA.",
        "logoHeader": "wp-content/uploads/2024/07/arunodaya-pharmacy-logo1.png",
        "logoHeaderWhite": "wp-content/uploads/2024/07/arunodaya-pharmacy-logo1-white.png"
    },
    "footer": {
        "logoFooter": "wp-content/uploads/2024/07/arunodaya-pharmacy-logo2.png",
        "ctaTitle": "Have Any Query? Please Contact Us!",
        "ctaText": "If I can be of assistance, please do not hesitate to contact me. If you require any further information, feel free to contact me. If you require any further information, let me know. Please feel free to contact me if you need any further information.",
        "ctaBtnText": "Click Hear",
        "bio": "Arunodaya College of Pharmacy Aurad (B) was established in 2019, approved by All India Council for Technical Education (AICTE), Pharmacy Council of India (PCI), New Delhi and affiliated to BEA, Bangalore.",
        "quickLinksCol1": ["About Us", "Academics", "Amenities", "Alumni", "Placements", "IQAC", "Contact Us"],
        "quickLinksCol2": ["Programs", "Examination cell", "Research", "Activities", "Gallery", "NIRF"],
        "contactAddress": "Arunodaya College Of Pharmacy, Ring Road, Opp to Sub jail, Aurad (B), Bidar-585320, Karnatak",
        "contactPhone": "+91 9483752034",
        "contactEmail": "arunodaya.pharm@gmail.com, patilsr193@gmail.com",
        "contactHugeNumber": "+91 9921877870",
        "copyright": "© 2023 - 2026 Arunodaya Pharmacy College by Hi-Ideals"
    },
    "home": {
        "title": "Arunodaya Pharmacy College Bidar",
        "sliderImages": [
            "wp-content/uploads/2024/05/slider1.png",
            "wp-content/uploads/2024/05/slider2.png",
            "wp-content/uploads/2024/05/slider3.png"
        ],
        "highlights": [
            {"title": "Qualified Faculty", "desc": "Highly knowledgeable and committed faculty members guiding students to success."},
            {"title": "Best Infrastructure", "desc": "Spacious, architecturally designed campus with modern classrooms and laboratories."},
            {"title": "Placements", "desc": "Active placement cell and job counseling facilitating student career growth."},
            {"title": "Certification", "desc": "Accredited programs meeting standard industry requirements."}
        ],
        "coursesTitle": "Courses Offered",
        "coursesList": [
            {"tab": "B. Pharm", "name": "B. Pharma", "desc": "B. Pharmacy course is a four years program. This is affiliated to Osmania University and approved by Pharmacy Council of India (PCI) New Delhi. It is recognized by the Government of Telangana and the B. Pharmacy course is accredited by the National Board of Accreditation, New Delhi.", "linkText": "Read more", "link": "b-pharm.html", "img": "Images/Courses/Screenshot (9).png"},
            {"tab": "D. Pharm", "name": "D. Pharma", "desc": "A diploma in pharmacy is a 2-year-long career-oriented, diploma course. Students who wish to pursue a long-term career in the medical field of pharmaceutical sciences, and start a career in the pharmaceutical industry, can take admitted to the D.Pharm course. D.Pharmacy syllabus is designed to prepare candidates to work under the supervision of a licensed pharmacist in hospitals, community pharmacies, and other pharmaceutical-related fields. Candidates can also pursue MBA in Pharmaceutical Management after this course, though they would need to complete their undergraduate degree first.", "linkText": "Read more", "link": "d-pharm.html", "img": "Images/Courses/Dpharmacy.png"},
            {"tab": "B.Sc", "name": "Bachelor Of Science", "desc": "The college follows non-elitist polices of admission, in keeping with its ideals of education to all and social justice. Arunodaya First Grade Degree College does not share the general perception of B.Sc. Courses being irrelevant. We value the understanding of the society and cultural process that the social sciences provide when pursued with interest.", "linkText": "Read more", "link": "b-sc.html", "img": "Images/Courses/BSc.png"},
            {"tab": "B.Com", "name": "Bachelor Of Commerce", "desc": "The college follows non-elitist polices of admission, in keeping with its ideals of education to all and social justice. Arunodaya First Grade Degree College does not share the general perception of B.Com. Courses being irrelevant. We value the understanding of the society and cultural process that the social sciences provide when pursued with interest.", "linkText": "Read more", "link": "b-com.html", "img": "Images/Courses/Bcom.png"},
            {"tab": "BCA", "name": "Bachelor Of Computer Applications", "desc": "The college follows non-elitist polices of admission, in keeping with its ideals of education to all and social justice. Arunodaya First Grade Degree College does not share the general perception of BCA Courses being irrelevant. We value the understanding of the society and cultural process that the social sciences provide when pursued with interest.", "linkText": "Read more", "link": "bca.html", "img": "Images/Courses/BCA.png"}
        ],
        "facilitiesTitle": "Our Facilities",
        "facilities": [
            {"name": "Library", "desc": "The Institute has established a spacious library & Information center providing National, International and E- Journals."},
            {"name": "Transport", "desc": "Transport facility for the students is provided from all corners of the city driven by a team of well trained drivers."},
            {"name": "Sports", "desc": "The institute offers extensive facilities and maintains excellent sections for both outdoor sports and indoor games."},
            {"name": "Career Guidance", "desc": "We give training and guidance to students on career related matters and assist them in exploring new opportunities."}
        ],
        "welcome": {
            "title": "Welcome To Arunodaya College of Pharmacy Aurad (B)",
            "p1": "As an Institute committed to quality education, ARUNODAYA COLLEGE OF PHARMACY (B) aims at providing learning with a technology-edge. It endeavors to provide consistent training to its students to help them evolve as competent professionals in the highly competitive world.",
            "p2": "ARUNODAYA COLLEGE OF PHARMACY (B) primary objective of this college is to offer instruction in pharmaceutical science to meet the needs of the health care system and also to provide opportunities for job oriented training to the student to eliminate unemployment. The college also aims to create awarwness on the use of indigenous system of medicines in bringing health, happiness, and prosperity and to assist the pharmaceutical industry in india in meeting the challenges of pharmaceutical industries.",
            "linkText": "Read more"
        },
        "placementsTitle": "Major Campus Placements",
        "placements": [
            "wp-content/uploads/2024/07/Placement1.png",
            "wp-content/uploads/2024/07/Placement2.png",
            "wp-content/uploads/2024/07/Placement3.png",
            "wp-content/uploads/2024/07/Placement4.png",
            "wp-content/uploads/2024/07/Placement5.png",
            "wp-content/uploads/2024/07/Placement6.png",
            "wp-content/uploads/2024/07/Placement7.png",
            "wp-content/uploads/2024/07/Placement8.png",
            "wp-content/uploads/2024/07/Placement9.png"
        ],
        "membersTitle": "Our Member",
        "members": [
            {
                "name": "Mr. Gundappa Vakil",
                "role": "President A.V.V Trust Bidar",
                "role2": "President A.V.V Trust",
                "phone": "9448126004",
                "img": "wp-content/uploads/2024/06/Prasident.png"
            },
            {
                "name": "Dr. Sridharamurthy N B",
                "role": "M.Pharm, Ph.D, BAMS",
                "role2": "Director",
                "phone": "9483752034",
                "img": "wp-content/uploads/2024/06/Gundappa1.png"
            },
            {
                "name": "Mrs. Gangamma",
                "role": "M.Pharm",
                "role2": "Director in Charge",
                "phone": "9632919737",
                "img": "wp-content/uploads/2024/07/Gangamma.png"
            },
            {
                "name": "Mr.Sandeep Ramkishan Patil",
                "role": "M.Pharm",
                "role2": "Principal",
                "phone": "9921877870",
                "img": "wp-content/uploads/2024/06/Pricipal-1.png"
            }
        ],
        "vision": {
            "title": "Our Vision",
            "text": "Arunodaya College of Pharmacy Aurad (B) to become a globally recognized standard institute, imparting quality Pharmacy education to the students with inculcative skill set, glimpse of knowledge , employability, leadership attitude, holistic approach & committed for industry interface, higher education, innovative research and patient care."
        },
        "mission": {
            "title": "Our Mission",
            "text": "To train and develop students into professional pharmacists so as to fulfill the industrial and community needs. To shoulder the responsibility of reducing the suffering of mankind by providing Pharmaceutical care. By encouraging innovations, self evaluation and reforms to meet the demands of an ever changing health care environment."
        },
        "whyUsTitle": "Why? Arunodaya College Of Pharmacy (B)",
        "whyUs": [
            "Established By Pharmacy Professors Having More Than 10 Years Experience",
            "Management Are The Faculty Members",
            "Spacious, Architecturally designed Building.",
            "Highly Qualified And Experienced Faculty",
            "Well Equipped And Sophisticated Laboratories",
            "Excellent results in University examinations.",
            "In Campus Homely Separate Hostels For Girls And Boys",
            "Student friendly atmosphere and ragging free environment.",
            "Active Placement Cell And Job Counseling",
            "Good Transportation Facility"
        ],
        "stats": [
            {"value": 15, "label": "Teacher"},
            {"value": 35, "label": "Class Rooms"},
            {"value": 200, "label": "Students"},
            {"value": 1000, "label": "Admissions"}
        ],
        "modalSliderImages": [
            "wp-content/uploads/2024/07/IMG-20240527-WA0063.jpg",
            "wp-content/uploads/2025/11/BED.webp"
        ],
        "announcementsTitle": "Announcements",
        "announcements": [
            "Academic Calender for D.Pharmacy  First Year  2022- 23",
            "D.Pharmacy I-Year I-Sem I-Mid Exams from 10/10/2024 To 12/10/2024",
            "Academic Calender for D.Pharmacy  First Year  2022- 23",
            "Academic Calender for D.Pharmacy  First Year  2022- 23",
            "Academic Calender for D.Pharmacy  First Year  2022- 23",
            "Academic Calender for D.Pharmacy  First Year  2022- 23"
        ],
        "quickLinksTitle": "Quick Links",
        "quickLinks": [
            {"text": "Program & Fees", "link": "#"},
            {"text": "Apply Now for Admissions", "link": "#"}
        ]
    },
    "about": {
        "title": "Who We Are",
        "welcomeTitle": "Welcome To Arunodaya College of Pharmacy Aurad (B)",
        "welcomeText1": "As an Institute committed to quality education, ARUNODAYA COLLEGE OF PHARMACY (B) aims at providing learning with a technology-edge. It endeavors to provide consistent training to its students to help them evolve as competent professionals in the highly competitive world.",
        "welcomeText2": "ARUNODAYA COLLEGE OF PHARMACY (B) primary objective of this college is to offer instruction in pharmaceutical science to meet the needs of the health care system and also to provide opportunities for job oriented training to the student to eliminate unemployment. The college also aims to create awarwness on the use of indigenous system of medicines in bringing health, happiness, and prosperity and to assist the pharmaceutical industry in india in meeting the challenges of pharmaceutical industries.",
        "welcomeText3": "Arunodaya College Of Pharmacy has been a nurturing ground for Pharmacy professionals since its inception and has been a developing center for future Pharma professionals for over a decade. The college has highly knowledgeable and committed faculty, and aims to contribute immensely to improve the health of the people across the world through Quality Pharmacy Education, High-impact Research and Clinical Innovation. Our students enjoy inter-professional opportunities as well as cultural, athletic and recreational activities at our premises. Continuous interaction with industry is maintained to ensure that the learning program remains relevant to the changing and challenging trends in Pharmaceutical Sciences. The college is constantly seeking to upgrade the quality of its education and actively participates in research to remain on the cutting edge.",
        "principalTitle": "Our Principal Message",
        "principalName": "Mr.Sandeep Ramkishan Patil",
        "principalRole": "Principal",
        "principalImg": "wp-content/uploads/2024/06/Pricipal-1.png",
        "principalText": "Dear Students,\n\nWe are committed to nurturing the future leaders of the pharmaceutical industry. The institution stands at the forefront of pharmaceutical education and research, offering a dynamic environment for academic excellence and creation.\n\nAs the Principal, I take pride in our dedicated faculty and the talents of our students who continuously push the boundaries of knowledge and discovery. Our mission is to empower the students with the skills and expertness needed to make a significant impact in the ever-evolving world of healthcare and pharmaceuticals.\n\nWe invite the students to explore our programs, research initiatives, and excellent approach to the field of pharmacy that makes the students a hub of inspiration and growth. Together, we can shape the future of pharmaceutical science.",
        "directorTitle": "Director Message",
        "directorName": "Dr.Sridharamurthy N B",
        "directorRole": "M.Pharm,Ph.D, BAMS",
        "directorRole2": "Director",
        "directorImg": "wp-content/uploads/2024/06/Gundappa1.png",
        "directorText": "As we all know that education, business, profession, in fact, everything is changing at a fast velocity globally. We need to be at the right place at right time otherwise we will be left behind. Hence the need arises to impart high quality education supplemented with the latest infrastructure, since it provides us a chance to exploit future opportunities. Hence our institution focuses on and we know by putting the right people on the right job which we can make it a big success story. The focus is on a balanced education that includes on tradition of ethics and on the needs of a changing world.\n\nToday, more than at any time in history, technology is changing day by day. It has the power to transform economic, social, cultural and environmental situations of our country, so that all our countrymen may have good food, shelter, education, health-care and employment within a given time-frame.\n\nArunodaya College of Pharmacy, Aurad (B), is dedicated to the task of making India a awareness society in pharmaceutical sciences: to create pharmacists of proven capability. The main goal is that the child not only becomes a successful individual in the vibrant and dynamic environment but also becomes a better human being that will make him a responsible citizen upholding our values and ethics.",
        "vision": "Arunodaya College of Pharmacy Aurad (B) to become a globally recognized standard institute, imparting quality Pharmacy education to the students with inculcative skill set, glimpse of knowledge , employability, leadership attitude, holistic approach & committed for industry interface, higher education, innovative research and patient care.",
        "mission": "To train and develop students into professional pharmacists so as to fulfill the industrial and community needs. To shoulder the responsibility of reducing the suffering of mankind by providing Pharmaceutical care. By encouraging innovations, self evaluation and reforms to meet the demands of an ever changing health care environment.",
        "facultyTitle": "Our Faculty Member",
        "faculties": [
            {"name": "Ms. Asharani", "role": "Lecturer", "qualification": "B. Pharm", "img": "wp-content/uploads/2024/05/about-collage.png"},
            {"name": "Mr. Ganesh Hulsure", "role": "Lecturer", "qualification": "B. Pharma", "img": "wp-content/uploads/2024/05/about-collage.png"},
            {"name": "Ms. Havubai Dombale", "role": "Lecturer", "qualification": "B. Pharma", "img": "wp-content/uploads/2024/05/about-collage.png"},
            {"name": "Mr. KrishnaDevkatte", "role": "Lecturer", "qualification": "B. Pharma", "img": "wp-content/uploads/2024/05/about-collage.png"}
        ]
    },
    "admission": {
        "title": "Admission Process",
        "subtitle": "Eligibility & Admission Process",
        "requirements": [
            "SSC Certificate (10th Class passed certificate)",
            "Intermediate or 10+2 Certificate",
            "Transfer Certificate",
            "Migration Certificate",
            "Latest Passport size photographs 5 No’s (Color)",
            "Originals to be submitted at the time of admission",
            "Students and their parents AAdhar Card Xerox Copies"
        ]
    },
    "teachingStaff": {
        "title": "Teaching Staff",
        "departments": [
            {
                "name": "Department of Pharmaceutics:",
                "staff": [
                    {"no": "01", "name": "Mrs. Pratiksha Biradar", "qualification": "M.pharm", "designation": "HOD", "photo": ""},
                    {"no": "02", "name": "Ms. Asharani", "qualification": "B. pharm", "designation": "Lecturer", "photo": ""}
                ]
            },
            {
                "name": "Department of Pharmaceutical Chemistry:",
                "staff": [
                    {"no": "01", "name": "Mr. Sandeep Patil", "qualification": "M.pharm", "designation": "HOD", "photo": ""},
                    {"no": "02", "name": "Mr. Ganesh Hulsure", "qualification": "B. pharm", "designation": "Lecturer", "photo": ""}
                ]
            },
            {
                "name": "Department of Pharmacognosy :",
                "staff": [
                    {"no": "01", "name": "Mr. Pankaj Biradar", "qualification": "M.pharm", "designation": "HOD", "photo": ""},
                    {"no": "02", "name": "Mr. KrishnaDevkatte", "qualification": "B. pharm", "designation": "Lecturer", "photo": ""}
                ]
            },
            {
                "name": "Department of Hospital and Clinical Pharmacy:",
                "staff": [
                    {"no": "01", "name": "Ms. Havubai Dombale", "qualification": "B. pharm", "designation": "Lecturer", "photo": ""}
                ]
            },
            {
                "name": "Department of HAP & Pharmacology:",
                "staff": [
                    {"no": "01", "name": "Dr. Sridharamurthy N.B.", "qualification": "M. pharm, P.hd", "designation": "HOD", "photo": ""},
                    {"no": "02", "name": "Name", "qualification": "M. pharm", "designation": "Lecturer", "photo": ""}
                ]
            },
            {
                "name": "Department of B. Pharmacy:",
                "staff": [
                    {"no": "01", "name": "Mr KARTHIK H K", "qualification": "M. pharm", "designation": "Assistant Professor", "photo": ""},
                    {"no": "02", "name": "Mr PAVAN KUMAR H L", "qualification": "M. pharm", "designation": "Assistant Professor", "photo": ""},
                    {"no": "03", "name": "Mr REVSNSPPA", "qualification": "M. pharm", "designation": "Assistant Professor", "photo": ""},
                    {"no": "04", "name": "Mr KIRAN E", "qualification": "M. pharm", "designation": "Assistant Professor", "photo": ""},
                    {"no": "05", "name": "Mr LIKITH Y", "qualification": "M. pharm", "designation": "Assistant Professor", "photo": ""},
                    {"no": "06", "name": "Mr AKSHAYKUMAR V", "qualification": "M. pharm", "designation": "Assistant Professor", "photo": ""},
                    {"no": "07", "name": "Mr PRAVEENKUMAR", "qualification": "M. pharm", "designation": "Assistant Professor", "photo": ""},
                    {"no": "08", "name": "Mr SACHIN", "qualification": "M. pharm", "designation": "Assistant Professor", "photo": ""},
                    {"no": "09", "name": "Mr BIRADAR PANKAJ KALIDAS", "qualification": "M. pharm", "designation": "Assistant Professor", "photo": ""},
                    {"no": "10", "name": "Mr VINAY DHIMAN MAST RAM DHIMAN", "qualification": "M. pharm", "designation": "Assistant Professor", "photo": ""}
                ]
            },
            {
                "name": "Department of B.Sc / B.Com / BCA:",
                "staff": [
                    {"no": "01", "name": "RANI D/O MACHANDRA", "qualification": "M.Sc (Maths), B.Ed", "designation": "Maths", "photo": ""},
                    {"no": "02", "name": "SHEKHAR S/O SHAMRAO", "qualification": "M.Sc (Physics), B.Ed", "designation": "Physics", "photo": ""},
                    {"no": "03", "name": "ASHA W/O ASHISHKUMAR", "qualification": "M.Sc (Chemistry), B.Ed", "designation": "Chemistry", "photo": ""},
                    {"no": "04", "name": "IRFANMIYYA S/O ZAMEERMIYYA", "qualification": "M.C.A", "designation": "Computer", "photo": ""},
                    {"no": "05", "name": "AMBIKA D/O BALAJI", "qualification": "M.Sc (Zoology), B.Ed", "designation": "Zoology", "photo": ""},
                    {"no": "06", "name": "PUSHPARAJ", "qualification": "B.E (Electronics)", "designation": "Electronics", "photo": ""},
                    {"no": "07", "name": "SANJEEVANI W/O VEERSH SWAMY", "qualification": "M.Com (Accountancy)", "designation": "Principles & Practice of Accounting", "photo": ""},
                    {"no": "08", "name": "GANESH S/O VIJAYKUMAR", "qualification": "M.Sc (Computer)", "designation": "Computer", "photo": ""},
                    {"no": "09", "name": "MALASHREE D/O NAGNATH", "qualification": "M.Sc (Botany), B.Ed", "designation": "Botany", "photo": ""},
                    {"no": "10", "name": "PRATIBHA D/O TULSHIRAM", "qualification": "M.A (Hindi), B.Ed", "designation": "Hindi", "photo": ""},
                    {"no": "11", "name": "YESHODHA D/O VILASRAO", "qualification": "M.A (English), B.Ed", "designation": "English", "photo": ""},
                    {"no": "12", "name": "VANISHREE", "qualification": "M.Com, B.Ed", "designation": "Contemporary Marketing", "photo": ""},
                    {"no": "13", "name": "DEVENDRA", "qualification": "M.Com, B.Ed", "designation": "Corporate Business Behaviour", "photo": ""}
                ]
            }
        ]
    },
    "nonTeachingStaff": {
        "title": "Non-Teaching Staff",
        "staff": [
            {"no": "01", "name": "Mr. Dhanaji Rode", "qualification": "M.A., B.Ed.", "designation": "Administration", "photo": ""},
            {"no": "02", "name": "Mr. Sidhu", "qualification": "M.Com", "designation": "Accountant", "photo": ""},
            {"no": "03", "name": "Mr. Sumit Shivraj", "qualification": "B.Com,. Typestry", "designation": "Computer Operator", "photo": ""},
            {"no": "04", "name": "Smt. Sridevi", "qualification": "8th", "designation": "Sweeper", "photo": ""}
        ]
    },
    "facilitiesPage": {
        "title": "Our Facilities",
        "facilities": [
            {"name": "Library", "desc": "The Institute has established a spacious library & Information center providing National, International and E- Journals."},
            {"name": "Hostel", "desc": "Excellent hostel facilities have been provided for the students with round the clock security, nutritious and hygienic food."},
            {"name": "Transport", "desc": "Transport facility for the students is provided from all corners of the city driven by a team of well trained drivers."},
            {"name": "Sports", "desc": "The institute offers extensive facilities and maintains excellent sections for both outdoor sports and indoor games."},
            {"name": "Canteen", "desc": "The college canteen provides high quality nutritious food and snacks at affordable price throughout the academic year."},
            {"name": "Career Guidance", "desc": "We give training and guidance to students on career related matters and assist them in exploring new opportunities."}
        ]
    },
    "courses": {
        "b_pharm": {
            "title": "B. Pharm",
            "name": "B. Pharma",
            "description": "B. Pharmacy course is a four years program. This is affiliated to Osmania University and approved by Pharmacy Council of India (PCI) New Delhi. It is recognized by the Government of Telangana and the B. Pharmacy course is accredited by the National Board of Accreditation, New Delhi.",
            "scopeTitle": "Scope of B. Pharm",
            "scopeDesc": "A qualified pharmacist has a brilliant career shine in several areas, such as manufacture of bulk drugs, formulation of synthetic, biotechnology natural, cosmetic and other allied products. A few opportunities are mentioned below.",
            "scopeOpportunities": [
                "Production supervisor",
                "Analyst in Pharmaceutical companies",
                "Drug Inspector",
                "Government Analyst",
                "Pharmaceutical Marketing",
                "Hospital Administrator",
                "Teaching faculty",
                "Clinical pharmacist",
                "Community pharmacist",
                "Hospital pharmacist",
                "A lot more opportunities are available abroad for the Registered Pharmacists."
            ],
            "approvalTitle": "Approval of B. Pharmacy",
            "approvals": [
                "Approved by Pharmacy Council of India, New Delhi.",
                "Approved by TS State Council of Higher Education, Hyderabad.",
                "Approved by Commissioner of Technical Education, Government of Telangana.",
                "Affiliated to Osmania University, Hyderabad",
                "CCSEA (Animal experimentation permission)F No: 1175/PO/Re/S/08/CPCSEA, dated on 28/04/2022",
                "EXCISE PERMIT, RS licence bearing No (B/163/2018), Dt.27.06.2018, dated on 27.03.2021"
            ],
            "jobTitle": "B. Pharm graduates will have job opportunities in –",
            "jobs": [
                "Clinical Pharmacist",
                "Medical writing",
                "Hospitals and Healthcare Centres",
                "Clinical Trials",
                "Community Pharmacy",
                "Academics",
                "Pharmacovigilance and Drug Safety",
                "Drug regulatory"
            ],
            "eligibilityTitle": "Eligibility:",
            "eligibilityDesc": "In order to get admission in the course, candidates must meet the entry criteria for B. Pharm as mentioned below.",
            "eligibilityPoints": [
                "Candidate shall have passed 10+2 examination conducted by the respective State / Central government authorities with Physics, Chemistry, Mathematics (P.C.M) and or Biology (P.C.B/ P.C.M.B) as optional subjects individually with the required percentage of marks (50% overall Grade point average).",
                "Qualifying at the entrance examination (EAPCET) conducted by the State council of Higher Education.",
                "A pass in Diploma in Pharmacy (B.Pharm) course from an institution approved by the Pharmacy council of India under section 12 of the Pharmacy Act."
            ],
            "durationTitle": "Duration of the Course",
            "durationDesc": "The duration of the course shall be six academic years during which 5 years is academic session and sixth year is completely bound to internship or residency training in hospital, involving posting in specialty units. During six years, students are exposed to actual Pharmacy practice or Clinical pharmacy services and acquires skill under supervision so that he or she may become capable of functioning independent."
        },
        "d_pharm": {
            "title": "D. Pharm",
            "name": "D. Pharma",
            "description": "Doctor of Pharmacy (abbreviated as D. Pharm) course was developed with an objective of developing students to play an important role as Clinical Pharmacist. It was approved by Govt. of India in the year 2008 with Pharmacy Council of India being the apex body governing it.",
            "scopeTitle": "Scope of D. Pharm",
            "scopeDesc": "At the end of the course, the Clinical pharmacists develop and acquire knowledge and skill to provide pharmaceutical care services, drug and poison information services, patient counseling, identify drug-drug interactions, monitor adverse drug reactions, carry out therapeutic drug monitoring, help in drug dosage adjustment in special population, assist/co-ordinate in the conduct of clinical trials, promote rational use of medicines and ultimately contribute to better patient care.\n\nThere is a huge need of a D. Pharm course as now-a-days there are huge drug related problems, irrational drug use and non-compliance to therapy among patients suffering from various chronic diseases. Pharmaceutical care by a physician along with the technical expertise of clinical Pharmacist is the ultimate and best way of achieving better patient care.",
            "jobTitle": "D. Pharm graduates will have job opportunities in –",
            "jobs": [
                "Clinical Pharmacist",
                "Medical writing",
                "Hospitals and Healthcare Centres",
                "Clinical Trials",
                "Community Pharmacy",
                "Academics",
                "Pharmacovigilance and Drug Safety",
                "Drug regulatory"
            ],
            "eligibilityTitle": "Eligibility:",
            "eligibilityDesc": "In order to get admission in the course, candidates must meet the entry criteria for D. Pharm as mentioned below.",
            "eligibilityPoints": [
                "Candidate shall have passed 10+2 examination conducted by the respective State / Central government authorities with Physics, Chemistry, Mathematics (P.C.M) and or Biology (P.C.B/ P.C.M.B) as optional subjects individually with the required percentage of marks (50% overall Grade point average).",
                "Qualifying at the entrance examination (EAPCET) conducted by the State council of Higher Education.",
                "A pass in Diploma in Pharmacy (D.Pharm) course from an institution approved by the Pharmacy council of India under section 12 of the Pharmacy Act."
            ],
            "durationTitle": "Duration of the Course",
            "durationDesc": "The duration of the course shall be six academic years during which 5 years is academic session and sixth year is completely bound to internship or residency training in hospital, involving posting in specialty units. During six years, students are exposed to actual Pharmacy practice or Clinical pharmacy services and acquires skill under supervision so that he or she may become capable of functioning independent."
        },
        "b_sc": {
            "title": "B.Sc",
            "name": "Bachelor Of Science ( B.Sc. )",
            "description": "The college follows non-elitist polices of admission, in keeping with its ideals of education to all and social justice. Arunodaya First Grade Degree College Ring Road, Aurad (B) does not share the general perception of B.Sc. Courses being irrelevant. We value the understanding of the society and cultural process that the social sciences provide when pursued with interest. Each of the combinations offered will give the student a true multidisciplinary perspective into contemporary affairs\n\nAs per University regulation Part-I consists of Languages and Part-II optional subjects.",
            "part1Title": "PART-I: Candidates have to select any two Indian Languages they are:",
            "languages": ["Kannada", "English", "Hindi", "Urdu"],
            "forUgText": "For all UG courses like B.Sc/B.Com/BCA.",
            "part2Title": "PART-II",
            "combinations": [
                "Chemistry – Botany – Zoology",
                "Physics – Chemistry – Mathematics",
                "Physics – Mathematics – Computer Science",
                "Physics – Mathematics – Electronics",
                "Electronics – Mathematics – Computer Science",
                "Physics – Electronics – Computer Science"
            ],
            "semTitle": "B. Sc. I Semester",
            "semEligibility": [
                "A candidate who has passed the two year Pre-University examination of Karnataka State or any other examination considered as equivalent is eligible to get admission for first semester of B.Sc. Degree.",
                "A Candidate who has passed two years job-oriented P.U. Diploma Examination conducted by Director Vocational Education, Govt. of Karnataka (Excluding the subject in the existing regulations) is also eligible."
            ],
            "studyTitle": "Course Study",
            "studyPoints": [
                "The Maximum period for the completion of course will be of three years from the date of admission.",
                "The course consists of a combination of three subjects of equal importance and shall also consist of two languages and Compulsory subject such as, Indian Constitution, Environmental Studies and ECA.",
                "The medium of instruction shall be in English with exception in case of language papers. The medium of examination shall be in English."
            ],
            "docsTitle": "Documents Required For Admission",
            "docs": [
                "PUC II year Original Marks Card + Five Xerox copies",
                "Transfer Certificate Original + Five Xerox copies",
                "SC/ST Caste Certificate + Five Xerox copies",
                "OBC Original Certificate + Five Xerox copies",
                "Migration Certificate Original + Five Xerox copies (FOR other University/Board)",
                "Aadhar Card + Five Xerox copies",
                "Bank Account detail + Five Xerox copies",
                "Recent passport size Photos (05)"
            ],
            "footerText": "A Bachelor of Science receives the designation BSc or BS for a major/pass degree and BSc (Hons) or BS (Hons) for an honours degree."
        },
        "b_com": {
            "title": "B.Com",
            "name": "Bachelor Of Commerce ( B.Com. )",
            "description": "The college follows non-elitist polices of admission, in keeping with its ideals of education to all and social justice. Arunodaya First Grade Degree College Ring Road, Aurad (B) does not share the general perception of B.Com. Courses being irrelevant. We value the understanding of the society and cultural process that the social sciences provide when pursued with interest. Each of the combinations offered will give the student a true multidisciplinary perspective into contemporary affairs\n\nAs per University regulation Part-I consists of Languages and Part-II optional subjects.",
            "part1Title": "PART-I: Candidates have to select any two Indian Languages they are:",
            "languages": ["Kannada", "English", "Hindi", "Urdu"],
            "forUgText": "For all UG courses like B.Sc/B.Com/BCA.",
            "part2Title": "PART-II",
            "combinations": [
                "Accounting",
                "Business law",
                "Economics",
                "Financial Management",
                "Business Computing"
            ],
            "semTitle": "B.Com. I Semester",
            "semEligibility": [
                "A candidate who has passed the two year Pre-University examination of Karnataka State or any other examination considered as equivalent is eligible for admission to first semester of B.Com. Degree.",
                "A candidate who has passed two year job-oriented Pre-University Diploma examination conducted by the Director of Vocational Education Government of Karnataka is eligible for admission.",
                "A candidate who has passed the Diploma course in commercial practice/secretarial practice examination conducted by the Board of Technical Education, Government of Karnataka is eligible for Third Semester subject to the condition that he/she should pass the subjects prescribed for First and Second Semester of B.Com. Degree Course which he/she has not studied at the said Diploma Course."
            ],
            "docsTitle": "Documents Required For Admission",
            "docs": [
                "PUC II year Original Marks Card + Five Xerox copies",
                "Transfer Certificate Original + Five Xerox copies",
                "SC/ST Caste Certificate + Five Xerox copies",
                "OBC Original Certificate + Five Xerox copies",
                "Migration Certificate Original + Five Xerox copies (FOR other University/Board)",
                "Aadhar Card + Five Xerox copies",
                "Bank Account detail + Five Xerox copies",
                "Recent passport size Photos (05)"
            ],
            "footerText": "Bachelor of Commerce"
        },
        "bca": {
            "title": "BCA",
            "name": "Bachelor Of Computer Applications ( BCA )",
            "description": "The college follows non-elitist polices of admission, in keeping with its ideals of education to all and social justice. Arunodaya First Grade Degree College Ring Road, Aurad (B) does not share the general perception of BCA. Courses being irrelevant. We value the understanding of the society and cultural process that the social sciences provide when pursued with interest. Each of the combinations offered will give the student a true multidisciplinary perspective into contemporary affairs\n\nAs per University regulation Part-I consists of Languages and Part-II optional subjects.",
            "part1Title": "PART-I: Candidates have to select any two Indian Languages they are:",
            "languages": ["Kannada", "English", "Hindi", "Urdu"],
            "forUgText": "For all UG courses like B.Sc/B.Com/BCA.",
            "eligibilityTitle": "Eligibility",
            "eligibilityPoints": [
                "A candidate who has passed the Two Year Pre-University Examination of Karnataka State OR any other examination considered as equivalent thereto and has studied Mathematics as one of the subjects/PUC Commerce is eligible for admission",
                "A candidate who has passed the Two Year Job Oriented Pre-University Diploma examination with Computer Science/Electrical subject conducted by the Directorate of Vocational Education, Government of Karnataka is eligible for admission.",
                "A candidate who has passed the Diploma in Computer Science Examination conducted by the Board of Technical Education, Government of Karnataka, shall be eligible for admission."
            ],
            "semTitle": "I SEMESTER",
            "subjects": [
                "English",
                "Any Indian Language",
                "Extra Curricular Activities",
                "Foundation Course in Mathematics for Computing-I",
                "Computer Fundamentals & Office Automation",
                "C-Programming",
                "Programming Lab-I"
            ],
            "exemptionTitle": "CLAIM OF EXEMPTION",
            "exemptionPoints": [
                "A candidate who keeps terms for I, III and V Semesters be allowed to keep terms for II, IV and VI Semesters, respectively, subject to the following conditions.",
                "A candidate who passes 50% of Theory and Practical put together of I and II semester examinations (at the end of II Semester) be allowed to keep terms for III Semester",
                "A candidate who has passed I and II Semester and 50% of Theory and Practical put together of III and IV Semester examinations (at the end of IV Semester) be allowed to keep terms for V Semester."
            ],
            "docsTitle": "Documents Required For Admission",
            "docs": [
                "PUC II year Original Marks Card + Five Xerox copies",
                "Transfer Certificate Original + Five Xerox copies",
                "SC/ST Caste Certificate + Five Xerox copies",
                "OBC Original Certificate + Five Xerox copies",
                "Migration Certificate Original + Five Xerox copies (FOR other University/Board)",
                "Aadhar Card + Five Xerox copies",
                "Bank Account detail + Five Xerox copies",
                "Recent passport size Photos (05)"
            ],
            "footerText": "Bachelor of Computer Application (B.C.A.) Degree shall extend over a period of Three Years consisting of Six Semester."
        }
    },
    "syllabus": {
        "title": "Syllabus",
        "headers": ["#", "Course Name", "Year", "Syllabus Attachment"],
        "rows": [
            {
                "no": "1",
                "courseName": "D Pharmacy",
                "year": "Revised Academic Calendar UG & PG AY 2023-24",
                "attachmentText": "Click Here For File…",
                "link": "wp-content/uploads/2024/07/ER-2020-SYLLABUS-TIME-DURATION-SUBJECTWISE-PART-I-AND-PART-II.pdf"
            }
        ]
    },
    "academic_calendar": {
        "title": "Academic Calendar",
        "headers": ["#", "Course Name", "Year", "Syllabus Attachment"],
        "rows": [
            {
                "no": "1",
                "courseName": "D Pharmacy",
                "year": "Calender of Events Part II academic year 2023-24",
                "attachmentText": "Click Here For File…",
                "link": "wp-content/uploads/2024/07/Calender-of-Events-for-D.Pharm-Part-II-academic-year-2023-24-dt.-8.5.2024.pdf"
            },
            {
                "no": "1",
                "courseName": "D Pharmacy",
                "year": "Calender events part 1 (2023-2024)",
                "attachmentText": "Click Here For File…",
                "link": "wp-content/uploads/2024/07/calender-events-part-1-2023-2024.pdf"
            }
        ]
    },
    "time_table": {
        "title": "Time Table",
        "headers": ["#", "Course Name", "Year", "Syllabus Attachment"],
        "rows": [
            {
                "no": "1",
                "courseName": "D Pharmacy",
                "year": "D. pharmacy part- I part – II regular theory timetable",
                "attachmentText": "Click Here For File…",
                "link": "wp-content/uploads/2024/07/dpharmacy-part-I-part-II-regular-theory-timetable.pdf"
            },
            {
                "no": "1",
                "courseName": "B.Sc / B.Com / BCA timetable",
                "year": "B.Sc/B.Com/BCA All Sem timetable",
                "attachmentText": "Click Here For File…",
                "link": "wp-content/uploads/2025/11/ARUNODAYA-FIRST-GRADE-DEGREE-COLLEGE-TIME-TABLE-TEACHING-STAFF-DETAILS-1.pdf"
            }
        ]
    },
    "gallery": {
        "title": "Gallery",
        "images": [
            {"src": "wp-content/uploads/2024/07/COLLEGE-BUS.jpeg", "title": "College Bus"},
            {"src": "wp-content/uploads/2024/07/Enquiry-Office.jpeg", "title": "Enquiry Office"},
            {"src": "wp-content/uploads/2024/05/about-collage.png", "title": "About College"},
            {"src": "wp-content/uploads/2024/07/COLLEGE-BUS-2.jpeg", "title": "College Bus 2"},
            {"src": "wp-content/uploads/2024/08/WhatsApp-Image-2024-07-24-at-10.48.56.jpeg", "title": "Campus View"},
            {"src": "wp-content/uploads/2024/07/2-WHEELER-PARKING.jpeg", "title": "2 Wheeler Parking"},
            {"src": "wp-content/uploads/2024/07/purified-water-filter.jpeg", "title": "Purified Water Filter"},
            {"src": "wp-content/uploads/2024/05/Pharmacy.png", "title": "Pharmacy Block"},
            {"src": "wp-content/uploads/2024/07/Herbal-Garden-2.jpeg", "title": "Herbal Garden 2"},
            {"src": "wp-content/uploads/2022/10/home.jpg", "title": "Home View"},
            {"src": "wp-content/uploads/2024/05/addmision.png", "title": "Admission Block"},
            {"src": "wp-content/uploads/2024/08/WhatsApp-Image-2024-07-24-at-10.48.55-1.jpeg", "title": "Laboratory"},
            {"src": "wp-content/uploads/2024/08/WhatsApp-Image-2024-07-24-at-10.48.56-1.jpeg", "title": "Classroom View"},
            {"src": "wp-content/uploads/2024/07/college-photo-2.jpeg", "title": "College Photo 2"},
            {"src": "wp-content/uploads/2024/08/WhatsApp-Image-2024-07-24-at-10.48.55.jpeg", "title": "Lab Facilities"},
            {"src": "wp-content/uploads/2024/05/slider2.png", "title": "Banner Slide 2"},
            {"src": "wp-content/uploads/2024/07/College-cultural-center.jpeg", "title": "Cultural Center"},
            {"src": "wp-content/uploads/2024/07/GENERATOR.jpeg", "title": "Generator Power"},
            {"src": "wp-content/uploads/2022/10/effective-supply-chain.jpg", "title": "Effective Supply Chain"},
            {"src": "wp-content/uploads/2024/07/part-1-theory-class.jpeg", "title": "Theory Class"},
            {"src": "wp-content/uploads/2024/05/slider1.png", "title": "Banner Slide 1"},
            {"src": "wp-content/uploads/2024/05/way.png", "title": "Main Pathway"},
            {"src": "wp-content/uploads/2024/07/herbal-Garden-1.jpeg", "title": "Herbal Garden 1"},
            {"src": "wp-content/uploads/2024/07/college-photo.jpeg", "title": "College Building"},
            {"src": "wp-content/uploads/2024/07/audotorium-hall.jpeg", "title": "Auditorium Hall"},
            {"src": "wp-content/uploads/2024/07/VEHICLE-PARKING.jpeg", "title": "Vehicle Parking"},
            {"src": "wp-content/uploads/2022/10/financial-growth-reporting.jpg", "title": "Financial Growth"},
            {"src": "wp-content/uploads/2024/07/LADEIS-TOILET.jpeg", "title": "Facilities block"},
            {"src": "wp-content/uploads/2024/08/WhatsApp-Image-2024-07-24-at-10.48.54.jpeg", "title": "Main Entrance View"}
        ]
    },
    "newsEvents": {
        "title": "News & Events",
        "posts": [
            {
                "title": "Hello world!",
                "category": "Uncategorized",
                "desc": "Welcome to WordPress. This is your first post. Edit or delete it, then start writing!",
                "date": "2024-05-23"
            },
            {
                "title": "Streamline exceptional process & unleash your collaboration",
                "category": "Finance",
                "desc": "Monetize proactive your e-business & access to accurate experiences. Streamline exceptional process & unleash your collaboration to drive dynamic growth.",
                "date": "2024-05-20"
            },
            {
                "title": "Monetize proactive your e-business & access to accurate experiences",
                "category": "Business Relations",
                "desc": "Understand the value & background of all public relation trends. Maintain value-added scenarios to grow your business mission.",
                "date": "2024-05-18"
            },
            {
                "title": "How to have a fantastic career opportunity with minimal spending",
                "category": "Audit & Taxation",
                "desc": "Discover the options and routes to building an amazing profession without high debt. High quality courses with career guidance make the difference.",
                "date": "2024-05-15"
            },
            {
                "title": "Maintain value-added scenarios to grow your business mission",
                "category": "Audit & Taxation",
                "desc": "Grow your business mission by maintaining value-added scenarios. Proactively adapt to changing guidelines and trends.",
                "date": "2024-05-12"
            },
            {
                "title": "Understanding the value & background of all public relation trends",
                "category": "Business Relations",
                "desc": "Public relations trends are changing at a fast velocity. Learn the value and background behind these changes to capitalize on future openings.",
                "date": "2024-05-10"
            },
            {
                "title": "Things you should know before getting into the business industry",
                "category": "Finance",
                "desc": "Entering the finance and business fields requires critical skills and solid preparation. Learn what to study and how to build a portfolio.",
                "date": "2024-05-08"
            }
        ],
        "sidebar": {
            "aboutTitle": "about avada business",
            "aboutText": "Integer euismod lacus magna uisque curd metus luctus vitae pharet auctor mattis semat.",
            "confTitle": "2026 Business Conference",
            "confDate": "15-18 December",
            "confLocation": "New York City",
            "confBtn": "book your seat"
        }
    },
    "contact": {
        "title": "Contact Us",
        "description": "Cuisque cursus metus vitae sed pharetra auctor semy magna augued egets diam. Vestibulum interdum ante ipsum faucibus luctus ultrices posuere ipsum sed cubilia.",
        "officeTitle": "office location",
        "officeAddress": "Arunodaya College of Pharmacy Aurad (B), Bidar-585403, Kranataka",
        "emailTitle": "Email our team",
        "emailList": ["Murthy.sridhara@yahoo.com", "satish99belkone@gmail.com"],
        "hoursTitle": "working hours",
        "hours": "Monday to Friday : 10 am – 4 pm",
        "subText": "Passionate – Dedicated – Professional",
        "formTitle": "Send your query or request a callback",
        "phoneTitle": "Let’s talk about your next project",
        "phoneNumber": "+91 9921877870",
        "mapTitle": "Aurad ಔರಾದ್ Karnataka 585326",
        "mapSubtitle": "Magni blanditiis expedita internos. Sed odio pariatur qui voluptatem."
    }
}

# Write content.js if not exists
if not os.path.exists(os.path.join(workspace_dir, "content.js")):
    with open(os.path.join(workspace_dir, "content.js"), "w", encoding="utf-8") as f:
        f.write(f"const siteContent = {json.dumps(content_data, indent=4, ensure_ascii=False)};\n")

# 2. Create style.css
style_css = """@import url('https://fonts.googleapis.com/css2?family=Mulish:ital,wght@0,300;0,400;0,600;0,700;0,800;1,400&family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap');

body {
    font-family: 'Mulish', sans-serif;
    overflow-x: hidden;
}

h1, h2, h3, h4, h5, h6, .font-poppins {
    font-family: 'Poppins', sans-serif;
}

/* Custom Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-track {
    background: #f1f1f1;
}
::-webkit-scrollbar-thumb {
    background: #0158a5;
    border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
    background: #0c2b5c;
}

/* Animations */
@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.animate-slide-up {
    animation: slideUp 0.8s ease-out forwards;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.animate-fade-in {
    animation: fadeIn 1s ease-in forwards;
}

/* Announcements Vertical Ticker */
.ticker-container {
    height: 320px;
    overflow: hidden;
    position: relative;
}

.ticker-wrapper {
    position: absolute;
    width: 100%;
    animation: ticker-animation 30s linear infinite;
}

.ticker-wrapper:hover {
    animation-play-state: paused;
}

@keyframes ticker-animation {
    0% { transform: translateY(0); }
    100% { transform: translateY(-50%); }
}

/* Submenu Dropdown transitions */
.dropdown:hover .dropdown-menu {
    display: block;
    opacity: 1;
    transform: translateY(0);
}

.dropdown-menu {
    display: none;
    opacity: 0;
    transform: translateY(10px);
    transition: all 0.3s ease;
}

/* Lightbox Modal */
.lightbox-modal {
    display: none;
    position: fixed;
    z-index: 9999;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.9);
}

.lightbox-content {
    margin: auto;
    display: block;
    max-width: 90%;
    max-height: 80%;
    transition: transform 0.25s ease;
}

.lightbox-caption {
    margin: auto;
    display: block;
    width: 80%;
    text-align: center;
    color: #ccc;
    padding: 10px 0;
}

/* Simple Banner Slider CSS */
.hero-slider {
    position: relative;
    height: 480px;
    width: 100%;
    overflow: hidden;
}
@media (max-width: 768px) {
    .hero-slider {
        height: 280px;
    }
}
.hero-slide {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0;
    transition: opacity 1s ease-in-out;
    background-size: cover;
    background-position: center;
}
.hero-slide.active {
    opacity: 1;
}

/* Table Style custom */
table {
    border-collapse: collapse !important;
}
th, td {
    border: 1px solid #cbd5e1 !important;
}
"""

if not os.path.exists(os.path.join(workspace_dir, "style.css")):
    with open(os.path.join(workspace_dir, "style.css"), "w", encoding="utf-8") as f:
        f.write(style_css)

# 3. Create main.js
main_js = """// Utility function to resolve image URL based on fallback config
function resolveImageUrl(src) {
    if (!src) return '';
    if (src.startsWith('http') || src.startsWith('//') || src.startsWith('data:')) {
        return src;
    }
    if (siteContent.config.useLiveImageFallback) {
        return siteContent.config.liveBaseUrl + src;
    }
    return src;
}

// Global Image Error handling / blank styling
function setElementImage(elementId, src, alt = '') {
    const el = document.getElementById(elementId);
    if (el) {
        el.src = resolveImageUrl(src);
        if (alt) el.alt = alt;
        el.onerror = function() {
            // Replaces image with a clean premium grey block
            el.style.display = 'none';
            const placeholder = document.createElement('div');
            placeholder.className = 'w-full h-full min-h-[160px] bg-slate-100 text-slate-400 flex flex-col items-center justify-center p-4 text-center rounded border border-slate-200';
            placeholder.innerHTML = `<i class="fa-regular fa-image text-3xl mb-2 text-slate-300"></i><span class="text-xs font-semibold uppercase tracking-wider">${alt || 'Image'}</span>`;
            el.parentNode.insertBefore(placeholder, el);
        };
    }
}

// Render Top Bar and Navigation Header
function renderHeader() {
    const topBar = document.getElementById('top-bar');
    if (topBar) {
        topBar.className = "bg-brandCyan text-white text-sm py-2 px-4 md:px-12 flex flex-col md:flex-row justify-between items-center z-50 relative gap-2";
        topBar.innerHTML = `
            <div class="flex flex-col sm:flex-row items-center gap-4">
                <a href="tel:${siteContent.header.phone}" class="flex items-center gap-1 hover:text-brandNavy transition-colors font-semibold">
                    <i class="fa-solid fa-mobile-alt"></i> ${siteContent.header.phone}
                </a>
                <a href="mailto:${siteContent.header.email}" class="flex items-center gap-1 hover:text-brandNavy transition-colors font-semibold">
                    <i class="fa-solid fa-envelope"></i> ${siteContent.header.email}
                </a>
            </div>
            <div class="w-full md:w-1/2 overflow-hidden relative">
                <marquee onmouseover="this.stop();" onmouseout="this.start();" scrollamount="4" class="font-bold text-center block">
                    ${siteContent.header.marqueeDesktop}
                </marquee>
            </div>
        `;
    }

    const mainHeader = document.getElementById('main-header');
    if (mainHeader) {
        mainHeader.className = "bg-white shadow-md relative z-40";
        
        // Active page extraction
        const path = window.location.pathname;
        const page = path.substring(path.lastIndexOf('/') + 1) || 'index.html';
        
        const isHome = page === 'index.html';
        const isAbout = page === 'about.html';
        const isAdmission = page === 'admission-process.html';
        const isFaculty = ['teaching-staff.html', 'non-teaching-staff.html'].includes(page);
        const isFacilities = page === 'facilities.html';
        const isCourses = ['b-pharm.html', 'd-pharm.html', 'b-sc.html', 'b-com.html', 'bca.html'].includes(page);
        const isAcademic = ['syllabus.html', 'academic-calendar.html', 'time-table.html'].includes(page);
        const isGallery = page === 'gallery.html';
        const isNews = page === 'news-events.html';
        const isContact = page === 'contact-us.html';

        mainHeader.innerHTML = `
            <div class="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
                <!-- Logo -->
                <a href="index.html" class="flex items-center gap-3">
                    <img id="header-logo-img" class="h-16 md:h-20 object-contain" alt="Arunodaya Institutions Logo">
                </a>

                <!-- Desktop Nav -->
                <nav class="hidden xl:flex items-center gap-6">
                    <ul class="flex items-center gap-6 text-[15px] font-bold text-brandNavy font-sans tracking-wide">
                        <li class="relative py-2">
                            <a href="index.html" class="hover:text-brandCyan transition-colors ${isHome ? 'text-brandCyan border-b-2 border-brandCyan pb-1' : ''}">Home</a>
                        </li>
                        <li class="relative py-2">
                            <a href="about.html" class="hover:text-brandCyan transition-colors ${isAbout ? 'text-brandCyan border-b-2 border-brandCyan pb-1' : ''}">About Us</a>
                        </li>
                        <li class="relative py-2">
                            <a href="admission-process.html" class="hover:text-brandCyan transition-colors ${isAdmission ? 'text-brandCyan border-b-2 border-brandCyan pb-1' : ''}">Admission</a>
                        </li>
                        
                        <!-- Faculty Dropdown -->
                        <li class="dropdown relative py-2 cursor-pointer group">
                            <span class="hover:text-brandCyan transition-colors flex items-center gap-1 ${isFaculty ? 'text-brandCyan border-b-2 border-brandCyan pb-1' : ''}">
                                Faculty <i class="fa-solid fa-angle-down text-xs"></i>
                            </span>
                            <ul class="dropdown-menu absolute left-0 mt-2 w-48 bg-brandNavy text-white rounded-b-xl py-2 shadow-lg hidden group-hover:block transition-all duration-300">
                                <li><a href="teaching-staff.html" class="block px-4 py-2 hover:bg-brandCyan hover:text-brandNavy transition-colors font-semibold">Teaching Staff</a></li>
                                <li><a href="non-teaching-staff.html" class="block px-4 py-2 hover:bg-brandCyan hover:text-brandNavy transition-colors font-semibold">Non-Teaching Staff</a></li>
                            </ul>
                        </li>

                        <li class="relative py-2">
                            <a href="facilities.html" class="hover:text-brandCyan transition-colors ${isFacilities ? 'text-brandCyan border-b-2 border-brandCyan pb-1' : ''}">Facilities</a>
                        </li>

                        <!-- Courses Dropdown -->
                        <li class="dropdown relative py-2 cursor-pointer group">
                            <span class="hover:text-brandCyan transition-colors flex items-center gap-1 ${isCourses ? 'text-brandCyan border-b-2 border-brandCyan pb-1' : ''}">
                                Courses <i class="fa-solid fa-angle-down text-xs"></i>
                            </span>
                            <ul class="dropdown-menu absolute left-0 mt-2 w-48 bg-brandNavy text-white rounded-b-xl py-2 shadow-lg hidden group-hover:block transition-all duration-300">
                                <li><a href="b-pharm.html" class="block px-4 py-2 hover:bg-brandCyan hover:text-brandNavy transition-colors font-semibold">B. Pharm</a></li>
                                <li><a href="d-pharm.html" class="block px-4 py-2 hover:bg-brandCyan hover:text-brandNavy transition-colors font-semibold">D. Pharm</a></li>
                                <li><a href="b-sc.html" class="block px-4 py-2 hover:bg-brandCyan hover:text-brandNavy transition-colors font-semibold">B.Sc</a></li>
                                <li><a href="b-com.html" class="block px-4 py-2 hover:bg-brandCyan hover:text-brandNavy transition-colors font-semibold">B.Com</a></li>
                                <li><a href="bca.html" class="block px-4 py-2 hover:bg-brandCyan hover:text-brandNavy transition-colors font-semibold">BCA</a></li>
                            </ul>
                        </li>

                        <!-- Academic Dropdown -->
                        <li class="dropdown relative py-2 cursor-pointer group">
                            <span class="hover:text-brandCyan transition-colors flex items-center gap-1 ${isAcademic ? 'text-brandCyan border-b-2 border-brandCyan pb-1' : ''}">
                                Academic <i class="fa-solid fa-angle-down text-xs"></i>
                            </span>
                            <ul class="dropdown-menu absolute left-0 mt-2 w-48 bg-brandNavy text-white rounded-b-xl py-2 shadow-lg hidden group-hover:block transition-all duration-300">
                                <li><a href="syllabus.html" class="block px-4 py-2 hover:bg-brandCyan hover:text-brandNavy transition-colors font-semibold">Syllabus</a></li>
                                <li><a href="academic-calendar.html" class="block px-4 py-2 hover:bg-brandCyan hover:text-brandNavy transition-colors font-semibold">Academic Calendar</a></li>
                                <li><a href="time-table.html" class="block px-4 py-2 hover:bg-brandCyan hover:text-brandNavy transition-colors font-semibold">Time Table</a></li>
                            </ul>
                        </li>

                        <li class="relative py-2">
                            <a href="gallery.html" class="hover:text-brandCyan transition-colors ${isGallery ? 'text-brandCyan border-b-2 border-brandCyan pb-1' : ''}">Gallery</a>
                        </li>
                        <li class="relative py-2">
                            <a href="news-events.html" class="hover:text-brandCyan transition-colors ${isNews ? 'text-brandCyan border-b-2 border-brandCyan pb-1' : ''}">News & Events</a>
                        </li>
                        <li class="relative py-2">
                            <a href="contact-us.html" class="hover:text-brandCyan transition-colors ${isContact ? 'text-brandCyan border-b-2 border-brandCyan pb-1' : ''}">Contact Us</a>
                        </li>
                    </ul>
                </nav>

                <!-- Mobile Menu Button -->
                <button id="mobile-menu-btn" class="xl:hidden text-brandNavy text-3xl focus:outline-none">
                    <i class="fa-solid fa-bars"></i>
                </button>
            </div>

            <!-- Mobile Drawer -->
            <div id="mobile-drawer" class="fixed inset-0 bg-brandNavy bg-opacity-95 text-white z-50 transform translate-x-full transition-transform duration-300 xl:hidden">
                <div class="flex justify-between items-center p-6 border-b border-slate-700">
                    <img id="mobile-logo-img" class="h-12 object-contain" alt="Arunodaya Logo">
                    <button id="mobile-menu-close" class="text-3xl"><i class="fa-solid fa-xmark"></i></button>
                </div>
                <div class="p-6 overflow-y-auto h-[calc(100vh-80px)]">
                    <ul class="flex flex-col gap-5 text-lg font-bold">
                        <li><a href="index.html" class="block py-1 hover:text-brandCyan transition-colors">Home</a></li>
                        <li><a href="about.html" class="block py-1 hover:text-brandCyan transition-colors">About Us</a></li>
                        <li><a href="admission-process.html" class="block py-1 hover:text-brandCyan transition-colors">Admission</a></li>
                        <li class="border-t border-slate-700 pt-3">
                            <span class="block text-slate-400 text-sm mb-2 uppercase tracking-widest font-semibold">Faculty</span>
                            <ul class="pl-4 flex flex-col gap-2 text-md">
                                <li><a href="teaching-staff.html" class="hover:text-brandCyan">Teaching Staff</a></li>
                                <li><a href="non-teaching-staff.html" class="hover:text-brandCyan">Non-Teaching Staff</a></li>
                            </ul>
                        </li>
                        <li><a href="facilities.html" class="block py-1 hover:text-brandCyan transition-colors">Facilities</a></li>
                        <li class="border-t border-slate-700 pt-3">
                            <span class="block text-slate-400 text-sm mb-2 uppercase tracking-widest font-semibold">Courses</span>
                            <ul class="pl-4 flex flex-col gap-2 text-md">
                                <li><a href="b-pharm.html" class="hover:text-brandCyan">B. Pharm</a></li>
                                <li><a href="d-pharm.html" class="hover:text-brandCyan">D. Pharm</a></li>
                                <li><a href="b-sc.html" class="hover:text-brandCyan">B.Sc</a></li>
                                <li><a href="b-com.html" class="hover:text-brandCyan">B.Com</a></li>
                                <li><a href="bca.html" class="hover:text-brandCyan">BCA</a></li>
                            </ul>
                        </li>
                        <li class="border-t border-slate-700 pt-3">
                            <span class="block text-slate-400 text-sm mb-2 uppercase tracking-widest font-semibold">Academic</span>
                            <ul class="pl-4 flex flex-col gap-2 text-md">
                                <li><a href="syllabus.html" class="hover:text-brandCyan">Syllabus</a></li>
                                <li><a href="academic-calendar.html" class="hover:text-brandCyan">Academic Calendar</a></li>
                                <li><a href="time-table.html" class="hover:text-brandCyan">Time Table</a></li>
                            </ul>
                        </li>
                        <li><a href="gallery.html" class="block py-1 hover:text-brandCyan transition-colors">Gallery</a></li>
                        <li><a href="news-events.html" class="block py-1 hover:text-brandCyan transition-colors">News & Events</a></li>
                        <li><a href="contact-us.html" class="block py-1 hover:text-brandCyan transition-colors">Contact Us</a></li>
                    </ul>
                </div>
            </div>
        `;

        // Bind Logo
        setElementImage('header-logo-img', siteContent.header.logoHeader, 'Arunodaya Logo');
        setElementImage('mobile-logo-img', siteContent.header.logoHeaderWhite, 'Arunodaya Logo');

        // Mobile Menu interactions
        const btn = document.getElementById('mobile-menu-btn');
        const drawer = document.getElementById('mobile-drawer');
        const close = document.getElementById('mobile-menu-close');

        if (btn && drawer && close) {
            btn.onclick = () => drawer.classList.remove('translate-x-full');
            close.onclick = () => drawer.classList.add('translate-x-full');
        }
    }
}

// Render Footer
function renderFooter() {
    const mainFooter = document.getElementById('main-footer');
    if (mainFooter) {
        mainFooter.className = "bg-slate-800 text-white mt-12 relative font-sans";
        mainFooter.innerHTML = `
            <!-- Query / CTA box -->
            <div class="max-w-6xl mx-auto px-4 -translate-y-12">
                <div class="bg-brandNavy text-white rounded-bl-3xl rounded-tr-3xl p-8 shadow-xl flex flex-col md:flex-row justify-between items-center gap-6 border-b-4 border-brandCyan">
                    <div class="text-center md:text-left md:w-3/4">
                        <h3 class="text-2xl font-bold font-poppins mb-2">${siteContent.footer.ctaTitle}</h3>
                        <p class="text-slate-300 text-[15px] leading-relaxed">${siteContent.footer.ctaText}</p>
                    </div>
                    <div class="md:w-1/4 text-center">
                        <a href="contact-us.html" class="inline-flex items-center gap-2 bg-brandGreen hover:bg-brandCyan text-brandNavy font-bold py-3 px-6 rounded-full shadow transition-all duration-300 group">
                            <span>${siteContent.footer.ctaBtnText}</span>
                            <i class="fa-solid fa-angle-right group-hover:translate-x-1 transition-transform"></i>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Footer Main columns -->
            <div class="max-w-7xl mx-auto px-6 pb-12 grid grid-cols-1 md:grid-cols-3 gap-10">
                <!-- Col 1: Bio -->
                <div class="flex flex-col gap-4">
                    <img id="footer-logo-img" class="h-16 w-fit object-contain mb-2" alt="Footer Logo">
                    <p class="text-slate-300 text-[15px] leading-relaxed text-justify">${siteContent.footer.bio}</p>
                </div>

                <!-- Col 2: Quick Links -->
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <h4 class="text-lg font-bold border-b-2 border-brandGreen w-fit pb-1 mb-4 font-poppins">Quick Links</h4>
                        <ul class="flex flex-col gap-2 text-[15px] text-slate-300">
                            ${siteContent.footer.quickLinksCol1.map(link => {
                                let url = "index.html";
                                if (link === "About Us") url = "about.html";
                                else if (link === "Admission") url = "admission-process.html";
                                else if (link === "Facilities") url = "facilities.html";
                                else if (link === "Gallery") url = "gallery.html";
                                else if (link === "News & Events") url = "news-events.html";
                                else if (link === "Contact Us") url = "contact-us.html";
                                return `<li><a href="${url}" class="hover:text-brandCyan transition-colors">${link}</a></li>`;
                            }).join('')}
                        </ul>
                    </div>
                    <div>
                        <h4 class="text-lg font-bold border-b-2 border-brandGreen w-fit pb-1 mb-4 font-poppins">Programs</h4>
                        <ul class="flex flex-col gap-2 text-[15px] text-slate-300">
                            ${siteContent.footer.quickLinksCol2.map(link => {
                                let url = "#";
                                if (link === "Gallery") url = "gallery.html";
                                return `<li><a href="${url}" class="hover:text-brandCyan transition-colors">${link}</a></li>`;
                            }).join('')}
                        </ul>
                    </div>
                </div>

                <!-- Col 3: Contact -->
                <div class="flex flex-col gap-4">
                    <h4 class="text-lg font-bold border-b-2 border-brandGreen w-fit pb-1 mb-4 font-poppins">Reach Us At</h4>
                    <ul class="flex flex-col gap-3 text-[15px] text-slate-300">
                        <li class="flex gap-3">
                            <span class="bg-brandGreen text-brandNavy h-9 w-9 flex items-center justify-center rounded-full shrink-0 font-bold"><i class="fa-solid fa-map-marker-alt"></i></span>
                            <span>${siteContent.footer.contactAddress}</span>
                        </li>
                        <li class="flex gap-3">
                            <span class="bg-brandGreen text-brandNavy h-9 w-9 flex items-center justify-center rounded-full shrink-0 font-bold"><i class="fa-solid fa-mobile-alt"></i></span>
                            <span>${siteContent.footer.contactPhone}</span>
                        </li>
                        <li class="flex gap-3">
                            <span class="bg-brandGreen text-brandNavy h-9 w-9 flex items-center justify-center rounded-full shrink-0 font-bold"><i class="fa-solid fa-envelope"></i></span>
                            <span class="break-all">${siteContent.footer.contactEmail}</span>
                        </li>
                    </ul>
                </div>
            </div>

            <!-- Big number banner -->
            <div class="bg-slate-900 border-t border-slate-700 py-6 text-center text-3xl md:text-5xl font-black font-poppins tracking-wider text-slate-400 bg-opacity-50">
                ${siteContent.footer.contactHugeNumber}
            </div>

            <!-- Bottom Copyright / Socials -->
            <div class="bg-brandNavy py-4 px-6 border-t border-slate-700">
                <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-4 text-sm text-slate-400">
                    <p class="font-semibold text-center md:text-left">${siteContent.footer.copyright}</p>
                    <div class="flex items-center gap-4">
                        <a href="#" class="h-8 w-8 rounded bg-slate-700 hover:bg-brandCyan hover:text-brandNavy flex items-center justify-center text-white transition-all"><i class="fa-brands fa-facebook-f"></i></a>
                        <a href="#" class="h-8 w-8 rounded bg-slate-700 hover:bg-brandCyan hover:text-brandNavy flex items-center justify-center text-white transition-all"><i class="fa-brands fa-twitter"></i></a>
                        <a href="#" class="h-8 w-8 rounded bg-slate-700 hover:bg-brandCyan hover:text-brandNavy flex items-center justify-center text-white transition-all"><i class="fa-brands fa-instagram"></i></a>
                        <a href="#" class="h-8 w-8 rounded bg-slate-700 hover:bg-brandCyan hover:text-brandNavy flex items-center justify-center text-white transition-all"><i class="fa-brands fa-pinterest-p"></i></a>
                        <a href="#" class="h-8 w-8 rounded bg-slate-700 hover:bg-brandCyan hover:text-brandNavy flex items-center justify-center text-white transition-all"><i class="fa-brands fa-linkedin-in"></i></a>
                    </div>
                </div>
            </div>
        `;

        setElementImage('footer-logo-img', siteContent.footer.logoFooter, 'Footer Logo');
    }
}

// ---------------------------------
// PAGE SPECIFIC LOADING BEHAVIORS
// ---------------------------------

function initHomePage() {
    // 1. Slider Setup
    const sliderContainer = document.getElementById('hero-slider');
    if (sliderContainer) {
        sliderContainer.innerHTML = siteContent.home.sliderImages.map((src, idx) => `
            <div class="hero-slide ${idx === 0 ? 'active' : ''}" style="background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('${resolveImageUrl(src)}');"></div>
        `).join('');

        let currentSlide = 0;
        const slides = sliderContainer.getElementsByClassName('hero-slide');
        if (slides.length > 0) {
            setInterval(() => {
                slides[currentSlide].classList.remove('active');
                currentSlide = (currentSlide + 1) % slides.length;
                slides[currentSlide].classList.add('active');
            }, 5000); // 5 seconds interval
        }
    }

    // 2. Highlights
    const highlightsGrid = document.getElementById('highlights-grid');
    if (highlightsGrid) {
        highlightsGrid.innerHTML = siteContent.home.highlights.map((h, idx) => `
            <div class="bg-brandNavy text-white p-6 rounded-bl-2xl rounded-tr-2xl shadow border-b-4 border-brandCyan text-center transform hover:-translate-y-2 transition-transform duration-300 flex flex-col items-center">
                <span class="text-3xl text-brandGreen mb-3"><i class="fa-solid ${idx === 0 ? 'fa-user-tie' : idx === 1 ? 'fa-building' : idx === 2 ? 'fa-briefcase' : 'fa-certificate'}"></i></span>
                <h5 class="text-lg font-bold font-poppins mb-2">${h.title}</h5>
                <p class="text-slate-300 text-sm leading-relaxed">${h.desc}</p>
            </div>
        `).join('');
    }

    // 3. Courses Highlight (tabbed, mirrors arunodayaginstitutions.in Courses Offered section)
    const coursesList = siteContent.home.coursesList;
    const coursesHighlight = document.getElementById('courses-highlight');
    if (coursesHighlight && coursesList && coursesList.length) {
        coursesHighlight.className = "anim-slideInUp";

        const renderCoursesPanel = (idx) => {
            const ch = coursesList[idx];
            return `
            <div class="flex flex-col md:flex-row bg-white rounded-bl-[40px] rounded-tr-[40px] border border-slate-200 shadow-lg overflow-hidden max-w-6xl mx-auto min-h-[500px]">
                <!-- Left Column: Courses Image -->
                <div class="md:w-1/2 w-full min-h-[350px] md:min-h-full anim-slideInLeft relative overflow-hidden" style="background-image: url('${resolveImageUrl(ch.img)}'); background-size: cover; background-position: center top; border-radius: 0px 0px 0px 25px;">
                </div>
                <!-- Right Column: Courses Content -->
                <div class="md:w-1/2 w-full p-8 md:p-12 flex flex-col justify-center anim-slideInRight">
                    <span class="text-sm font-bold text-brandGreen uppercase tracking-widest block mb-2">${siteContent.home.coursesTitle}</span>
                    <div class="w-24 h-0.5 border-t border-dotted border-slate-300 mb-4"></div>
                    <h2 class="text-3xl font-bold font-poppins text-brandNavy mb-4">${ch.name}</h2>
                    <p class="text-slate-600 leading-relaxed text-justify mb-6 text-[15px]">${ch.desc}</p>
                    <div>
                        <a href="${ch.link}" class="inline-flex items-center gap-2 bg-brandBlue hover:bg-brandCyan text-white font-bold py-3 px-8 rounded-full shadow transition-all duration-300 group">
                            <span>${ch.linkText}</span> <i class="fa-solid fa-angle-right group-hover:translate-x-1 transition-transform"></i>
                        </a>
                    </div>
                </div>
            </div>`;
        };

        const renderTabs = (activeIdx) => coursesList.map((c, idx) => `
            <button type="button" data-course-tab="${idx}" class="course-tab-btn px-5 py-2.5 rounded-full text-sm font-bold font-poppins tracking-wide transition-all duration-300 border ${idx === activeIdx ? 'bg-brandNavy text-white border-brandNavy shadow' : 'bg-white text-brandNavy border-slate-200 hover:border-brandCyan hover:text-brandCyan'}">${c.tab}</button>
        `).join('');

        const renderAll = (activeIdx) => {
            coursesHighlight.innerHTML = `
                <div class="flex flex-wrap justify-center gap-3 mb-6" id="courses-tab-bar">
                    ${renderTabs(activeIdx)}
                </div>
                <div id="courses-tab-panel">${renderCoursesPanel(activeIdx)}</div>
            `;

            coursesHighlight.querySelectorAll('.course-tab-btn').forEach(btn => {
                btn.addEventListener('click', () => {
                    const idx = parseInt(btn.getAttribute('data-course-tab'), 10);
                    renderAll(idx);
                });
            });
        };

        renderAll(0);
    }

    // 4. Facilities
    const facilitiesGrid = document.getElementById('facilities-grid');
    if (facilitiesGrid) {
        facilitiesGrid.innerHTML = siteContent.home.facilities.map((f, idx) => `
            <div class="bg-white rounded-bl-2xl rounded-tr-2xl p-6 border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
                <div class="flex items-center gap-3 mb-3">
                    <span class="h-10 w-10 flex items-center justify-center rounded-full bg-brandCyan bg-opacity-20 text-brandCyan text-lg font-bold"><i class="fa-solid ${idx === 0 ? 'fa-book' : idx === 1 ? 'fa-bus' : idx === 2 ? 'fa-volleyball' : 'fa-compass'}"></i></span>
                    <h4 class="text-lg font-bold text-brandNavy font-poppins">${f.name}</h4>
                </div>
                <p class="text-slate-600 text-sm leading-relaxed">${f.desc}</p>
            </div>
        `).join('');
    }

    // 5. Welcome section
    const welcomeSection = document.getElementById('welcome-section');
    if (welcomeSection) {
        const welcome = siteContent.home.welcome;
        welcomeSection.innerHTML = `
            <div class="bg-gradient-to-r from-brandGreen to-brandBlue text-white rounded-bl-3xl rounded-tr-3xl p-8 md:p-12 shadow-xl">
                <h2 class="text-3xl md:text-4xl font-bold font-poppins mb-6 border-b border-white/20 pb-4">${welcome.title}</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 text-[15px] leading-relaxed">
                    <p class="text-slate-100 text-justify">${welcome.p1}</p>
                    <p class="text-slate-100 text-justify">${welcome.p2}</p>
                </div>
                <div class="mt-8 text-center md:text-left">
                    <a href="about.html" class="inline-flex items-center gap-2 bg-white hover:bg-brandCyan text-brandNavy font-bold py-3 px-8 rounded-full shadow transition-all duration-300 group">
                        <span>${welcome.linkText}</span> <i class="fa-solid fa-angle-right group-hover:translate-x-1 transition-transform"></i>
                    </a>
                </div>
            </div>
        `;
    }

    // 6. Placements
    const placementsTitle = document.getElementById('placements-title');
    if (placementsTitle) placementsTitle.innerText = siteContent.home.placementsTitle;
    
    const placementsGrid = document.getElementById('placements-grid');
    if (placementsGrid) {
        placementsGrid.innerHTML = siteContent.home.placements.map((src, idx) => `
            <div class="bg-white rounded-xl p-4 border border-slate-200 shadow-sm flex items-center justify-center hover:shadow-md transition-shadow h-24">
                <img id="placement-logo-${idx}" class="max-h-full max-w-full object-contain" alt="Placement Logo">
            </div>
        `).join('');

        siteContent.home.placements.forEach((src, idx) => {
            setElementImage(`placement-logo-${idx}`, src, `Placement logo ${idx + 1}`);
        });
    }

    // 7. Members
    const membersTitle = document.getElementById('members-title');
    if (membersTitle) membersTitle.innerText = siteContent.home.membersTitle;
    
    const membersGrid = document.getElementById('members-grid');
    if (membersGrid) {
        membersGrid.innerHTML = siteContent.home.members.map((m, idx) => `
            <div class="bg-white border border-slate-200 rounded-bl-3xl rounded-tr-3xl overflow-hidden shadow-sm hover:shadow-md transition-shadow flex flex-col">
                <div class="h-64 bg-slate-100 relative overflow-hidden">
                    <img id="member-photo-${idx}" class="w-full h-full object-cover object-top" alt="${m.name}">
                </div>
                <div class="p-6 text-center border-t border-slate-100 flex-grow">
                    <h5 class="text-lg font-bold text-brandNavy font-poppins">${m.name}</h5>
                    <p class="text-brandCyan text-sm font-semibold mb-1">${m.role}</p>
                    <p class="text-slate-500 text-xs font-semibold uppercase tracking-wider mb-3">${m.role2}</p>
                    <a href="tel:${m.phone}" class="inline-flex items-center gap-1 text-slate-700 hover:text-brandCyan font-bold text-sm bg-slate-100 py-1.5 px-4 rounded-full transition-colors">
                        <i class="fa-solid fa-phone text-xs"></i> ${m.phone}
                    </a>
                </div>
            </div>
        `).join('');

        siteContent.home.members.forEach((m, idx) => {
            setElementImage(`member-photo-${idx}`, m.img, m.name);
        });
    }

    // 8. Vision & Mission
    const visionBox = document.getElementById('vision-box');
    if (visionBox) {
        const v = siteContent.home.vision;
        visionBox.innerHTML = `
            <div class="bg-brandNavy text-white rounded-bl-3xl rounded-tr-3xl p-8 border-b-4 border-brandCyan h-full shadow-md">
                <div class="flex items-center gap-3 mb-4">
                    <span class="text-3xl text-brandGreen"><i class="fa-solid fa-eye"></i></span>
                    <h2 class="text-2xl font-bold font-poppins">${v.title}</h2>
                </div>
                <p class="text-slate-300 leading-relaxed text-justify text-[15px]">${v.text}</p>
            </div>
        `;
    }

    const missionBox = document.getElementById('mission-box');
    if (missionBox) {
        const m = siteContent.home.mission;
        missionBox.innerHTML = `
            <div class="bg-white text-slate-800 rounded-bl-3xl rounded-tr-3xl p-8 border border-slate-200 border-b-4 border-brandGreen h-full shadow-md">
                <div class="flex items-center gap-3 mb-4">
                    <span class="text-3xl text-brandCyan"><i class="fa-solid fa-rocket"></i></span>
                    <h2 class="text-2xl font-bold font-poppins text-brandNavy">${m.title}</h2>
                </div>
                <p class="text-slate-600 leading-relaxed text-justify text-[15px]">${m.text}</p>
            </div>
        `;
    }

    // 9. Why Us
    const whyUsTitle = document.getElementById('why-us-title');
    if (whyUsTitle) whyUsTitle.innerText = siteContent.home.whyUsTitle;
    
    const whyUsList = document.getElementById('why-us-list');
    if (whyUsList) {
        whyUsList.className = "grid grid-cols-1 md:grid-cols-2 gap-4 max-w-5xl mx-auto px-6";
        whyUsList.innerHTML = siteContent.home.whyUs.map((w, idx) => `
            <div class="flex items-start gap-3 bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
                <span class="h-6 w-6 rounded-full bg-brandGreen text-white flex items-center justify-center shrink-0 text-sm font-bold"><i class="fa-solid fa-check"></i></span>
                <span class="text-brandNavy font-semibold text-[15px]">${w}</span>
            </div>
        `).join('');
    }

    // 10. Stats counter animation
    const statsContainer = document.getElementById('stats-container');
    if (statsContainer) {
        statsContainer.innerHTML = siteContent.home.stats.map((s, idx) => `
            <div class="text-center bg-slate-100 p-6 rounded-2xl border border-slate-200 shadow-sm shrink-0 w-48 mx-auto md:w-56">
                <div class="text-4xl font-extrabold text-brandBlue font-poppins mb-1">
                    <span class="stat-number" data-target="${s.value}">0</span>+
                </div>
                <div class="text-sm font-bold text-slate-500 uppercase tracking-widest">${s.label}</div>
            </div>
        `).join('');

        // IntersectionObserver for Counter
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counters = statsContainer.querySelectorAll('.stat-number');
                    counters.forEach(c => {
                        const target = parseInt(c.getAttribute('data-target'));
                        let count = 0;
                        const speed = Math.max(10, Math.floor(2000 / target)); // duration 2 seconds approx
                        const timer = setInterval(() => {
                            count += Math.ceil(target / 40);
                            if (count >= target) {
                                c.innerText = target;
                                clearInterval(timer);
                            } else {
                                c.innerText = count;
                            }
                        }, speed);
                    });
                    observer.unobserve(statsContainer);
                }
            });
        }, { threshold: 0.2 });
        observer.observe(statsContainer);
    }

    // 11. Announcements Infinite Scrolling
    const annTitle = document.getElementById('announcements-title');
    if (annTitle) annTitle.innerText = siteContent.home.announcementsTitle;

    const annTicker = document.getElementById('announcements-ticker-items');
    if (annTicker) {
        // Duplicate items list to create seamless infinite scrolling marquee loop
        const items = [...siteContent.home.announcements, ...siteContent.home.announcements];
        annTicker.innerHTML = items.map((ann, idx) => `
            <div class="p-4 bg-slate-50 hover:bg-slate-100 rounded-xl border border-slate-200 border-l-4 border-brandCyan mb-3 shadow-sm hover:shadow transition-all cursor-pointer">
                <div class="flex items-start gap-2.5">
                    <span class="text-brandCyan text-lg shrink-0 mt-0.5"><i class="fa-solid fa-bullhorn animate-pulse"></i></span>
                    <p class="text-brandNavy text-sm font-bold leading-normal">${ann}</p>
                </div>
            </div>
        `).join('');
    }

    // 12. Home Quick Links
    const qLinksTitle = document.getElementById('home-quick-links-title');
    if (qLinksTitle) qLinksTitle.innerText = siteContent.home.quickLinksTitle;
    
    const qLinksList = document.getElementById('home-quick-links');
    if (qLinksList) {
        qLinksList.innerHTML = siteContent.home.quickLinks.map(q => `
            <a href="${q.link}" class="flex items-center justify-between bg-brandBlue hover:bg-brandCyan text-white font-bold py-4 px-6 rounded-xl shadow transition-all duration-300 group">
                <span>${q.text}</span>
                <i class="fa-solid fa-arrow-right group-hover:translate-x-1 transition-transform"></i>
            </a>
        `).join('');
    }

    // 13. Pop-up slider modal
    const modal = document.getElementById('myModal');
    if (modal) {
        // Injects photos inside slideBox
        const slideBox = document.getElementById('slideBox');
        if (slideBox) {
            slideBox.innerHTML = siteContent.home.modalSliderImages.map((src, idx) => `
                <img id="modal-slide-${idx}" class="w-full shrink-0 object-cover object-center h-80 md:h-[450px]" alt="Modal slide ${idx + 1}">
            `).join('');

            siteContent.home.modalSliderImages.forEach((src, idx) => {
                setElementImage(`modal-slide-${idx}`, src, `Modal slide ${idx + 1}`);
            });
        }

        // Show modal on load
        modal.style.display = 'block';

        const closeBtn = modal.querySelector('.close');
        if (closeBtn) {
            closeBtn.onclick = () => modal.style.display = 'none';
        }
        window.onclick = (e) => {
            if (e.target === modal) {
                modal.style.display = 'none';
            }
        };

        // Slider logic inside modal
        let modalIndex = 0;
        const slides = slideBox.children;
        const totalSlides = slides.length;
        
        window.plusSlides = function(n) {
            if (totalSlides === 0) return;
            modalIndex = (modalIndex + n + totalSlides) % totalSlides;
            
            // Temporary disable keyframe animation and shift translate x
            slideBox.style.animation = 'none';
            slideBox.style.transform = `translateX(-${modalIndex * 100}%)`;
        };
    }
}

function initAboutPage() {
    const welcome = siteContent.about;
    
    // Page Title
    const pageTitle = document.getElementById('about-title');
    if (pageTitle) pageTitle.innerText = welcome.title;

    // Welcome Section text
    const wTitle = document.getElementById('about-welcome-title');
    if (wTitle) wTitle.innerText = welcome.welcomeTitle;
    const wText1 = document.getElementById('about-welcome-text1');
    if (wText1) wText1.innerText = welcome.welcomeText1;
    const wText2 = document.getElementById('about-welcome-text2');
    if (wText2) wText2.innerText = welcome.welcomeText2;
    const wText3 = document.getElementById('about-welcome-text3');
    if (wText3) wText3.innerText = welcome.welcomeText3;

    // Principal message
    const pTitle = document.getElementById('about-principal-title');
    if (pTitle) pTitle.innerText = welcome.principalTitle;
    const pName = document.getElementById('about-principal-name');
    if (pName) pName.innerText = welcome.principalName;
    const pRole = document.getElementById('about-principal-role');
    if (pRole) pRole.innerText = welcome.principalRole;
    const pText = document.getElementById('about-principal-text');
    if (pText) pText.innerText = welcome.principalText;
    setElementImage('about-principal-img', welcome.principalImg, welcome.principalName);

    // Director Message
    const dTitle = document.getElementById('about-director-title');
    if (dTitle) dTitle.innerText = welcome.directorTitle;
    const dName = document.getElementById('about-director-name');
    if (dName) dName.innerText = welcome.directorName;
    const dRole = document.getElementById('about-director-role');
    if (dRole) dRole.innerText = welcome.directorRole + " / " + welcome.directorRole2;
    const dText = document.getElementById('about-director-text');
    if (dText) dText.innerText = welcome.directorText;
    setElementImage('about-director-img', welcome.directorImg, welcome.directorName);

    // Vision / Mission
    const vText = document.getElementById('about-vision-text');
    if (vText) vText.innerText = welcome.vision;
    const mText = document.getElementById('about-mission-text');
    if (mText) mText.innerText = welcome.mission;

    // Faculty Grid list
    const facTitle = document.getElementById('about-faculty-title');
    if (facTitle) facTitle.innerText = welcome.facultyTitle;
    const facGrid = document.getElementById('about-faculty-grid');
    if (facGrid) {
        facGrid.innerHTML = welcome.faculties.map((f, idx) => `
            <div class="bg-white border border-slate-200 rounded-2xl p-6 text-center shadow-sm">
                <div class="h-44 w-44 rounded-full bg-slate-100 mx-auto overflow-hidden border border-slate-200 mb-4">
                    <img id="fac-img-${idx}" class="w-full h-full object-cover object-top" alt="${f.name}">
                </div>
                <h5 class="text-[17px] font-bold text-brandNavy font-poppins mb-1">${f.name}</h5>
                <p class="text-brandCyan text-sm font-semibold">${f.role}</p>
                <p class="text-slate-500 text-xs font-semibold uppercase tracking-wider mt-1">${f.qualification}</p>
            </div>
        `).join('');

        welcome.faculties.forEach((f, idx) => {
            setElementImage(`fac-img-${idx}`, f.img, f.name);
        });
    }
}

function initAdmissionPage() {
    const pageTitle = document.getElementById('admission-title');
    if (pageTitle) pageTitle.innerText = siteContent.admission.title;

    const subTitle = document.getElementById('admission-subtitle');
    if (subTitle) subTitle.innerText = siteContent.admission.subtitle;

    const list = document.getElementById('admission-list');
    if (list) {
        list.innerHTML = siteContent.admission.requirements.map(req => `
            <li class="flex items-start gap-3 bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
                <span class="h-6 w-6 rounded-full bg-brandCyan text-brandNavy flex items-center justify-center shrink-0 text-sm font-bold"><i class="fa-solid fa-angle-right"></i></span>
                <span class="text-brandNavy font-semibold text-[15px]">${req}</span>
            </div>
        `).join('');
    }
}

function initTeachingStaffPage() {
    const pageTitle = document.getElementById('teaching-staff-title');
    if (pageTitle) pageTitle.innerText = siteContent.teachingStaff.title;

    const wrapper = document.getElementById('teaching-staff-wrapper');
    if (wrapper) {
        wrapper.innerHTML = siteContent.teachingStaff.departments.map((dept, deptIdx) => {
            const isBscBcomBca = dept.name.includes("B.Sc / B.Com / BCA");
            return `
                <div class="mb-10 animate-slide-up">
                    <h2 class="text-2xl font-bold font-poppins text-brandNavy border-l-4 border-brandCyan pl-3 mb-4">${dept.name}</h2>
                    <div class="overflow-x-auto bg-white rounded-xl shadow-md border border-slate-200">
                        <table class="w-full text-left text-brandNavy">
                            <thead>
                                <tr class="bg-brandBlue text-white font-poppins text-[15px] border-b border-slate-200">
                                    <th class="p-4 w-20 text-center font-semibold">SL. No</th>
                                    <th class="p-4 font-semibold">Name of the Staff</th>
                                    <th class="p-4 font-semibold">Qualification</th>
                                    <th class="p-4 font-semibold">${isBscBcomBca ? 'Subject' : 'Designation'}</th>
                                    <th class="p-4 w-32 text-center font-semibold">Photo</th>
                                </tr>
                            </thead>
                            <tbody>
                                ${dept.staff.map((s, idx) => `
                                    <tr class="border-b border-slate-200 last:border-0 hover:bg-slate-50 transition-colors">
                                        <td class="p-4 text-center font-bold text-slate-500">${s.no}</td>
                                        <td class="p-4 font-bold text-[15px]">${s.name}</td>
                                        <td class="p-4 text-slate-600 font-semibold text-[14px]">${s.qualification}</td>
                                        <td class="p-4 text-slate-700 font-bold text-[14px]">${isBscBcomBca ? s.designation : s.designation}</td>
                                        <td class="p-3 text-center">
                                            <div class="h-16 w-16 bg-slate-100 border border-slate-200 rounded-full mx-auto overflow-hidden flex items-center justify-center text-slate-400 text-xl">
                                                <i class="fa-regular fa-user"></i>
                                            </div>
                                        </td>
                                    </tr>
                                `).join('')}
                            </tbody>
                        </table>
                    </div>
                </div>
            `;
        }).join('');
    }
}

function initNonTeachingStaffPage() {
    const pageTitle = document.getElementById('non-teaching-staff-title');
    if (pageTitle) pageTitle.innerText = siteContent.nonTeachingStaff.title;

    const tableBody = document.getElementById('non-teaching-staff-tbody');
    if (tableBody) {
        tableBody.innerHTML = siteContent.nonTeachingStaff.staff.map(s => `
            <tr class="border-b border-slate-200 last:border-0 hover:bg-slate-50 transition-colors">
                <td class="p-4 text-center font-bold text-slate-500">${s.no}</td>
                <td class="p-4 font-bold text-[15px]">${s.name}</td>
                <td class="p-4 text-slate-600 font-semibold text-[14px]">${s.qualification}</td>
                <td class="p-4 text-slate-700 font-bold text-[14px]">${s.designation}</td>
                <td class="p-3 text-center">
                    <div class="h-16 w-16 bg-slate-100 border border-slate-200 rounded-full mx-auto overflow-hidden flex items-center justify-center text-slate-400 text-xl">
                        <i class="fa-regular fa-user"></i>
                    </div>
                </td>
            </tr>
        `).join('');
    }
}

function initFacilitiesPage() {
    const pageTitle = document.getElementById('facilities-title');
    if (pageTitle) pageTitle.innerText = siteContent.facilitiesPage.title;

    const grid = document.getElementById('facilities-grid');
    if (grid) {
        grid.innerHTML = siteContent.facilitiesPage.facilities.map((f, idx) => `
            <div class="bg-white rounded-bl-3xl rounded-tr-3xl p-8 border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
                <div class="flex items-center gap-4 mb-4">
                    <span class="h-12 w-12 flex items-center justify-center rounded-full bg-brandCyan bg-opacity-20 text-brandCyan text-2xl font-bold"><i class="fa-solid ${idx === 0 ? 'fa-book' : idx === 1 ? 'fa-bed' : idx === 2 ? 'fa-bus' : idx === 3 ? 'fa-volleyball' : idx === 4 ? 'fa-utensils' : 'fa-compass'}"></i></span>
                    <h4 class="text-xl font-bold text-brandNavy font-poppins">${f.name}</h4>
                </div>
                <p class="text-slate-600 leading-relaxed text-justify text-[15px]">${f.desc}</p>
            </div>
        `).join('');
    }
}

function initCoursePage(courseKey) {
    const c = siteContent.courses[courseKey];
    if (!c) return;

    // Set simple details
    document.title = c.title + " - Arunodaya Institutions";
    const nameEl = document.getElementById('course-name');
    if (nameEl) nameEl.innerText = c.name;
    const descEl = document.getElementById('course-desc');
    if (descEl) descEl.innerText = c.description;

    // Optional languages grid
    const langSection = document.getElementById('languages-section');
    if (langSection && c.languages) {
        langSection.innerHTML = `
            <h4 class="text-lg font-bold text-brandNavy mb-3 font-poppins">${c.part1Title}</h4>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-3">
                ${c.languages.map(l => `<div class="bg-white border border-slate-200 p-3 rounded-lg text-center font-bold text-brandNavy shadow-sm">${l}</div>`).join('')}
            </div>
            <p class="text-sm font-bold text-slate-500">${c.forUgText}</p>
        `;
    }

    // Optional list (Scope or Part II options)
    const scopeTitle = document.getElementById('scope-title');
    if (scopeTitle) scopeTitle.innerText = c.scopeTitle || c.part2Title;
    const scopeDesc = document.getElementById('scope-desc');
    if (scopeDesc) {
        if (c.scopeDesc) {
            scopeDesc.innerText = c.scopeDesc;
            scopeDesc.style.display = 'block';
        } else {
            scopeDesc.style.display = 'none';
        }
    }

    const scopeList = document.getElementById('scope-list');
    if (scopeList) {
        const items = c.scopeOpportunities || c.combinations;
        scopeList.innerHTML = items.map(item => `
            <li class="flex items-start gap-3 bg-white p-4 rounded-xl border border-slate-200 shadow-sm font-semibold text-brandNavy">
                <span class="h-6 w-6 rounded-full bg-brandCyan text-brandNavy flex items-center justify-center shrink-0 text-xs"><i class="fa-solid fa-check"></i></span>
                <span>${item}</span>
            </li>
        `).join('');
    }

    // Approvals Section
    const approvalSection = document.getElementById('approval-section');
    if (approvalSection) {
        if (c.approvalTitle && c.approvals) {
            approvalSection.innerHTML = `
                <h3 class="text-2xl font-bold font-poppins text-brandNavy border-l-4 border-brandCyan pl-3 mb-6">${c.approvalTitle}</h3>
                <ul class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    ${c.approvals.map(app => `
                        <li class="flex items-start gap-3 bg-slate-50 border border-slate-200 p-4 rounded-xl shadow-sm font-semibold text-slate-700">
                            <span class="text-brandCyan text-lg shrink-0 mt-0.5"><i class="fa-solid fa-stamp"></i></span>
                            <span>${app}</span>
                        </li>
                    `).join('')}
                </ul>
            `;
            approvalSection.style.display = 'block';
        } else {
            approvalSection.style.display = 'none';
        }
    }

    // Jobs Section
    const jobTitle = document.getElementById('job-title');
    if (jobTitle) {
        if (c.jobTitle) {
            jobTitle.innerText = c.jobTitle;
            jobTitle.parentElement.style.display = 'block';
        } else {
            jobTitle.parentElement.style.display = 'none';
        }
    }
    const jobList = document.getElementById('job-list');
    if (jobList && c.jobs) {
        jobList.innerHTML = c.jobs.map(job => `
            <div class="bg-brandNavy text-white p-4 rounded-xl text-center font-bold tracking-wide shadow-sm hover:bg-brandCyan hover:text-brandNavy transition-colors">${job}</div>
        `).join('');
    }

    // Subjects List for BCA
    const subjectsSection = document.getElementById('subjects-section');
    if (subjectsSection) {
        if (c.subjects) {
            subjectsSection.innerHTML = `
                <h3 class="text-2xl font-bold font-poppins text-brandNavy border-l-4 border-brandCyan pl-3 mb-6">${c.semTitle}</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    ${c.subjects.map(sub => `
                        <div class="bg-white border border-slate-200 p-4 rounded-xl shadow-sm font-bold text-brandNavy flex items-center gap-3">
                            <span class="h-8 w-8 rounded-full bg-slate-100 flex items-center justify-center text-brandCyan text-sm font-bold"><i class="fa-solid fa-book-open"></i></span>
                            <span>${sub}</span>
                        </div>
                    `).join('')}
                </div>
            `;
            subjectsSection.style.display = 'block';
        } else {
            subjectsSection.style.display = 'none';
        }
    }

    // Claim of Exemptions for BCA
    const exemptionSection = document.getElementById('exemption-section');
    if (exemptionSection) {
        if (c.exemptionTitle && c.exemptionPoints) {
            exemptionSection.innerHTML = `
                <h3 class="text-2xl font-bold font-poppins text-brandNavy border-l-4 border-brandCyan pl-3 mb-6">${c.exemptionTitle}</h3>
                <ul class="flex flex-col gap-4">
                    ${c.exemptionPoints.map(ex => `
                        <li class="flex items-start gap-3 bg-slate-50 border border-slate-200 p-4 rounded-xl shadow-sm font-semibold text-slate-700">
                            <span class="text-brandCyan text-lg shrink-0 mt-0.5"><i class="fa-solid fa-circle-exclamation"></i></span>
                            <span>${ex}</span>
                        </li>
                    `).join('')}
                </ul>
            `;
            exemptionSection.style.display = 'block';
        } else {
            exemptionSection.style.display = 'none';
        }
    }

    // Eligibility
    const eligTitle = document.getElementById('eligibility-title');
    if (eligTitle) eligTitle.innerText = c.eligibilityTitle;
    const eligDesc = document.getElementById('eligibility-desc');
    if (eligDesc) {
        if (c.eligibilityDesc) {
            eligDesc.innerText = c.eligibilityDesc;
            eligDesc.style.display = 'block';
        } else {
            eligDesc.style.display = 'none';
        }
    }
    const eligList = document.getElementById('eligibility-list');
    if (eligList) {
        const points = c.eligibilityPoints || c.semEligibility;
        eligList.innerHTML = points.map(pt => `
            <li class="flex items-start gap-3 bg-white p-4 rounded-xl border border-slate-200 shadow-sm font-semibold text-slate-700">
                <span class="text-brandCyan text-lg shrink-0 mt-0.5"><i class="fa-solid fa-user-check"></i></span>
                <span>${pt}</span>
            </li>
        `).join('');
    }

    // Duration
    const durTitle = document.getElementById('duration-title');
    if (durTitle) durTitle.innerText = c.durationTitle || c.studyTitle;
    const durDesc = document.getElementById('duration-desc');
    if (durDesc) {
        if (c.durationDesc) {
            durDesc.innerText = c.durationDesc;
            durDesc.style.display = 'block';
        } else {
            durDesc.style.display = 'none';
        }
    }
    const durList = document.getElementById('duration-list');
    if (durList) {
        if (c.studyPoints) {
            durList.innerHTML = c.studyPoints.map(pt => `
                <li class="flex items-start gap-3 bg-white p-4 rounded-xl border border-slate-200 shadow-sm font-semibold text-slate-700">
                    <span class="text-brandCyan text-lg shrink-0 mt-0.5"><i class="fa-solid fa-clock"></i></span>
                    <span>${pt}</span>
                </li>
            `).join('');
            durList.style.display = 'flex';
        } else {
            durList.style.display = 'none';
        }
    }

    // Required Docs for Degrees
    const docsSection = document.getElementById('docs-section');
    if (docsSection) {
        if (c.docsTitle && c.docs) {
            docsSection.innerHTML = `
                <h3 class="text-2xl font-bold font-poppins text-brandNavy border-l-4 border-brandCyan pl-3 mb-6">${c.docsTitle}</h3>
                <ul class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    ${c.docs.map(doc => `
                        <li class="flex items-start gap-3 bg-white border border-slate-200 p-4 rounded-xl shadow-sm font-semibold text-slate-700">
                            <span class="text-brandGreen text-lg shrink-0 mt-0.5"><i class="fa-solid fa-file-invoice"></i></span>
                            <span>${doc}</span>
                        </li>
                    `).join('')}
                </ul>
            `;
            docsSection.style.display = 'block';
        } else {
            docsSection.style.display = 'none';
        }
    }

    const courseFooter = document.getElementById('course-footer-text');
    if (courseFooter) {
        if (c.footerText) {
            courseFooter.innerText = c.footerText;
            courseFooter.style.display = 'block';
        } else {
            courseFooter.style.display = 'none';
        }
    }
}

function initTablePage(pageKey) {
    const data = siteContent[pageKey];
    if (!data) return;

    // Header Title
    const titleEl = document.getElementById('table-page-title');
    if (titleEl) titleEl.innerText = data.title;

    // Headers
    const headersTr = document.getElementById('table-headers');
    if (headersTr) {
        headersTr.innerHTML = data.headers.map(h => `<th class="p-4 font-bold text-[15px]">${h}</th>`).join('');
    }

    // Rows
    const tbody = document.getElementById('table-body');
    if (tbody) {
        tbody.innerHTML = data.rows.map(row => `
            <tr class="border-b border-slate-200 last:border-0 hover:bg-slate-50 transition-colors">
                <td class="p-4 text-center font-bold text-slate-500">${row.no}</td>
                <td class="p-4 font-bold">${row.courseName}</td>
                <td class="p-4 font-semibold text-slate-700">${row.year}</td>
                <td class="p-4">
                    <a href="${resolveImageUrl(row.link)}" target="_blank" class="inline-flex items-center gap-1.5 text-brandCyan hover:text-brandNavy font-bold">
                        <i class="fa-solid fa-file-pdf text-red-500"></i> ${row.attachmentText}
                    </a>
                </td>
            </tr>
        `).join('');
    }
}

function initGalleryPage() {
    const pageTitle = document.getElementById('gallery-title');
    if (pageTitle) pageTitle.innerText = siteContent.gallery.title;

    const grid = document.getElementById('gallery-grid');
    if (grid) {
        grid.innerHTML = siteContent.gallery.images.map((img, idx) => `
            <div class="group relative bg-slate-100 rounded-2xl overflow-hidden border border-slate-200 shadow-sm hover:shadow-md cursor-pointer aspect-video" onclick="openLightbox(${idx})">
                <img id="gallery-img-${idx}" class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-300" alt="${img.title}">
                <div class="absolute inset-0 bg-black bg-opacity-40 flex items-end p-4 opacity-0 group-hover:opacity-100 transition-opacity">
                    <h5 class="text-white font-bold font-poppins text-sm truncate w-full">${img.title}</h5>
                </div>
            </div>
        `).join('');

        siteContent.gallery.images.forEach((img, idx) => {
            setElementImage(`gallery-img-${idx}`, img.src, img.title);
        });
    }

    // Lightbox modal logic
    const lightbox = document.getElementById('lightbox-modal');
    if (lightbox) {
        const lightboxImg = document.getElementById('lightbox-img');
        const lightboxTitle = document.getElementById('lightbox-title');
        let currentIdx = 0;

        window.openLightbox = function(idx) {
            currentIdx = idx;
            const img = siteContent.gallery.images[currentIdx];
            if (img) {
                lightboxImg.src = resolveImageUrl(img.src);
                lightboxTitle.innerText = img.title;
                lightbox.style.display = 'flex';
            }
        };

        window.closeLightbox = function() {
            lightbox.style.display = 'none';
        };

        window.changeLightboxImage = function(n) {
            const total = siteContent.gallery.images.length;
            if (total === 0) return;
            currentIdx = (currentIdx + n + total) % total;
            const img = siteContent.gallery.images[currentIdx];
            if (img) {
                lightboxImg.src = resolveImageUrl(img.src);
                lightboxTitle.innerText = img.title;
            }
        };

        const closeBtn = lightbox.querySelector('.close');
        if (closeBtn) closeBtn.onclick = closeLightbox;

        lightbox.onclick = (e) => {
            if (e.target === lightbox || e.target.classList.contains('lightbox-container')) {
                closeLightbox();
            }
        };
    }
}

function initNewsEventsPage() {
    const pageTitle = document.getElementById('news-title');
    if (pageTitle) pageTitle.innerText = siteContent.newsEvents.title;

    const postsGrid = document.getElementById('news-posts');
    if (postsGrid) {
        postsGrid.innerHTML = siteContent.newsEvents.posts.map(post => `
            <article class="bg-white border border-slate-200 rounded-2xl overflow-hidden shadow-sm hover:shadow-md transition-shadow p-6 flex flex-col gap-3">
                <div class="flex items-center gap-2">
                    <span class="text-xs font-bold bg-brandCyan bg-opacity-20 text-brandCyan py-1 px-3 rounded-full uppercase tracking-wider">${post.category}</span>
                    <span class="text-xs text-slate-500 font-semibold"><i class="fa-regular fa-calendar"></i> ${post.date}</span>
                </div>
                <h4 class="text-xl font-bold text-brandNavy font-poppins hover:text-brandCyan cursor-pointer transition-colors leading-snug">${post.title}</h4>
                <p class="text-slate-600 text-sm leading-relaxed text-justify flex-grow">${post.desc}</p>
                <div class="border-t border-slate-100 pt-3 flex items-center justify-between">
                    <span class="text-xs text-slate-500 font-semibold">Posted by: arunodayapharmacy</span>
                    <a href="#" class="text-xs text-brandCyan hover:text-brandNavy font-bold uppercase tracking-wider flex items-center gap-1 group">
                        <span>Read More</span> <i class="fa-solid fa-angle-right group-hover:translate-x-1 transition-transform"></i>
                    </a>
                </div>
            </article>
        `).join('');
    }

    // Sidebar widgets loading
    const sb = siteContent.newsEvents.sidebar;
    const aboutTitle = document.getElementById('sb-about-title');
    if (aboutTitle) aboutTitle.innerText = sb.aboutTitle;
    const aboutText = document.getElementById('sb-about-text');
    if (aboutText) aboutText.innerText = sb.aboutText;

    const confTitle = document.getElementById('sb-conf-title');
    if (confTitle) confTitle.innerText = sb.confTitle;
    const confDate = document.getElementById('sb-conf-date');
    if (confDate) confDate.innerText = sb.confDate;
    const confLoc = document.getElementById('sb-conf-loc');
    if (confLoc) confLoc.innerText = sb.confLocation;
    const confBtn = document.getElementById('sb-conf-btn');
    if (confBtn) confBtn.innerText = sb.confBtn;
}

function initContactPage() {
    const c = siteContent.contact;

    const pageTitle = document.getElementById('contact-title');
    if (pageTitle) pageTitle.innerText = c.title;

    const descEl = document.getElementById('contact-desc');
    if (descEl) descEl.innerText = c.description;

    // Contact Details Cards
    const officeTitle = document.getElementById('card-office-title');
    if (officeTitle) officeTitle.innerText = c.officeTitle;
    const officeAddr = document.getElementById('card-office-addr');
    if (officeAddr) officeAddr.innerText = c.officeAddress;

    const emailTitle = document.getElementById('card-email-title');
    if (emailTitle) emailTitle.innerText = c.emailTitle;
    const emailList = document.getElementById('card-email-list');
    if (emailList) {
        emailList.innerHTML = c.emailList.map(email => `<a href="mailto:${email}" class="hover:text-brandCyan block break-all font-semibold">${email}</a>`).join('');
    }

    const hoursTitle = document.getElementById('card-hours-title');
    if (hoursTitle) hoursTitle.innerText = c.hoursTitle;
    const hoursText = document.getElementById('card-hours');
    if (hoursText) hoursText.innerText = c.hours;
    const hoursSub = document.getElementById('card-hours-sub');
    if (hoursSub) hoursSub.innerText = c.subText;

    // Sidebar query
    const formTitle = document.getElementById('form-title');
    if (formTitle) formTitle.innerText = c.formTitle;
    const phoneTitle = document.getElementById('phone-title');
    if (phoneTitle) phoneTitle.innerText = c.phoneTitle;
    const phoneNum = document.getElementById('phone-num');
    if (phoneNum) phoneNum.innerText = c.phoneNumber;

    // Map box
    const mapTitle = document.getElementById('map-title');
    if (mapTitle) mapTitle.innerText = c.mapTitle;
    const mapSub = document.getElementById('map-subtitle');
    if (mapSub) mapSub.innerText = c.mapSubtitle;

    // Handle Contact Form Submit Toggles
    const form = document.getElementById('contact-form');
    const successToast = document.getElementById('success-toast');
    const errorToast = document.getElementById('error-toast');

    if (form) {
        form.onsubmit = function(e) {
            e.preventDefault();
            // Simulate response
            const name = form.querySelector('[name="name"]').value;
            const email = form.querySelector('[name="email"]').value;
            if (name && email) {
                if (successToast) {
                    successToast.classList.remove('hidden');
                    setTimeout(() => successToast.classList.add('hidden'), 5000);
                }
                form.reset();
            } else {
                if (errorToast) {
                    errorToast.classList.remove('hidden');
                    setTimeout(() => errorToast.classList.add('hidden'), 5000);
                }
            }
        };

        // Modal triggers on close alerts
        const closeAlerts = document.querySelectorAll('.close-alert');
        closeAlerts.forEach(cBtn => {
            cBtn.onclick = function() {
                cBtn.parentElement.classList.add('hidden');
            };
        });
    }
}

// ---------------------------------
// INITIALIZATION ROUTER
// ---------------------------------

document.addEventListener("DOMContentLoaded", () => {
    // 1. Load Common layout
    renderHeader();
    renderFooter();

    // 2. Load Page Specific modules
    const path = window.location.pathname;
    const page = path.substring(path.lastIndexOf('/') + 1) || 'index.html';

    if (page === 'index.html') {
        initHomePage();
    } else if (page === 'about.html') {
        initAboutPage();
    } else if (page === 'admission-process.html') {
        initAdmissionPage();
    } else if (page === 'teaching-staff.html') {
        initTeachingStaffPage();
    } else if (page === 'non-teaching-staff.html') {
        initNonTeachingStaffPage();
    } else if (page === 'facilities.html') {
        initFacilitiesPage();
    } else if (['b-pharm.html', 'd-pharm.html', 'b-sc.html', 'b-com.html', 'bca.html'].includes(page)) {
        const courseKey = page.replace('.html', '').replace('-', '_');
        initCoursePage(courseKey);
    } else if (page === 'syllabus.html') {
        initTablePage('syllabus');
    } else if (page === 'academic-calendar.html') {
        initTablePage('academic_calendar');
    } else if (page === 'time-table.html') {
        initTablePage('time_table');
    } else if (page === 'gallery.html') {
        initGalleryPage();
    } else if (page === 'news-events.html') {
        initNewsEventsPage();
    } else if (page === 'contact-us.html') {
        initContactPage();
    }
});
"""

if not os.path.exists(os.path.join(workspace_dir, "main.js")):
    with open(os.path.join(workspace_dir, "main.js"), "w", encoding="utf-8") as f:
        f.write(main_js)

# 4. Define HTML template generator
def generate_html_shell(title, active_class, inner_body_content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Yoast SEO Optimization replica -->
    <title>{title}</title>
    <meta name="description" content="Arunodaya Pharmacy College Of Pharmacy Aurad (B), affiliated to BEA. Qualified Faculty, Best Infrastructure, Placements, and Certification.">
    <link rel="shortcut icon" href="https://arunodayaginstitutions.in/wp-content/uploads/2024/05/cropped-arunodaya-pharmacy-logo.png" type="image/x-icon">
    <!-- Tailwind CSS via CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        brandNavy: '#0c2b5c',
                        brandBlue: '#0158a5',
                        brandCyan: '#23b1e7',
                        brandGreen: '#47ba7d',
                        brandLightGray: '#f4f6f8',
                    }},
                    fontFamily: {{
                        sans: ['Mulish', 'sans-serif'],
                        poppins: ['Poppins', 'sans-serif'],
                    }}
                }}
            }}
        }}
    </script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Custom Style Sheet -->
    <link rel="stylesheet" href="style.css">
</head>
<body class="bg-gray-50 text-gray-800 font-sans">
    
    <!-- Top Utility Bar (Shared Header Section) -->
    <div id="top-bar"></div>

    <!-- Main Navigation Header (Shared Header Section) -->
    <header id="main-header"></header>

    <!-- Page Specific Main Content Area -->
    <main id="page-content" class="min-h-screen">
        {inner_body_content}
    </main>

    <!-- Shared Footer Area -->
    <footer id="main-footer" class="relative"></footer>

    <!-- Single Source of Truth Data -->
    <script src="content.js"></script>
    <!-- Rendering & Page Routing Controller -->
    <script src="main.js"></script>
</body>
</html>"""

# Generate 17 page templates
# index.html
index_content = """
<!-- Hero Slider -->
<div id="hero-slider" class="hero-slider shadow-inner"></div>

<!-- Highlights Section -->
<section class="max-w-7xl mx-auto px-6 py-12">
    <div id="highlights-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 animate-slide-up"></div>
</section>

<!-- Courses Highlight -->
<section class="max-w-5xl mx-auto px-6 py-6 animate-slide-up">
    <div id="courses-highlight"></div>
</section>

<!-- Facilities Summary -->
<section class="bg-slate-50 border-t border-b border-slate-200 py-16 px-6">
    <div class="max-w-7xl mx-auto">
        <h1 class="text-3xl md:text-4xl font-extrabold text-brandNavy font-poppins text-center mb-10 tracking-tight" id="facilities-title-home">Our Facilities</h1>
        <div id="facilities-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 animate-slide-up"></div>
    </div>
</section>

<!-- Welcome section -->
<section class="max-w-6xl mx-auto px-6 py-16 animate-slide-up">
    <div id="welcome-section"></div>
</section>

<!-- Placements Section -->
<section class="bg-slate-100 py-16 px-6 border-t border-b border-slate-200">
    <div class="max-w-7xl mx-auto">
        <h2 id="placements-title" class="text-3xl md:text-4xl font-extrabold text-brandNavy font-poppins text-center mb-10 tracking-tight"></h2>
        <div id="placements-grid" class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-9 gap-4 max-w-6xl mx-auto animate-slide-up"></div>
    </div>
</section>

<!-- Our Members -->
<section class="max-w-7xl mx-auto px-6 py-16">
    <h2 id="members-title" class="text-3xl md:text-4xl font-extrabold text-brandNavy font-poppins text-center mb-10 tracking-tight"></h2>
    <div id="members-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 max-w-6xl mx-auto animate-slide-up"></div>
</section>

<!-- Vision & Mission -->
<section class="bg-slate-50 border-t border-b border-slate-200 py-16 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 animate-slide-up">
        <div id="vision-box"></div>
        <div id="mission-box"></div>
    </div>
</section>

<!-- Why Us Section -->
<section class="py-16 bg-brandNavy text-white">
    <h3 id="why-us-title" class="text-3xl md:text-4xl font-extrabold font-poppins text-center mb-10 tracking-tight text-brandGreen"></h3>
    <div id="why-us-list" class="animate-slide-up"></div>
</section>

<!-- Stats counters -->
<section class="border-b border-slate-200 py-12 px-6">
    <div id="stats-container" class="max-w-5xl mx-auto flex flex-wrap justify-center items-center gap-6 animate-slide-up"></div>
</section>

<!-- Announcements & Quick Links -->
<section class="max-w-7xl mx-auto px-6 py-16 grid grid-cols-1 lg:grid-cols-3 gap-10">
    <!-- Announcements Ticker (Col 1 & 2) -->
    <div class="lg:col-span-2 border border-slate-200 rounded-3xl p-6 shadow bg-white">
        <h2 id="announcements-title" class="text-2xl font-bold font-poppins text-brandNavy mb-6 border-b-2 border-brandGreen w-fit pb-1"></h2>
        <div class="ticker-container">
            <div id="announcements-ticker-items" class="ticker-wrapper flex flex-col"></div>
        </div>
    </div>
    
    <!-- Quick Links (Col 3) -->
    <div class="border border-slate-200 rounded-3xl p-6 shadow bg-white flex flex-col justify-between">
        <div>
            <h2 id="home-quick-links-title" class="text-2xl font-bold font-poppins text-brandNavy mb-6 border-b-2 border-brandGreen w-fit pb-1"></h2>
            <div id="home-quick-links" class="flex flex-col gap-4"></div>
        </div>
    </div>
</section>

<!-- Modal Slider POPUP -->
<div id="myModal" class="lightbox-modal flex items-center justify-center">
    <div class="relative bg-white rounded-3xl max-w-4xl w-[90%] overflow-hidden shadow-2xl p-4 m-auto">
        <span class="close absolute top-3 right-5 text-4xl font-bold text-slate-800 cursor-pointer hover:text-black z-50">&times;</span>
        <div class="slider relative w-full overflow-hidden rounded-2xl">
            <div id="slideBox" class="flex transition-transform duration-500"></div>
            <!-- Slide controls -->
            <button class="absolute top-1/2 left-4 -translate-y-1/2 bg-black bg-opacity-40 text-white h-10 w-10 flex items-center justify-center rounded-full text-xl font-bold hover:bg-opacity-60 transition-opacity" onclick="plusSlides(-1)">&#10094;</button>
            <button class="absolute top-1/2 right-4 -translate-y-1/2 bg-black bg-opacity-40 text-white h-10 w-10 flex items-center justify-center rounded-full text-xl font-bold hover:bg-opacity-60 transition-opacity" onclick="plusSlides(1)">&#10095;</button>
        </div>
    </div>
</div>
"""

# about.html
about_content = """
<!-- Title Banner -->
<section class="bg-brandNavy text-white py-12 px-6">
    <div class="max-w-7xl mx-auto">
        <h1 id="about-title" class="text-3xl md:text-4xl font-extrabold font-poppins tracking-tight"></h1>
    </div>
</section>

<!-- Welcome Section -->
<section class="max-w-6xl mx-auto px-6 py-12">
    <h2 id="about-welcome-title" class="text-2xl md:text-3xl font-extrabold font-poppins text-brandNavy mb-6"></h2>
    <div class="flex flex-col gap-6 text-[15px] leading-relaxed text-slate-600 text-justify animate-slide-up">
        <p id="about-welcome-text1" class="font-bold text-brandNavy text-lg"></p>
        <p id="about-welcome-text2"></p>
        <p id="about-welcome-text3"></p>
    </div>
</section>

<!-- Messages Section -->
<section class="bg-slate-50 border-t border-b border-slate-200 py-16 px-6">
    <div class="max-w-6xl mx-auto flex flex-col gap-16">
        <!-- Principal Message -->
        <div class="flex flex-col md:flex-row gap-10 items-start animate-slide-up">
            <div class="w-full md:w-1/3 bg-white p-4 border border-slate-200 rounded-3xl shadow-sm">
                <div class="h-80 bg-slate-100 rounded-2xl overflow-hidden mb-4">
                    <img id="about-principal-img" class="w-full h-full object-cover object-top" alt="Principal">
                </div>
                <h5 id="about-principal-name" class="text-lg font-bold text-brandNavy font-poppins text-center mb-1"></h5>
                <p id="about-principal-role" class="text-sm font-bold text-brandCyan text-center uppercase tracking-wider"></p>
            </div>
            <div class="w-full md:w-2/3">
                <h2 id="about-principal-title" class="text-2xl font-bold font-poppins text-brandNavy border-l-4 border-brandCyan pl-3 mb-4"></h2>
                <div id="about-principal-text" class="text-slate-600 leading-relaxed text-justify whitespace-pre-line text-[15px]"></div>
            </div>
        </div>

        <!-- Director Message -->
        <div class="flex flex-col md:flex-row gap-10 items-start animate-slide-up">
            <div class="w-full md:w-2/3 order-2 md:order-1">
                <h2 id="about-director-title" class="text-2xl font-bold font-poppins text-brandNavy border-l-4 border-brandCyan pl-3 mb-4"></h2>
                <div id="about-director-text" class="text-slate-600 leading-relaxed text-justify whitespace-pre-line text-[15px]"></div>
            </div>
            <div class="w-full md:w-1/3 bg-white p-4 border border-slate-200 rounded-3xl shadow-sm order-1 md:order-2">
                <div class="h-80 bg-slate-100 rounded-2xl overflow-hidden mb-4">
                    <img id="about-director-img" class="w-full h-full object-cover object-top" alt="Director">
                </div>
                <h5 id="about-director-name" class="text-lg font-bold text-brandNavy font-poppins text-center mb-1"></h5>
                <p id="about-director-role" class="text-sm font-bold text-brandCyan text-center uppercase tracking-wider"></p>
            </div>
        </div>
    </div>
</section>

<!-- Vision & Mission -->
<section class="max-w-6xl mx-auto px-6 py-16 grid grid-cols-1 md:grid-cols-2 gap-8 animate-slide-up">
    <div class="bg-brandNavy text-white rounded-bl-3xl rounded-tr-3xl p-8 border-b-4 border-brandCyan shadow-md">
        <h3 class="text-2xl font-bold font-poppins mb-4 flex items-center gap-3"><span class="text-brandGreen text-3xl"><i class="fa-solid fa-eye"></i></span> Vision</h3>
        <p id="about-vision-text" class="text-slate-300 leading-relaxed text-justify text-[15px]"></p>
    </div>
    <div class="bg-white text-slate-800 rounded-bl-3xl rounded-tr-3xl p-8 border border-slate-200 border-b-4 border-brandGreen shadow-md">
        <h3 class="text-2xl font-bold font-poppins text-brandNavy mb-4 flex items-center gap-3"><span class="text-brandCyan text-3xl"><i class="fa-solid fa-rocket"></i></span> Mission</h3>
        <p id="about-mission-text" class="text-slate-600 leading-relaxed text-justify text-[15px]"></p>
    </div>
</section>

<!-- Faculty Section -->
<section class="bg-slate-50 py-16 px-6 border-t border-slate-200">
    <div class="max-w-6xl mx-auto">
        <h2 id="about-faculty-title" class="text-2xl md:text-3xl font-extrabold font-poppins text-brandNavy text-center mb-10 tracking-tight"></h2>
        <div id="about-faculty-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 animate-slide-up"></div>
    </div>
</section>
"""

# admission-process.html
admission_content = """
<section class="bg-brandNavy text-white py-12 px-6">
    <div class="max-w-7xl mx-auto">
        <h1 id="admission-title" class="text-3xl md:text-4xl font-extrabold font-poppins tracking-tight"></h1>
    </div>
</section>

<section class="max-w-4xl mx-auto px-6 py-16">
    <h2 id="admission-subtitle" class="text-2xl md:text-3xl font-extrabold font-poppins text-brandNavy mb-8 border-b-2 border-brandGreen w-fit pb-1"></h2>
    <ul id="admission-list" class="flex flex-col gap-4 animate-slide-up"></ul>
</section>
"""

# teaching-staff.html
teaching_staff_content = """
<section class="bg-brandNavy text-white py-12 px-6">
    <div class="max-w-7xl mx-auto">
        <h1 id="teaching-staff-title" class="text-3xl md:text-4xl font-extrabold font-poppins tracking-tight"></h1>
    </div>
</section>

<section class="max-w-6xl mx-auto px-6 py-16">
    <div id="teaching-staff-wrapper" class="flex flex-col gap-10"></div>
</section>
"""

# non-teaching-staff.html
non_teaching_staff_content = """
<section class="bg-brandNavy text-white py-12 px-6">
    <div class="max-w-7xl mx-auto">
        <h1 id="non-teaching-staff-title" class="text-3xl md:text-4xl font-extrabold font-poppins tracking-tight"></h1>
    </div>
</section>

<section class="max-w-5xl mx-auto px-6 py-16">
    <div class="overflow-x-auto bg-white rounded-xl shadow-md border border-slate-200 animate-slide-up">
        <table class="w-full text-left text-brandNavy">
            <thead>
                <tr class="bg-brandBlue text-white font-poppins text-[15px] border-b border-slate-200">
                    <th class="p-4 w-20 text-center font-semibold">SL. No</th>
                    <th class="p-4 font-semibold">Name of the Staff</th>
                    <th class="p-4 font-semibold">Qualification</th>
                    <th class="p-4 font-semibold">Designation</th>
                    <th class="p-4 w-32 text-center font-semibold">Photo</th>
                </tr>
            </thead>
            <tbody id="non-teaching-staff-tbody"></tbody>
        </table>
    </div>
</section>
"""

# facilities.html
facilities_content = """
<section class="bg-brandNavy text-white py-12 px-6">
    <div class="max-w-7xl mx-auto">
        <h1 id="facilities-title" class="text-3xl md:text-4xl font-extrabold font-poppins tracking-tight"></h1>
    </div>
</section>

<section class="max-w-6xl mx-auto px-6 py-16">
    <div id="facilities-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 animate-slide-up"></div>
</section>
"""

# course-detail-template (b-pharm.html, d-pharm.html, b-sc.html, b-com.html, bca.html)
course_detail_content = """
<section class="bg-brandNavy text-white py-12 px-6">
    <div class="max-w-7xl mx-auto">
        <h1 id="course-name" class="text-3xl md:text-4xl font-extrabold font-poppins tracking-tight"></h1>
    </div>
</section>

<section class="max-w-6xl mx-auto px-6 py-16 flex flex-col gap-12">
    <!-- Description Card -->
    <div class="bg-white rounded-bl-3xl rounded-tr-3xl p-8 border border-slate-200 shadow-sm animate-slide-up">
        <p id="course-desc" class="text-slate-600 leading-relaxed text-justify text-[16px]"></p>
    </div>

    <!-- Languages Option Section -->
    <div id="languages-section" class="animate-slide-up"></div>

    <!-- Scope Section -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 items-start animate-slide-up">
        <div class="lg:col-span-2">
            <h3 id="scope-title" class="text-2xl font-bold font-poppins text-brandNavy border-l-4 border-brandCyan pl-3 mb-4"></h3>
            <p id="scope-desc" class="text-slate-600 leading-relaxed text-justify mb-6 text-[15px]"></p>
        </div>
        <div class="bg-white p-6 border border-slate-200 rounded-2xl shadow-sm">
            <ul id="scope-list" class="flex flex-col gap-3"></ul>
        </div>
    </div>

    <!-- Approvals Section -->
    <div id="approval-section" class="animate-slide-up"></div>

    <!-- Job Opportunities Section -->
    <div class="bg-slate-50 border-t border-b border-slate-200 py-12 px-6 -mx-6 md:-mx-12">
        <div class="max-w-6xl mx-auto">
            <h3 id="job-title" class="text-2xl font-bold font-poppins text-brandNavy text-center mb-8"></h3>
            <div id="job-list" class="grid grid-cols-2 md:grid-cols-4 gap-4 animate-slide-up"></div>
        </div>
    </div>

    <!-- Subjects Section (BCA) -->
    <div id="subjects-section" class="animate-slide-up"></div>

    <!-- Exemptions Section (BCA) -->
    <div id="exemption-section" class="animate-slide-up"></div>

    <!-- Eligibility & Admission -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-start animate-slide-up">
        <div>
            <h3 id="eligibility-title" class="text-2xl font-bold font-poppins text-brandNavy border-l-4 border-brandCyan pl-3 mb-6"></h3>
            <p id="eligibility-desc" class="text-slate-600 mb-4 leading-relaxed font-semibold"></p>
            <ul id="eligibility-list" class="flex flex-col gap-3"></ul>
        </div>
        <div>
            <h3 id="duration-title" class="text-2xl font-bold font-poppins text-brandNavy border-l-4 border-brandGreen pl-3 mb-6"></h3>
            <p id="duration-desc" class="text-slate-600 leading-relaxed text-justify text-[15px] mb-4"></p>
            <ul id="duration-list" class="flex flex-col gap-3"></ul>
        </div>
    </div>

    <!-- Required Docs List -->
    <div id="docs-section" class="animate-slide-up"></div>

    <!-- Footer Text -->
    <div id="course-footer-text" class="text-center font-bold text-slate-500 uppercase tracking-widest text-sm pt-4 border-t border-slate-200"></div>
</section>
"""

# table-pages-template (syllabus.html, academic-calendar.html, time-table.html)
table_pages_content = """
<section class="bg-brandNavy text-white py-12 px-6">
    <div class="max-w-7xl mx-auto">
        <h1 id="table-page-title" class="text-3xl md:text-4xl font-extrabold font-poppins tracking-tight"></h1>
    </div>
</section>

<section class="max-w-5xl mx-auto px-6 py-16">
    <div class="overflow-x-auto bg-white rounded-xl shadow-md border border-slate-200 animate-slide-up">
        <table class="w-full text-left text-brandNavy">
            <thead>
                <tr id="table-headers" class="bg-brandBlue text-white font-poppins border-b border-slate-200"></tr>
            </thead>
            <tbody id="table-body"></tbody>
        </table>
    </div>
</section>
"""

# gallery.html
gallery_content = """
<section class="bg-brandNavy text-white py-12 px-6">
    <div class="max-w-7xl mx-auto">
        <h1 id="gallery-title" class="text-3xl md:text-4xl font-extrabold font-poppins tracking-tight"></h1>
    </div>
</section>

<section class="max-w-7xl mx-auto px-6 py-16">
    <div id="gallery-grid" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 animate-slide-up"></div>
</section>

<!-- Lightbox Modal -->
<div id="lightbox-modal" class="lightbox-modal flex flex-col justify-center items-center">
    <span class="close absolute top-6 right-8 text-white text-5xl font-bold cursor-pointer hover:text-slate-300 z-50">&times;</span>
    <div class="lightbox-container max-w-5xl w-[90%] flex flex-col items-center justify-center relative p-4">
        <img id="lightbox-img" class="lightbox-content rounded-xl shadow-2xl" alt="">
        <div id="lightbox-title" class="lightbox-caption font-bold text-lg tracking-wide uppercase font-poppins mt-4"></div>
        <!-- Lightbox Cycle controls -->
        <button class="absolute top-1/2 left-4 -translate-y-1/2 bg-black bg-opacity-40 text-white h-12 w-12 flex items-center justify-center rounded-full text-2xl font-bold hover:bg-opacity-65 transition-opacity" onclick="changeLightboxImage(-1)">&#10094;</button>
        <button class="absolute top-1/2 right-4 -translate-y-1/2 bg-black bg-opacity-40 text-white h-12 w-12 flex items-center justify-center rounded-full text-2xl font-bold hover:bg-opacity-65 transition-opacity" onclick="changeLightboxImage(1)">&#10095;</button>
    </div>
</div>
"""

# news-events.html
news_events_content = """
<section class="bg-brandNavy text-white py-12 px-6">
    <div class="max-w-7xl mx-auto">
        <h1 id="news-title" class="text-3xl md:text-4xl font-extrabold font-poppins tracking-tight"></h1>
    </div>
</section>

<section class="max-w-7xl mx-auto px-6 py-16 grid grid-cols-1 lg:grid-cols-3 gap-10">
    <!-- Main posts list (Col 1 & 2) -->
    <div class="lg:col-span-2 flex flex-col gap-8" id="news-posts"></div>

    <!-- Sidebar widgets (Col 3) -->
    <div class="flex flex-col gap-8 animate-slide-up">
        <!-- Widget 1: About avada -->
        <div class="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm">
            <h4 id="sb-about-title" class="text-lg font-bold font-poppins text-brandNavy border-b-2 border-brandGreen w-fit pb-1 mb-4 uppercase tracking-wider"></h4>
            <p id="sb-about-text" class="text-slate-600 leading-relaxed text-justify text-sm"></p>
        </div>

        <!-- Widget 2: Conference details -->
        <div class="bg-brandNavy text-white rounded-3xl p-6 shadow-sm flex flex-col gap-4 text-center border-t-4 border-brandCyan">
            <span class="text-brandGreen text-3xl"><i class="fa-solid fa-calendar-days"></i></span>
            <h4 id="sb-conf-title" class="text-xl font-bold font-poppins tracking-tight"></h4>
            <div class="bg-slate-800 bg-opacity-40 rounded-xl p-3 flex flex-col gap-1.5 text-slate-300 text-sm font-semibold">
                <p id="sb-conf-date"></p>
                <p id="sb-conf-loc"></p>
            </div>
            <button id="sb-conf-btn" class="bg-brandGreen hover:bg-brandCyan text-brandNavy font-bold py-2.5 px-6 rounded-full transition-colors font-poppins uppercase text-sm"></button>
        </div>
    </div>
</section>
"""

# contact-us.html
contact_us_content = """
<section class="bg-brandNavy text-white py-12 px-6">
    <div class="max-w-7xl mx-auto">
        <h1 id="contact-title" class="text-3xl md:text-4xl font-extrabold font-poppins tracking-tight"></h1>
    </div>
</section>

<section class="max-w-7xl mx-auto px-6 py-16 grid grid-cols-1 lg:grid-cols-3 gap-10">
    <!-- Info Details Cards (Col 1 & 2) -->
    <div class="lg:col-span-2 flex flex-col gap-8">
        <p id="contact-desc" class="text-slate-600 leading-relaxed text-[15px] font-semibold text-justify"></p>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 animate-slide-up">
            <!-- Office -->
            <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm hover:shadow transition-shadow flex flex-col items-center text-center">
                <span class="h-10 w-10 bg-brandCyan bg-opacity-20 text-brandCyan text-lg flex items-center justify-center rounded-full mb-4"><i class="fa-solid fa-map-marker-alt"></i></span>
                <h4 id="card-office-title" class="text-md font-bold text-brandNavy uppercase tracking-wider mb-2 font-poppins"></h4>
                <p id="card-office-addr" class="text-slate-600 text-sm leading-relaxed font-semibold"></p>
            </div>
            <!-- Email -->
            <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm hover:shadow transition-shadow flex flex-col items-center text-center">
                <span class="h-10 w-10 bg-brandGreen bg-opacity-20 text-brandGreen text-lg flex items-center justify-center rounded-full mb-4"><i class="fa-solid fa-envelope"></i></span>
                <h4 id="card-email-title" class="text-md font-bold text-brandNavy uppercase tracking-wider mb-2 font-poppins"></h4>
                <div id="card-email-list" class="text-slate-600 text-sm flex flex-col gap-1 w-full"></div>
            </div>
            <!-- Working Hours -->
            <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm hover:shadow transition-shadow flex flex-col items-center text-center">
                <span class="h-10 w-10 bg-brandBlue bg-opacity-20 text-brandBlue text-lg flex items-center justify-center rounded-full mb-4"><i class="fa-solid fa-clock"></i></span>
                <h4 id="card-hours-title" class="text-md font-bold text-brandNavy uppercase tracking-wider mb-2 font-poppins"></h4>
                <p id="card-hours" class="text-slate-600 text-sm leading-relaxed font-bold mb-1"></p>
                <p id="card-hours-sub" class="text-xs text-brandGreen font-bold tracking-wide uppercase mt-1"></p>
            </div>
        </div>

        <!-- Static Replica Address Map Details -->
        <div class="bg-slate-100 rounded-2xl p-6 border border-slate-200 mt-4 animate-slide-up flex flex-col gap-2">
            <h4 id="map-title" class="text-lg font-bold text-brandNavy font-poppins"></h4>
            <p id="map-subtitle" class="text-slate-600 text-sm font-semibold"></p>
        </div>
    </div>

    <!-- Form Callback Sidebar (Col 3) -->
    <div class="bg-white border border-slate-200 rounded-3xl p-6 shadow-md animate-slide-up flex flex-col gap-6">
        <div>
            <h2 id="form-title" class="text-xl font-bold font-poppins text-brandNavy mb-2 border-b-2 border-brandGreen w-fit pb-1"></h2>
            <p class="text-slate-500 text-xs font-bold uppercase mb-4 tracking-wider">Send your message below</p>
        </div>

        <form id="contact-form" class="flex flex-col gap-4">
            <input type="text" name="name" placeholder="Your Name" class="w-full bg-slate-50 border border-slate-300 rounded-xl p-3 focus:outline-none focus:border-brandCyan text-sm font-semibold" required>
            <input type="email" name="email" placeholder="Your Email" class="w-full bg-slate-50 border border-slate-300 rounded-xl p-3 focus:outline-none focus:border-brandCyan text-sm font-semibold" required>
            <input type="text" name="phone" placeholder="Phone Number" class="w-full bg-slate-50 border border-slate-300 rounded-xl p-3 focus:outline-none focus:border-brandCyan text-sm font-semibold">
            <textarea name="message" rows="4" placeholder="Your Message" class="w-full bg-slate-50 border border-slate-300 rounded-xl p-3 focus:outline-none focus:border-brandCyan text-sm font-semibold" required></textarea>
            
            <button type="submit" class="w-full bg-brandBlue hover:bg-brandCyan text-white font-bold py-3 px-6 rounded-xl shadow transition-colors font-poppins uppercase text-sm">Send call back request</button>
        </form>

        <div id="success-toast" class="hidden p-4 bg-emerald-50 text-emerald-800 rounded-xl border border-emerald-200 text-sm font-semibold relative">
            <span class="close-alert absolute top-2 right-3 text-lg font-bold cursor-pointer">&times;</span>
            <i class="fa-solid fa-circle-check text-emerald-500 mr-1"></i> Thank you for your message. It has been sent.
        </div>
        <div id="error-toast" class="hidden p-4 bg-rose-50 text-rose-800 rounded-xl border border-rose-200 text-sm font-semibold relative">
            <span class="close-alert absolute top-2 right-3 text-lg font-bold cursor-pointer">&times;</span>
            <i class="fa-solid fa-circle-xmark text-rose-500 mr-1"></i> There was an error trying to send your message. Please try again later.
        </div>

        <div class="border-t border-slate-200 pt-6">
            <h4 id="phone-title" class="text-sm font-bold text-slate-500 uppercase tracking-widest mb-1"></h4>
            <a id="phone-num" href="tel:+919921877870" class="text-2xl font-bold text-brandBlue hover:text-brandCyan transition-colors font-poppins"></a>
        </div>
    </div>
</section>
"""

# Map templates to files
pages = {
    "index.html": ("Arunodaya Pharmacy College Bidar - Arunodaya Pharmacy College Of Pharmacy Aurad", "home", index_content),
    "about.html": ("Who We Are - Arunodaya Pharmacy College Of Pharmacy Aurad", "about", about_content),
    "admission-process.html": ("Admission Process - Arunodaya Pharmacy College Of Pharmacy Aurad", "admission", admission_content),
    "teaching-staff.html": ("Teaching Staff - Arunodaya Pharmacy College Of Pharmacy Aurad", "teachingStaff", teaching_staff_content),
    "non-teaching-staff.html": ("Non-Teaching Staff - Arunodaya Pharmacy College Of Pharmacy Aurad", "nonTeachingStaff", non_teaching_staff_content),
    "facilities.html": ("Facilities - Arunodaya Pharmacy College Of Pharmacy Aurad", "facilities", facilities_content),
    "b-pharm.html": ("B. Pharm - Arunodaya Pharmacy College Of Pharmacy Aurad", "courses", course_detail_content),
    "d-pharm.html": ("D. Pharm - Arunodaya Pharmacy College Of Pharmacy Aurad", "courses", course_detail_content),
    "b-sc.html": ("B.Sc - Arunodaya Pharmacy College Of Pharmacy Aurad", "courses", course_detail_content),
    "b-com.html": ("B.Com - Arunodaya Pharmacy College Of Pharmacy Aurad", "courses", course_detail_content),
    "bca.html": ("BCA - Arunodaya Pharmacy College Of Pharmacy Aurad", "courses", course_detail_content),
    "syllabus.html": ("Syllabus - Arunodaya Pharmacy College Of Pharmacy Aurad", "syllabus", table_pages_content),
    "academic-calendar.html": ("Academic Calendar - Arunodaya Pharmacy College Of Pharmacy Aurad", "academicCalendar", table_pages_content),
    "time-table.html": ("Time Table - Arunodaya Pharmacy College Of Pharmacy Aurad", "timeTable", table_pages_content),
    "gallery.html": ("Gallery - Arunodaya Pharmacy College Of Pharmacy Aurad", "gallery", gallery_content),
    "news-events.html": ("News & Events - Arunodaya Pharmacy College Of Pharmacy Aurad", "newsEvents", news_events_content),
    "contact-us.html": ("Contact Us - Arunodaya Pharmacy College Of Pharmacy Aurad", "contact", contact_us_content)
}

# Write all HTML files
for filename, (title, active_class, inner_body) in pages.items():
    html_data = generate_html_shell(title, active_class, inner_body)
    with open(os.path.join(workspace_dir, filename), "w", encoding="utf-8") as f:
        f.write(html_data)
    print(f"Generated {filename}")

print("Site generation completed successfully!")
