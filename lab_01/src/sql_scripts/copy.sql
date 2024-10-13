\copy client(id, name, surname, email, phone, vehicleId) from 'C:\Study\2024\db_2024\lab_01\data\client.csv' delimiter ',' csv header;
\copy employee(id, name, surname, specializationId) from 'C:\Study\2024\db_2024\lab_01\data\employee.csv' delimiter ',' csv header;
\copy service(id, clientId, employeeId, serviceTypeId, cost) from 'C:\Study\2024\db_2024\lab_01\data\service.csv' delimiter ',' csv header;
\copy serviceType(id, name) from 'C:\Study\2024\db_2024\lab_01\data\serviceType.csv' delimiter ',' csv header;
\copy specialization(id, name) from 'C:\Study\2024\db_2024\lab_01\data\specizialtion.csv' delimiter ',' csv header;
\copy vehicle(id, brand, model, vehicleClassId, urgent) from 'C:\Study\2024\db_2024\lab_01\data\vehicle.csv' delimiter ',' csv header;
\copy client(id, class) from 'C:\Study\2024\db_2024\lab_01\data\vehicleClass.csv' delimiter ',' csv header;
