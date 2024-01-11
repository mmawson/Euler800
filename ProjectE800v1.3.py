""" Project Euler Problem 800
An integer of the form p^q*q^p with prime numbers p not equal to q is called a hybrid-integer.
Let C(n) be the number of hybrid-integers less than or equal to n.
What is C(800800^800800)?

This program searches through a two arrays of prime numbers using binary search to find C(800800^800800)
Results are written in a .csv file (800800Result.csv)
Sum the second column of the csv to get the answer
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
import time
from multiprocessing import Process

upper = 800800 ** 800800

def solveC(procNum, data_array1, data_array2):
     # Start with p = 2 and find q for which p^q*q^p is just less than 800800^800800
  for i in range(0, len(data_array1)):
    if data_array1[i] > 420331:  # We know the largest value of p (variable i) is when x^2x = 800800^800800.  So i can never be more than 420331  
      break
    else:
      data_array2.pop(0)
    # This line advances data_array2 so that p < q since p and q cannot be equal
    #  The folowing 5 lines set up the search space.  It gets smaller every iteration
    low = 0
    if i == 0:
      high = len(data_array2)-1
    else:
      high = mid
    # Perform binary search on high - low
    while low <= high:
      mid = (high + low) // 2
      # The following statement finds the maximum q for a given p which satisfies q^p*p^2 <= 800800^800800.  
      if ((pow(data_array2[mid], data_array1[i]) * pow(data_array1[i], data_array2[mid])) <= upper) and ((pow(data_array2[mid+1], data_array1[i]) * pow(data_array1[i], data_array2[mid+1])) > upper):
        # It follows that all primes less than q will also satisfiy the inequality, so we count them and save them to file.
        print(f'Found an answer for all primes, q for which {data_array1[i]}^q * q^{data_array1[i]} <= 800800^800800\nmax q = {data_array2[mid+1]}\nThere are {(mid+1)} primes less than or equal to {data_array2[mid+1]}')
        table = open("800800Result" + str(procNum) +".csv", "a")
        table.writelines("{0}:{1}\n".format(data_array1[i], mid+1))
        table.close()
        data_array2.pop(0)
        data_array2.pop(0)
        data_array2.pop(0)
        break
      if ((pow(data_array2[mid], data_array1[i]) * pow(data_array1[i], data_array2[mid])) > upper):
        # if (p^q*q^p > upper) then drop the top half
        # print("Doing binary serach: " +str(mid))
        high = mid - 1
      else:
        # if (p^q*q^p > upper) then drop the bottom half
        # print("Doing binary serach: " +str(mid))
        low = mid +1
  return
   

if __name__ == '__main__':
    
  begin_time = time.time()

#    with open('/home/matt/Programming/Euler800/Primes-beta.csv', 'r') as f:  Use this file for solving C(800^800) for which we know the answer is 10790 
  
  # This block opens the file PrimesUltra which contains 1013281 primes which is just enough q for 2^q*q^2 > 800800^800800  
  with open('/home/matt/Programming/Euler800/PrimesUltra.csv', 'r') as f:
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

  filenames = ['800800Result1.csv', '800800Result2.csv', '800800Result3.csv', '800800Result4.csv']
  with open('800800Result', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

  print("Total runtime --- %s seconds ---" % (time.time() - begin_time))

'''
  # Start with p = 2 and find q for which p^q*q^p is just less than 800800^800800
  for i in range(0, len(data_array1)):
        loop_time = time.time()   # start a timer
        if data_array1[i] > 420331:  # We know the largest value of p (variable i) is when x^2x = 800800^800800.  So i can never be more than 420331  
          break
        else:
          data_array2.pop(0)  # This line advances data_array2 so that p < q since p and q cannot be equal
        #  The folowing 5 lines set up the search space.  It gets smaller every iteration
        low = 0
        if i == 0:
           high = len(data_array2)-1
        else:
          high = mid
        # Perform binary search on high - low
        while low <= high:
          mid = (high + low) // 2
          # The following statement finds the maximum q for a given p which satisfies q^p*p^2 <= 800800^800800.  
          if ((pow(data_array2[mid], data_array1[i]) * pow(data_array1[i], data_array2[mid])) <= upper) and ((pow(data_array2[mid+1], data_array1[i]) * pow(data_array1[i], data_array2[mid+1])) > upper):
            # It follows that all primes less than q will also satisfiy the inequality, so we count them and save them to file.
            print(f'Found an answer for all primes, q for which {data_array1[i]}^q * q^{data_array1[i]} <= 800800^800800\nmax q = {data_array2[mid+1]}\nThere are {(mid+1)} primes less than or equal to {data_array2[mid+1]}')
            #print("Writing a value --- %s seconds ---" % (time.time() - loop_time))
            table = open("800800Result.csv", "a")
            table.writelines("{0}:{1}\n".format(data_array1[i], mid+1))
            table.close()
            break
          if ((pow(data_array2[mid], data_array1[i]) * pow(data_array1[i], data_array2[mid])) > upper):
            # if (p^q*q^p > upper) then drop the top half
            # print("Doing binary serach: " +str(mid))
            high = mid - 1
          else:
            # if (p^q*q^p > upper) then drop the bottom half
            # print("Doing binary serach: " +str(mid))
            low = mid +1
'''