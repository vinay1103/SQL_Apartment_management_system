-- Creating a new database
create database apna_ghar_new;
use apna_ghar_new;
-- Creating resident table 


create table flat
(
	FlatID varchar(10) primary key not null,
	no_bhk int not null
);

create table resident
(
	Aadhar varchar(12) not null,
	Fname varchar(15) not null,
	Lname varchar(15),
	DOB date not null,
	phone varchar(10) not null,
	gender varchar(2) not null,
	pet_info varchar(20) default 'no pet',
	FlatID varchar(10), 
	rent_owned varchar(10), 
	primary key (Aadhar),
	foreign key(FlatID) references flat(FlatID)
);

-- Creating security table 
create table security
(
	securityID varchar(10) not null,
	Fname varchar(15) not null,
	Lname varchar(15),
	phone varchar(10) not null,
	doj date not null,
	shift varchar(5) default 'day',
	primary key (securityID)
);

-- Creating services table 
create table services
(
	serviceID varchar(10) not null,
	cost real,
	type varchar(20),
	primary key (serviceID)
);

-- Creating employee table 
create table employee
(
	employeeID varchar(10) not null,
	Fname varchar(15) not null,
	Lname varchar(15),
	phone varchar(10) not null,
	doj date not null,
	gender varchar(2) not null,
	shift varchar(5) default 'day',
	serviceID varchar(10) not null,
	salary real not null check(salary>15000),
	primary key (employeeID),
	foreign key (serviceID) references services(serviceID)
);

-- Creating flat table 


-- Creating parking_slot table 
create table parking_slot
(
	slotNo integer not null,
	vehicle_type varchar(10),
	flatID varchar(10) not null,
	primary key (slotNo),
	foreign key (flatID) references flat(flatID)
);

-- Creating dependent table 
create table dependent
(
	Aadhar varchar(12) not null,
	residentUID varchar(12) not null,
	Fname varchar(15) not null,
	Lname varchar(15),
	DOB date not null,
	phone varchar(10) not null,
	gender varchar(2) not null,
	primary key (Aadhar),
	foreign key(residentUID) references resident(Aadhar)
);

-- Creating visitor table 
create table visitor
(
	visitorID varchar(10) not null,
	flatID varchar(10) not null,
	Fname char(15) not null,
	Lname char(15), 
	purpose varchar(100),
	phonenumber varchar(10), 
	time_of_entry timestamp,
	time_of_exit timestamp,
	primary key(visitorID,flatID),
	foreign key(flatID) references flat(FlatID)
);

-- Creating complaints table 
create table complaints
(
	ComplaintID varchar(10) primary key, 
	ResidentUID varchar(14), 
	Complain char(100), 
	date date,time time,
	foreign key(ResidentUID) references resident(Aadhar)
);


-- Creating flat_has_security table 
create table flat_has_security
(
	FlatID varchar(10),
	securityID varchar(10),
	primary key(FlatID,securityID),
	foreign key(FlatID) references flat(FlatID),
	foreign key(securityID) references security(securityID)
	);

-- Creating resident_avails_services table 
create table resident_avails_services
(
	ResidentUID varchar(14),
	serviceID varchar(10), 
	serviceTime timestamp DEFAULT CURRENT_TIMESTAMP,
	primary key(ResidentUID,serviceID,serviceTime),
	foreign key(ResidentUID) references resident(Aadhar)
	);

create table auth
(
	username varchar(12) not null,
	password varchar(20) not null,
	type varchar(10) not null,
	Primary key (username)
);

-- Agregate Function and View
CREATE VIEW complaint_counts_view AS
SELECT ResidentUID, COUNT(*) AS ComplaintCount
FROM complaints
GROUP BY ResidentUID;

-- Procedure
DELIMITER //
CREATE PROCEDURE get_residents_with_dependents_count()
BEGIN
    SELECT r.Aadhar, r.Fname, r.FlatID, (COUNT(d.Aadhar)+1) AS dependents_count
    FROM resident r
    LEFT JOIN dependent d ON r.Aadhar = d.residentUID
    GROUP BY r.Aadhar;
END;
//
DELIMITER ;

-- Trigger
-- Trigger
DELIMITER //

CREATE TRIGGER before_complaint_update
BEFORE UPDATE ON complaints
FOR EACH ROW
BEGIN
    -- Set the updated date and time to the current date and time
    SET NEW.date = CURDATE();
    SET NEW.time = CURTIME();
END;

//

DELIMITER ;


show tables;
select * from auth;
select * from resident;
