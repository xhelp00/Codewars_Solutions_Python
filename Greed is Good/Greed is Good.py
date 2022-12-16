def score(dice):
  # Create a list of all the possible values in the dice
    values = [1, 2, 3, 4, 5, 6]

  # Initialize the score to 0
    score = 0

  # Count the number of each value in the dice
    counts = [dice.count(value) for value in values]

  # Calculate the score for each value
    for value, count in zip(values, counts):
    # If the value appears three times, add the corresponding score
        if count >= 3:
            if value == 1:
                score += 1000
            else:
                score += value * 100
        # If the value appears one or more times, add the corresponding score for each individual die
        if count > 0:
            if value == 1:
                score += 100 * (count % 3)
            elif value == 5:
                score += 50 * (count % 3)
    return score