#####....HW 8.2....#####
import HW8CoinTossSource as Cls
import StatisticalClasses as Stat

HEADPROBABILITYFAIR = 0.5
ALPHA = 0.05
## superset = length of 1 cohort to help with PI
SUPERSET = 10
NUMBEROFROUNDS = 10 ## how many sim cohorts?
ALPHA = 0.05

HEADPROBABILITYUNFAIR= 0.45

multiplegames_fair = Cls.MultipleGameSets(
    ids=range(NUMBEROFROUNDS),
    prob_head=HEADPROBABILITYFAIR,
    n_games_in_a_set = SUPERSET)
multiplegames_fair.simulation()

##now the unfair part####
multiplegames_unfair = Cls.MultipleGameSets(
    ids = range(NUMBEROFROUNDS, 2*NUMBEROFROUNDS),
    prob_head = HEADPROBABILITYUNFAIR,
    n_games_in_a_set = SUPERSET)
multiplegames_unfair.simulation()

###
Changes = Stat.DifferenceStatIndp(
    name= "Changes in transient state model",
    x= multiplegames_unfair.get_all_total_rewards(),
    y = multiplegames_fair.get_all_total_rewards()
    )

print("The avg reward change... ", Changes.get_mean())
print("95% PI is...", Changes.get_PI(ALPHA))
print("The player only plays 10x, avg reward is higher w lower headprob. But this can vary; you can still lose money b/c there's a small amt.")


## an answer:
#The avg reward change... 40.0
#The 95% PI is... (-100.0, 300.0)
