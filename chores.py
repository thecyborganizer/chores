#!/usr/bin/env python

#0: SWEEP_KITCHEN
#1: SWEEP_OTHER
#2: CLEAN_TOILET
#3: TAKE_OUT_TRASH
#
#0: MOP_KITCHEN
#1: CLEAN_FRIDGE
#2: CLEAN_TUB
#3: SCRUB_SHOWER
#
#0: Anna: 0,1,2,3 / 0,1,2,3
#1: Kaileigh: 0,2,1,3 / 1,2,0,3
#2: Ian: 3,2,0,1 / 3,2,0,1
#3: Josh: 3,2,0,1 / 2,3,1,0

import sys

weekly_chores = ["Sweep kitchen", "Sweep other", "Clean toilet", "Take out trash"]
monthly_chores = ["Mop kitchen", "Clean fridge", "Clean tub", "Scrub shower curtain"]
names = ["Anna", "Kaileigh", "Ian", "Josh"]

class person:
    def __init__(self, name, weekly, monthly):
        self.name = name
        self.weekly_preferences = weekly
        self.monthly_preferences = monthly 

anna = person(names[0], {weekly_chores[0] : 0, weekly_chores[1] : 1, weekly_chores[2] : 2, weekly_chores[3] : 3},{monthly_chores[0] : 0, monthly_chores[1] : 1, monthly_chores[2] : 2, monthly_chores[3] : 3})
kaileigh = person(names[1], {weekly_chores[0] : 0, weekly_chores[1] : 2, weekly_chores[2] : 1, weekly_chores[3] : 3},{monthly_chores[0] : 2, monthly_chores[1] : 0, monthly_chores[2] : 1, monthly_chores[3] : 3})
ian = person(names[2], {weekly_chores[0] : 2, weekly_chores[1] : 3, weekly_chores[2] : 1, weekly_chores[3] : 0},{monthly_chores[0] : 2, monthly_chores[1] : 3, monthly_chores[2] : 1, monthly_chores[3] : 0})
josh = person(names[3], {weekly_chores[0] : 2, weekly_chores[1] : 3, weekly_chores[2] : 1, weekly_chores[3] : 0},{monthly_chores[0] : 3, monthly_chores[1] : 2, monthly_chores[2] : 0, monthly_chores[3] : 1})

people = [anna, kaileigh, ian, josh]

# assignments: { person : chore }
def apply_prefs(weekly_assignments,monthly_assignments):
    weekly_score = 0
    monthly_score = 0
    for person in people:
        weekly_chore = weekly_assignments[person.name]
        weekly_score = weekly_score + person.weekly_preferences[weekly_chore]
        monthly_chore = monthly_assignments[person.name]
        monthly_score = monthly_score + person.monthly_preferences[monthly_chore]
    return weekly_score, monthly_score

def permutations(n):
    if n == 1:
        return [[0]]
    else:
        sublists = permutations(n-1)
        collector = []
        for item in sublists:
            for i in range(n):
                new_list = list(item)
                new_list.insert(i,n-1)
                collector.append(new_list)
        return collector

best_weekly_score = sys.maxint
best_weekly_trials = [] 
best_monthly_score = sys.maxint
best_monthly_trials = []
for permutation in permutations(4):
    weekly_trial = {names[0] : weekly_chores[permutation[0]] , names[1] : weekly_chores[permutation[1]], names[2] : weekly_chores[permutation[2]], names[3] : weekly_chores[permutation[3]]} 
    monthly_trial = {names[0] : monthly_chores[permutation[0]] , names[1] : monthly_chores[permutation[1]], names[2] : monthly_chores[permutation[2]], names[3] : monthly_chores[permutation[3]]} 
    scores = apply_prefs(weekly_trial,monthly_trial)
    if scores[0] == best_weekly_score:
        best_weekly_trials.append(weekly_trial)
    if scores[0] < best_weekly_score:
        best_weekly_score = scores[0]
        best_weekly_trials = [weekly_trial]
    if scores[1] == best_monthly_score:
        best_monthly_trials.append(monthly_trial)
    if scores[1] < best_monthly_score:
        best_monthly_score = scores[1]
        best_monthly_trials = [monthly_trial]

print "best weekly score is " + str(best_weekly_score)
print best_weekly_trials
print "best monthly score is " + str(best_monthly_score)
print best_monthly_trials
