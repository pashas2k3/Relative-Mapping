
-- Relative Details insertion
INSERT INTO RelativeDetails (first_name, middle_name, last_name, address, nickname, gender) VALUES
('Rima', NULL, 'Kaul', 'Pune', NULL, 0);
('Vikram', NULL, 'Gigoo', 'Boston', NULL, 1),
('Angela', NULL, 'Kaul', 'Boston', NULL, 0),
('Virendar', NULL, 'Gigoo', 'New Delhi', NULL, 1);

-- Relative Mapping information

INSERT INTO ParentChildRelationship(parentId, childId) VALUES
((SELECT id FROM RelativeDetails WHERE first_name = 'Virendar' AND last_name = 'Gigoo'),
(SELECT id FROM RelativeDetails WHERE first_name = 'Vikram' AND last_name = 'Gigoo')),
((SELECT id FROM RelativeDetails WHERE first_name = 'Rima' AND last_name = 'Kaul'),
(SELECT id FROM RelativeDetails WHERE first_name = 'Angela' AND last_name = 'Kaul'))
;

-- Find Relationships
SELECT parent.first_name, child.first_name FROM RelativeDetails parent INNER JOIN ParentChildRelationship ON parent.id = parentId  INNER JOIN RelativeDetails child ON child.id = childId WHERE child.first_name = 'Vikram';
