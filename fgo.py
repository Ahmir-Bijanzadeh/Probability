from rich import print
import math

def probability_of_at_least_one_win(single_win_prob: float, num_rolls: int):
    at_least_one_win = 1- ((1-single_win_prob)**num_rolls) # 1-(1-p)^n aka 1-p(loose every simulation)
    return at_least_one_win

# Parameters
single_win_prob = .007   # full odds SSR (.7%)
quartz = int(input("quartz count: "))
tix = int(input("golden tix count: "))

num_rolls = (math.floor((quartz)/3) + math.floor((quartz)/30)) + (tix + math.floor(tix/10))
pre11x_rolls = math.floor(quartz/3) + tix
dollars = 79.99*math.floor(quartz/167)

#our final values considering pity/no pity/ old gacha system
probability = probability_of_at_least_one_win(single_win_prob, num_rolls)
ignore_pity = probability_of_at_least_one_win(single_win_prob,num_rolls)
oldprob = probability_of_at_least_one_win(single_win_prob,pre11x_rolls)
if num_rolls >= 330:
    probability = 1
    
packs = (int(input("how many premium top ups: ")))
spent_rolls = (math.floor((167*packs)/3) + math.floor((167*packs)/30))
spent_money = 79.99*packs
spend_check_prob = probability_of_at_least_one_win(single_win_prob, spent_rolls)

total_rolls = (math.floor((167*packs + quartz)/3) + math.floor((167*packs + quartz)/30) + (tix + math.floor(tix/10)))
total_prob = probability_of_at_least_one_win(single_win_prob, total_rolls)

# Display the result
print("\n")
print(f"The probability of at least one win out of {num_rolls} rolls (regular quartz + tix) is {probability:.2f}, which is approximately {probability * 100:.2f}%.")
print(f"that also means that within {num_rolls} rolls the probability of NOT getting your character is {(1 - probability )* 100:.2f}%.")
print(f"the aproximate dollar conversion of that many quartz is {dollars}$ (consdering only the highest pack is purchased)")

print("\n\n")
print(f"if you spent {spent_money}$ to get aprox {spent_rolls} rolls, which resulted in an independant {spend_check_prob * 100:.2f}% chance of obtaining your desired ssr")
if spent_rolls >= 330:
    print("however since the amount of rolls will exceed 330, note you will hit pity with this amount of money")

print("\n\n")
print(f"The combined probability of at least one win out of {total_rolls} checks is {total_prob:.2f}, which is approximately {total_prob * 100:.2f}%.")
print(f"that also means that within {total_rolls} rolls the probability of NOT getting your character is {(1 - total_prob )* 100:.2f}%.")

print("\n\n")
print(f"hypothetically, if fgo had no pity and no 11x per multi, your quartz would afford you {pre11x_rolls} rolls with a ssr win rate of {oldprob:.2f}, or {oldprob * 100:.2f}%.")
print(f"that also means that within {pre11x_rolls} rolls the probability of NOT getting your character is {(1 - oldprob )* 100:.2f}%.")