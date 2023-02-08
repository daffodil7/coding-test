# 다시 풀 문제
# 가격이 제일 비싼 식품의 정보 출력하기
select *
from food_product
where price = (SELECT max(price) as price from food_product)
