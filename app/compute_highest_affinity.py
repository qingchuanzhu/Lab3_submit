#! /usr/bin/python
"""This is the target file for Lab3 """

# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list):
    """ Compute the highest affinity taken site list and user list"""
    # Step1 construct the dict {site => name list}
    sitenamedict = givemedictnamelist(site_list, user_list)

    # Step2 construct dict of {site = > name_list len}
    sitenamelendict = dict()
    for k in sorted(sitenamedict):
        sitenamelendict[k] = len(sitenamedict[k])

    # Step3 for each pair of site compute number of users, log the max pair in Tuple
    current_max = 0
    sitenamesetlist = list(set(site_list))
    numofsite = len(sitenamesetlist)
    for i in range(numofsite):
        for j in range(i+1, numofsite):
            paircount = 0
            elem1 = sitenamesetlist[i]
            elem2 = sitenamesetlist[j]
            count1 = sitenamelendict[elem1]
            count2 = sitenamelendict[elem2]
            if count1 < count2:
                lessl = sitenamedict[elem1]
                largel = sitenamedict[elem2]
            else:
                lessl = sitenamedict[elem2]
                largel = sitenamedict[elem1]

            for name in lessl:
                if name in largel:
                    paircount = paircount +1

            if paircount > current_max:
                largepair = (elem1, elem2)
                current_max = paircount

    listpair = list(largepair)
    listpair.sort()
    return tuple(listpair)

def givemedictnamelist(site_list, user_list):
    """ compute the dictionary of site => user list"""
    namedict = dict()
    for i in range(len(site_list)):
        site = site_list[i]
        namedict[site] = (namedict.get(site, set()))
        namedict[site].add(user_list[i])
    return namedict
