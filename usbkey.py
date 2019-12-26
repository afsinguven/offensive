import sys

modifiers = {"01": "Left CTRL",
           "02": "Left Shift",
           "04": "Left Alt",
           "08": "Left Winkey",
           "10": "Right Ctrl",
           "20": "Right Shift",
           "40": "Right Alt",
           "80": "Right Winkey"}
keycodes = {1: "err", 2: "err", 3: "err", 4: "A", 5: "B", 6: "C", 7: "D", 8: "E", 9: "F", 10: "G", 11: "H", 12: "I", 13: "J", 14: "K",
            15: "L", 16: "M", 17: "N", 18: "O", 19: "P", 20: "Q", 21: "R", 22: "S", 23: "T", 24: "U", 25: "V", 26: "W", 27: "X", 28: "Y",
            29: "Z", 30: "1", 31: "2", 32: "3", 33: "4", 34: "5", 35: "6", 36: "7", 37: "8", 38: "9", 39: "0", 40: "Enter",
            41: "Esc", 42: "BSp", 43: "Tab", 44: "Space", 45: "- / _", 46: "= / +", 47: "[ / {", 48: "] / }", 49: "\\ / |", 50: "...", 51: "; / :",
            52: "' / \"", 53: "` / ~", 54: ", / <", 55: ". / >", 56: "/ / ?", 57: "Caps Lock", 58: "F1", 59: "F2", 60: "F3", 61: "F4", 62: "F5",
            63: "F6", 64: "F7", 65: "F8", 66: "F9", 67: "F10", 68: "F11", 69: "F12", 70: "PrtScr", 71: "Scroll Lock", 72: "Pause", 73: "Insert",
            74: "Home", 75: "PgUp", 76: "Delete", 77: "End", 78: "PgDn", 79: "Right", 80: "Left", 81: "Down", 82: "Up", 83: "Num Lock", 84: "KP /",
            85: "KP *", 86: "KP -", 87: "KP +", 88: "KP Enter", 89: "KP 1 / End", 90: "KP 2 / Down", 91: "KP 3 / PgDn", 92: "KP 4 / Left", 93: "KP 5",
            94: "KP 6 / Right", 95: "KP 7 / Home", 96: "KP 8 / Up", 97: "KP 9 / PgUp", 98: "KP 0 / Ins", 99: "KP . / Del", 100: "...", 101: "Applic",
            102: "Power", 103: "KP =", 104: "F13", 105: "F14", 106: "F15", 107: "F16", 108: "F17", 109: "F18", 110: "F19", 111: "F20", 112: "F21",
            113: "F22", 114: "F23", 115: "F24", 116: "Execute", 117: "Help", 118: "Menu", 119: "Select", 120: "Stop", 121: "Again", 122: "Undo",
            123: "Cut", 124: "Copy", 125: "Paste", 126: "Find", 127: "Mute", 128: "Volume Up", 129: "Volume Down", 130: "Locking Caps Lock",
            131: "Locking Num Lock", 132: "Locking Scroll Lock", 133: "KP ,", 134: "KP =", 135: "Internat", 136: "Internat", 137: "Internat",
            138: "Internat", 139: "Internat", 140: "Internat", 141: "Internat", 142: "Internat", 143: "Internat", 144: "LANG", 145: "LANG",
            146: "LANG", 147: "LANG", 148: "LANG", 149: "LANG", 150: "LANG", 151: "LANG", 152: "LANG", 153: "Alt Erase", 154: "SysRq", 155: "Cancel",
            156: "Clear", 157: "Prior", 158: "Return", 159: "Separ", 160: "Out", 161: "Oper", 162: "Clear / Again", 163: "CrSel / Props", 164: "ExSel"}
if len(sys.argv) < 2:
    print("Usage: python usbkey.py file")
    sys.exit()

f = open(sys.argv[1], "r")
for x in f:
    s = ""
    if x[:2] in modifiers:
        s = modifiers.get(x[:2])
    for start in range(4, 14, 2):
        if int(x[start:start+2], 16) in keycodes:
            if s != "":
                s = s + " " + keycodes[int(x[start:start+2], 16)]
            else:
                s = keycodes[int(x[start:start + 2], 16)]
        elif int(x[start:start+2], 16) == 00:
            if s != "":
                print(s)
                break
        else:
            print("Undefined keycode 0x:"+x[start:start+2])
