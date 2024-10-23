import random

def simulate_single_run():
    win_prob = 0.006  # 0.6% initial probability
    consecutive_losses = 0
    consecutive_true_win_losses = 0
    true_win = False
    
    while True:
        for check in range(1, 91):  # 1 to 90
            # If we're at the 74th check or above, increase the win probability
            if check >= 74:
                win_prob = min(0.006 + (check - 73) * 0.06, 1.0)  # increases by 6% per check, maxing at 100%

            # Simulate the win check
            if random.random() <= win_prob:
                # A win has occurred, now check for "true win" based on consecutive true win losses
                if consecutive_true_win_losses == 0:
                    true_win_prob = 0.50  # First true win probability is 50%
                elif consecutive_true_win_losses == 1:
                    true_win_prob = 0.50  # Second true win probability is still 50%
                elif consecutive_true_win_losses == 2:
                    true_win_prob = 0.75  # Third true win probability is 75%
                else:
                    true_win_prob = 1.00  # Fourth true win probability is guaranteed (100%)

                # Perform the true win check
                if random.random() <= true_win_prob:
                    true_win = True

                # Determine the position of the win
                position = consecutive_losses  # This will tell us how many losses before this win
                # If true win is not achieved, increment the true win loss count
                if not true_win:
                    consecutive_true_win_losses += 1
                else:
                    # True win achieved, reset the counters
                    consecutive_true_win_losses = 0
                    return position  # Return the position of the true win
                
                # Reset the win count since a win occurred
                consecutive_losses = 0
                break  # After a win, restart counting

            consecutive_losses += 1

            # If we reach the 90th check, the win is guaranteed
            if check == 90 and not true_win:
                if consecutive_true_win_losses == 0:
                    true_win_prob = 0.50  # Still 50% for the first true win check
                elif consecutive_true_win_losses == 1:
                    true_win_prob = 0.50  # Still 50%
                elif consecutive_true_win_losses == 2:
                    true_win_prob = 0.75  # 75%
                else:
                    true_win_prob = 1.00  # 100% on the fourth true win check

                # Final true win check on the 90th guaranteed win
                if random.random() <= true_win_prob:
                    true_win = True

                if not true_win:
                    consecutive_true_win_losses += 1

                # Reset the counters after the guaranteed win
                consecutive_losses = 0
                return position  # Return when the 90th check guarantees a win

def run_simulations(num_simulations: int):
    true_win_count = {1: 0, 2: 0, 3: 0, 4: 0}  # Dictionary to count true wins at each position
    
    for _ in range(num_simulations):
        position = simulate_single_run()
        
        # Increment the count for the respective position of the true win
        if position in true_win_count:
            true_win_count[position] += 1
    
    return true_win_count


# Run 1000 simulations
num_simulations = 100
true_win_occurrences = run_simulations(num_simulations)

# Calculate and display the results
total_true_wins = sum(true_win_occurrences.values())
print(f"Out of {num_simulations} simulations, the counts of true wins are:")
print(f"First check: {true_win_occurrences[1]} times")
print(f"Second check: {true_win_occurrences[2]} times")
print(f"Third check: {true_win_occurrences[3]} times")
print(f"Fourth check: {true_win_occurrences[4]} times")
print(f"The total number of true wins: {total_true_wins}")
