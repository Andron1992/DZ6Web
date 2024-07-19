SELECT t.first_name AS teacher_first_name, s.subject_name
FROM subjects s
JOIN teachers t ON s.teacher_id = t.teacher_id;

