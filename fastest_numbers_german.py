#by @Spunk42
#dont expect any good code or comments
#German syntax based on https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024.pdf
#Million and others have adjusted syllable count to make them more common

import math

'''
one_names = [
    [["null", 1], ["nullter", 2]],
    [["ein", 1], ["erster", 2]],
    [["zwei", 1], ["zweiter", 2]],
    [["drei", 1], ["dritter", 2]],
    [["vier", 1], ["vierter", 2]],
    [["fünf", 1], ["fünfter", 2]],
    [["sechs", 1], ["sechster", 2]],
    [["sieben", 2], ["siebter", 2]],
    [["acht", 1], ["achter", 2]],
    [["neun", 1], ["neunter", 2]],
    [["zehn", 1], ["zehnter", 2]],
    [["elf", 1], ["elfter", 2]],
    [["zwölf", 1], ["zwölfter", 2]],
    [["dreizehn", 2], ["dreizehnter", 3]],
    [["vierzehn", 2], ["vierzehnter", 3]],
    [["fünfzehn", 2], ["fünfzehnter", 3]],
    [["sechzehn", 2], ["sechzehnter", 3]],
    [["siebzehn", 2], ["siebzehnter", 3]],
    [["achtzehn", 2], ["achtzehnter", 3]],
    [["neunzehn", 2], ["neunzehnter", 3]],
]

ten_names = [
    [[]],  # 0 Zehner
    [[]],  # 1 Zehner
    [["zwanzig", 2], ["zwanzigster", 3]],
    [["dreißig", 2], ["dreißigster", 3]],
    [["vierzig", 2], ["vierzigster", 3]],
    [["fünfzig", 2], ["fünfzigster", 3]],
    [["sechzig", 2], ["sechzigster", 3]],
    [["siebzig", 2], ["siebzigster", 3]],
    [["achtzig", 2], ["achtzigster", 3]],
    [["neunzig", 2], ["neunzigster", 3]],
]

large_names = [
    ["hundert",2,100,2],
    ["tausend",2,1000,3],
    ["Million",2,1000000,6],
    ["Milliarde",3,1000000000,9],
]
'''
superscripts = ['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹',
                '¹⁰','¹¹','¹²','¹³','¹⁴','¹⁵','¹⁶','¹⁷','¹⁸','¹⁹',
                '²⁰','²¹','²²','²³']

number_names = []
pemdas_count = 6


'''
def base_syllables(n):
    if n < 20:
        return one_names[n][0][1], one_names[n][0][0], one_names[n][1][1], one_names[n][1][0], 0, 1
    elif n < 100:
        n_mod = n % 10
        n_div = n // 10
        if n % 10 == 0: 
            return ten_names[n_div][0][1], ten_names[n_div][0][0], ten_names[n_div][1][1], ten_names[n_div][1][0], 1, 2

        return (
                number_names[n_mod]["syllables"][1] + ten_names[n_div][0][1] + 1, 
                number_names[n_mod]["names"][1] + "und" + ten_names[n_div][0][0],
                number_names[n_mod]["syllables"][0]+ ten_names[n_div][1][1] + 1, 
                number_names[n_mod]["names"][1] + "und" + ten_names[n_div][1][0],
                0,
                2
            )
    

    large_index = 0
    while (large_names[large_index+1][2] <= n):
        large_index += 1

    n_mod = n % large_names[large_index][2]
    n_div = n // large_names[large_index][2]

    if large_index == 0 and n_div == 1:
        div_name = ""  # nur "hundert"
        div_syllables = 0
    else:
        div_name = number_names[n_div]["names"][1]
        div_syllables = number_names[n_div]["syllables"][1]

    if n_mod == 0:
        return (
            div_syllables + large_names[large_index][1],
            div_name + large_names[large_index][0],
            div_syllables + large_names[large_index][1] + 1,
            div_name + large_names[large_index][0] + "ster",
            large_names[large_index][3] + number_names[n_div]["zeroes"],
            large_names[large_index][3] + number_names[n_div]["digits"]
        )
    
    

    return (
        div_syllables + large_names[large_index][1] + number_names[n_mod]["syllables"][1],
        div_name      + large_names[large_index][0] + number_names[n_mod]["names"][1],
        div_syllables + large_names[large_index][1] + number_names[n_mod]["syllables"][0],
        div_name      + large_names[large_index][0] + number_names[n_mod]["names"][0],
        number_names[n_mod]["zeroes"],
        large_names[large_index][3] + number_names[n_div]["digits"]
    )
'''

einer=["","ein","zwei","drei","vier","fünf","sechs","sieben","acht","neun"]
einer_silben=[1,1,1,1,1,1,1,2,1,1]
spzehner=["zehn","elf","zwölf","dreizehn","vierzehn","fünfzehn","sechzehn","siebzehn","achtzehn","neunzehn"]
spzehner_silben=[1,1,1,2,2,2,2,2,2,2]
zehner=["","","zwanzig","dreißig","vierzig","fünfzig","sechzig","siebzig","achtzig","neunzig"]
zehner_silben=[0,0,2,2,2,2,2,2,2,2]
smllscl=["","tausend","Million","Milliarde","Billion","Billiarde"]  
smllscl_silben=[0,2,2,3,2,3]
fraction_names = [
    [],  # 0
    [],  # 1
    ["halbe", 2],
    ["drittel", 2],
    ["viertel", 2],
    ["fünftel", 2],
    ["sechstel", 2],
    ["siebtel", 2],
    ["achtel", 2],
    ["neuntel", 2],
]
def base_syllables(n):
    def twodigit(num):
        if num[0]=="0":
            if num[1]=="0":
                nam=""
                silben_anz=0
            else:
                nam=einer[int(num)]
                silben_anz=einer_silben[int(num)]
        elif num[0]=="1":
            nam=spzehner[int(num[1])]
            silben_anz=spzehner_silben[int(num[1])]
        elif num[1]=="0":
            nam=zehner[int(num[0])]
            silben_anz=zehner_silben[int(num[0])]
        else:
            nam=einer[int(num[1])]+"und"+zehner[int(num[0])]
            silben_anz=einer_silben[int(num[1])] + 1 + zehner_silben[int(num[0])]
        return nam, silben_anz
    def digit3(num):
        silben_anz=0
        if num[0]=="0":nam, silben_anz=twodigit(num[1:])
        else:
            if num[0]=="1":
                nam="hundert"
                silben_anz+=2
            else:
                nam=einer[int(num[0])]+"hundert"
                silben_anz=einer_silben[int(num[0])] + 2
            if int(num[1:])!=0:
                a, b =twodigit(num[1:])
                nam += a
                silben_anz += b
        return nam, silben_anz
    def scale(num):
        if num=="0":return "Null", 1
        l=math.floor(math.log(int(num),1000))
        x=""
        w=""
        silben_anz=0
        num="0"*((3-len(num))%3)+num
        for i in range(l+1):
            z, a=digit3(num[-3*i-3:][:3])
            p=""
            if i>1 and int(num[-3*i-3:][:3])>1:
                p=(i-1)%2*"e"+"n"
            if i>1 and z[:3]=="ein":
                z="eine"+z[3:]
                silben_anz+=1
            if i==1 and z=="ein":
                x=smllscl[1]+x
            elif i>1 and z!="":
                x=z+" "+smllscl[i]+p+" "+x
                silben_anz+=a
            elif z!="":
                x=z+smllscl[i]+p+x
                silben_anz+=a
            if z!="":silben_anz += smllscl_silben[i]
        return w+x, silben_anz
    num=str(n)
    digits = len(num)
    zeros = digits - len(num.rstrip('0'))
    nam, silben_anz=scale(num)
    if nam[-3:]=="ein":nam+="s"
    nam=nam[0].upper()+nam[1:]
    #_, _, sil2, nam2, _, _ = base_syllables2(n)
    #if not silben_anz == sil2 -2 : print(n, silben_anz, nam, sil2, nam2)
    sil_frac, nam_frac = get_fraction_name(n, nam, silben_anz)
    return silben_anz, nam, sil_frac, nam_frac, zeros, digits

def get_fraction_name(n, nam, silben_anz):
        if n < len(fraction_names) and fraction_names[n]:
            return fraction_names[n][0], fraction_names[n][1]
        # Fallback: Kardinal + "tel"
        return nam + "tel", silben_anz + 1

def number_names_generator(leave_point,max_number):
    max_syllables = 0

    for n in range(0,max_number + 1):
        n_syllables, n_name, frac_name, frac_syllables, zeroes, digits = base_syllables(n)
        adj_zeroes = zeroes
        if zeroes > 3:
            adj_zeroes = (zeroes // 3)*3

        
        number_names.append(
            {
                "value": n,
                "syllables": [frac_syllables] + [n_syllables]*(pemdas_count-1),
                "names": [frac_name] + [n_name]*(pemdas_count-1),
                "equations": [str(n)]*pemdas_count,
                "original": n_syllables,
                "zeroes": adj_zeroes,
                "digits": digits,
                "nonzero": digits-zeroes,
                "auto pass": (n%100 < 20 and n%100 > 0) or zeroes < 1 or digits < 3,
            }
        )
        max_syllables = max(max_syllables, n_syllables)
    
    #print(len(number_names))
    #number_names[2]["syllables"][0] = 2
    #number_names[2]["names"][0] = "halb"

    syllable_key = [[]]
    for u in range(pemdas_count):
        syllable_key[0].append([])

    # pemdas indices: 0 ordinal, 1 original, 2 exponent, 3 multiplication, 4 division, 5 addition and subtraction
    unary = [
        {"id": "²", "syllables": 2, "text": " quadriert", "value": 2, "pemdas_input": 2,"pemdas_result": 2},
        {"id": "³", "syllables": 2, "text": " kubiert", "value": 3, "pemdas_input": 2,"pemdas_result": 2},
        {"id": "⁴", "syllables": 2, "text": " hoch vier", "value": 4, "pemdas_input": 2,"pemdas_result": 2},
    ]
    
    binary = [
        { "id": "+",        "syllables": 1, "text": " plus ",   "pemdas_left": 5,"pemdas_right": 5,"pemdas_result": 5},
        { "id": "*",        "syllables": 1, "text": " mal ",    "pemdas_left": 3,"pemdas_right": 4,"pemdas_result": 4},
        { "id": "*",        "syllables": 1, "text": " mal ",    "pemdas_left": 3,"pemdas_right": 3,"pemdas_result": 3},
        { "id": "-",        "syllables": 2, "text": " minus ",  "pemdas_left": 5,"pemdas_right": 4,"pemdas_result": 5},
        #{ "id": "/",        "syllables": 1, "text": " durch ",  "pemdas_left": 3,"pemdas_right": 2,"pemdas_result": 4},
        { "id": "fraction", "syllables": 0, "text": " ",        "pemdas_left": 3,"pemdas_right": 2,"pemdas_result": 4},
        { "id": "^",        "syllables": 1, "text": " hoch ",   "pemdas_left": 2, "pemdas_right": 2,"pemdas_result": 2},
    ]

    min_missing = 1
    for s in range(1, max_syllables + 1):
        print("searching", s, "syllables, at",min_missing)

        syllable_key.append([])
        for u in range(pemdas_count):
            syllable_key[s].append([])
            
        for n in range(min_missing,max_number+1):
            for u in range(pemdas_count):
                if number_names[n]["syllables"][u] < s:
                    break
                if number_names[n]["syllables"][u] == s:
                    syllable_key[s][u].append(number_names[n]["value"])
                elif u > 0:
                    break


        for op in binary:
            #print(op)

            min_left, max_left = get_first_extremes(op, min_missing, max_number)
            for left_syllables in range(s - op["syllables"]):
                for left_value in syllable_key[left_syllables][op["pemdas_left"]]:
                    if left_value < min_left:
                        continue
                    if left_value > max_left:
                        break

                    min_right, max_right = get_second_extremes(op, min_missing, max_number, left_value)

                    for right_value in syllable_key[s - op["syllables"] - left_syllables][op["pemdas_right"]]:
                        if right_value < min_right:
                            continue
                        if right_value > max_right:
                            break
                        if (op["id"] == "fraction"
                            and not number_names[left_value]["auto pass"]
                            and right_value != 2
                            and number_names[left_value]["zeroes"] > number_names[right_value]["digits"]
                            and (number_names[left_value]["nonzero"] > 1 or number_names[right_value]["nonzero"] > 1)
                            and number_names[left_value]["names"][1] == number_names[left_value]["names"][2]):
                            continue


                        op_output, valid_output = get_output(op, left_value, right_value)
                        if not valid_output:
                            continue
                        
                        if op["id"] == "fraction":
                            new_name = (
                                number_names[left_value]["names"][op["pemdas_left"]]
                                + op["text"]
                                + number_names[right_value]["names"][0]
                            )
                            real_s = left_syllables + number_names[right_value]["syllables"][0]
                        else:
                            new_name = (
                                number_names[left_value]["names"][op["pemdas_left"]] 
                                + op["text"] 
                                + number_names[right_value]["names"][op["pemdas_right"]]
                            )
                            real_s = number_names[left_value]["syllables"][op["pemdas_left"]]+ op["syllables"] + number_names[right_value]["syllables"][op["pemdas_right"]]
                        
                        new_equation = number_names[left_value]["equations"][op["pemdas_left"]] 
                        if op["id"] == "^" and new_equation == number_names[left_value]["equations"][1]:
                            new_equation = new_equation + "" + superscripts[right_value]
                        elif op["id"] == "^":
                            new_equation = "(" + new_equation + ")" + superscripts[right_value]

                        else:
                            if op["id"] == "fraction":
                                new_equation += " / "
                            else: #should not happen
                                new_equation += " " + op["id"] + " "
                            new_equation += number_names[right_value]["equations"][op["pemdas_right"]]
                        

                        for u in range(op["pemdas_result"], pemdas_count):
                            if number_names[op_output]["syllables"][u] > real_s:
                                number_names[op_output]["names"][u] = new_name
                                number_names[op_output]["equations"][u] = new_equation
                                number_names[op_output]["syllables"][u] = real_s
                                syllable_key[s][u].append(op_output)

        for op in unary:
            #print(op)
            if s <= op["syllables"]:
                continue
            
            


            min_value, max_value = get_first_extremes(op, min_missing, max_number)
            for input_value in syllable_key[s - op["syllables"]][op["pemdas_input"]]:
                if input_value < min_value:
                    continue
                if input_value > max_value:
                    break

                op_output, valid_output = get_output(op, input_value)
                if not valid_output:
                    continue

                new_name = number_names[input_value]["names"][op["pemdas_input"]] + op["text"]
                new_equation = number_names[input_value]["equations"][op["pemdas_input"]]
                if new_equation == number_names[input_value]["equations"][1]:
                    new_equation = new_equation + "" + op["id"]
                else:
                    new_equation = "(" + new_equation + ")" + op["id"]
                    
                for u in range(op["pemdas_result"],pemdas_count):
                    if number_names[op_output]["syllables"][u] >= s:
                        number_names[op_output]["names"][u] = new_name
                        number_names[op_output]["equations"][u] = new_equation

                        if number_names[op_output]["syllables"][u] > s:
                            number_names[op_output]["syllables"][u] = s
                            syllable_key[s][u].append(op_output)
                

        for i in range(pemdas_count):
            syllable_key[s][i].sort()
        while number_names[min_missing]["syllables"][-1] <= s:
            min_missing += 1
            if min_missing > leave_point:
                    break
        if min_missing > leave_point:
                break

    return number_names[0:leave_point+1]


def get_first_extremes(op,min_missing,max_number):
    if op["id"] == "²":
        return min_missing**(1/2), max_number**(1/2)
    elif op["id"] == "³":
        return min_missing**(1/3), max_number**(1/3)
    elif op["id"] == "⁴":
        return min_missing**(1/4), max_number**(1/4)
    elif op["id"] == "+":
        return 6, max_number-1
    elif op["id"] == "*":
        return 2, max_number**0.5
    elif op["id"] == "-":
        return min_missing+1, max_number
    elif op["id"] == "/" or op["id"] == "fraction":
        return min_missing*2, max_number
    elif op["id"] == "^":
        return 2, max_number**0.2
    
def get_second_extremes(op,min_missing,max_number,left_value):
    if op["id"] == "+":
        return 1, min(left_value,max_number - left_value)
    elif op["id"] == "*":
        return max(left_value,min_missing/left_value), max_number/left_value
    elif op["id"] == "-":
        return 1, left_value-min_missing
    elif op["id"] == "/" or op["id"] == "fraction":
        return 2, left_value/2
    elif op["id"] == "^":
        return 5, math.log(max_number)/math.log(left_value)
    
def get_output(op,left_value,right_value=0):
    if op["id"] == "²":
        return left_value**2, True
    if op["id"] == "³":
        return left_value**3, True
    elif op["id"] == "⁴":
        return left_value**4, True
    elif op["id"] == "^":
        return left_value**right_value, True
    elif op["id"] == "+":
        return left_value + right_value, True
    elif op["id"] == "*":
        return left_value * right_value, True
    elif op["id"] == "-":
        return left_value - right_value, True
    elif op["id"] == "/" or op["id"] == "fraction":
        if left_value % right_value == 0:
            return left_value // right_value, True
        return 0, False

def numbers_out(number_names, file_name):
    with open(file_name,"w",encoding="utf-8") as f:
        f.write(f"{'#Silben':<3}{'Wert':<6}{'Gleichung':<25}Name\n")
        for l in number_names:
           #f.write(str(l["value"]) + "," + l["names"][-1] + "," + l["equations"][-1] + "," + str(l["syllables"][-1])  +"\n")
            f.write(f"#{l['syllables'][-1]:<3}  {l['value']:<6}  =  {l['equations'][-1]:<25}  {l['names'][-1]}\n")

fast_numbers = number_names_generator(100000,1001000)
numbers_out(fast_numbers, "fastest_numbers_de.txt")