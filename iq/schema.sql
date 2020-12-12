DROP TABLE IF EXISTS Department;

DROP TABLE IF EXISTS Treatment;
DROP TABLE IF EXISTS Wards;
DROP TABLE IF EXISTS Nurse;
DROP TABLE IF EXISTS Nurse_Contact;
DROP TABLE IF EXISTS Doctor;
DROP TABLE IF EXISTS Doctor_Contact;
DROP TABLE IF EXISTS Patient;
DROP TABLE IF EXISTS Bill;
 
DROP TABLE IF EXISTS Patient_Contact;


CREATE TABLE Department
(
 Dept_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
 Name VARCHAR(30) NOT NULL
);

CREATE TABLE Treatment
(
 T_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
 Name VARCHAR(30) NOT NULL,
 Cost FLOAT NOT NULL
);

CREATE TABLE Wards
(
 Ward_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
 Room_type VARCHAR(30) NOT NULL
);

CREATE TABLE Nurse
(
 N_ID  INTEGER  IDENTITY(1,1),
 Name VARCHAR(30)  NOT NULL,
 Address VARCHAR(30)  NOT NULL,
 DOB DATE NOT NULL,
 Sex VARCHAR(30) NOT NULL,
 Salary INT NOT NULL,
 Ward_ID INT,
 PRIMARY KEY (N_ID, Ward_ID),
 FOREIGN KEY (Ward_ID) REFERENCES Wards(Ward_ID)
);

CREATE TABLE Nurse_Contact
(
 Contact INT NOT NULL,
 N_ID INT NOT NULL,
 Ward_ID INT NOT NULL,
 PRIMARY KEY (Contact, N_ID, Ward_ID),
 FOREIGN KEY (N_ID, Ward_ID) REFERENCES Nurse(N_ID, Ward_ID)
);

CREATE TABLE Doctor
(
 Name VARCHAR(30)  NOT NULL,
 DOB DATE NOT NULL,
 Address VARCHAR(30) NOT NULL,
 Sex VARCHAR(30) NOT NULL,
 D_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
 Salary INT NOT NULL,
 Dept_ID INT ,
 FOREIGN KEY (Dept_ID) REFERENCES Department(Dept_ID)
);
CREATE TABLE Doctor_Contact
(
 Contact INT NOT NULL,
 D_ID INT NOT NULL,
 PRIMARY KEY (Contact, D_ID),
 FOREIGN KEY (D_ID) REFERENCES Doctor(D_ID)
);


CREATE TABLE Patient
(
 Address VARCHAR(30) NOT NULL,
 Sex VARCHAR(30) NOT NULL,
 Date_admit DATE NOT NULL,
 Date_Discharged DATE ,
 DOB DATE NOT NULL,
 Name VARCHAR(30) NOT NULL,
 P_ID INTEGER PRIMARY KEY   AUTOINCREMENT NOT NULL,
 D_ID INT ,
 Ward_ID INT NOT NULL ,
 FOREIGN KEY (D_ID) REFERENCES Doctor(D_ID),
 FOREIGN KEY (Ward_ID) REFERENCES Wards(Ward_ID)
);
CREATE TABLE Bill
(
 T_ID INT NOT NULL,
 P_ID INT NOT NULL,
 PRIMARY KEY (T_ID, P_ID),
 FOREIGN KEY (T_ID) REFERENCES Treatment(T_ID),
 FOREIGN KEY (P_ID) REFERENCES Patient(P_ID)
);
CREATE TABLE Patient_Contact
(
 Contact INT NOT NULL,
 P_ID INT NOT NULL,
 PRIMARY KEY (Contact, P_ID),
 FOREIGN KEY (P_ID) REFERENCES Patient(P_ID)
);

