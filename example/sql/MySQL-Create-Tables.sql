/********************************************************************************/
/*																				*/
/*	Kroenke and Auer - Database Concepts (5th Edition) Chapter 03				*/
/*																				*/
/*	Wedgewood Pacific Corporation Create Tables									*/
/*																				*/
/*	These are the Microsoft SQL Server 2008/2008R2 SQL code solutions			*/
/*																				*/
/********************************************************************************/

CREATE  TABLE DEPARTMENT(
	DepartmentName	Char(35)		NOT NULL	PRIMARY KEY, 
	BudgetCode		Char(30)		NOT NULL,
	OfficeNumber	Char(15)		NOT NULL,
	Phone			Char(12)		NOT NULL
	);

CREATE  TABLE EMPLOYEE(
	EmployeeNumber	Int 			NOT NULL auto_increment PRIMARY KEY,
	FirstName		Char(25) 		NOT NULL,
	LastName        Char(25) 		NOT NULL,
	Department		Char(35)		NOT NULL DEFAULT 'Human Resources',
	Phone			Char(12)		NULL,
	Email 			VarChar(100)	NOT NULL UNIQUE,
	/* Define foreign key using constraint */
	/* ON UPDATE CASCADE means that if the DepartmentName attribute changes in DEPARTMENT table, 
	the value will also be updated in EMPLOYEE table. */
	/* If ON UPDATE CASCADE is not specified, ON UPDATE NO ACTION is used by default.*/
	/* ON UPDATE NO ACTION specifies that if an attempt is made to update a key value in a row whose key is referenced by foreign keys in existing rows in other tables, an error is raised and the UPDATE is rolled back.*/
	CONSTRAINT 		EMP_DEPART_FK	FOREIGN KEY(Department)
						REFERENCES DEPARTMENT(DepartmentName)
							ON UPDATE CASCADE
) AUTO_INCREMENT=12;

CREATE  TABLE PROJECT (
	ProjectID		Int				NOT NULL AUTO_INCREMENT	PRIMARY KEY,
	ProjectName		Char(50) 		NOT NULL,
	Department		Char(35)		NOT NULL,
	MaxHours		Numeric(8,2)	NOT NULL DEFAULT 100,
    StartDate		DateTime		NULL,
    EndDate			DateTime		NULL,

	CONSTRAINT 		PROJ_DEPART_FK	FOREIGN KEY(Department)
						REFERENCES DEPARTMENT(DepartmentName)
							ON UPDATE CASCADE
);

CREATE  TABLE ASSIGNMENT (
   	ProjectID		Int	 			NOT NULL,
	EmployeeNumber	Int	 			NOT NULL,
    HoursWorked		Numeric(6,2)	NULL,
   	CONSTRAINT 		ASSIGNMENT_PK 	PRIMARY KEY (ProjectID, EmployeeNumber),
   	/* ON DELETE CASCADE means that if there is an attempt is made to delete a ProjectID in PROJECT table, the deletion will also be carried in ASSIGNMENT table. */
   	CONSTRAINT 		ASSIGN_PROJ_FK  FOREIGN KEY (ProjectID)
						REFERENCES PROJECT (ProjectID)
							ON UPDATE NO ACTION
							ON DELETE CASCADE,
    CONSTRAINT 		ASSIGN_EMP_FK   FOREIGN KEY (EmployeeNumber)
						REFERENCES EMPLOYEE (EmployeeNumber)
							ON UPDATE NO ACTION
							ON DELETE NO ACTION
 	);

/********************************************************************************/
