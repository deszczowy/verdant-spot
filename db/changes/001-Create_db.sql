-- Tables

CREATE TABLE "info" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"author"	TEXT,
	"description"	TEXT,
	"border_left"	NUMERIC NOT NULL,
	"border_right"	NUMERIC NOT NULL,
	"border_top"	NUMERIC NOT NULL,
	"border_bottom"	NUMERIC NOT NULL,
	"viewport_left"	NUMERIC,
	"viewport_right"	NUMERIC,
	"viewport_top"	NUMERIC,
	"viewport_bottom"	NUMERIC,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "kind" (
	"id"	INTEGER NOT NULL,
	"label"	TEXT NOT NULL,
	"symbol"	TEXT(2) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "layer" (
	"id"	INTEGER NOT NULL,
	"label"	TEXT NOT NULL,
	"succession"	INTEGER NOT NULL,
	"visible"	BOOLEAN NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "element" (
    "id" INTEGER NOT NULL,
    "caption" TEXT NOT NULL, 
    "layer" INTEGER NOT NULL,
    "kind" INTEGER NOT NULL,
    FOREIGN KEY("layer") REFERENCES "layer"("id"),
    FOREIGN KEY("kind") REFERENCES "kind"("id"),
    PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "point" (
	"id"	INTEGER NOT NULL,
	"element"	INTEGER,
	"x"	NUMERIC NOT NULL,
	"y"	NUMERIC NOT NULL,
	"succession"	INTEGER NOT NULL DEFAULT (1),
	FOREIGN KEY("element") REFERENCES "element"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);

-- Data

INSERT INTO "layer" ("id","label","succession","visible") VALUES (1,'Ground',1,1);
INSERT INTO "layer" ("id","label","succession","visible") VALUES (2,'Buildings',2,1);
INSERT INTO "layer" ("id","label","succession","visible") VALUES (3,'Vegetables',3,1);
INSERT INTO "layer" ("id","label","succession","visible") VALUES (4,'Shrubs',4,1);
INSERT INTO "layer" ("id","label","succession","visible") VALUES (5,'Trees',5,1);

INSERT INTO "kind" ("id","label","symbol") VALUES (1,'Ground','GR');
INSERT INTO "kind" ("id","label","symbol") VALUES (2,'Building','BD');
INSERT INTO "kind" ("id","label","symbol") VALUES (3,'Section','SC');
INSERT INTO "kind" ("id","label","symbol") VALUES (4,'Shrub','SH');
INSERT INTO "kind" ("id","label","symbol") VALUES (5,'Tree','TR');

INSERT INTO "info" ("id","name","author","description","border_left","border_right","border_top","border_bottom","viewport_left","viewport_right","viewport_top","viewport_bottom") VALUES (1,'Untitled','',NULL,0,100,100,0,NULL,NULL,NULL,NULL);
