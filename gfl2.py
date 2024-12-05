def probability_of_at_least_one_win(single_win_prob: float, num_rolls: int):
    at_least_one_win = 1- ((1-single_win_prob)**num_rolls) # 1-(1-p)^n aka 1-p(loose every simulation)
    return at_least_one_win

# Parameters
single_win_prob = .006   # full odds SSR (.6%)
num_rolls = 300           # num of cosecutive/simultaneos checks on that same single win probability 

# soft pity numbers
# single_win_prob = .189   # boosted soft pity rates
# num_rolls = 22 # rolls from 58th onwards to 79th roll (not counting the 80th or 57th)

# hard pity at 80
# single_win_prob = 1
# num_rolls = 1

# Calculate the probability of at least one win
probability = probability_of_at_least_one_win(single_win_prob, num_rolls)

# Display the result
print(f"The probability of at least one win out of {num_rolls} checks is {probability:.8f}, which is approximately {probability * 100:.6f}%.")
print(f"For comparison, the base probability is {single_win_prob:.3f}, which is approximately {single_win_prob * 100:.1f}%.")
