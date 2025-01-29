# Video Game Trading-Store

My project models a video game trading store where users can trade games with each other and buy game bundles at a discounted price. The database is designed to store information about users, games, user inventories, trades, game bundles, and the games that are part of the bundles.

## Query that I thought it did well on

Question: What is the total value of each user's inventory based on the current trade values?

GPT SQL Response:

```sql
SELECT u.userID, u.username, SUM(ui.tradeValue) as total_inventory_value​
FROM Users u
JOIN UserInventory ui ON u.userID = ui.userID
GROUP BY u.userID;
```

Friendly Response: The total value of each user's inventory based on the current trade values is as follows: John Doe's inventory is worth 85, Jane Smith's inventory is worth 75, Mike Johnson's inventory is worth 65, Emily Brown's inventory is worth 85, and David Wilson's inventory is valued at 23.

## The Question that it tripped up on

Question: "Who has referred who in the referral program?

The GPT-3 response could not provide a query for this question. Once I changed it to GPT-4, it was able to provide a query for this question. The GPT-4 model is more advanced and can handle more complex queries. The friendly response is also not great, as it only lists the referrer and the referred user.

GPT SQL Response:

```sql
SELECT referrer.username AS Referrer, referred.username AS Referred
FROM Users referred
JOIN Users referrer ON referrer.userID = referred.referredBy;
```

Friendly Response: John Doe has referred Jane Smith and Mike Johnson. Jane Smith referred Emily Brown. Mike Johnson referred David Wilson. And Emily Brown referred Sarah Lee.

## Conclusion

The strategies used by ask_gpt yielded similar results, but the GPT-4 model provided a query for the question that the GPT-3 model could not handle. My findings suggest that the GPT-4 model is more advanced and can handle more complex queries. GPT is a powerful tool that can help generate SQL queries for various questions. However, it is essential to note that the quality of the responses may vary depending on the complexity of the question and the version of the model used.

