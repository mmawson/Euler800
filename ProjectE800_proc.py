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
from multiprocessing import Process, Lock


totalCount = 0
upper = 800 ** 800

def solveC(l, i, data_array1, data_array2):
    
    table = open("800800Test.csv", "a")
    iCount = 1;

    for i in range(0, len(data_array1)):
        if iCount == 0:
            break
        iCount = 0
        data_array2.pop(0)
        for j in range(0, len(data_array2)):
            if ((pow(data_array2[j],data_array1[i])*pow(data_array1[i],data_array2[j])) <= upper):
                iCount += 1
                #totalCount += 1
            elif ((pow(data_array2[j],data_array1[i])*pow(data_array1[i],data_array2[j])) > upper):
                break
        table.writelines("{0}:{1}\n".format(data_array1[i],iCount))

    #table.writelines("Total: {0}".format(totalCount)) 
    #print("")
    table.close()
    return iCount

if __name__ == '__main__':
    
    start_time = time.time()
    
    """ Split up the array of primes here """
    
    with open('/Users/mattmawson/Desktop/Euler800/Primes-beta.csv', 'r') as f: 
        reader = csv.reader(f)
        data = list(reader)
        data = [eval(i) for i in data[0]]
    #    data_array = np.array(data, dtype=object)
        data_array1 = data.copy()
        data_array2 = data.copy()
    
    print(data_array1[6])
    
    
    
    lock = Lock()
    p = Process(target=solveC, args=(lock, 0, data_array1, data_array2,))
    #q = Process(target=solveC, args=(lock, 1, [3], [5,7,11],))
    p.start()
    #q.start()
    print(p.join())
    #q.join()

    #print(data)

    print("--- %s seconds ---" % (time.time() - start_time))

"""

totalCount = 0
iCount = 1
upper = 800800 ** 800800


start_time = time.time()

with open('/Users/mattmawson/Desktop/Euler800/PrimesUltra.csv', 'r') as f: 
    reader = csv.reader(f)
    data = list(reader)
    data = [eval(i) for i in data[0]]
#    data_array = np.array(data, dtype=object)
    data_array1 = data.copy()
    data_array2 = data.copy()

table = open("800800Result.csv", "a")

for i in range(0, len(data_array1)):
    if iCount == 0:
        break
    iCount = 0
    data_array2.pop(0)
    for j in range(0, len(data_array2)):
        if ((pow(data_array2[j],data_array1[i])*pow(data_array1[i],data_array2[j])) <= upper):
            iCount += 1
            totalCount += 1
        elif ((pow(data_array2[j],data_array1[i])*pow(data_array1[i],data_array2[j])) > upper):
            break
    table.writelines("{0}:{1}\n".format(data_array1[i],iCount))

table.writelines("Total: {0}".format(totalCount)) 
print(totalCount)
print("--- %s seconds ---" % (time.time() - start_time))

table.close()

#print(upper)
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    line_count = 0
#    for row in csv_reader:
#        print(row[1])
#        print("Next number")
#        if line_count == 0:
#            print(f'Column names are {", ".join(row)}')
#            line_count += 1
#        else:
#            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#            line_count += 1
#    print(f'Processed {line_count} lines.')
"""