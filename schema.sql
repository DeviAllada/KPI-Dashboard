
CREATE DATABASE operations_kpi;
USE operations_kpi;

CREATE TABLE operations_data(
id INT AUTO_INCREMENT PRIMARY KEY,
agent VARCHAR(100),
team VARCHAR(50),
cases_processed INT,
pending_cases INT,
sla_status VARCHAR(20),
process_date DATE
);
