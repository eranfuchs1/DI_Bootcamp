```
select first_name, last_name, birth_date from students order by last_name limit 4;


select first_name, last_name, birth_date from students order by date(birth_date) desc limit 1;

select first_name, last_name, birth_date from students offset 2 limit 3;
```
