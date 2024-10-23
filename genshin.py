import random

def run_simulation(num_rounds: int):
    # Define the probability pattern
    probabilities = [
        (0.5, 0.5),   # First check (50/50)
        (0.5, 0.5),   # Second check (50/50 after loss)
        (0.75, 0.25), # Third check (75/25 after two losses)
        (1.0, 0.0)    # Fourth check (100/0 after three losses)
    ]

    reached_fourth_check = 0  # Counter for how many times the 4th check was reached

    for _ in range(num_rounds):
        check_index = 0  # Start from the first probability set
        while check_index < len(probabilities):
            # Perform the check based on the current probability
            win_prob = probabilities[check_index][0]
            if random.random() <= win_prob:
                break  # Reset back to the first check on a win
            else:
                if check_index == 2:  # If we are at the 3rd check and lose, increment the counter
                    reached_fourth_check += 1
                check_index += 1  # Move to the next check after a loss

    return reached_fourth_check


# Run the simulation for a given number of rounds
num_rounds = 100  # You can adjust this value
times_fourth_check_reached = run_simulation(num_rounds)

# Display how many times the 4th check was reached
print(f"The 4th check was reached {times_fourth_check_reached} times out of {num_rounds} rounds.")
