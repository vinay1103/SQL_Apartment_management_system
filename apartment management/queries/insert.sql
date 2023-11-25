insert into flat values('A1001',2);
insert into flat values('C202',3);
insert into flat values('A103',2);
insert into flat values('A208',2);
insert into flat values('B304',3);


insert into parking_slot values(100,'E-Scooter','A1001');
insert into parking_slot values(322,'SUV','C202');
insert into parking_slot values(103,'Cycle','A103');
insert into parking_slot values(128,'Sedan','A208');
insert into parking_slot values(234,'SUV','B304');


-- IF HAVING PET INSERT DIRECTLY, else mention attributes and register

-- Replace the first value of each schema with 'Firstletter_Number' format
insert into resident values('R01','Sahana','Ramesh','2001-07-10',9837837628,'F','Dog','A1001','Own');
insert into resident (Aadhar,Fname,Lname,DOB,phone,gender,FlatID,rent_owned) values('R02','Ritesh','Kumar','2001-04-03',9987452411,'M','C202','Own');
insert into resident values('R03','Sachin','Shenoy','2001-06-16',9848367537,'M','Cat','A103','Rent');
insert into resident (Aadhar,Fname,Lname,DOB,phone,gender,FlatID,rent_owned) values('R04','Vaibhav','Suresh','2001-07-16',8723786821,'M','A208','Rent');
insert into resident (Aadhar,Fname,Lname,DOB,phone,gender,FlatID,rent_owned) values('R05','Shreyas','Devraj','2001-01-05',8362627761,'M','B304','Own');

insert into security values('S01','Bahadur','J','6366536763','2018-10-01','Day');
insert into security values('S02','Praveen','Singh','3675372582','2015-01-04','Day');
insert into security values('S03','Ravi','Kumar','9847638375','2016-11-01','Night');
insert into security values('S04','Sharma','Ji','7375167251','2014-06-01','Night');
insert into security values('S05','Nayak','A','7636453771','2017-03-05','Day');

insert into dependent values('D01','R01','Ikya','Beria','2001-08-10','8736278563','F');
insert into dependent values('D02','R01','Sahan','Shetty','2010-04-01','7465736245','M');
insert into dependent values('D03','R01','Shreya','Shetty','1950-04-10','7465736245','F');
insert into dependent values('D04','R01','Raksha','Hemmige','2001-03-11','6237161571','F');
insert into dependent values('D05','R02','Ramesh','G','2001-02-08','8762542161','M');
insert into dependent values('D06','R03','Suhas','K','2001-11-24','9863534643','M');
insert into dependent values('D07','R03','Mehul','Mehta','2004-05-03','9123534643','M');
insert into dependent values('D08','R04','Raghu','NV','2001-10-01','2753625711','M');
insert into dependent values('D09','R05','Sanjana','Atrey','2001-11-01','8726353171','M');
insert into dependent values('D10','R05','Sanjay','Atrey','1940-11-01','8726353171','M');

insert into visitor (visitorID,flatID,Fname,Lname,purpose,phonenumber,time_of_entry) values('V01','A103','Raghu','NV','Personal','8926781618','2020-10-19 12:30:01');
insert into visitor (visitorID,flatID,Fname,Lname,purpose,phonenumber,time_of_entry) values('V02','A1001','Nihal','Shetty','Visit','8926781623','2021-11-19 11:36:01');
insert into visitor (visitorID,flatID,Fname,Lname,purpose,phonenumber,time_of_entry) values('V03','A1001','Neha','Shetty','Visit','8926121623','2021-11-19 12:36:01');
insert into visitor (visitorID,flatID,Fname,Lname,purpose,phonenumber,time_of_entry) values('V04','A1001','Roopak','M','Inspection','8926671623','2021-11-23 09:18:19');
insert into visitor (visitorID,flatID,Fname,Lname,purpose,phonenumber,time_of_entry) values('V05','B304','Nihal','Shetty','Visit','8926781623','2021-11-21 10:32:01');
insert into visitor (visitorID,flatID,Fname,Lname,purpose,phonenumber,time_of_entry) values('V06','B304','Dhruv','Shetty','Professional','823726531','2021-11-18 09:01:12');
insert into visitor (visitorID,flatID,Fname,Lname,purpose,phonenumber,time_of_entry) values('V07','C202','Dhanush','Kumar','Party','8237231531','2021-11-18 21:11:12');
insert into visitor (visitorID,flatID,Fname,Lname,purpose,phonenumber,time_of_entry) values('V08','C202','Iqrar','Ahmed','Sports','8224231531','2021-11-18 16:16:12');

insert into complaints values('C01','R01','Water leakage from faucet','2021-10-01','18:01:10');
insert into complaints values('C02','R02','Plug points not working','2021-11-01','15:01:10');
insert into complaints values('C03','R05','Internet down','2021-11-01','06:11:21');
insert into complaints values('C04','R05','Street Light','2021-11-03','22:19:21');

insert into services values('Svc01',200.00,'Plumbing');
insert into services values('Svc02',500.00,'Electrician');
insert into services values('Svc03',600.00,'Internet');
insert into services values('Svc04',200.00,'Car Wash');

insert into employee values('E01','Ramesh','Krishna','8767381681','2017-01-04','M','Day','Svc04',16000);
insert into employee values('E02','Saral','V','8767381688','2010-01-04','M','Night','Svc04',18000);
insert into employee values('E03','Kiran','Krishna','8767381611','2015-11-14','M','Night','Svc03',25000);
insert into employee values('E04','Ganga','Manoj','8767381621','2015-07-14','F','Day','Svc03',15700);
insert into employee values('E05','Kaveri','G','8767387652','2015-08-18','F','Day','Svc01',19000);
insert into employee values('E06','Manoj','Kumar','8767381612','2016-11-14','M','Day','Svc02',19500);

insert into flat_has_security values('A1001','S02');
insert into flat_has_security values('A103','S05');
insert into flat_has_security values('C202','S03');
insert into flat_has_security values('A208','S04');
insert into flat_has_security values('B304','S05');

insert into resident_avails_services (ResidentUID,serviceID) values('R01','Svc01');
insert into resident_avails_services (ResidentUID,serviceID) values('R02','Svc02');
insert into resident_avails_services (ResidentUID,serviceID) values('R05','Svc03');
insert into resident_avails_services (ResidentUID,serviceID) values('R05','Svc03');

-- Residents
insert into auth values ('R01', 'R01', 'res');
insert into auth values ('R02', 'R02', 'res');
insert into auth values ('R03', 'R03', 'res');
insert into auth values ('R04', 'R04', 'res');
insert into auth values ('R05', 'R05', 'res');
insert into auth values ('R06', 'R06', 'res');

-- Security
insert into auth values ('S01', 'S01', 'sec');
insert into auth values ('S02', 'S02', 'sec');
insert into auth values ('S03', 'S03', 'sec');
insert into auth values ('S04', 'S04', 'sec');

-- Admin
insert into auth values ('adm', 'adm', 'adm');
