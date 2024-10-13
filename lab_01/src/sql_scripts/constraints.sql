alter table client
(
    add constraint pk_client_id primary key(id),
    alter column name set not null,
    alter column surname set not null,
    alter column email set not null,
    alter column phone set not null,
    add constraint fk_vehicle_id foreign key(vehicleId)
    reference vehicle(vehicleId);
);

alter table employee
(
    add constraint pk_employee_id primary key(id),
    alter column name set not null,
    alter column surname set not null,
    add constraint fk_specialization_id foreign key(specializationId)
    references specialization(id);
);

alter table specialization
(   
     add constraint pk_specialization_id primary key(id),
    alter column name set not null;
);

alter table vehicle
(
    add constraint pk_vehicle_id primary key(id),
    alter column brand set not null,
    alter column model set not null,
    add constraint fk_vehicleClass_id foreign key(vehicleClassId)
    references vehicleClass(id),
    alter column urgent set not null;

alter table vehicleClass
    add constraint pk_vehicleClass_id primary key(id),
    alter column class set not null;
);

alter table service
(
    add constraint pk_service_id primary key(id),
    add constraint fk_client foreign key(clientId)
    references client(id),
    add constraint fk_employee foreign key(employeeId)
    references employee(id),
    add constraint fk_serviceType foreign key(serviceTypeId)
    references serviceType(id),
    alter column cost set not null;
);

alter table serviceType
(
    add constraint pk_serviceType_if primary key(id),
    alter column name set not null;
);
