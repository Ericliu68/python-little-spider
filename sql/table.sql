-- 
-- NAME:area  地点（省，市，区）;Type:TABLE;
-- 
create table province(
id serial primary key,
province varchar
);
create table city(
id serial primary key,
city varchar,
province_foreign_id int not null
);
create table area(
id serial primary key,
area varchar,
city_foreign_id int not null
);
-- 
-- NAME:yemo  时间（年月）;Type:TABLE;
-- 
create table yemo(
id serial primary key,
sight_name varchar,
year_month varchar ,
sight_soldnum varchar,
area_foreign_id int not null
);
-- 
-- NAME:yemo  景点信息表;Type:TABLE;
-- 
create table attractions(
id serial primary key,
sight_name varchar not null,
sight_level varchar ,
-- sight_area varchar,
sight_price varchar,
sight_soldnum varchar,
sight_hot varchar,
sight_addreplace varchar,
sight_point varchar,
year_month varchar,
area_foreign_id int not null
);
-- alter table attractions add constraint FK_year_month foreign key(year_month) references yemo(year_month);
-- alter table area add constraint FK_sight_area foreign key(sight_area) references attractions(sight_area);
ALTER TABLE province ADD CONSTRAINT uni_3 unique(province);
alter table city add constraint uni_4 unique(city,province_foreign_id);
alter table area add constraint uni_5 unique(area,city_foreign_id);
alter table yemo add constraint uni_1 unique(sight_name,year_month,area_foreign_id);
alter table attractions add constraint uni_2 unique(sight_name);