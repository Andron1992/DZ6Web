SELECT AVG(gr.grade) as avg_grade
FROM grades gr
JOIN subjects s ON gr.subject_id = s.subject_id
WHERE s.teacher_id = 2;
