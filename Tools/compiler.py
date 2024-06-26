import json
import random
m = (
    0.2
    ,0.3
    ,0.4
    ,0.5
    ,0.6
    ,0.7

    )
Data = {}
for starmass in m:
    with open('data/'+('0'+str(int(10*starmass)) if starmass<1 else str(int(10*starmass)))+'.dat') as f:
        splited = [line.split() for line in f][2:]
        Year = [float(x[1]) for x in splited]
        Tempeff = [10**float(x[2]) for x in splited]
        Tempcen = [10**float(x[10]) for x in splited]
        Lum = [10**float(x[3]) for x in splited]
        Mass = [float(x[5]) for x in splited]
        Radius = [float(x[6]) for x in splited]
    while(Lum[0]>=Lum[1]):
        Year.pop(0)
        Tempcen.pop(0)
        Tempeff.pop(0)
        Lum.pop(0)
        Mass.pop(0)
        Radius.pop(0)
    if(starmass>=0.3):
            Year.append(Year[-1]+1e9)
            Tempeff.append(3000)
            Lum.append(Lum[0]*150)
            Mass.append(Mass[-1])
            Radius.append(Radius[0]*40)
            Tempcen.append(Tempcen[-1])
    if(starmass>=0.3):
            Year.append(Year[-1])
            Tempeff.append(3000)
            Lum.append(Lum[0]*30)
            Mass.append(Mass[-1])
            Radius.append(Radius[0]*20)
            Tempcen.append(Tempcen[-1])
    for x in range(len(Year)):
        Year[x]-=Year[0]
        
    NormalizedYear = [x/Year[-1] for x in Year]
    Data[starmass] = {'year':Year,'nyear':NormalizedYear,'tempeff':Tempeff,'tempcen':Tempcen, 'lum':Lum, 'mass': Mass, "radius": Radius}

with open('outputs/low.json','w') as out:
    json.dump(Data,out,indent=4)
