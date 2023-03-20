--Create Table:
create table products(name varchar(100), sku varchar(5), price decimal(5,2), type varchar(30), size varchar(10));

--Script One:
insert into products(name, sku, price, type, size)
    values 
        ('Mint Tea', '01001', 10.50, 'Loose Leaf Tea', '4 oz'), 
        ('Chamomile Tea', '01002', 10.00, 'Loose Leaf Tea', '4 oz'), 
        ('Earl Grey Tea', '01003', 5.25, 'Loose Leaf Tea', '2 oz'), 
        ('Tea Sampler Kit', '02001', 3.00, 'Tea Kit', 'Pack of 5'), 
        ('Measuring Spoon', '03001', 1.50, 'Accessories', 'Teaspoon'), 
        ('Ginger Honey Tea', '01004', 8.00, 'Loose Leaf Tea', '4 oz'), 
        ('Enthusiast Tea Set', '02002', 100.00, 'Tea Kit', 'Set of 5 Teas'),
        ('Insulated Mug', '04001', 24.99, 'Mugs', 'One piece'),
        ('Mug Warmer', '03002', 14.99, 'Accessories', 'One piece'),
        ('Gift Card', '05001', 10.00, 'Gifts', 'Card with sleeve');

--Script Two:
update products 
    set type = 'Loose Leaf Tea Tin' where type = 'Loose Leaf Tea';
update products
    set price = 9.99 where sku = '01003';
update products
    set price = 9.99 where sku = '01002';
update products
    set price = 4.99 where sku = '02001';
update products
    set size = 'Pack of 5 teabags' where sku = '02001';
update products
    set price = 99.99 where sku = '02002';
update products
    set size = 'Set of 12 loose leaf tea tins' where sku = '02002';
update products
    set price = 9.99 where name = 'Ginger Honey Tea';
update products
    set price = 1.99 where sku = '03001';
update products
    set size = '4 oz' where sku = '01003';

--Script Three:
select * from products;
select * from products order by price;
select * from products order by name desc;
select * from products where price > 10.00;
select count(*) from products;
select count(*) from products where name like '%Tea%';

--Script Four:
delete from products where sku = '05001';
alter table products drop column size;
delete from products where price < 2.00;