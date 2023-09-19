create database email_sender;
\c email_sender
     
create table emails (
    id serial not null,
    data timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    assunto varchar(100) not null,
    mensagem varchar(250) not null
);

ALTER TABLE email_sender OWNER TO postgres;

GRANT ALL PRIVILEGES ON DATABASE postgres TO postgres;