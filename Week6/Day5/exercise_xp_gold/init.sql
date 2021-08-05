create database credentials;
\c credentials;
create table users(user_id serial primary key, username varchar(100) unique not null, password varchar(512) not null);
