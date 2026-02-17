scores = [0.92, 0.45, 0.70, 0.30, 0.99, 0.65]

# Part 1
filtered_scores = [score for score in scores if score > 0.70 and score != 0.99]
print("Filtered Scores:", filtered_scores)

# Part 2
is_below_50 = any(score < 0.50 for score in filtered_scores)
print("Is any score below 0.50?", is_below_50)
