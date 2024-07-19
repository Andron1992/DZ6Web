SELECT g.group_name, AVG(gr.grade) as avg_grade
FROM grades gr
JOIN students s ON gr.student_id = s.student_id
JOIN groups g ON s.group_id = g.group_id
WHERE gr.subject_id = your_subject_id
GROUP BY g.group_name;
