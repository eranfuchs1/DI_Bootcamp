```
\c public
select * from items order by price;
select * from items where price >= 80 order by price desc;
select customer_fname, customer_lname from customers order by customer_fname || customer_lname;
select customer_lname from customers order by customer_lname desc;
create table purchases(customer_id int, item_id int, foreign key (customer_id) references customers(customer_id), foreign key (item_id) references items(item_id));
insert into purchases(customer_id) values((select customer_id from customers limit 1));
```
*it works because the table definition allows nulls, since we didn't specify "not null" in the table creation.*
```
insert into purchases(customer_id, item_id) values (1,2), (2,1), (3,1),(4,2),(5,3);
select * from purchases;
```
it's not useful because we don't directly see who bought what.
```
select * from purchases inner join customers on purchases.customer_id = customers.customer_id;
select * from purchases inner join customers on purchases.customer_id = customers.customer_id where customers.customer_id = 4;
select * from purchases inner join items on purchases.item_id = items.item_id where items.item = 'Small Desk' or items.item = 'Large Desk';
insert into purchases(customer_id, item_id) values((select customers.customer_id from customers where customers.customer_fname = 'Scott' and customers.customer_lname = 'Scott' limit 1), (select items.item_id from items where items.item = 'Hard Drive' limit 1));
select customers.customer_fname, customers.customer_lname, items.item from purchases inner join items on items.item_id = purchases.item_id inner join customers on purchases.customer_id = customers.customer_id;
\c dvdrental
select * from customer;
select first_name || last_name as full_name from customer;
select distinct create_date from customer;
select * from customer order by first_name desc;
select film_id, title, description, release_year from film order by rental_rate asc;
select address.address, address.phone from address inner join customer on address.address_id = customer.address_id and address.district = 'Texas';
select * from film where film_id = 15 or film_id = 150;
select film_id, title, description, length, rental_rate from film where title like '%Fast and Furious%';
select film_id, title, description, length, rental_rate from film where title like 'Fa%';
select film_id, title, description, length, rental_rate from film order by rental_rate limit 10;
select payment.amount, payment.payment_date from payment inner join customer on customer.customer_id = payment.customer_id order by payment.customer_id;
select * from film where film.film_id not in (select inventory.film_id from inventory);
select city.city, country.country from city inner join country on city.country_id = country.country_id;
select customer.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date from customer inner join payment on customer.customer_id = payment.customer_id order by payment.staff_id;
```
