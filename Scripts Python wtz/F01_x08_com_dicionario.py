import re

traduz_palavra = {
    65: 'ka', 97: 'ka', 131: 'ka', 132: 'ka', 133: 'ka', 134: 'ka', 142: 'ka', 143: 'ka', 181: 'ka', 183: 'ka',
    192: 'ka', 198: 'ka', 199: 'ka',
    66: 'tu', 98: 'tu',
    67: 'mi', 99: 'mi', 128: 'mi', 135: 'mi',
    68: 'te', 100: 'te',
    69: 'ku', 101: 'ku',
    70: 'lu', 102: 'lu',
    71: 'ji', 103: 'ji',
    72: 'ri', 104: 'ri',
    73: 'ki', 105: 'ki', 139: 'ki', 140: 'ki', 141: 'ki', 161: 'ki', 213: 'ki', 214: 'ki', 215: 'ki', 216: 'ki',
    222: 'ki',
    74: 'zu', 106: 'zu',
    75: 'me', 107: 'me',
    76: 'ta', 108: 'ta',
    77: 'rin', 109: 'rin',
    78: 'to', 110: 'to', 164: 'to', 165: 'to',
    79: 'mo', 111: 'mo', 147: 'mo', 148: 'mo', 149: 'mo', 153: 'mo', 162: 'mo', 224: 'mo', 226: 'mo', 227: 'mo',
    228: 'mo', 229: 'mo',
    80: 'no', 112: 'no',
    81: 'ke', 113: 'ke',
    82: 'shi', 114: 'shi',
    83: 'ari', 115: 'ari',
    84: 'chi', 116: 'chi',
    85: 'do', 117: 'do', 129: 'do', 150: 'do', 151: 'do', 154: 'do', 163: 'do', 233: 'do', 234: 'do', 235: 'do',
    86: 'ru', 118: 'ru',
    88: 'na', 120: 'na',
    87: 'mei', 119: 'mei',
    89: 'fu', 121: 'fu', 152: 'fu', 236: 'fu', 237: 'fu',
    90: 'ra', 122: 'ra',
}


def tradutor(nome):
    letra = re.findall(r'.', nome)
    traduzido = []
    for i in range(len(letra)):
        traduzido.append(traduz_palavra[ord(letra[i])])
    traduzido = (''.join(traduzido))
    return traduzido

#nao pode haver espaco, ele n reconhece

print(tradutor('lutar'))
