CREATE TABLE RelativeDetails (
	id INTEGER PRIMARY KEY ,
	first_name TEXT NOT NULL,
	middle_name TEXT ,
	last_name TEXT NOT NULL,
	address	 TEXT NOT NULL,
	nickname TEXT,
        gender INTEGER NOT NULL
);

CREATE TABLE ParentChildRelationship(
       parentId INTEGER NOT NULL,
       childId  INTEGER NOT NULL,
       FOREIGN KEY(parentId) REFERENCES RelativeDetails(Id),
       FOREIGN KEY(childId)  REFERENCES RelativeDetails(Id)
);

CREATE TABLE SiblingRelationship(
       sibling1 INTEGER NOT NULL,
       sibling2 INTEGER NOT NULL,
       FOREIGN KEY(sibling1) REFERENCES RelativeDetails(Id),
       FOREIGN KEY(sibling2)  REFERENCES RelativeDetails(Id)
);

CREATE TABLE NeighborRelationship(
       neighbor1 INTEGER NOT NULL,
       neighbor2 INTEGER NOT NULL,
       FOREIGN KEY(neighbor1) REFERENCES RelativeDetails(Id),
       FOREIGN KEY(neighbor2)  REFERENCES RelativeDetails(Id)
);
