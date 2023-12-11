""" Project Euler Problem 800
An integer of the form p^q*q^p with prime numbers p not equal to q is called a hybrid-integer.
Let C(n) be the number of hybrid-integers less than or equal to n.
What is C(800^800)?
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Thu Dec  7 11:07:31 2023


                                                                    ..;===+.
                                                                .:=iiiiii=+=
                                                             .=i))=;::+)i=+,
                                                          ,=i);)I)))I):=i=;
                                                       .=i==))))ii)))I:i++
                                                     +)+))iiiiiiii))I=i+:'
                                .,:;;++++++;:,.       )iii+:::;iii))+i='
                             .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'
                           ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:
                         ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+
                        ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,
                      ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+
                     ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='
                    ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`
                    =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'
                   +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,
                   =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;
                  .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;
                  :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:
                  :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=
                  .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+
                  =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'
                +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;
              +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;
             =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;
           +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,
         :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+'
       .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+
      ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'
     +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'
   .+=:))iiiiiiii)))+ii;
  .+=;))iiiiii)));ii+
 .+=i:)))))))=+ii+
.;==i+::::=)i=;
,+==iiiiii+,
`+=+++;`


@author: mattmawson matt.mawson@alum.mit.edu
"""

import csv
import numpy as np
import time
from multiprocessing import Process

upper = 800800 ** 800800

def solveC(i, data_array1, data_array2):
    
    table = open("800800Grail"+str(i)+".csv", "a")

    for i in range(0, len(data_array1)):
        data_array2.pop(0)
        for j in range(len(data_array2)-1,-1,-1):
            if ((pow(data_array2[j],data_array1[i])*pow(data_array1[i],data_array2[j])) > upper):
                continue
                #totalCount += 1
            elif ((pow(data_array2[j],data_array1[i])*pow(data_array1[i],data_array2[j])) <= upper):
                table.writelines("{0}:{1}\n".format(data_array1[i],j+1))
                data_array2.pop(0)
                data_array2.pop(0)
                data_array2.pop(0)
                break
    table.close()
    return

if __name__ == '__main__':
    
    start_time = time.time()
    
    """ Split up the array of primes here """
    
#    with open('/Users/mattmawson/Desktop/Euler800/Primes-beta.csv', 'r') as f: 
    with open('/Users/mattmawson/Desktop/Euler800/PrimesUltra.csv', 'r') as f: 
        reader = csv.reader(f)
        data = list(reader)
        data = [eval(i) for i in data[0]]
        data_array1 = data.copy()
        data_array2 = data.copy()
    
    p = Process(target=solveC, args=(1, data_array1[0::4], data_array2,))
    q = Process(target=solveC, args=(2, data_array1[1::4], data_array2[1::],))
    r = Process(target=solveC, args=(3, data_array1[2::4], data_array2[2::],))
    s = Process(target=solveC, args=(4, data_array1[3::4], data_array2[3::],))
    p.start()
    q.start()
    r.start()
    s.start()
    p.join()
    q.join()
    r.join()
    s.join()

    print("--- %s seconds ---" % (time.time() - start_time))