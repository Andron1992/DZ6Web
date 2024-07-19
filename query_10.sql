SELECT DISTINCT subject_name,
FROM grades gr
JOIN subjects s ON gr.subject_id = s.subject_id
WHERE gr.student_id = student_id AND s.teacher_id = teacher_id;