```
create table foreign_table(id serial primary key);
create table one_to_one(id serial primary key, foreign_id int, constraint foreign_id foreign key (foreign_id) references foreign_table(id));
create table one_to_many(id serial primary key, foreign_id int, foreign key (foreign_id) references foreign_table(id) on delete cascade);
create table many_to_many(id serial primary key, foreign_id int, other_foreign_id int, foreign key (foreign_id) references foreign_table(id) on update cascade, foreign key (other_foreign_id) references foreign_table(id) on update cascade);

insert into foreign_table(id) values(1),(2),(3);
insert into one_to_one(foreign_id) values (1),(2),(3);
insert into one_to_many(foreign_id) values (1),(2),(2),(3),(3),(3);
insert into many_to_many(foreign_id, other_foreign_id) values (1,2),(2,2),(3,2),(2,3),(1,3),(3,3);

select * from one_to_one inner join one_to_many on one_to_one.foreign_id = one_to_many.foreign_id left join many_to_many on many_to_many.other_foreign_id = one_to_many.foreign_id;
select * from one_to_one inner join one_to_many on one_to_one.foreign_id = one_to_many.foreign_id left outer join many_to_many on many_to_many.other_foreign_id = one_to_many.foreign_id;
select * from one_to_one right outer join one_to_many on one_to_one.foreign_id = one_to_many.foreign_id full join many_to_many on many_to_many.other_foreign_id = one_to_many.foreign_id;
select * from one_to_one right outer join one_to_many on one_to_one.foreign_id = one_to_many.foreign_id full outer join many_to_many on many_to_many.other_foreign_id = one_to_many.foreign_id;
```
