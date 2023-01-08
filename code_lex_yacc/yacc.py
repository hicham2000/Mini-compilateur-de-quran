import ply.yacc as yacc
from pyarabic import *

from lex import tokens
import re
global resultParser;global positionParserError

positionLexerError,positionParserError = dict(),dict()






#def p_fi3l1(p):
 #   'fi3l1 : FI3L1'
  #  p[0] = p[1]

  

#def p_harf1(p):
 #   'harf1 : HARF1'
  #  p[0] = p[1]

#def p_issm1(p):
 #   'issm1 : ISSM1'
  #  p[0] = p[1]  


#def p_modafilaih1(p):
 #   'modafilaih1 : MODAFILAIH1'
  #  p[0]=p[1]

#def p_harf2(p):
 #   'harf2 : HARF2'
  #  p[0] = p[1] 

#def p_issmmawsole(p):
 #   'issmmawsole : ISSMMAWSOLE'
  #  p[0]=p[1]

#def p_fi3l2(p):
    #'fi3l2 : FI3L2'
   # p[0] = p[1]    

#def p_JOUMLA(p):
 # '''AYA : FI3L1 HARF1 ISSM1 ISSM3 HARF2 ISSMMAWSOLE FI3L2 DELIMITER FI3L2 MAF3OLBIH1 HARF3 ISSM2 DELIMITER FI3L1 WAW ISSM3 HARF2 KHABAR1 DELIMITER ISSMMAWSOLE FI3L3 HARF1 ISSMMAJ DELIMITER FI3L3 MAF3OLBIH1 ISSMMAWSOLE2 HARFNAFI FI3L4 DELIMITER HARFRADR HARFTAWKID MAF3OLBIH1 LAM FI3L5 DELIMITER HARFMASSDR FI3L6 HAE FI3L7 DELIMITER HARFTAWKID HARFJAR ISSM3 HARF2 ISSMMOAKHAR DELIMITER ALIF FI3L8 TAE ISSMMAWSOLE FI3L9 DELIMITER MAF3OLBIH2 DARFZAMAN FI3L10 DELIMITER ALIF FI3L8 TAE HARFTAWKID FI3LNAKISS HARFJAR2 ISSM4 DELIMITER HARF3ATF FI3L11 HARF1 ISSM5 DELIMITER ALIF FI3L8 TAE HARFTAWKID FI3L12 WAW FI3L13 DELIMITER ALIF HARFNAFI FI3L4 HARF1 HARFMASSDR ISSMJALLALA FI3L14 DELIMITER HARFRADR LAM HARFCHARTE HARFNAFI FI3L15 LAM FI3L16 HARF4 HARF1 ISSM6 DELIMITER BADL SIFA SIFA2 DELIMITER FAE LAM FI3L17 MAF3OLBIH2 HAE DELIMITER SSIN FI3L18 MAF3OLBIH4 DELIMITER HARFRADR HARFNAHI FI3L19 HAE WAW FI3L20 WAW FI3L21 DELIMITER
  #       | FI3L1 HARF1 ISSM1 ISSM3 HARF2 ISSMMAWSOLE FI3L2 
   #      | FI3L2 MAF3OLBIH1 HARF3 ISSM2
    #     | FI3L1 WAW ISSM3 HARF2 KHABAR1
     #    | ISSMMAWSOLE FI3L3 HARF1 ISSMMAJ
      #   | FI3L3 MAF3OLBIH1 ISSMMAWSOLE2 HARFNAFI FI3L4
      #   | HARFRADR HARFTAWKID MAF3OLBIH1 LAM FI3L5
      #   | HARFMASSDR FI3L6 HAE FI3L7
      #   | HARFTAWKID HARFJAR ISSM3 HARF2 ISSMMOAKHAR
      #   | ALIF FI3L8 TAE ISSMMAWSOLE FI3L9
      #   | MAF3OLBIH2 DARFZAMAN FI3L10
      #   | ALIF FI3L8 TAE HARFTAWKID FI3LNAKISS HARFJAR2 ISSM4
      #   | HARF3ATF FI3L11 HARF1 ISSM5
      #   | ALIF FI3L8 TAE HARFTAWKID FI3L12 WAW FI3L13
      #   | ALIF HARFNAFI FI3L4 HARF1 HARFMASSDR ISSMJALLALA FI3L14
       #  | HARFRADR LAM HARFCHARTE HARFNAFI FI3L15 LAM FI3L16 HARF4 HARF1 ISSM6
      #   | BADL SIFA SIFA2
      #   | FAE LAM FI3L17 MAF3OLBIH2 HAE
      #   | SSIN FI3L18 MAF3OLBIH4
      #   | HARFRADR HARFNAHI FI3L19 HAE WAW FI3L20 WAW FI3L21
       #  '''
 
 # print('correctii')

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
    print("basmala est correcte")


def p_nihayasora(p):
    'nihaya : SSADAQA ISSMJALLALA ADIM'
    p[0] = " ".join(p[1:])
    print("khitama sorat est correcte")    

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
            print('AYA1 est correcte avec delimiter')
      else:
              print('erreur au niveau du delimiter de aya1,il faut mettre le delimiter 1') 

def p_verset2(p):
      'verset2 : aya2 DELIMITER '
      if(p[2]=='(2)'): 
            print('AYA2 est correcte avec delimiter')
            #print(p[1])
      else:
              print('erreur au niveau du delimiter de aya2,il faut mettre le delimiter 2') 

def p_verset3(p):
      'verset3 : aya3 DELIMITER '
      if(p[2]=='(3)'): 
            print('AYA3 est correcte avec delimiter')
      else:
              print('erreur au niveau du delimiter de aya3,il faut mettre le delimiter 3') 

def p_verset4(p):
      'verset4 : aya4 DELIMITER '
      if(p[2]=='(4)'): 
            print('AYA4 est correcte avec delimiter')
      else:
              print('erreur au niveau du delimiter de aya4,il faut mettre le delimiter 4') 


def p_verset5(p):
      'verset5 : aya5 DELIMITER '
      if(p[2]=='(5)'): 
            print('AYA5 est correcte avec delimiter')
      else:
              print('erreur au niveau du delimiter de aya5,il faut mettre le delimiter 5') 


def p_verset6(p):
      'verset6 : aya6 DELIMITER '
      if(p[2]=='(6)'): 
            print('AYA6 est correcte avec delimiter')
      else:
              print('erreur au niveau du delimiter de aya6,il faut mettre le delimiter 6')

def p_verset7(p):
      'verset7 : aya7 DELIMITER '
      if(p[2]=='(7)'): 
            print('AYA7 est correcte avec delimiter')
      else:
              print('erreur au niveau du delimiter de aya7,il faut mettre le delimiter 7') 


def p_verset8(p):
      'verset8 : aya8 DELIMITER '
      if(p[2]=='(8)'): 
            print('AYA8 est correcte avec delimiter')
      else:
              print('erreur au niveau du delimiter de aya8,il faut mettre le delimiter 8') 


def p_verset9(p):
      'verset9 : aya9 DELIMITER '
      if(p[2]=='(9)'): 
            print('AYA9 est correcte avec delimiter')
      else:
              print('erreur au niveau du delimiter de aya9,il faut mettre le delimiter 9') 


def p_verset10(p):
      'verset10 : aya10 DELIMITER '
      if(p[2]=='(10)'): 
            print('AYA10 est correcte avec delimiter')
      else:
              print('erreur au niveau du delimiter de aya10,il faut mettre le delimiter 10')                             


def p_verset11(p):
      'verset11 : aya11 DELIMITER '
      if(p[2]=='(11)'): 
            print('AYA11 est correcte avec delimiter')
      else:
              print('erreur au niveau du delimiter de aya11,il faut mettre le delimiter 11') 

def p_verset12(p):
      'verset12 : aya12 DELIMITER '
      if(p[2]=='(12)'): 
            print('AYA12 est correcte avec delimiter')
      else:
              print('erreur au niveau du delimiter de aya12,il faut mettre le delimiter 12') 

def p_verset13(p):
      'verset13 : aya13 DELIMITER '
      if(p[2]=='(13)'): 
            print('AYA13 est correcte avec delimiter')
      else:
              print('erreur au niveau du delimiter de aya13,il faut mettre le delimiter 13')



def p_verset14(p):
      'verset14 : aya14 DELIMITER '
      if(p[2]=='(14)'): 
            print('AYA14 est correcte avec delimiter')
      else:
              print('erreur au niveau du delimiter de aya14,il faut mettre le delimiter 14')                              



def p_verset15(p):
      'verset15 : aya15 DELIMITER '
      if(p[2]=='(15)'): 
            print('AYA15 est correcte avec delimiter')
      else:
              print('erreur au niveau du delimiter de aya15,il faut mettre le delimiter 15') 


def p_verset16(p):
      'verset16 : aya16 DELIMITER '
      if(p[2]=='(16)'): 
            print('AYA16 est correcte avec delimiter')
      else:
              print('erreur au niveau du delimiter de aya16,il faut mettre le delimiter 16') 


def p_verset17(p):
      'verset17 : aya17 DELIMITER '
      if(p[2]=='(17)'): 
            print('AYA17 est correcte avec delimiter')
      else:
              print('erreur au niveau du delimiter de aya17,il faut mettre le delimiter 17') 

def p_verset18(p):
      'verset18 : aya18 DELIMITER '
      if(p[2]=='(18)'): 
            print('AYA18 est correcte avec delimiter')
      else:
              print('erreur au niveau du delimiter de aya18,il faut mettre le delimiter 18') 


def p_verset19(p):
      'verset19 : aya19 DELIMITER '
      if(p[2]=='(19)'): 
            print('AYA19 est correcte avec delimiter')
      else:
              print('erreur au niveau du delimiter de aya19,il faut mettre le delimiter 19') 




def p_aya1(p):
    'aya1 : FI3L1 HARF1 ISSM1 ISSM3 HARF2 ISSMMAWSOLE FI3L2'
       
    print("AYA 1 sans delimiter est correcte")
   
  
def p_aya2(p):
    'aya2 : FI3L2 MAF3OLBIH1 HARF3 ISSM2'

    print("AYA 2 sans delimiter est correcte")


         

    
def p_aya3(p):
    'aya3 : FI3L1 WAW ISSM3 HARF2 KHABAR1'
          
         

    print(" AYA 3 sans delimiter est correcte")
    


def p_aya4(p):
    'aya4 : ISSMMAWSOLE FI3L3 HARF1 ISSMMAJ' 

    print(" AYA4 sans delimiter est correcte")             
     

def p_aya5(p):
    'aya5 : FI3L3 MAF3OLBIH1 ISSMMAWSOLE2 HARFNAFI FI3L4'
 
    print(" AYA5 sans delimiter est correcte")           
    

def p_aya6(p):
    'aya6 : HARFRADR HARFTAWKID MAF3OLBIH1 LAM FI3L5'         
    
    print("AYA 6 sans delimiter EST correcte")           
    p[0] = " ".join(p[1:]) 

def p_aya7(p):
    'aya7 : HARFMASSDR FI3L6 HAE FI3L7' 
    
    p[0] = " ".join(p[1:])
    print("aya7 sans delimiter est correcte")           
    
def p_aya8(p):
    'aya8 : HARFTAWKID HARFJAR ISSM3 HARF2 ISSMMOAKHAR'

    print(" aya8 sans delimiter est correcte")           
    p[0] = " ".join(p[1:])

def p_aya9(p):
    'aya9 : ALIF FI3L8 TAE ISSMMAWSOLE FI3L9 '

    print(" AYA9 sans delimiter est correcte")           
    p[0] = " ".join(p[1:])

def p_aya10(p):
    'aya10 : MAF3OLBIH2 DARFZAMAN FI3L10' 
     
    print("aya10 sans delimiter est correcte")           
    p[0] = " ".join(p[1:])

def p_aya11(p):
    'aya11 : ALIF FI3L8 TAE HARFTAWKID FI3LNAKISS HARFJAR2 ISSM4' 
    

    print("aya11 sans delimiter est correcte")           
    p[0] = " ".join(p[1:])



def p_aya12(p):
    'aya12 : HARF3ATF FI3L11 HARF1 ISSM5'  
  
    print(" aya 12 sans delimiter est correcte")           
    p[0] = " ".join(p[1:])

def p_aya13(p):
    'aya13 : ALIF FI3L8 TAE HARFTAWKID FI3L12 WAW FI3L13'
   
    print("AYA13 sans delimiter est correcte")           
    p[0] = " ".join(p[1:])

def p_aya14(p):
    'aya14 : ALIF HARFNAFI FI3L4 HARF1 HARFMASSDR ISSMJALLALA FI3L14'
    
    print("AYA14 sans delimiter est correcte")           
    p[0] = " ".join(p[1:])


def p_aya15(p):
    'aya15 : HARFRADR LAM HARFCHARTE HARFNAFI FI3L15 LAM FI3L16 HARF4 HARF1 ISSM6'
      
   
    print("AYA15 sans delimiter est correcte")           
    p[0] = " ".join(p[1:]) 

def p_aya16(p):
    'aya16 : BADL SIFA SIFA2'
    
    print("AYA16 sans delimiter est correcte")           
    p[0] = " ".join(p[1:]) 


def p_aya17(p):
    'aya17 : FAE LAM FI3L17 MAF3OLBIH3 HAE' 
      
    print("AYA17 sans delimiter est correcte")           
    p[0] = " ".join(p[1:]) 


def p_aya18(p):
    'aya18 : SSIN FI3L18 MAF3OLBIH4 '
    
    print("AYA18 sans delimiter est correcte")           
    p[0] = " ".join(p[1:])  

def p_aya19(p):
    'aya19 : HARFRADR HARFNAHI FI3L19 HAE WAW FI3L20 WAW FI3L21' 
     
    print("AYA19 sans delimiter est correcte")           
    p[0] = " ".join(p[1:]) 


#def p_AYAK(P):
 #   'aya : aya DELIMITER aya'
  #  print('correct')



def p_error(p):
    global resultParser
    global positionParserError
    #print("Syntax error in input!")
    positionParserError = {
         "ligne":p.lineno,
         "index":p.lexpos,
         "value":p.value,
        "length":len(p.value)
    }
    print("positionParserError = ",positionParserError)
    resultParser = "incorrect"
    

parser = yacc.yacc()

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
res = parser.parse(dataf) 
#print(data3)
#print(data1)


#parser = yacc.yacc()
#yacc.yacc()
#path = '.\program.txt'
#file = open(path, 'rb')
#file_handle = open(path,"r")
# file contents is the code written in your program
#data = file.read()
#text=data.decode('utf-8')
#res = parser.parse(text) 
#data = file.readlines()