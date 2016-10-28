
-- Relative Details insertion
INSERT INTO RelativeDetails (first_name, middle_name, last_name, address, nickname, gender) VALUES
('R', NULL, 'K', 'P', NULL, 0);
('V', NULL, 'G', 'B', NULL, 1),
('A', NULL, 'K', 'B', NULL, 0),
('V', NULL, 'G', 'ND', NULL, 1);

-- Relative Mapping information

INSERT INTO ParentChildRelationship(parentId, childId) VALUES
((SELECT id FROM RelativeDetails WHERE first_name = 'V' AND last_name = 'G'),
(SELECT id FROM RelativeDetails WHERE first_name = 'V' AND last_name = 'G')),
((SELECT id FROM RelativeDetails WHERE first_name = 'R' AND last_name = 'K'),
(SELECT id FROM RelativeDetails WHERE first_name = 'A' AND last_name = 'K'))
;

-- Find Relationships
SELECT parent.first_name, child.first_name FROM RelativeDetails parent INNER JOIN ParentChildRelationship ON parent.id = parentId  INNER JOIN RelativeDetails child ON child.id = childId WHERE child.first_name = 'V';
