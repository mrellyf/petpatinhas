CREATE DATABASE petagenda;

USE petagenda;

CREATE TABLE agendamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tutor VARCHAR(100) NOT NULL,
    pet VARCHAR(100) NOT NULL,
    servico VARCHAR(50) NOT NULL,
    data DATE NOT NULL,
    horario TIME NOT NULL
);