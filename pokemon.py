def probability_of_at_least_one_win(single_win_prob: float, num_machines: int):
    at_least_one_shiny = 1- ((1-single_win_prob)**num_machines) #1 - (1-p)^n aka 1-p(loose every simulation)
    return at_least_one_shiny

# Parameters
single_win_prob = 1 / 8192   # full odds shiny
num_machines = 10000           # num simultaneous shiny checks

# Calculate the probability of at least one win
probability = probability_of_at_least_one_win(single_win_prob, num_machines)

# Display the result
print(f"The probability of at least one win out of {num_machines} machines is {probability:.8f}, which is approximately {probability * 100:.6f}%.")
print(f"For comparison, the probability of a win with a single machine is {single_win_prob:.8f}, which is approximately {single_win_prob * 100:.6f}%.")