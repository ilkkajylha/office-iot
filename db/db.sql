CREATE DATABASE IF NOT EXISTS `officeiot` DEFAULT CHARACTER SET utf8;
USE `officeiot`;


CREATE TABLE rooms (
        id              int NOT NULL AUTO_INCREMENT,
        name            char(100),
        company_name    char(100),
        status          int(1),
        primary key (id),
        foreign key (company_name) references companies
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE users (
        email           char(100) not null,
        password        char(100),
        company_name    char(100),
        primary key (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE companies (
        id              int NOT NULL AUTO_INCREMENT,
        company_name    char(100) not null,
        primary key (id),
        foreign key (comapny_name) references rooms,
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

