def linePrn(line):
    hitide_prn = []
    lowtide_prn = []

    for hi in line.hitide:
        hitide_prn.append(str(' %5s - %3s' % (hi[0],hi[1])))

    for lo in line.lowtide:
        lowtide_prn.append(str(' %5s - %3s' % (lo[0],lo[1])))

    if len(hitide_prn) < 2 :
        hitide_prn.append(' --:--   ***')

    if len(lowtide_prn) < 2 :
        lowtide_prn.append(' --:--   ***')

    prn_line = line.weekday+' '+line.tname+' {0:4.1f}'.format(line.moon_age)+hitide_prn[0]+hitide_prn[1]+lowtide_prn[0]+lowtide_prn[1]

    #print(prn_line)
    return (prn_line)
