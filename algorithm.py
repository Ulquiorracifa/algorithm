def groupAnagrams( strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    res = []
    resB = {}
    # res.append([strs[0]])
    # resB[str(len(strs[0]))]=[strs[0]]
    pot = ""
    for c in strs:
        boolRes = False
        if str(len(c)) in resB:
            for x in resB[str(len(c))]:
                lenx = len(c)
                leny = len(c)
                for a in c:
                    if not a in x:
                        break
                    if a in x:
                        lenx = lenx - 1
                for b in x:
                    if not b in c:
                        break
                    if b in c:
                        leny = leny - 1
                if leny == 0 and lenx == 0:
                    boolRes = True
                    pot = x
                    break
        if boolRes == False:
            res.append([c])
            if not str(len(strs[0])) in resB:
                resB[str(len(strs[0]))] = [c]
            else:
                resB[str(len(strs[0]))].append(c)
        else:
            for m in res:
                if pot in m:
                    m.append(c)

    return res
s='123'
# print(groupAnagrams(["wol","owl","fed","fee"]))
print(s[1:2])