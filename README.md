
Picture Perfect:




Packages to be installed:

1.python
2.flask 
3.smtplib
4.flask_bootstrap 
5.pillow
6.flask_mail
7.paypalrestsdk
8.psycopg2
9.opencv-python
10.flask_wtf
11.sqlalchemy

Database Commands:
1. CREATE TABLE customer(USERNAME TEXT PRIMARY KEY NOT NULL, EMAIL TEXT NOT NULL,PASSWORD TEXT 	NOT NULL, FIRSTNAME TEXT NOT NULL,LASTNAME TEXT NOT NULL, CONFIRMED BOOLEAN not null);


2.CREATE TABLE premiumcustomer( premiumid SERIAL PRIMARY KEY, USERNAME text references customer(username), paymentstatus TEXT    NOT NULL, ispremium BOOLEAN NOT NULL,   paymentid  TEXT 	NOT NULL);  
   
3.CREATE TABLE images (user_name text references customer(username),  image_data bytea,"timestamp" time without time zone,  image_size integer,  id SERIAL primary key ) WITH ( OIDS=FALSE );

Group Members:
1. Shreya Nair 
2. Archita Gupta 
3.Vibhuti Gajinkar
