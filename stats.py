import json
import requests
import sys

#javascritp to get unit 
#  window.location.href.substring(window.location.href.lastIndexOf('/')+1)
unit=''

#To get appSession, go to Network > (any request starting with "households?unit=") > Headers > Request Headers > Cookie > appSession (at the end)
appSession=''

def parseWardData(jsonData):
    membersInWard = 0
    membersWithCalling = 0
    membersWithoutCalling = 0
    membersWithMultipleCallings = 0
    membersWithStakeCallings = 0
    visibleChildrenRecordsInWard = 0

    #loop over each household
    for houseHold in jsonData:
        #loop over each member, count each member
        if "members" in houseHold and isinstance(houseHold["members"], list) and len(houseHold["members"]) > 0:
            for member in houseHold["members"]:
                countThePositionForThisMember = True
                if member["head"] == True:
                    membersInWard = membersInWard + 1

                    if "positions" in member and isinstance(member["positions"], list) and len(member["positions"]) > 0:
                        if len(member["positions"]) > 1:
                            membersWithMultipleCallings = membersWithMultipleCallings + 1
                        
                        for position in member["positions"]:
                            if countThePositionForThisMember:
                                membersWithCalling = membersWithCalling + 1
                                countThePositionForThisMember = False
                            if position["unitNumber"] != member["unitNumber"]:
                                membersWithStakeCallings = membersWithStakeCallings + 1
                    else:
                        membersWithoutCalling = membersWithoutCalling + 1
                else:
                    visibleChildrenRecordsInWard = visibleChildrenRecordsInWard + 1

    print("Adult members in ward: " + str(membersInWard))
    print("Adult members with callings: " + str(membersWithCalling))
    print("Adult members without a calling: " + str(membersWithoutCalling))
    print("Adult members with multiple callings: " + str(membersWithMultipleCallings))
    print("Adult members in the ward with Stake callings: " + str(membersWithStakeCallings))
    print("Average estimated adult activity in ward: " + str(float(membersWithCalling / membersInWard)))
    
    return membersInWard, membersWithCalling
    

membersInStake = 0
membersInStakeWithCalling = 0

cookies = {'appSession':appSession+';'}
r = requests.get('https://directory.churchofjesuschrist.org/api/v4/units/'+unit, cookies=cookies)
if r.status_code != 200:
    sys.exit("Something failed. Check your appSession cookie and try again. (HTTP status code " + str(r.status_code) + ")")

stakeData = json.loads(r.text)
print("stake: " + stakeData['name'])
if 'childUnits' in stakeData:
    childUnits = stakeData['childUnits']
    #print("childUnits: " + str(childUnits))
    for childUnit in childUnits:
        print("childUnit: " + childUnit['name'])
        unitNumber = childUnit['unitNumber']
        r = requests.get('https://directory.churchofjesuschrist.org/api/v4/households?unit='+str(unitNumber), cookies=cookies)
        ward = json.loads(r.text)
        membersInWard, membersWithCalling = parseWardData(json.loads(r.text))
        membersInStakeWithCalling = membersInStakeWithCalling + membersWithCalling
        membersInStake = membersInStake + membersInWard

print("Adult members in Stake: " + str(membersInStake))
print("Adult members in Stake with callings: " + str(membersInStakeWithCalling))
print("Average estimated adult activity in stake: " + str(float(membersInStakeWithCalling / membersInStake)))

