
a = "CREATE TABLE USER1 ("
b = "id INT auto_increment PRIMARY KEY ,"
c = "name CHAR(10) NOT NULL UNIQUE,"
d = "age TINYINT NOT NULL"
e = ")ENGINE=innodb DEFAULT CHARSET=utf8;  #注意：charset='utf8' 不能写成utf-8"
sql = a + "\n" + b + "\n" + c + "\n" + d

print(sql)