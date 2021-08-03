```
select * from language;
select title, description, and language
select film.title, film.description, language.name from film left join language on film.language_id = language.language_id;
select film.title, film.description, language.name from film right join language on film.language_id = language.language_id;
create table new_film(id serial primary key, name varchar(200));
create table customer_review(review_id serial primary key, film_id int, language_id int, title varchar(100), score smallint, review_text text, last_update timestamp default now(), foreign key (film_id) references new_film(id) on delete cascade, foreign key (language_id) references language(language_id));
insert into new_film(name) values('film1');
insert into new_film(name) values('film2');
insert into new_film(name) values('film3');
insert into customer_review(film_id, language_id, title, score, review_text) values((select id from new_film where name='film1'), (select language_id from language where name = 'English'), 'dont watch', 1, 'didnt enjoy this film, maybe next time');
insert into customer_review(film_id, language_id, title, score, review_text) values((select id from new_film where name='film2'), (select language_id from language where name = 'English'), 'watchable', 7, 'great film');
delete from new_film where name='film1';
```

the customer\_review table also gets the related row deleted because of the added on delete cascade.

```
update film set language_id = (select language_id from language where name = 'French') where film_id < 10;
```

store\_id and address\_id, so we need to provide each time the correct id's (because its not null), possibly by
selecting those id's in subqueries.

```
drop table customer_review;
select count(*) from rental where return_date = null;
select film.title, film.rental_rate from rental inner join inventory on rental.inventory_id = inventory.inventory_id inner join film on film.film_id = inventory.film_id where rental.return_date = null order by film.rental_rate desc limit 30;
select film.title from film_actor inner join actor on film_actor.actor_id = actor.actor_id inner join film on film.film_id = film_actor.film_id where actor.first_name = 'Penelope' and actor.last_name = 'Monroe' and film.description like '%Sumo%';
select film.title from film_category inner join category on film_category.category_id = category.category_id inner join film on film.film_id = film_category.film_id where category.name = 'Documentary' and film.rating = 'R' and film.length < 60;
select film.title from customer inner join payment on customer.customer_id = payment.customer_id inner join rental on payment.rental_id = rental.rental_id inner join inventory on rental.inventory_id = inventory.inventory_id inner join film on film.film_id = inventory.film_id where customer.first_name = 'Matthew' and customer.last_name = 'Mahan' and payment.amount > 4 and rental.return_date > date 'July 28 2005' and rental.return_date < date 'August 1 2005';
select film.title, film.replacement_cost from customer inner join payment on customer.customer_id = payment.customer_id inner join rental on payment.rental_id = rental.rental_id inner join inventory on rental.inventory_id = inventory.inventory_id inner join film on film.film_id = inventory.film_id where customer.first_name = 'Matthew' and customer.last_name = 'Mahan' and film.title like '%Boat%' or film.description like '%Boat%' order by film.replacement_cost desc limit 1;
```
