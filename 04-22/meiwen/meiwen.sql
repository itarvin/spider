drop table if exists meiwen;
create table meiwen
(
	id mediumint unsigned not null auto_increment comment 'id',
	title varchar(150) not null comment '标题',
	url varchar(250) not null comment '链接',
	addtime varchar(150) not null comment '添加时间',
	hits varchar(150) not null comment '查看次数',
	author varchar(150) not null comment '作者',
	content longtext  comment '内容',
	primary key(id)
)engine = innodb default charset=utf8 comment "美文";
