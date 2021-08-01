```
create database public;

\c public

create table items (item_id serial primary key, item varchar(70), price int);

create table customers (customer_id serial primary key, customer_fname varchar(100), customer_lname varchar(100));

insert into items(item, price) values ('Small Desk', 100);

insert into items(item, price) values ('Large Desk', 300), ('Fan', 80);

insert into customers (customer_fname, customer_lname ) values ('Greg','Jones'),
('Sandra','Jones'),
('Scott','Scott'),
('Trevor','Green'),
('Melanie','Johnson');

select * from items;

select * from items where price > 80;

select * from items where price <= 300;

select * from customers where customer_lname = 'Smith';

select * from customers where customer_lname = 'Jones';

select * from customers where customer_lname != 'Scott';

```
