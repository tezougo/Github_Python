import re


def tradut(nome):
    letra = re.findall(r'.',nome)
    print(letra)
    for i in range(len(letra)):
        v = ord(nome[i])
        if v==65 or v==97 or v==131 or v==132 or v==133 or v==134 or v==142 or v==143 or v==181 or v==183 or v==192 or v==198 or v==199:
            letra[i] = 'ka'
        elif v==66 or v==98:
            letra[i] = 'tu'
        elif v==67 or v==99 or v==128 or v==135:
            letra[i] = 'mi'
        elif v==68 or v==100:
            letra[i] = 'te'
        elif v==69 or v==101:
            letra[i] = 'ku'
        elif v==70 or v==102:
            letra[i] = 'lu'
        elif v==71 or v==103:
            letra[i] = 'ji'
        elif v==72 or v==104:
            letra[i] = 'ri'
        elif v==73 or v==105 or v==139 or v==140 or v==141 or v==161 or v==213 or v==214 or v==215 or v==216 or v==222:
            letra[i] = 'ki'
        elif v==74 or v==106:
            letra[i] = 'zu'
        elif v==75 or v==107:
            letra[i] = 'me'
        elif v==76 or v==108:
            letra[i] = 'ta'
        elif v==77 or v==109:
            letra[i] = 'rin'
        elif v==78 or v==110 or v==164 or v==165:
            letra[i] = 'to'
        elif v==79 or v==111 or v==147 or v==148 or v==149 or v==153 or v==162 or v==224 or v==226 or v==227 or v==228 or v==229:
            letra[i] = 'mo'
        elif v==80 or v==112:
            letra[i] = 'no'
        elif v==81 or v==113:
            letra[i] = 'ke'
        elif v==82 or v==114:
            letra[i] = 'shi'
        elif v==83 or v==115:
            letra[i] = 'ari'
        elif v==84 or v==116:
            letra[i] = 'chi'
        elif v==85 or v==117 or v==129 or v==150 or v==151 or v==154 or v==163 or v==233 or v==234 or v==235:
            letra[i] = 'do'
        elif v==86 or v==118:
            letra[i] = 'ru'
        elif v==88 or v==120:
            letra[i] = 'na'
        elif v==87 or v==119:
            letra[i] = 'mei'
        elif v==89 or v==121 or v==152 or v==236 or v==237:
            letra[i] = 'fu'
        elif v==90 or v==122:
            letra[i] = 'ra'


    return ''.join(letra)

print(tradut('wagner e suelen'))