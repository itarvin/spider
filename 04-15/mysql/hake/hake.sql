create database hake;
use hake;
set names utf8;

drop table if exists hakeinfo;
create table hakeinfo
(
	id mediumint unsigned not null auto_increment comment 'id',
	title varchar(150) not null comment '标题',
	url varchar(250) not null comment '链接',
	times varchar(150) not null comment '添加时间',
	tag  varchar(150) not null comment '分类',
	view varchar(150) not null comment '查看次数',
	content longtext  comment '内容',
	primary key(id)
)engine = innodb default charset = utf8;
