def probability_of_at_least_one_win(single_win_prob: float, num_rolls: int):
    at_least_one_win = 1- ((1-single_win_prob)**num_rolls) # 1-(1-p)^n aka 1-p(loose every simulation)
    return at_least_one_win

# Parameters
single_win_prob = .007   # full odds SSR (.7%)
quartz = 900
num_rolls = ((quartz/3) + (quartz/30))

# Calculate the probability of at least one win
probability = probability_of_at_least_one_win(single_win_prob, num_rolls)
if num_rolls >= 330:
    probability = 1

# Display the result
print(f"The probability of at least one win out of {num_rolls} checks is {probability:.8f}, which is approximately {probability * 100:.6f}%.")
print(f"For comparison, the base probability is {single_win_prob:.3f}, which is approximately {single_win_prob * 100:.1f}%.")
