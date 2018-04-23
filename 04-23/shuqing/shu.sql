drop table if exists shuqing;
create table shuqing
(
	id mediumint unsigned not null auto_increment comment 'id',
	title varchar(150) not null comment '标题',
	url varchar(250) not null comment '链接',
	addtime varchar(150) not null comment '添加时间',
	cate varchar(150) not null comment '分类',
	content longtext  comment '内容',
	primary key(id)
)engine = innodb default charset=utf8 comment "抒情美文";
