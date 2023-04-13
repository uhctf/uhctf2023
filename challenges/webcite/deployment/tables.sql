drop table if exists `users`;
create table `users` (
    id int not null auto_increment,
    username text not null,
    password text not null,
    primary key (id)
);
insert into `users` (username, password) values
    ("admin","password"),
    ("Alice","this is my password"),
    ("Job","12345678");

drop table if exists `papers`;
create table `papers` (
    id varchar(20) not null,
    title text not null,
    doi text,
    primary key (id)
);
insert into `papers` (id, title, doi) values
    ("0001.0001","Paper Template", "0001.0001"),
    ("0506.0x4254","Icelandic Principles of Networking", "0506.0x4254"),
    ("UHCTF{dont-forget-to-prepare-your-statements-73716c69}","Extraction by Injection", "0707.01298"),
    ("72656468657272696e67","Vexillology", "72656468657272696e67");

drop table if exists `authors`;
create table `authors` (
    id int not null auto_increment,
    name text not null,
    primary key (id)
);
insert into `authors` (id, name) values
    (10, "John Claxon"),
    (11, "Seña Lizar");

drop table if exists `wrote_paper`;
create table `wrote_paper` (
    paper varchar(20) not null,
    author int not null,
    primary key (paper, author),
    foreign key (paper) references papers(id),
    foreign key (author) references authors(id)
);
insert into `wrote_paper` (paper, author) values
    ("72656468657272696e67", 10),
    ("0506.0x4254", 11);