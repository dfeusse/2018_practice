/* loyal customer defined in below where statement) */
/* select customer_id, is_member, count(distinct hotel_id), sum(number_of_nights),sum(total_spend) */
select customer_id, hotel_id, sum(number_of_nights) as nights, sum(total_spend)
/* select sum(total_spend) */
from customers2
where is_member = "TRUE"  AND number_of_nights>0 AND count(
group by 1,2
order by customer_id

/*
loyal" customer is defined as 
(1) having a memebership with your company's point system
(2) having >2 stays at each hotel the customer visited
(3) having stayed at 3 different locations throughout the US
*/