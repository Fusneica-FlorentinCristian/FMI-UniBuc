
--creare tabele--
CREATE TABLE EDITURI 
(cod_editura VARCHAR2(15) CONSTRAINT pkk_ed PRIMARY KEY,
nume_editura VARCHAR(25) NOT NULL,
adresa_editura VARCHAR2(40),
telefon_editura NUMBER(10));
ALTER TABLE EDITURI
ADD CONSTRAINT ED_NUME_NN1 CHECK("NUME_EDITURA" IS NOT NULL);

CREATE TABLE CARTI
(cod_carte VARCHAR2(20) primary key,
denumire VARCHAR2(50) NOT NULL,
nr_exemplare NUMBER(2),
pret NUMBER(2),
cod_editura REFERENCES edituri_1(cod_editura),
an_aparitie number(4));
ALTER TABLE CARTI_1
ADD CONSTRAINT CARTE_NUME_N1 CHECK("DENUMIRE_CARTE" IS NOT NULL);

CREATE TABLE FISE_LECTURA1
(cod_fisa VARCHAR(25) PRIMARY KEY,
cod_carte REFERENCES carti_1(cod_carte),
cod_cititor references clienti(cod_cititor),
data_imprumut DATE, 
data_returnare DATE DEFAULT SYSDATE);

CREATE TABLE AUTORI
(cod_autor NUMBER(13) PRIMARY KEY,
nume_autor VARCHAR2(20) ,
prenume_autor VARCHAR2(20));

ALTER TABLE AUTORI_1
ADD CONSTRAINT AUT_NUME_N1 CHECK("NUME_AUTOR" IS NOT NULL);

CREATE TABLE SCRISE
(cod_autor REFERENCES autori(cod_autor),
cod_carte REFERENCES carti(cod_carte));

CREATE TABLE LOCATII_BIBLIOTECA
(id_locatie NUMBER(7) PRIMARY KEY,
adresa_locatie VARCHAR2(50) ,
cod_postal NUMBER(10),
cod_carte REFERENCES carti(cod_carte));

CREATE TABLE ANGAJATI_BIBLIOTECA
(cod_angajat NUMBER(13) PRIMARY KEY,
nume_angajat VARCHAR2(20) ,
prenume_angajat VARCHAR2(20),
adresa_angajat VARCHAR2(50),
telefon_angajat NUMBER(10),
mail VARCHAR2(20),
id_locatie REFERENCES locatii_biblioteca(id_locatie));

CREATE TABLE CLIENTI
(cod_cititor NUMBER(13) PRIMARY KEY,
nume_cititor VARCHAR2(50) ,
prenume_cititor VARCHAR2(50),
email VARCHAR2(25),
adresa_cititor VARCHAR2(50),
telefon VARCHAR2(10),
cod_fisa varchar(20) );
ALTER TABLE CLIENTI
ADD (COD_FISA VARCHAR2(25)REFERENCES FISE_LECTURA1(COD_FISA));

ALTER TABLE CLIENTI
ADD CONSTRAINT CIT_NUME_N1 CHECK("NUME_CITITOR" IS NOT NULL);

--inserturi--
INSERT INTO AUTORI VALUES(25678543,'Verne','Jules');
INSERT INTO AUTORI VALUES(34747584,'Eliade','Mircea');
INSERT INTO AUTORI VALUES(27583623,'Eminescu','Mihai');
INSERT INTO AUTORI VALUES(37353327,'Cartarescu','Mircea');
INSERT INTO AUTORI VALUES(37387637,'Creanga','Ion');
INSERT INTO AUTORI VALUES(35363627,'Nabokov','Vladimir');
INSERT INTO AUTORI VALUES(37459027,'Proust','Marcel');
INSERT INTO AUTORI VALUES(30593827,'Joyce','James');
INSERT INTO AUTORI VALUES(30483927,'Woolf','Virginia');
INSERT INTO AUTORI VALUES(36083627,'Marquez','Gabriel');
INSERT INTO AUTORI VALUES(26483627,'Tolstoi','Lev');
INSERT INTO AUTORI VALUES(22483627,'Twain','Mark');
INSERT INTO AUTORI VALUES(32486627,'Eliot','George');
INSERT INTO AUTORI VALUES(32486600,'Andruh','Marius');
INSERT INTO AUTORI VALUES(32486601,'Costeniuc','Iuliana');


INSERT INTO CLIENTI VALUES(2671604578392,'Dinu','Cristina','cristinadinu@gmail.com','Sos. Pantelimon,nr 286,bl 40,ap 2,Bucuresti',0732013081,202);
INSERT INTO CLIENTI VALUES(2681664578452,'Dumitru','Cristian','cristiandumitru@gmail.com','Sos. Pantelimon,nr 265,bl 6,ap 20,Bucuresti',0735613081,203);
INSERT INTO CLIENTI VALUES(2651404075392,'Popescu','Daria','popdaria@gmail.com','Sos. Cernica,nr 12,Bucuresti',0732078061,204);

ALTER TABLE CARTI ADD TIP VARCHAR(15);

INSERT INTO EDITURI VALUES('101','Accent','Str. Dimitrie Cantemir,nr. 20,Bucuresti',021745634);
INSERT INTO EDITURI VALUES('102','ALL','Str. Aleea Lotrului,nr. 25,Bucuresti',031745658);
INSERT INTO EDITURI VALUES('103','Art','Str. Aleea Alexandru,nr. 80,Bucuresti',021485694);
INSERT INTO EDITURI VALUES('104','Egmont','Str. Aleea Pajurei,nr. 33,Bucuresti',021215634);
INSERT INTO EDITURI VALUES('105','IDEA','Str. Aleea Teisani,nr. 10,Bucuresti',021747024);
INSERT INTO EDITURI VALUES('106','Natiunea','Str.Aleea Faurei,nr. 30,Bucuresti',021745710);
INSERT INTO EDITURI VALUES('107','Adevarul Holding','Str. Priporului,nr. 108,Bucuresti',021745300);
INSERT INTO EDITURI VALUES('108','Salco','Str.Matelotilor,nr. 70,Bucuresti',021745610);
INSERT INTO EDITURI VALUES('109','Unirea','Str. Somesul Rece,nr. 100,Bucuresti',021740048);
INSERT INTO EDITURI VALUES('110','Valdo','Str. Privighetorilor,nr. 29,Bucuresti',021785004);

INSERT INTO CARTI VALUES('ISBN 120-4590','Ocolul Pamantului in 80 de zile',3,23,107,1873,'FICTIUNE');
INSERT INTO CARTI VALUES('ISBN 103-4570','Copiii Capitanului Grant',5,28,107,186,'FICTIUNE');
INSERT INTO CARTI VALUES('ISBN 193-4767','Amintiri din copilarie',2,30,109,1959,'BIOGRAFIE');
INSERT INTO CARTI VALUES('ISBN 193-0567','Maitreyi',5,26,110,1933,'FICTIUNE');
INSERT INTO CARTI VALUES('ISBN 123-9577','Zece Negri Mititei',3,25,105,1939,'POLITIST');
INSERT INTO CARTI VALUES('ISBN 129-4568','Crima din Orient Express',5,24,105,1934,'POLITIST');
INSERT INTO CARTI VALUES('ISBN 125-9067','Orbitor',2,30,102,2007,'ISTORIC');
INSERT INTO CARTI VALUES('ISBN 123-4576','Nostalgia',6,36,103,1989,'FICTIUNE');
INSERT INTO CARTI VALUES('ISBN 120-4997','Lolita',4,21,108,1955,'FICTIUNE');
INSERT INTO CARTI VALUES('ISBN 123-4550','Razboi si pace',5,36,104,1867,'ISTORIC');
INSERT INTO CARTI VALUES('ISBN 122-4695','Invierea',5,31,109,1899,'FICTIUNE');
INSERT INTO CARTI VALUES('ISBN 102-4986','Sanctuar',5,34,107,1931,'POLITIST');
INSERT INTO CARTI VALUES('ISBN 123-4570','Middlemarch',5,36,109,1871,'ISTORIC');
INSERT INTO CARTI VALUES('ISBN 123-4500','Manual chimie clasa a8-a',2,40,107,2011,'MANUAL');

INSERT INTO LOCATII_BIBLIOTECA VALUES(500,'Str. Pajurii,nr. 280,Bucuresti',656325);
INSERT INTO LOCATII_BIBLIOTECA VALUES(502,'Str. Uverturii,nr. 27,Bucuresti',656236);
INSERT INTO LOCATII_BIBLIOTECA VALUES(504,'Str. Vatra Dornei,nr. 26,Bucuresti',656200);

INSERT INTO ANGAJATI_BIBLIOTECA VALUES(002,'Pop','Andreea','Str. Aleea Stanila 23,Bucuresti',0736013028,'poopand@gmail.coom',500,'ADMINISTRATOR',2400,to_date('08-09-2016','dd-mm-yyyy')); 
INSERT INTO ANGAJATI_BIBLIOTECA VALUES(003,'Mihai','Andrei','Blv.Iuliu Maniu,nr. 23,bl.41C,ap.4',0722623902,'mihaindrei@gmail.com',502,'AJUTOR BIBLIOTECAR',2000,to_date('01-01-2017','dd-mm-yyyy'));
INSERT INTO ANGAJATI_BIBLIOTECA VALUES(004,'Chiritescu','Silviu','Str. Mihai Viteazul,nr. 2A,Bucuresti',0766256202,'silviuch@gmail.com',504,'ADMINISTRATOR',3400,to_date('04-05-2015','dd-mm-yyyy'));
INSERT INTO ANGAJATI_BIBLIOTECA VALUES(005,'Agapie','Miruna','Str. Mihail Mirinescu nr.26, Bucuresti',0733612025,'agapiemir@gmail.com',500,'BIBLIOTECARA',1500,to_date('08-11-2018','dd-mm-yyyy')); 
INSERT INTO ANGAJATI_BIBLIOTECA VALUES(006,'Apostol','Miruna','Str. Mihai Viteazul nr.6, Bucuresti',07336574025,'apostolmir@gmail.com',502,'BIBLIOTECARA',1800,to_date('08-01-2018','dd-mm-yyyy'));

alter table angajati_biblioteca add functie varchar(20);
alter table angajati_biblioteca add salariu number(5);
alter table angajati_biblioteca add data_ang date;

INSERT INTO SCRISE VALUES(25678543,'ISBN 120-4590');
INSERT INTO SCRISE VALUES(25678543,'ISBN 123-4567');
INSERT INTO SCRISE VALUES(25678543,'ISBN 103-4570');
INSERT INTO SCRISE VALUES(34747584,'ISBN 193-0567');
INSERT INTO SCRISE VALUES(37353327,'ISBN 125-9067');
INSERT INTO SCRISE VALUES(37353327,'ISBN 123-4576');
INSERT INTO SCRISE VALUES(32483629,'ISBN 183-4599');
INSERT INTO SCRISE VALUES(32483629,'ISBN 120-4599');
INSERT INTO SCRISE VALUES(35363627,'ISBN 120-4997');
INSERT INTO SCRISE VALUES(35363627,'ISBN 123-4907');
INSERT INTO SCRISE VALUES(26483627,'ISBN 123-4550');
INSERT INTO SCRISE VALUES(26483627,'ISBN 122-4695');
INSERT INTO SCRISE VALUES(36083627,'ISBN 185-4558');
INSERT INTO SCRISE VALUES(34483627,'ISBN 102-4986');
INSERT INTO SCRISE VALUES(37387637,'ISBN 193-4767');
INSERT INTO SCRISE VALUES(37387637,'ISBN 183-4557');
INSERT INTO SCRISE VALUES(27583623,'ISBN 126-4559');
INSERT INTO SCRISE VALUES(32483657,'ISBN 123-4907');
INSERT INTO SCRISE VALUES(32183629,'ISBN 123-7959');
INSERT INTO SCRISE VALUES(36483627,'ISBN 196-4789');
INSERT INTO SCRISE VALUES(32883627,'ISBN 120-4570');
INSERT INTO SCRISE VALUES(32483624,'ISBN 193-4557');
INSERT INTO SCRISE VALUES(32486600,'ISBN 123-4500');
INSERT INTO SCRISE VALUES(32486601,'ISBN 123-4500');

INSERT INTO FISE_LECTURA1 VALUES('200','ISBN 196-4789',2671604578392,TO_DATE('12-09-2020','DD-MM-YYYY'),TO_DATE('10-10-2020','DD-MM-YYYY'));
INSERT INTO FISE_LECTURA1 VALUES('201','ISBN 193-4557',2671604578392,TO_DATE('12-02-2021','DD-MM-YYYY'),TO_DATE('18-02-2021','DD-MM-YYYY'));
INSERT INTO FISE_LECTURA1 VALUES('202','ISBN 122-4695',2651404075392,TO_DATE('12-03-2021','DD-MM-YYYY'),TO_DATE('18-03-2021','DD-MM-YYYY'));
INSERT INTO FISE_LECTURA1 VALUES('203','ISBN 123-4500',2681664578452,TO_DATE('12-04-2021','DD-MM-YYYY'),TO_DATE('18-04-2021','DD-MM-YYYY'));
INSERT INTO FISE_LECTURA1 VALUES('204','ISBN 102-4986',2651404075392,TO_DATE('12-05-2021','DD-MM-YYYY'),TO_DATE('18-05-2021','DD-MM-YYYY'));

--procedura de modificare a pretului--

set serveroutput on
create or replace procedure modif_pr (v_cod in carti.cod_carte%type,proc in number)
as
v_pret carti.pret%type;
v_denumire carti.denumire%type;
begin
select pret,denumire into v_pret,v_denumire from carti
where cod_carte=v_cod;
dbms_output.put_line ('Pret initial: '||v_pret);
dbms_output.put_line ('Denumire carte: '||v_denumire);
update carti
set pret=pret*(1+proc/100)
where cod_carte=v_cod;
select pret into v_pret from carti where cod_carte=v_cod;
dbms_output.put_line ('Noul pret : '||v_pret|| ' lei ');
end;
/

execute modif_pr('ISBN 120-4590',5);

--functie cu 3 tabele--
set serveroutput on
create or replace function val_tot(nrc in varchar) return number
as
ex exception;
nre number;
v_codc scrise.cod_carte%type;
v_coda scrise.cod_autor%type;
v_den carti.denumire%type;
v_aut autori.nume_autor%type;
v_autp autori.prenume_autor%type;
v_tip carti.tip%type;
begin
select s.cod_carte,c.denumire,s.cod_autor,a.nume_autor,a.prenume_autor,c.tip,sum(c.pret*c.nr_exemplare)  into v_codc,v_den,v_coda,v_aut,v_autp,v_tip,nre from carti c,autori a, scrise s where
s.cod_carte=c.cod_carte and s.cod_autor=a.cod_autor and c.cod_carte=nrc
group by s.cod_carte,c.denumire,s.cod_autor,a.nume_autor,a.prenume_autor,c.tip ;
dbms_output.put_line('Carte:'||v_den||';valoare totala'||nre||';nume autor:'||v_aut||';prenume autor:'||v_autp);
return nre;
if(nre=0)
then raise ex;
end if;
exception
when ex then dbms_output.put_line ('Nu sunt exemplare');
end;
/
DECLARE
var NUMBER;
BEGIN
var:=val_tot('ISBN 120-4590');
IF var>0 THEN
DBMS_OUTPUT.PUT_LINE(var);
ELSIF var=0 THEN
DBMS_OUTPUT.PUT_LINE('Nu exista exemplare!');
ELSE DBMS_OUTPUT.PUT_LINE('Eroare! - '||SQLERRM);
END IF;
END;
/
update carti set nr_exemplare=0 where cod_carte='ISBN 120-4590';

--colectie index by table--
set serveroutput on
create or replace procedure nr_ed 
as
TYPE ed_tab IS TABLE OF edituri%ROWTYPE INDEX BY
PLS_INTEGER;
v_ed ed_tab;
BEGIN
DBMS_OUTPUT.PUT_LINE('Edituri:');
FOR i IN 101..110 LOOP
SELECT * INTO v_ed(i) FROM edituri WHERE
cod_editura=i;
END LOOP;
FOR i IN v_ed.FIRST..v_ed.LAST LOOP
DBMS_OUTPUT.PUT_LINE(v_ed(i).nume_editura);
END LOOP;
DBMS_OUTPUT.PUT_LINE('Total edituri: '||v_ed.COUNT);
END;
/
execute nr_ed;

--cursor implicit--

SET SERVEROUTPUT ON
CREATE OR REPLACE PROCEDURE MARIRE_SALARIU(MAR IN NUMBER, ID_ANG IN NUMBER)
AS
EXC EXCEPTION;
BEGIN
UPDATE ANGAJATI_BIBLIOTECA
SET SALARIU= SALARIU*(1+mar/100)
WHERE COD_ANGAJAT= (select cod_angajat from angajati_biblioteca where  extract (year from data_ang)=2017 ) and COD_ANGAJAT= ID_ANG;
IF(SQL%ROWCOUNT=0)
THEN RAISE EXC;
ELSE
DBMS_OUTPUT.PUT_LINE('S-a modificat SALARIUL.');
END IF;
EXCEPTION WHEN EXC
THEN DBMS_OUTPUT.PUT_LINE('Nu exista angajatul/Nu s-a angajat in anul 2018');
when others then dbms_output.put_line(sqlerrm);
end MARIRE_SALARIU;

/

execute MARIRE_SALARIU(10,003);

--procedura cu cursor--
CREATE OR REPLACE PROCEDURE CARTI_IST
AS
cursor c is select cod_carte,denumire from carti
where tip='ISTORIC';
v_cod carti.cod_carte%type;
v_den carti.denumire%type;
begin
open c;
loop
fetch c into v_cod,v_den;
exit when c%notfound;
dbms_output.put_line('Denumire: ' ||v_den||';Cod: '||v_cod);
end loop;
close c;
end;
/
execute carti_ist;

--trigger la nivel de comanda--

set serveroutput on
create or replace trigger trigger_nr_ex
before update of nr_exemplare or insert on carti
for each row
declare
nr_max carti.nr_exemplare%type;
begin
select nr_exemplare into nr_max
from carti
where cod_carte=:new.cod_carte;
if(:new.nr_exemplare<nr_max) then dbms_output.put_line(:new.nr_exemplare);
else raise_application_error(-20001,'Numarul de exemplare depaseste numarul maxim admis!!');
end if;
end;
/
--trigger stergere--
set serveroutput on
create or replace trigger trigger_stergere
before delete on carti
begin
raise_application_error(-20000,'Nu puteti sterge inregistrari din aceasta tabela');
end;
/
delete from carti
where cod_carte='ISBN 123-4500';

--trigger la nivel de linie--

create or replace trigger trigger_angajati
BEFORE DELETE OR INSERT OR UPDATE ON angajati_biblioteca
FOR EACH ROW
 WHEN (NEW.functie <> 'BIBILIOTECARA') 
DECLARE
diferenta  NUMBER;
BEGIN
diferenta  := :NEW.salariu  - :OLD.salariu;
DBMS_OUTPUT.PUT(:NEW.nume_angajat || ': ');
 DBMS_OUTPUT.PUT('Salariul vechi = ' || :OLD.salariu || ', ');
 DBMS_OUTPUT.PUT('Salariul nou = ' || :NEW.salariu || ', ');
 DBMS_OUTPUT.PUT_LINE('Diferenta: ' || diferenta);
END;
/
update  angajati_biblioteca
set salariu=3800
where functie='BIBLIOTECARA';

--procedura 5 tabele--

set serveroutput on
create or replace procedure modif_pr (v_cod in carti_biblioteca.cod_carte%type,proc in number)
as
v_pret carti_biblioteca.pret%type;
begin
select pret into v_pret from carti_biblioteca
where cod_carte=v_cod;
dbms_output.put_line ('Cartea are pretul: '||v_pret);
update carti_biblioteca
set pret=pret*(1+proc/100)
where cod_carte=v_cod;
select pret into v_pret from carti_biblioteca where cod_carte=v_cod;
dbms_output.put_line ('Noul pret : '||v_pret|| 'lei ');
end;
/
C.DENUMIRE_CARTE,A.NUME_AUTOR,A.PRENUME_AUTOR,C.COD_CARTE,COUNT(C.NR_EXEMPLARE)
FROM CARTI_BIBLIOTECA C,AUTORI A,SCRISE S
WHERE C.COD_CARTE=S.COD_CARTE AND A.COD_AUTOR=S.COD_AUTOR
GROUP BY  C.DENUMIRE_CARTE,A.NUME_AUTOR,A.PRENUME_AUTOR,C.COD_CARTE;

execute modif_pr('ISBN 123-4567',10);

--triger LDD--


CREATE TABLE useri
 (username VARCHAR2(20),
 nume_bd VARCHAR2(50),
 eveniment VARCHAR2(20),
 data DATE);


CREATE OR REPLACE TRIGGER trigger_ldd1
 AFTER CREATE OR DROP OR ALTER ON SCHEMA
BEGIN
 INSERT INTO useri
 VALUES (SYS.LOGIN_USER, SYS.DATABASE_NAME, SYS.SYSEVENT, 
  SYSDATE);
END;
/
insert into useri values ('andrei','carti','eveniment',TO_DATE('12-05-2021','DD-MM-YYYY'));

--procedura--
set serveroutput on
create or replace procedure modif_pret (nrc in varchar,proc in number)
as
ex exception;
nre number;
v_cod carti.cod_carte%type;
v_coda scrise.cod_autor%type;
v_den carti.denumire%type;
v_aut autori.nume_autor%type;
v_autp autori.prenume_autor%type;
v_tip carti.tip%type;
v_ed edituri.nume_editura%type;
begin
select s.cod_carte,c.denumire,s.cod_autor,a.nume_autor,a.prenume_autor,c.tip,e.nume_editura,sum(c.pret*c.nr_exemplare) into v_cod,v_den,v_coda,v_aut,v_autp,v_tip,v_ed,nre from carti c,autori a, scrise s,edituri e where
s.cod_carte=c.cod_carte and s.cod_autor=a.cod_autor and c.cod_editura=e.cod_editura and c.cod_carte=v_cod
group by s.cod_carte,c.denumire,s.cod_autor,a.nume_autor,a.prenume_autor,c.tip,e.nume_editura ;
update carti
set pret=pret*(1+proc/100)
where cod_carte=v_cod and pret*nr_exemplare>150;
dbms_output.put_line('Carte:'||v_den||';valoare totala'||nre||';nume autor:'||v_aut||';prenume autor:'||v_autp||';editura:'||v_ed);
if(nre=0)
then raise ex;
end if;
exception
when ex then dbms_output.put_line ('Nu sunt exemplare');
end;
/

execute modif_pret('ISBN 122-4695',10);

--pachet--

create or replace package carti_up is
procedure ins_carti
(cod_c in carti.cod_carte%type,
nume out carti.denumire%type,
pr out carti.pret%type);

function ex_cod(cod_c carti.cod_carte%type)
return boolean;

function exp (a_nr_exemplare in number) return number;

function pretul(a_pret in number) return number;
function val_tot(nrc in varchar) return number;
PROCEDURE MARIRE_SALARIU(MAR IN NUMBER, ID_ANG IN NUMBER);
procedure inf_clienti;
exc exception;
end;

create or replace package body carti_up is
procedure ins_carti

(cod_c in carti.cod_carte%type,
nume out carti.denumire%type,
pr out carti.pret%type)
is
begin
if ex_cod(cod_c) then
raise exc;
else
insert into carti(cod_carte,denumire,pret) values (cod_c,nume,pr);
end if;
exception
when exc then
dbms_output.put_line('Nu exista cartea');
end;

function ex_cod
(cod_c carti.cod_carte%type)
return boolean
is
v_adv number;
begin
select 1 into v_adv
from carti
where cod_carte=cod_c;
return true;
exception
when no_data_found then
return false;
end;

function exp (a_nr_exemplare in number) return number
is
begin
return(a_nr_exemplare+2);
end;

function pretul(a_pret in number) return number
is
begin
return (a_pret+a_pret*0.05);
end;

function val_tot(nrc in varchar) return number
as
ex exception;
nre number;
v_codc scrise.cod_carte%type;
v_coda scrise.cod_autor%type;
v_den carti.denumire%type;
v_aut autori.nume_autor%type;
v_autp autori.prenume_autor%type;
v_tip carti.tip%type;
begin
select s.cod_carte,c.denumire,s.cod_autor,a.nume_autor,a.prenume_autor,c.tip,sum(c.pret*c.nr_exemplare)  into v_codc,v_den,v_coda,v_aut,v_autp,v_tip,nre from carti c,autori a, scrise s where
s.cod_carte=c.cod_carte and s.cod_autor=a.cod_autor and c.cod_carte=nrc
group by s.cod_carte,c.denumire,s.cod_autor,a.nume_autor,a.prenume_autor,c.tip ;
dbms_output.put_line('Carte:'||v_den||';valoare totala'||nre||';nume autor:'||v_aut||';prenume autor:'||v_autp);
return nre;
if(nre=0)
then raise ex;
end if;
exception
when ex then dbms_output.put_line ('Nu sunt exemplare');
end;

PROCEDURE MARIRE_SALARIU(MAR IN NUMBER, ID_ANG IN NUMBER)
AS
EXC EXCEPTION;
BEGIN
UPDATE ANGAJATI_BIBLIOTECA
SET SALARIU= SALARIU*(1+MAR*SALARIU)
WHERE id_locatie=(select id_locatie from locatii_biblioteca where adresa_locatie='%Bucuresti') and COD_ANGAJAT= ID_ANG;
IF(SQL%ROWCOUNT=0)
THEN RAISE EXC;
ELSE
DBMS_OUTPUT.PUT_LINE('S-a modificat SALARIUL.');
END IF;
EXCEPTION WHEN EXC
THEN DBMS_OUTPUT.PUT_LINE('Nu exista angajatul');
when others then dbms_output.put_line(sqlerrm);
end MARIRE_SALARIU;

procedure INF_CLIENTI as
tel clienti.telefon%type;
nume clienti.nume_cititor%type;
fis clienti.cod_fisa%type;
id_c clienti.cod_cititor%type:=&cod_cititor;
begin
begin
select nume_cititor into nume
from clienti
where cod_cititor=id_c;
dbms_output.put_line ('Cititorul'||id_c);
exception
when no_data_found then
dbms_output.put_line ('Nu sunt informatii');
end;
begin
select cod_fisa into fis
from fise_lectura_1
where cod_cititor=id_c;
dbms_output.put_line ('Cititorul'||nume||'are fisa:'||fis);
end;
exception
when no_data_found then
dbms_output.put_line ('Nu exista informatii despre fisa de lectura a acestui cititor');
end;
end;
/

select cod_carte,denumire,an_aparitie,
carti_up.pretul(pret) PretActualizat
from carti;


select cod_carte,denumire,an_aparitie,
carti_up.exp(nr_exemplare) ExemplareActualizate
from carti;

select email,carti_up.inf_clienti from clienti;

begin
carti_up.INF_CLIENTI;
end;
/

