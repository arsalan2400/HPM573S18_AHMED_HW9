#####....HW 8.1....#####
import HW8CoinTossSource as Cls
import StatisticalClasses as Stat

# A fair game setup
####note that prob_head and n_games are names that come from the original Classes.py (HW8CoinTossSource)###
fair_game = Cls.SetOfGames(
        id=1,
        prob_head = HEADPROBABILITYFAIR,
        n_games=NUMBEROFROUNDS)
fair_result = fair_game.simulation()
###....5000 games because why not?
NUMBEROFROUNDS = 5000
HEADPROBABILITYFAIR = 0.5
ALPHA = 0.05

# An unfair game setup
HEADPROBABILITYUNFAIR = 0.45
unfair_game = Cls.SetOfGames(
        id=2,
        prob_head = HEADPROBABILITYUNFAIR,
        n_games=NUMBEROFROUNDS)
unfair_result = unfair_game.simulation()

#let's see changes....
Changes = Stat.DifferenceStatIndp(
    name="Changes",
    x=unfair_result.get_rewards(),
    y =fair_result.get_rewards())
print("The avg reward change... ", Changes.get_mean())
print("95% CI is...", Changes.get_t_CI(ALPHA))
print("The positive reward change means the player gained, but the casino-owner lost the equivalent over 5000 rounds. This is expected, winning seq is TTH so want less head freq.")

###Sample answer:
##The avg reward change... 17.42
#95% CI is... [10.668218478018163, 24.171781521981842]