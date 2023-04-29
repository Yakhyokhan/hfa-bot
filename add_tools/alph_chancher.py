LaToKr= {"'": 'ъ', 'a': 'а', 'b': 'б', 'ch': 'ч', 'd': 'д', 'e': 'э', 'f': 'ф', 'g': 'г', "g'": 'ғ', 'h': 'ҳ', 'i': 'и', 'j': 'ж', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', "o'": 'ў', 'p': 'п', 'q': 'қ', 'r': 'р', 's': 'с', 'sh': 'ш', 't': 'т', 'u': 'у', 'v': 'в', 'w': 'ш', 'x': 'х', 'y': 'й', 'ya': 'я', 'ye': 'е', 'yo': 'ё', 'yu': 'ю', 'z': 'з'}

def latin_to_krill(text):
    result = ''
    for i in range(len(text)):
        doubles = ['ch', 'sh','g\'', 'o\'','ya','ye','yo','yu']
        # agar bir tovush ikki harflik bolsa ikkinchi harfga kelganda uni qoshmasin
        if i: 
            if text[i-1: i+1] in  doubles:
                continue 
        single = text[i]
        
        #agar e harfi soz boshida kelmasa
        if single == 'e' and i != 0 and text[i-1] not in (' ',',','_','.','/','\\','(',')','[',']','{','}'): 
            result += 'e'
            continue
        #agar bir tovush ikki harflik bolsa 
        double = text[i: i+2]
        if double in doubles:
            result += LaToKr[double]
            continue
        #agar bir tovush bir harflik bolsa 
        try:
            result += LaToKr[single]
        #alfabetda bunday tovush bolmasa
        except Exception:
            result += single
    return result
            
# print(latin_to_krill("erad/etish"))         
