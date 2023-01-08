import ply.lex as lex
from pyarabic import *

import re
global resultLexer;global positionLexerError


positionLexerError = dict(),

tokens = [ 'FI3L1','ISSM1','ISSM3','HARF1','HARF2','ISSMMAWSOLE','FI3L2','MAF3OLBIH1','HARF3','ISSM2','SSADAQA','ADIM',
'WAW','KHABAR1','LAM','FI3L3','ISSMMAJ','ISSMMAWSOLE2','HARFNAFI','FI3L4','HARFRADR','HARFTAWKID','FI3L5',
'HARFMASSDR','FI3L6','HAE','FI3L7','HARFJAR','ISSMMOAKHAR','ALIF','FI3L8','TAE',
 'FI3LNAKISS','HARFJAR2','ISSM4','FI3L9','MAF3OLBIH2','DARFZAMAN','FI3L10','HARF3ATF','FI3L11','ISSM5','FI3L12',
 'FI3L13','FI3L14','ISSMJALLALA','FI3L15','FI3L16','HARF4','ISSM6','HARFCHARTE','BADL','SIFA','SIFA2','FI3L17',
 'MAF3OLBIH3','FAE','SSIN','FI3L18','MAF3OLBIH4','HARFNAHI','FI3L19','FI3L20','FI3L21','DELIMITER','BISSMI','ALRAHMAN','ALRAHIM']

t_ignore = ' \t'
#t_LETTER=[أ]
t_DELIMITER=r'\(\d+\)'
# صدق الله العظيم
t_BISSMI=r'بسم'
#t_ALLAH=r'الله'
t_ALRAHMAN=r'الرحمن'
t_ALRAHIM=r'الرحيم'
t_SSADAQA=r'صدق'
t_ADIM=r'العظيم'
t_FI3L1=r' اقرأ'
t_ISSM1=r'اسم'
#t_mot7=r'ربك'
t_ISSM3=r'رب'
t_HARF2=r'ك'
t_HARF1=r'ب'
t_ISSMMAWSOLE=r'الذي'
t_FI3L2=r'خلق'
t_MAF3OLBIH1=r'الإنسان'
t_HARF3=r'من'
t_ISSM2=r'علق'
t_WAW=r'و'
t_LAM=r'ل'
t_KHABAR1=r'الأكرم'
t_FI3L3=r'علم'

t_ISSMMAJ=r'القلم'
t_ISSMMAWSOLE2=r'ما'
t_HARFNAFI=r'لم'
t_FI3L4=r'يعلم'
t_HARFRADR=r'كلا'
t_HARFTAWKID=r'إن'
t_FI3L5=r'يطغى'
t_HARFMASSDR=r'أن'
#t_mot26=r'رآه'
t_FI3L6=r'رآ'
t_HAE=r'ه'
t_FI3L7=r'استغنى'
t_HARFJAR=r'إلى'
t_ISSMMOAKHAR=r'الرجعى'
t_ALIF=r'أ'
t_FI3L8=r'رأي'
t_TAE=r'ت'
t_FI3LNAKISS=r'كان'
t_HARFJAR2=r'على'
t_ISSM4=r'الهدى'
t_FI3L9=r'ينهى'
t_MAF3OLBIH2=r'عبدا'
t_DARFZAMAN=r'إذا'
t_FI3L10=r'صلى'


t_HARF3ATF=r'أو'
t_FI3L11=r'أمر'
t_ISSM5=r'التقوى'
t_FI3L12=r'كذب'
t_FI3L13=r'تولى'


t_FI3L14=r'يرى'
t_ISSMJALLALA=r'الله'
t_FI3L15=r'ينته'
t_FI3L16=r'نسفع '
t_HARF4=r'ا'
#t_HAMZA=r'ئ'
t_ISSM6=r'الناصية'
t_HARFCHARTE=r'ئن'




t_BADL=r'ناصية'
t_SIFA=r'كاذبة'
t_SIFA2=r'خاطئة'

t_FI3L17=r'يدع'
t_MAF3OLBIH3=r'نادي'
t_FAE=r'ف'
t_SSIN=r'س'
t_FI3L18=r'ندع'
t_MAF3OLBIH4=r'الزبانية'
t_HARFNAHI=r'لا'
t_FI3L19=r'تطع'

t_FI3L20=r'اسجد'
t_FI3L21=r'اقترب'





#t_mot65=r'لم'

#t_mot67=r'ف'
#t_mot68=r'س'
#t_mot5=


#t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'




#lexer = lex.lex()
lex.lex()
path = '.\program.txt'
file = open(path, 'rb')
file_handle = open(path,"r")
# file contents is the code written in your program
data = file.read()
text=data.decode('utf-8')
lex.input(text)
data = file.readlines()
#lexer.input(file_contents)



def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
   # t.lexer.lexpos += len(t.value)

def t_error(t):
    global resultLexer
    global positionLexerError
    #print("Illegal character '%s'" % t.value)
    t.lexer.skip(len(t.value))
    
    positionLexerError = {
        "value":  t.value,
        "length": len(t.value)
    }
    #print("positionLexerError = ",positionLexerError)
    resultLexer = "incorrect"

#lex.lex()
#data ="صدق الله العظيم"
#lex.input(data)

while 1:
    tok = lex.token()
    if not tok:
        break
    print(tok)