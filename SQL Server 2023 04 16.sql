/*CREATING DATABASE*/
create database overflow;

/*Creating a table*/
create table users(
	nombre VARCHAR(30),
	clave VARCHAR(30)
);

/*Excute procedures, exec, IS A NATIVE PROCEDURE OF SQL SERVER*/
exec sp_columns users;

drop table users;

SELECT * FROM users;

INSERT INTO users(nombre, clave) values('Ricardo','78rr');