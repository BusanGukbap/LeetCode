SELECT user_id,
       COUNT(prompt) AS prompt_count,
       ROUND(AVG(tokens), 2) AS avg_tokens
FROM prompts
GROUP BY user_id
HAVING COUNT(prompt) >= 3
    AND user_id IN (
        SELECT p2.user_id
        FROM prompts p2
        GROUP BY p2.user_id
        HAVING MAX(p2.tokens) > AVG(p2.tokens)
    )
ORDER BY avg_tokens DESC, user_id ASC;
