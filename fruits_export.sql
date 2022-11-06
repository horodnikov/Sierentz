-- 2.1. How many tons worth of fruit does an average seller have?
select avg(total_weight_per_seller) as avg_fruits_weight
from (select s.seller_id,
			sum(s.fruit_weight) as total_weight_per_seller
		from seller_info as s
		group by s.seller_id) as total


--2.2. How many sellers have at least one client who purchased their fruit?
select count(distinct c.seller_id) as Nb_of_sellers
from consumption_info as c
where client_id is not null
    and quantity_purchased_fruit > 0;
