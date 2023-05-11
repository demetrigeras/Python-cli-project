TRUNCATE TABLE CONTACTS

ALTER SEQUENCE contacts_id_seq RESTART WITH 1;

INSERT INTO contacts(name, email, phone_number) VALUES ('Conzer Digimon', 'Conxer@digi.com', 1715345678);
INSERT INTO contacts(name, email, phone_number) VALUES ('Demetri Geras',   'Demetri@gmail.com', 1965234567);
INSERT INTO contacts(name, email, phone_number) VALUES ('Justin theflash',  'Justin@flash.com', 1924324567);
INSERT INTO contacts(name, email, phone_number) VALUES ('Pearse Man',  'pearse@man.com', 1899345677);