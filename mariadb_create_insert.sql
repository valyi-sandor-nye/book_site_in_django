DROP TABLE IF EXISTS book_app_book;
DROP TABLE IF EXISTS book_app_author;
CREATE TABLE IF NOT EXISTS book_app_author (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	is_female BOOLEAN NOT NULL
    );
INSERT INTO book_app_author VALUES(5,'Jókai Mór',0);
INSERT INTO book_app_author VALUES(6,'Petőfi Sándor',0);
INSERT INTO book_app_author VALUES(15,'Pelevin Viktor',0);
INSERT INTO book_app_author VALUES(16,'Kaffka Margit',1);
CREATE TABLE IF NOT EXISTS book_app_book (
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    title varchar(100) NOT NULL,
    is_available BOOLEAN NOT NULL,
    author_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES book_app_author (id)
    );
INSERT INTO book_app_book VALUES(6,'Az aranyember',0,5);
INSERT INTO book_app_book VALUES(7,'Az apostol',1,6);
INSERT INTO book_app_book VALUES(9,'A jövő század regénye',0,5);
INSERT INTO book_app_book VALUES(12,'A kőszívű ember fiai',1,5);
INSERT INTO book_app_book VALUES(20,'Színek és évek',1,16);
