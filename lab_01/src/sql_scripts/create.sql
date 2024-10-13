create table if not exists client
(
    id serial,
    name varchar(50),
    surname varchar(50),
    email varchar(50),
    phone varchar(12),
    vehicleId int
);

create table if not exists employee
(
    id serial,
    name varchar(50),
    surname varchar(50),
    specializationId int 
);

create table if not exists specialization
(
    id serial,
    name varchar(50) 
);

create table if not exists vehicle
(
    id serial,
    brand varchar(50),
    model varchar(50),
    vehicleClassId int,
    urgent boolean    
);

create table if not exists vehicleClass
(
    id serial,
    class varchar(50) 
);

create table if not exists service
(
    id serial,
    clientId int,
    employeeId int,
    serviceTypeId int,
    cost float    
);

create table if not exists serviceType
(
    id serial,
    name varchar(50) 
);