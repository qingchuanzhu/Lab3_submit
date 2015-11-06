#! /usr/bin/python

# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list):
    # Step1 construct the dict {site => name list}
    siteNameDict = giveMeDictNameList(site_list, user_list)
    
    # Step2 construct dict of {site = > name_list len}
    siteNameLenDict = dict()
    for k in sorted(siteNameDict):
        siteNameLenDict[k] = len(siteNameDict[k])
    
    # Step3 for each pair of site compute number of users, log the max pair in Tuple
    MAX = 0
    siteNameSetList = list(set(site_list))
    numOfSite = len(siteNameSetList)
    for i in range(numOfSite):
        for j in range(i+1,numOfSite):
            pairCount = 0
            elem1 = siteNameSetList[i]
            elem2 = siteNameSetList[j]
            count1 = siteNameLenDict[elem1]
            count2 = siteNameLenDict[elem2]
            if count1 < count2:
                lessL = siteNameDict[elem1]
                largeL = siteNameDict[elem2]
            else:
                lessL = siteNameDict[elem2]
                largeL = siteNameDict[elem1]
            
            for name in lessL:
                if(name in largeL):
                    pairCount = pairCount +1
        
            if(pairCount > MAX):
                largePair = (elem1, elem2)
                MAX = pairCount

    listPair = list(largePair)
    listPair.sort()
    return tuple(listPair)

def giveMeDictNameList(site_list, user_list):
    nameDict = dict()
    for i in range(len(site_list)):
        site = site_list[i]
        nameDict[site] = (nameDict.get(site, set()))
        nameDict[site].add(user_list[i])
    return nameDict
