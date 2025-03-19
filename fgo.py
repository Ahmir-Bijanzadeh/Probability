from rich import print
import math

def probability_of_at_least_one_win(single_win_prob: float, num_rolls: int):
    at_least_one_win = 1- ((1-single_win_prob)**num_rolls) # 1-(1-p)^n aka 1-p(loose every simulation)
    return at_least_one_win

#Inputs
quartz = int(input("\nquartz count: "))
tix = int(input("golden tix count: "))
packs = (int(input("how many premium top ups: ")))
old_calcs = input("do you want to know what that would look like before pity was a thing? (y/n): ")

#Mathing + Params
single_win_prob = .007   # full odds SSR (.7%)

num_rolls = (math.floor((quartz)/3) + math.floor((quartz)/30)) + (tix + math.floor(tix/10))
pre11x_rolls = math.floor(quartz/3) + tix
spent_rolls = (math.floor((167*packs)/3) + math.floor((167*packs)/30))
spent_money = 79.99*packs
total_rolls = (math.floor((167*packs + quartz)/3) + math.floor((167*packs + quartz)/30) + (tix + math.floor(tix/10)))
pack_multiplier = (quartz + (tix*3))/167
dollars = 79.99*pack_multiplier
pack_count = math.floor(pack_multiplier)
dollar_round = 79.99*pack_count



#final values after plugging into function
probability = probability_of_at_least_one_win(single_win_prob, num_rolls)
ignore_pity = probability_of_at_least_one_win(single_win_prob,num_rolls)
oldprob = probability_of_at_least_one_win(single_win_prob,pre11x_rolls)
spend_check_prob = probability_of_at_least_one_win(single_win_prob, spent_rolls)
total_prob = probability_of_at_least_one_win(single_win_prob, total_rolls)  
# if num_rolls >= 330:
#     probability = 1
 


# Display the result
print("\n")
if num_rolls >= 330:
        print("[red]Since the amount of rolls will exceed 330, you will hit pity with this amount of resources")
else:
    print(f"[green]Your resources would net you {num_rolls} rolls (regular quartz + tix), which has a win probability of {probability:.2f}, or [cyan]{probability * 100:.2f}%.")
    print(f"[green]that also means that within {num_rolls} rolls the probability of NOT getting your character is [red]{(1 - probability )* 100:.2f}%.")
print(f"[green]The aproximate dollar conversion of that many quartz is {dollars:.2f}$ so {pack_multiplier:.2f} packs. {pack_count} packs cost {dollar_round:.2f}$")

print("\n\n")
if spent_rolls >= 330:
    print("[red]however since the amount of rolls will exceed 330, note you will hit pity with this amount of money")
else:
    print(f"[green]if you spent {spent_money:.2f}$ to get aprox {spent_rolls} rolls, which resulted in an independant [cyan]{spend_check_prob * 100:.2f}%[/cyan] chance of obtaining your desired ssr")


print("\n\n")
if total_rolls >= 330:
    print("[red]Since the amount of rolls will exceed 330, you will hit pity with this amount of resources")
else:
    print(f"[green]The probability of at least one win out of {total_rolls} rolls (designated free currency + premium packs) is {total_prob:.2f}, which is approximately [cyan]{total_prob * 100:.2f}%.")
    print(f"[green]that also means that within those {total_rolls} rolls the probability of NOT getting your character is [/green][red]{(1 - total_prob )* 100:.2f}%.")

if old_calcs.isalpha == True:
    print("\n\n")
    print(f"[yellow]hypothetically, if fgo had no pity and no 11x per multi, your resources would net you[/yellow] {pre11x_rolls}[yellow] rolls with a ssr win rate of [/yellow]{oldprob:.2f}[yellow], or [/yellow]{oldprob * 100:.2f}[yellow]%.")
    print(f"[yellow]that also means that within [/yellow]{pre11x_rolls}[yellow] rolls the probability of NOT getting your character is[/yellow] {(1 - oldprob )* 100:.2f}[yellow]%.")
print("\n\n")