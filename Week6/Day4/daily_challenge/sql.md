```
create database daily_challengew6d4;
\c daily_challengew6d4;
create table items(item_id serial primary key, price int not null);
create table orders(order_id serial primary key, item_id int not null, date timestamp default now(), foreign key(item_id) references items(item_id));
create function get_total_order_price(order_id int)
returns int
language plpgsql
as $$
declare
	total_price int;
begin
	select sum(items.price) into total_price from orders inner join items on orders.item_id = items.item_id where orders.order_id = order_id;
	return total_price;
end
$$;
create table users(user_id serial primary key, user_name varchar(100) not null, order_id int not null, foreign key (order_id) references orders(order_id));
create function get_total_order_price_of_user(user_name varchar(100), order_id int)
returns int
language plpgsql
as $$
declare
	total_price int;
begin
	select sum(items.price) into total_price from orders inner join items on orders.item_id = items.item_id inner join users on users.user_name = user_name and users.order_id = order_id where orders.order_id = order_id;
	return total_price;
end
$$;
```
