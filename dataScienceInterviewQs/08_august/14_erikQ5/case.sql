SELECT employee_id,
(sum(CASE WHEN action="answer" THEN 1.0
         ELSE 0 
		 END))
		 /
		 /*
sum(CASE WHEN action="skip" THEN 1
         WHEN action="view" THEN 1
         ELSE 0
         END) as "Not_Answered",
		 */
count(question_id)
FROM survey
group by 1

