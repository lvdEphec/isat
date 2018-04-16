DROP TABLE tbCategories2;
CREATE TABLE "DBA"."tbCategories2" (
	"categId" CHAR(1) NOT NULL,
	"categLib" VARCHAR(20) NULL,
	CONSTRAINT "pkCateg" PRIMARY KEY ( "categId" ASC )
);
select * from tbCategories2

DROP TABLE tbAliments2;
CREATE TABLE "DBA"."tbAliments2" (
	"alimId" INTEGER NOT NULL DEFAULT AUTOINCREMENT,
	"alimLib" VARCHAR(25) NULL,
	"alimPrixKg" DECIMAL(4,2) NULL,
	"categId" CHAR(1) NULL,
	CONSTRAINT "pkAlim" PRIMARY KEY ( "alimId" ASC )
);
select * from tbAliments2;


/* NOT NULL, ON UPDATE CASCADE */
ALTER TABLE "DBA"."tbAliments2" ADD CONSTRAINT "fkAliCat2" NOT NULL
FOREIGN KEY ( "categId" ASC ) REFERENCES "DBA"."tbCategories2" ( "categId" ) ON UPDATE CASCADE;
/***/

/* QUE VA-T-IL SE PASSER ? */
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('ananas',2.99,'F');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('orange',1.50,'F');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('pomme',1.79,'F');

/***********************************************/
INSERT INTO "DBA"."tbCategories2" ("categId","categLib") VALUES('E','Epices');
INSERT INTO "DBA"."tbCategories2" ("categId","categLib") VALUES('F','Fruits');
INSERT INTO "DBA"."tbCategories2" ("categId","categLib") VALUES('H','Herbes');
INSERT INTO "DBA"."tbCategories2" ("categId","categLib") VALUES('L','Légumes');
INSERT INTO "DBA"."tbCategories2" ("categId","categLib") VALUES('P','Pokemon');

INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('ananas',2.99,'F');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('orange',1.50,'F');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('pomme',1.79,'F');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('banane',2.31,'F');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('citron',3.70,'F');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('dattes',6.25,'F');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('poire',4.16,'F');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('raisin',2.49,'F');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('noix',7.80,'F');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('prune',4.52,'F');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('carotte',1.05,'L');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('oignon',0.55,'L');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('ail',1.49,'L');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('céleri',1.71,'L');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('patate',1.32,'L');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('navet',0.93,'L');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('potiron',1.14,'L');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('persil',0.21,'H');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('cibloulette',0.19,'H');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('basilic',0.22,'H');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('coriandre',0.17,'H');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('poivre',0.19,'E');
INSERT INTO "DBA"."tbAliments2" ("alimLib","alimPrixKg","categId") VALUES('girofle',0.21,'E');
/*********************************************/
SELECT * from tbCategories2;
SELECT * from tbAliments2;
/*********************************************/
/* QUE VA-T-IL SE PASSER ? */
DELETE from tbCategories2 where categID = 'E'
//* QUE VA-T-IL SE PASSER ? */
DELETE from tbCategories2 where categID = 'P'
SELECT * from tbAliments2 where categID = 'P'
/*********************************************/
/* QUE VA-T-IL SE PASSER ? */
UPDATE tbCategories2 set categID = 'Z' where categID = 'F';
SELECT * from tbCategories2;
/* QUE VA-T-IL SE PASSER ? */
SELECT * from tbAliments2;
/* QUE VA-T-IL SE PASSER ? */
UPDATE tbCategories2 set categID = NULL where categID = 'Z';
/* QUE VA-T-IL SE PASSER ? */
UPDATE tbAliments2 set categID = 'Y' where categID = 'Z';
/*********************************************/
ALTER TABLE "DBA"."tbAliments2" DROP CONSTRAINT "fkAliCat2";
/* NOT NULL, ON UPDATE RESTRICT */
ALTER TABLE "DBA"."tbAliments2" ADD CONSTRAINT "fkAliCat2" NOT NULL
FOREIGN KEY ( "categId" ASC ) REFERENCES "DBA"."tbCategories2" ( "categId" ) ON UPDATE RESTRICT;
SELECT * from tbAliments2;
/* QUE VA-T-IL SE PASSER ? */
UPDATE tbCategories2 set categID = 'F' where categID = 'Z';
SELECT * from tbAliments2;
/* QUE VA-T-IL SE PASSER ? */
UPDATE tbAliments2 set categID = 'Y' where categID = 'Z';
/* QUE VA-T-IL SE PASSER ? */
UPDATE tbAliments2 set categID = NULL where categID = 'Z';
/*********************************************/
ALTER TABLE "DBA"."tbAliments2" DROP CONSTRAINT "fkAliCat2";
/*(NULL), ON UPDATE RESTRICT */
ALTER TABLE "DBA"."tbAliments2" ADD CONSTRAINT "fkAliCat2" FOREIGN KEY ( "categId" ASC )
REFERENCES "DBA"."tbCategories2" ( "categId" ) ON UPDATE RESTRICT;
/***/
SELECT * from tbAliments2;
/* QUE VA-T-IL SE PASSER ? */
UPDATE tbAliments2 set categID = 'Y' where categID = 'Z';
/* QUE VA-T-IL SE PASSER ? */
UPDATE tbAliments2 set categID = NULL where categID = 'Z';
UPDATE tbAliments2 set categID = 'Z' where categID IS NULL;
/* QUE VA-T-IL SE PASSER ? */
DELETE from tbCategories2;
/***  ajouter contrainte incorrecte? existence?  *************************/
ALTER TABLE "DBA"."tbAliments2" DROP CONSTRAINT "fkAliCat2";
ALTER TABLE "DBA"."tbAliments2" ADD CONSTRAINT "incorrect" NOT NULL FOREIGN KEY ( "categId" ASC )
REFERENCES "DBA"."tbCategories2" ( "categLib" ) ON UPDATE RESTRICT;
/*********************************************/
ALTER TABLE "DBA"."tbAliments2" DROP CONSTRAINT "fkAliCat2";
/* NOT NULL ON UPDATE CASCADE ON DELETE CASCADE */
ALTER TABLE "DBA"."tbAliments2" ADD CONSTRAINT "fkAliCat2" NOT NULL FOREIGN KEY ( "categId" ASC )
REFERENCES "DBA"."tbCategories2" ( "categId" ) ON UPDATE CASCADE ON DELETE CASCADE;
/***/
SELECT * from tbAliments2;
/* QUE VA-T-IL SE PASSER ? */
DELETE FROM tbCategories2 where categID = 'E';
SELECT * from tbAliments2;
SELECT * from tbCategories2;
/* QUE VA-T-IL SE PASSER ? */
DELETE from tbCategories2;
SELECT * from tbAliments2;
/* QUE VA-T-IL SE PASSER ? */
ALTER TABLE "DBA"."tbAliments2" ADD CONSTRAINT "incorrect" NOT NULL
FOREIGN KEY ( "categId" ASC ) REFERENCES "DBA"."tbCategories2" ( "categLib" ) ON UPDATE RESTRICT;


/************* ET MAINTENANT??? **************************/

INSERT INTO "DBA"."tbCategories2" ("categId","categLib") VALUES('E','Epices');
INSERT INTO "DBA"."tbCategories2" ("categId","categLib") VALUES('H','Herbes');

INSERT INTO "DBA"."tbAliments2" ("alimId","alimLib","alimPrixKg","categId") VALUES(18,'persil',0.21,'H');
INSERT INTO "DBA"."tbAliments2" ("alimId","alimLib","alimPrixKg","categId") VALUES(19,'cibloulette',0.19,'H');
INSERT INTO "DBA"."tbAliments2" ("alimId","alimLib","alimPrixKg","categId") VALUES(20,'basilic',0.22,'H');
INSERT INTO "DBA"."tbAliments2" ("alimId","alimLib","alimPrixKg","categId") VALUES(21,'coriandre',0.17,'H');
INSERT INTO "DBA"."tbAliments2" ("alimId","alimLib","alimPrixKg","categId") VALUES(22,'poivre',0.19,'E');
INSERT INTO "DBA"."tbAliments2" ("alimId","alimLib","alimPrixKg","categId") VALUES(23,'girofle',0.21,'E');

ALTER TABLE "DBA"."tbAliments2" DROP CONSTRAINT "fkAliCat2";
ALTER TABLE "DBA"."tbAliments2" ADD CONSTRAINT "fkAliCat2" NOT NULL FOREIGN KEY ( "categId" ASC )
REFERENCES "DBA"."tbCategories2" ( "categId" ) ON UPDATE RESTRICT ON DELETE CASCADE; /* particulier! */

SELECT * from tbCategories2;
SELECT * from tbAliments2;

/* QUE VA-T-IL SE PASSER ? */
update tbAliments2 set categId = 'E' where categId = 'H';
SELECT * from tbAliments2;
SELECT * from tbCategories2;

/* QUE VA-T-IL SE PASSER ? */
INSERT INTO "DBA"."tbCategories2" ("categId","categLib") VALUES('T','Test');
SELECT * from tbAliments2;
SELECT * from tbCategories2;

/* QUE VA-T-IL SE PASSER ? */
delete from tbCategories2 where categId = 'E'
SELECT * from tbAliments2;
SELECT * from tbCategories2;


/********************************************/
















/***  Pour le fun *************************/
/*  Foreign key doit toujours faire référence à primary key ou unique */
/*  PK et unique ne peuvent pas être null */
/* donc il est impossible qu'une FK pointe vers null */
/*  Supprimer une table peut supprimer les contraintes qui y font référence */
DROP TABLE tbCategories2;


CREATE TABLE "DBA"."tbCategories2" (
	"categId" CHAR(1) NOT NULL,
	"categLib" VARCHAR(20) NULL,
    "testId" CHAR(1) NOT NULL,
	CONSTRAINT "pkCateg" PRIMARY KEY ( "categId" ASC )
);

SELECT * from tbAliments2;
SELECT * from tbCategories2;

INSERT INTO "DBA"."tbCategories2" ("categId","categLib","testId") VALUES('E','Epices','E');
INSERT INTO "DBA"."tbCategories2" ("categId","categLib","testId") VALUES('F','Fruits','F');
INSERT INTO "DBA"."tbCategories2" ("categId","categLib","testId") VALUES('H','Herbes','H');
INSERT INTO "DBA"."tbCategories2" ("categId","categLib","testId") VALUES('L','Légumes','L');

ALTER TABLE "DBA"."tbCategories2" ADD UNIQUE (testId);




