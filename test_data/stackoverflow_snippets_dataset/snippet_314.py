# Extracted from https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
data = [
('betty', 1),
('bought', 1),
('a', 1),
('bit', 1),
('of', 1),
('butter', 2),
('but', 1),
('the', 1),
('was', 1),
('bitter', 1)]

sorted(data, key=lambda tup:(-tup[1], tup[0]))

[('butter', 2),
('a', 1),
('betty', 1),
('bit', 1),
('bitter', 1),
('bought', 1),
('but', 1),
('of', 1),
('the', 1),
('was', 1)]

