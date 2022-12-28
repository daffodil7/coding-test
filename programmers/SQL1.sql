# select
# 과일로 만든 아이스크림 고르기(join)

# 상반기 아이스크림 총주문량이 3,000보다 높으면서 아이스크림의 주 성분이 과일인 아이스크림의 맛을 총주문량이 큰 순서대로 조회하는 SQL 문을 작성해주세요.
SELECT a.FLAVOR
FROM FIRST_HALF as a
JOIN ICECREAM_INFO as b 
ON a.FLAVOR = b.FLAVOR
WHERE TOTAL_ORDER > 3000 and b.INGREDIENT_TYPE = "fruit_based"
ORDER BY TOTAL_ORDER DESC
