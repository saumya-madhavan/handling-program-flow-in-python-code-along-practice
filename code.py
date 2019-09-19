# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

print(data.keys()) 
 
# Code starts here

#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
first=data['innings'][0]['1st innings']['deliveries']
counterV=0
for rec in first:
    for key,val in rec.items():
        if val['batsman']=='SC Ganguly':
            counterV+=1
print("No. of deliveries faced by Ganguly = ",counterV)
#  Who was man of the match and how many runs did he scored ?
#print(data['info']['player_of_match'][0])
#first=data['innings'][0]['1st innings']['deliveries']
runscored=0
for foo in first:
    for key,val in foo.items():
        if val['batsman']==data['info']['player_of_match'][0]:
            runscored+=val['runs']['batsman']
print("Man of the match = ",data['info']['player_of_match'][0]," and No. of runs scored = ",runscored)

#  Which batsman played in the first inning?
l1=[]
for delVal in first:
    for key,val in delVal.items():
        if val['batsman'] not in l1:
            l1.append(val['batsman'])
print (l1)

# Which batsman had the most no. of sixes in first inning ?
dict1={}
for rec in first:
    for key,val in rec.items():
        if val['runs']['batsman']==6:
            if val['batsman'] in dict1:
                dict1[val['batsman']]+=1
                #print(dict1)
            else:
                dict1[val['batsman']]=1
                #print(dict1)
print (dict1)
# Find the names of all players that got bowled out in the second innings.
SecondInn=data['innings'][1]['2nd innings']['deliveries']
l3=[]
for rec in SecondInn:
    for key,val in rec.items():
        if 'wicket' in val and val['wicket']['kind']=='bowled':
            l3.append(val['batsman'])
print (l3)

# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
E2=0
for rec in SecondInn:
    for key,val in rec.items():
        if val.get('extras'):
            E2+=1
print(E2)

E1=0
for rec in first:
    for key,val in rec.items():
        if val.get('extras'):
            E1+=1
print(E1)
print("More Extras = ",(E2-E1))
# Code ends here


