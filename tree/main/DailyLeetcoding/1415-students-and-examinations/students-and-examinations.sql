SELECT Students.student_id, Students.student_name, Subjects.subject_name, COUNT(Examinations.subject_name) AS attended_exams
FROM Students
CROSS JOIN Subjects
LEFT JOIN Examinations
    ON Examinations.student_id = Students.student_id
    AND Examinations.subject_name = Subjects.subject_name
GROUP BY Students.student_id, Students.student_name, Subjects.subject_name
ORDER BY Students.student_id, Subjects.subject_name