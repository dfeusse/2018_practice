select 
ROUND(100*(
select sum(spend) from
(
select customer_id, count(distinct hotel_id), sum(number_of_nights) as nights, sum(total_spend) as spend
from customers2
where is_member = "TRUE"  AND number_of_nights>0 
group by 1
having count(distinct hotel_id) > 3
)
) )
/ 
sum(total_spend) 
from customers2