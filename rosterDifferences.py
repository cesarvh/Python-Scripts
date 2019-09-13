import json
import sys
import os

args = sys.argv

if len(args) < 3: 
  print("Need to input both an old roster and a new roster!")
  sys.exit()

oldRoster = args[1] 
newRoster = args[2]

with open(oldRoster, 'r') as oldRosterFile:
    oldRosterData = sorted(json.loads(oldRosterFile.read()), key=lambda x : x['id'])

with open(newRoster, 'r') as newRosterFile:
    newRosterData = sorted(json.loads(newRosterFile.read()), key=lambda x : x['id'])


if oldRosterData == newRosterData:
  print ("Your roster has not changed")
  sys.exit()

oldRosterDancers = [dancer['name'] for dancer in oldRosterData]
newRosterDancers = [dancer['name'] for dancer in newRosterData]

droppedDancers = list(set(oldRosterDancers)- set(newRosterDancers))
newDancers = list(set(newRosterDancers)- set(oldRosterDancers))

print("The following dancers dropped your team: ")
print "\n".join(sorted(droppedDancers))

# nDInfo = [newRosterData[dancer] == dancer for dancer in newDancers if dancer in newDancers]

print("\nThe following joined: ")
print "\n".join(sorted(newDancers))

yesNoMeta = ''
newRosterMeta = [(newRosterData[d]['id'], str(newDancers[n])) for n in range(len(newDancers)) for d in range(len(newRosterData)) if newDancers[n] == newRosterData[d]['name']]

yesNoMeta = raw_input("Do you want their names and # copied to your clipboard? (Y/N)\n")

if (yesNoMeta in ['Y', 'Yes', 'y', 'yes']):
  os.system("echo '%s' | pbcopy" % newRosterMeta)
