import ply.lex as lex
import ply.yacc as yacc
import re
global resultLexer;global positionLexerError
global resultParser;global positionParserError

positionLexerError,positionParserError = dict(),dict()


#Analyse lexical

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




def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

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

#*******************************Analyse syntaxique**********************************


def p_joumla(p):
    '''joumla : aya1
              | aya2
              | aya3
              | aya4
              | aya5
              | aya6
              | aya7
              | aya8
              | aya9  
              | aya10
              | aya11
              | aya12
              | aya13
              | aya14
              | aya15
              | aya16
              | aya17
              | aya18
              | aya19
              | verset1
              | verset2
              | verset3
              | verset4
              | verset5
              | verset6
              | verset7
              | verset8
              | verset9
              | verset10
              | verset11
              | verset12
              | verset13
              | verset14
              | verset15
              | verset16
              | verset17
              | verset18
              | verset19
              | ayat
              | basmala
              | nihaya  
              | soura

     '''
    p[0] = p[1]




def p_soura(p):
    'soura : basmala ayat nihaya'
    print('correcte')


def p_basmala(p):
    'basmala : BISSMI ISSMJALLALA ALRAHMAN ALRAHIM'
    p[0] = " ".join(p[1:])
    print("بسم الله الرحمن الرحيم")


def p_nihayasora(p):
    'nihaya : SSADAQA ISSMJALLALA ADIM'
    p[0] = " ".join(p[1:])
    print("صدق الله العظيم")    

#cette fonction permet d'entrer soit sora kamla ou bien quelque verset 
def p_ayat(p):
    '''ayat  : verset1 verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18 verset19
             | verset1 verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18
             | verset1 verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 
             | verset1 verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 
             | verset1 verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15
             | verset1 verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14
             | verset1 verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13
             | verset1 verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 
             | verset1 verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11
             | verset1 verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10
             | verset1 verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9
             | verset1 verset2 verset3 verset4 verset5 verset6 verset7 verset8
             | verset1 verset2 verset3 verset4 verset5 verset6 verset7
             | verset1 verset2 verset3 verset4 verset5 verset6
             | verset1 verset2 verset3 verset4 verset5
             | verset1 verset2 verset3 verset4
             | verset1 verset2 verset3
             | verset1 verset2
             | verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18 verset19
             | verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18 
             | verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17
             | verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16
             | verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15
             | verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14
             | verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13
             | verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12
             | verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11
             | verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 
             | verset2 verset3 verset4 verset5 verset6 verset7 verset8 verset9
             | verset2 verset3 verset4 verset5 verset6 verset7 verset8
             | verset2 verset3 verset4 verset5 verset6 verset7
             | verset2 verset3 verset4 verset5 verset6 
             | verset2 verset3 verset4 verset5 
             | verset2 verset3 verset4
             | verset2 verset3
             | verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18 verset19
             | verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18
             | verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 
             | verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16
             | verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15
             | verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 
             | verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13
             | verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 
             | verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 
             | verset3 verset4 verset5 verset6 verset7 verset8 verset9 verset10
             | verset3 verset4 verset5 verset6 verset7 verset8
             | verset3 verset4 verset5 verset6 verset7
             | verset3 verset4 verset5 verset6 
             | verset3 verset4 verset5 
             | verset3 verset4
             | verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18 verset19
             | verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18
             | verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 
             | verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 
             | verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 
             | verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14
             | verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 
             | verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12
             | verset4 verset5 verset6 verset7 verset8 verset9 verset10 verset11 
             | verset4 verset5 verset6 verset7 verset8 verset9 verset10
             | verset4 verset5 verset6 verset7 verset8 verset9
             | verset4 verset5 verset6 verset7 verset8 
             | verset4 verset5 verset6 verset7
             | verset4 verset5 verset6
             | verset4 verset5 
             | verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18 verset19
             | verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18 
             | verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17
             | verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 
             | verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15
             | verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14
             | verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13
             | verset5 verset6 verset7 verset8 verset9 verset10 verset11 verset12
             | verset5 verset6 verset7 verset8 verset9 verset10 verset11
             | verset5 verset6 verset7 verset8 verset9 verset10
             | verset5 verset6 verset7 verset8 verset9
             | verset5 verset6 verset7 verset8 
             | verset5 verset6 verset7
             | verset5 verset6
             | verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18 verset19
             | verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18
             | verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17
             | verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16
             | verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15
             | verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 
             | verset6 verset7 verset8 verset9 verset10 verset11 verset12 verset13
             | verset6 verset7 verset8 verset9 verset10 verset11 verset12
             | verset6 verset7 verset8 verset9 verset10 verset11
             | verset6 verset7 verset8 verset9 verset10
             | verset6 verset7 verset8 verset9
             | verset6 verset7 verset8
             | verset6 verset7 
             | verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18 verset19
             | verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18
             | verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17
             | verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16
             | verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 
             | verset7 verset8 verset9 verset10 verset11 verset12 verset13 verset14 
             | verset7 verset8 verset9 verset10 verset11 verset12 verset13 
             | verset7 verset8 verset9 verset10 verset11 verset12
             | verset7 verset8 verset9 verset10 verset11
             | verset7 verset8 verset9 verset10
             | verset7 verset8 verset9
             | verset7 verset8
             | verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18 verset19
             | verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18
             | verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17
             | verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16
             | verset8 verset9 verset10 verset11 verset12 verset13 verset14 verset15
             | verset8 verset9 verset10 verset11 verset12 verset13 verset14
             | verset8 verset9 verset10 verset11 verset12 verset13
             | verset8 verset9 verset10 verset11 verset12
             | verset8 verset9 verset10 verset11 
             | verset8 verset9 verset10
             | verset8 verset9
             | verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18 verset19
             | verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18
             | verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17
             | verset9 verset10 verset11 verset12 verset13 verset14 verset15 verset16
             | verset9 verset10 verset11 verset12 verset13 verset14 verset15
             | verset9 verset10 verset11 verset12 verset13 verset14 
             | verset9 verset10 verset11 verset12 verset13 
             | verset9 verset10 verset11 verset12
             | verset9 verset10 verset11
             | verset9 verset10 
             | verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18 verset19
             | verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18
             | verset10 verset11 verset12 verset13 verset14 verset15 verset16 verset17
             | verset10 verset11 verset12 verset13 verset14 verset15 verset16
             | verset10 verset11 verset12 verset13 verset14 verset15
             | verset10 verset11 verset12 verset13 verset14
             | verset10 verset11 verset12 verset13
             | verset10 verset11 verset12
             | verset10 verset11
             | verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18 verset19
             | verset11 verset12 verset13 verset14 verset15 verset16 verset17 verset18
             | verset11 verset12 verset13 verset14 verset15 verset16 verset17
             | verset11 verset12 verset13 verset14 verset15 verset16
             | verset11 verset12 verset13 verset14 verset15
             | verset11 verset12 verset13 verset14
             | verset11 verset12 verset13 
             | verset11 verset12
             | verset12 verset13 verset14 verset15 verset16 verset17 verset18 verset19
             | verset12 verset13 verset14 verset15 verset16 verset17 verset18
             | verset12 verset13 verset14 verset15 verset16 verset17
             | verset12 verset13 verset14 verset15 verset16 
             | verset12 verset13 verset14 verset15
             | verset12 verset13 verset14 
             | verset12 verset13 
             | verset13 verset14 verset15 verset16 verset17 verset18 verset19
             | verset13 verset14 verset15 verset16 verset17 verset18
             | verset13 verset14 verset15 verset16 verset17
             | verset13 verset14 verset15 verset16
             | verset13 verset14 verset15
             | verset13 verset14
             | verset14 verset15 verset16 verset17 verset18 verset19
             | verset14 verset15 verset16 verset17 verset18 
             | verset14 verset15 verset16 verset17 
             | verset14 verset15 verset16 
             | verset14 verset15 
             | verset15 verset16 verset17 verset18 verset19
             | verset15 verset16 verset17 verset18
             | verset15 verset16 verset17 
             | verset15 verset16 
             | verset16 verset17 verset18 verset19
             | verset16 verset17 verset18
             | verset16 verset17 
             | verset17 verset18 verset19
             | verset17 verset18
             | verset18 verset19
        

        


    '''
  


def p_verset1(p):
      'verset1 : aya1 DELIMITER '
      if(p[2]=='(1)'): 
            print('اقرأ باسم ربك الذي خلق (1)')
      else:
              print('erreur au niveau du delimiter de aya1,il faut mettre le delimiter 1') 

def p_verset2(p):
      'verset2 : aya2 DELIMITER '
      if(p[2]=='(2)'): 
            print('خلق الإنسان من علق (2)')
            #print(p[1])
      else:
              print('erreur au niveau du delimiter de aya2,il faut mettre le delimiter 2') 

def p_verset3(p):
      'verset3 : aya3 DELIMITER '
      if(p[2]=='(3)'): 
            print('اقرأ وربك الأكرم (3)')
      else:
              print('erreur au niveau du delimiter de aya3,il faut mettre le delimiter 3') 

def p_verset4(p):
      'verset4 : aya4 DELIMITER '
      if(p[2]=='(4)'): 
            print('الذي علم بالقلم (4)')
      else:
              print('erreur au niveau du delimiter de aya4,il faut mettre le delimiter 4') 


def p_verset5(p):
      'verset5 : aya5 DELIMITER '
      if(p[2]=='(5)'): 
            print('علم الإنسان ما لم يعلم (5)')
      else:
              print('erreur au niveau du delimiter de aya5,il faut mettre le delimiter 5') 


def p_verset6(p):
      'verset6 : aya6 DELIMITER '
      if(p[2]=='(6)'): 
            print('كلا إن الإنسان ليطغى (6)')
      else:
              print('erreur au niveau du delimiter de aya6,il faut mettre le delimiter 6')

def p_verset7(p):
      'verset7 : aya7 DELIMITER '
      if(p[2]=='(7)'): 
            print('أن رآه استغنى (7) ')
      else:
              print('erreur au niveau du delimiter de aya7,il faut mettre le delimiter 7') 


def p_verset8(p):
      'verset8 : aya8 DELIMITER '
      if(p[2]=='(8)'): 
            print('إن إلى ربك الرجعى (8)')
      else:
              print('erreur au niveau du delimiter de aya8,il faut mettre le delimiter 8') 


def p_verset9(p):
      'verset9 : aya9 DELIMITER '
      if(p[2]=='(9)'): 
            print('أرأيت الذي ينهى (9)')
      else:
              print('erreur au niveau du delimiter de aya9,il faut mettre le delimiter 9') 


def p_verset10(p):
      'verset10 : aya10 DELIMITER '
      if(p[2]=='(10)'): 
            print('عبدا إذا صلى (10)')
      else:
              print('erreur au niveau du delimiter de aya10,il faut mettre le delimiter 10')                             


def p_verset11(p):
      'verset11 : aya11 DELIMITER '
      if(p[2]=='(11)'): 
            print('رأيت إن كان على الهدى (11)')
      else:
              print('erreur au niveau du delimiter de aya11,il faut mettre le delimiter 11') 

def p_verset12(p):
      'verset12 : aya12 DELIMITER '
      if(p[2]=='(12)'): 
            print('أو أمر بالتقوى (12)')
      else:
              print('erreur au niveau du delimiter de aya12,il faut mettre le delimiter 12') 

def p_verset13(p):
      'verset13 : aya13 DELIMITER '
      if(p[2]=='(13)'): 
            print('أرأيت إن كذب وتولى (13)')
      else:
              print('erreur au niveau du delimiter de aya13,il faut mettre le delimiter 13')



def p_verset14(p):
      'verset14 : aya14 DELIMITER '
      if(p[2]=='(14)'): 
            print('ألم يعلم بأن الله يرى (14)')
      else:
              print('erreur au niveau du delimiter de aya14,il faut mettre le delimiter 14')                              



def p_verset15(p):
      'verset15 : aya15 DELIMITER '
      if(p[2]=='(15)'): 
            print('كلا لئن لم ينته لنسفعا بالناصية (15)')
      else:
              print('erreur au niveau du delimiter de aya15,il faut mettre le delimiter 15') 


def p_verset16(p):
      'verset16 : aya16 DELIMITER '
      if(p[2]=='(16)'): 
            print('ناصية كاذبة خاطئة (16)')
      else:
              print('erreur au niveau du delimiter de aya16,il faut mettre le delimiter 16') 


def p_verset17(p):
      'verset17 : aya17 DELIMITER '
      if(p[2]=='(17)'): 
            print('فليدع ناديه (17) ')
      else:
              print('erreur au niveau du delimiter de aya17,il faut mettre le delimiter 17') 

def p_verset18(p):
      'verset18 : aya18 DELIMITER '
      if(p[2]=='(18)'): 
            print('سندع الزبانية (18)')
      else:
              print('erreur au niveau du delimiter de aya18,il faut mettre le delimiter 18') 


def p_verset19(p):
      'verset19 : aya19 DELIMITER '
      if(p[2]=='(19)'): 
            print('كلا لا تطعه واسجد واقترب(19)')
      else:
              print('erreur au niveau du delimiter de aya19,il faut mettre le delimiter 19') 




def p_aya1(p):
    'aya1 : FI3L1 HARF1 ISSM1 ISSM3 HARF2 ISSMMAWSOLE FI3L2'
       
    #print("AYA 1 sans delimiter est correcte")
   
  
def p_aya2(p):
    'aya2 : FI3L2 MAF3OLBIH1 HARF3 ISSM2'

    #print("AYA 2 sans delimiter est correcte")


         

    
def p_aya3(p):
    'aya3 : FI3L1 WAW ISSM3 HARF2 KHABAR1'
          
         

    #print(" AYA 3 sans delimiter est correcte")
    


def p_aya4(p):
    'aya4 : ISSMMAWSOLE FI3L3 HARF1 ISSMMAJ' 

    #print(" AYA4 sans delimiter est correcte")             
     

def p_aya5(p):
    'aya5 : FI3L3 MAF3OLBIH1 ISSMMAWSOLE2 HARFNAFI FI3L4'
 
    #print(" AYA5 sans delimiter est correcte")           
    

def p_aya6(p):
    'aya6 : HARFRADR HARFTAWKID MAF3OLBIH1 LAM FI3L5'         
    
    #print("AYA 6 sans delimiter EST correcte")           
    p[0] = " ".join(p[1:]) 

def p_aya7(p):
    'aya7 : HARFMASSDR FI3L6 HAE FI3L7' 
    
    p[0] = " ".join(p[1:])
    #print("aya7 sans delimiter est correcte")           
    
def p_aya8(p):
    'aya8 : HARFTAWKID HARFJAR ISSM3 HARF2 ISSMMOAKHAR'

    #print(" aya8 sans delimiter est correcte")           
    p[0] = " ".join(p[1:])

def p_aya9(p):
    'aya9 : ALIF FI3L8 TAE ISSMMAWSOLE FI3L9 '

    #print(" AYA9 sans delimiter est correcte")           
    p[0] = " ".join(p[1:])

def p_aya10(p):
    'aya10 : MAF3OLBIH2 DARFZAMAN FI3L10' 
     
    #print("aya10 sans delimiter est correcte")           
    p[0] = " ".join(p[1:])

def p_aya11(p):
    'aya11 : ALIF FI3L8 TAE HARFTAWKID FI3LNAKISS HARFJAR2 ISSM4' 
    

    #print("aya11 sans delimiter est correcte")           
    p[0] = " ".join(p[1:])



def p_aya12(p):
    'aya12 : HARF3ATF FI3L11 HARF1 ISSM5'  
  
    #print(" aya 12 sans delimiter est correcte")           
    p[0] = " ".join(p[1:])

def p_aya13(p):
    'aya13 : ALIF FI3L8 TAE HARFTAWKID FI3L12 WAW FI3L13'
   
    #print("AYA13 sans delimiter est correcte")           
    p[0] = " ".join(p[1:])

def p_aya14(p):
    'aya14 : ALIF HARFNAFI FI3L4 HARF1 HARFMASSDR ISSMJALLALA FI3L14'
    
    #print("AYA14 sans delimiter est correcte")           
    p[0] = " ".join(p[1:])


def p_aya15(p):
    'aya15 : HARFRADR LAM HARFCHARTE HARFNAFI FI3L15 LAM FI3L16 HARF4 HARF1 ISSM6'
      
   
    #print("AYA15 sans delimiter est correcte")           
    p[0] = " ".join(p[1:]) 

def p_aya16(p):
    'aya16 : BADL SIFA SIFA2'
    
    #print("AYA16 sans delimiter est correcte")           
    p[0] = " ".join(p[1:]) 


def p_aya17(p):
    'aya17 : FAE LAM FI3L17 MAF3OLBIH3 HAE' 
      
    #print("AYA17 sans delimiter est correcte")           
    p[0] = " ".join(p[1:]) 


def p_aya18(p):
    'aya18 : SSIN FI3L18 MAF3OLBIH4 '
    
    #print("AYA18 sans delimiter est correcte")           
    p[0] = " ".join(p[1:])  

def p_aya19(p):
    'aya19 : HARFRADR HARFNAHI FI3L19 HAE WAW FI3L20 WAW FI3L21' 
     
    #print("AYA19 sans delimiter est correcte")           
    p[0] = " ".join(p[1:]) 
        
def p_error(p):
    global resultParser
    global positionParserError
    #print("Syntax error in input!")
    positionParserError = {
        "value":  p.value,
        "length": len(p.value),
        "ligne":  p.lineno,
        "index":  p.lexpos
    }
    print("positionParserError = ",positionParserError)
    resultParser = "incorrect"


data1=" اقرأ باسم ربك الذي خلق (1) خلق الإنسان من علق (2) اقرأ وربك الأكرم (3) الذي علم بالقلم (4) علم الإنسان ما لم يعلم (5) كلا إن الإنسان ليطغى (6) أن رآه استغنى (7) إن إلى ربك الرجعى (8) أرأيت الذي ينهى (9) عبدا إذا صلى (10) أرأيت إن كان على الهدى (11) أو أمر بالتقوى (12) أرأيت إن كذب وتولى (13) ألم يعلم بأن الله يرى (14) كلا لئن لم ينته لنسفعا بالناصية (15) ناصية كاذبة خاطئة (16) فليدع ناديه (17) سندع الزبانية (18) كلا لا تطعه واسجد واقترب (19) صدق الله العظيم"

data2= "خلق الإنسن من علق (2)"

data = " اقرأ باسم ربك الذي خلق (1) خلق الإنسان من علق (2) اقرأ وربك الأكرم (3) الذي علم بالقلم (4) علم الإنسان ما لم يعلم (5) كلا إن الإنسان ليطغى (6) أن رآه استغنى (7) إن إلى ربك الرجعى (8) أرأيت الذي ينهى (9) عبدا إذا صلى (10) أرأيت إن كان على الهدى (11) أو أمر بالتقوى (12) أرأيت إن كذب وتولى (13) ألم يعلم بأن الله يرى (14) كلا لئن لم ينته لنسفعا بالناصية (15) ناصية كاذبة خاطئة (16) "   
data5= " اقرأ باسم ربك الذي خلق (1) خلق الإنسان من علق (2) اقرأ وربك الأكرم (3) الذي علم بالقلم (4) علم الإنسان ما لم يعلم (5) كلا إن الإنسان ليطغى (6) أن رآه استغنى (7) إن إلى ربك الرجعى (8) أرأيت الذي ينهى (9) عبدا إذا صلى (10) أرأيت إن كان على الهدى (11) أو أمر بالتقوى (12) أرأيت إن كذب وتولى (13) ألم يعلم بأن الله يرى (14) كلا لئن لم ينته لنسفعا بالناصية (15) ناصية كاذبة خاطئة (16) فليدع ناديه (17) سندع الزبانية (18)"
data3= "اقرأ اسم ربك الذي خلق (9) خلق الإنسان من علق (2) "
data4=" اقرأ باسم ربك الذي خلق (1) خلق الإنسان من علق (2) اقرأ وربك الأكرم (3) الذي علم بالقلم (4)"
#(19) اقرأ باسم ربك الذي خلق (1) خلق الإنسان من علق (2) اقرأ وربك الأكرم (3) الذي علم بالقلم (4) علم الإنسان ما لم يعلم (5) كلا إن الإنسان ليطغى (6) أن رآه استغنى (7) إن إلى ربك الرجعى (8) أرأيت الذي ينهى (9) عبدا إذا صلى (10) أرأيت إن كان على الهدى (11) أو أمر بالتقوى (12) أرأيت إن كذب وتولى (13) ألم يعلم بأن الله يرى (14) كلا لئن لم ينته لنسفعا بالناصية (15) ناصية كاذبة خاطئة (16) فليدع ناديه (17) سندع الزبانية (18) كلا لا تطعه واسجد واقترب
#'''
#dataf aya19 juste
dataf="اقرأ باسم ربك الذي خلق (1) خلق الإنسان من علق (2) اقرأ وربك الأكرم (3) الذي علم بالقلم (4) علم الإنسان ما لم يعلم (5) كلا إن الإنسان ليطغى (6) أن رآه استغنى (7) إن إلى ربك الرجعى (8) أرأيت الذي ينهى (9) عبدا إذا صلى (10) أرأيت إن كان على الهدى (11) أو أمر بالتقوى (12) أرأيت إن كذب وتولى (13) ألم يعلم بأن الله يرى (14) كلا لئن لم ينته لنسفعا بالناصية (15) ناصية كاذبة خاطئة (16) فليدع ناديه (17) سندع الزبانية (18)كلا لا تطعه واسجد واقترب (19)"
dataf2="بسم الله الرحمن الرحيم اقرأ باسم ربك الذي خلق (1) خلق الإنسان من علق (2) اقرأ وربك الأكرم (3) الذي علم بالقلم (4) علم الإنسان ما لم يعلم (5) كلا إن الإنسان ليطغى (6) أن رآه استغنى (7) إن إلى ربك الرجعى (8) أرأيت الذي ينهى (9) عبدا إذا صلى (10) أرأيت إن كان على الهدى (11) أو أمر بالتقوى (12) أرأيت إن كذب وتولى (13) ألم يعلم بأن الله يرى (14) كلا لئن لم ينته لنسفعا بالناصية (15) ناصية كاذبة خاطئة (16) فليدع ناديه (1) سندع الزبانية (18)كلا لا تطعه واسجد واقترب (19) صدق الله العظيم"

#Analyse Lexique
#print("\n********************** Analyse lexical **********************\n")
lex.lex()
lex.input(data2)
#while 1:
#    tok = lex.token()
#    if not tok:
#        break
#    #print(tok)
#Analyse syntaxique
#print("\n********************** Analyse syntaxique **********************\n")
parser = yacc.yacc()
res = parser.parse(dataf)
#print(res)