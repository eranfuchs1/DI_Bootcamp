```
create database bootcamp;

\c bootcamp

create table students(id serial, last_name varchar(100), first_name varchar(100), birth_date varchar(100));

insert into students(first_name, last_name, birth_date) values

('Marc','Benichou','02/11/1998'),
('Yoan','Cohen','03/12/2010'),
('Lea','Benichou','27/07/1987'),
('Amelia','Dux','07/04/1996'),
('David','Grez','14/06/2003'),
('Omer','Simpson','03/10/1980');

insert into students(first_name, last_name, birth_date) values ('Eran','Fuchs','29/04/1996');

select * from students;

select first_name, last_name from students;

select first_name, last_name from students where id = 2;

select first_name, last_name from students where last_name = 'Benichou' and first_name = 'Marc';

select first_name, last_name from students where last_name = 'Benichou' or first_name = 'Marc';

select first_name, last_name from students where first_name like '%a%';

select first_name, last_name from students where first_name like 'a%';

select first_name, last_name from students where first_name like '%a';

select first_name, last_name from students where first_name like '%a_';

select first_name, last_name from students where id = 1 and id = 3;

select * from students where date(birth_date) >= date '01/01/2000';




```
