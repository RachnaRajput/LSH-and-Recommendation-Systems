import json
import sys
import numpy.matrixlib
from numpy.matrixlib.defmatrix import matrix
# import Rachna_Rajput_Recommendations



def lsh_algo(json_data):  #loading josn file
 list_array = json_data
 len_listarray = len(list_array)
 #making the characteristic matrix
 columns = len_listarray + 20
 rows = 100
 user_list_unicode = [None]*len_listarray
 # print user_list
 for list1 in list_array:
      for user_count in range(len_listarray):
        if user_list_unicode[user_count]== None:
         user_list_unicode[user_count] = list1[0]        # saving the user's name
         break
 user_list = []
 user_list = [x.encode('utf-8')for x in user_list_unicode]
 # print user_list


 A = matrix( [[0 for x in range(columns)] for x in range(rows)])
 count = 0
 for i in list_array:
     for j in range(0,len(i[1])):
       A[i[1][j],count] = 1      #update the characteristic matrix
     count += 1
 for x in range (rows):
         i = 1;
         j = len_listarray
         while (i<21):
              hashfun = (3*x+i)%100
              while(j<columns):
                   A[x,j]= hashfun
                   j = j+1
                   break
              i =i + 1
         # print "matrix:",x," ",A[x]

#making of signature matrix
 col = len_listarray
 rowsize = 20
 sign = matrix( [[None for x in range(col)] for x in range(rowsize)])
 # print sign
 p = 0
 q = 0
 # print A
 for m in range (rows):
     for n in range (len_listarray):
       # print A[m,n]
       if A[m,n] == 1:
                for p in range(rowsize):
                    if(sign[p,n]== None):
                        sign[p,n] = A[m,len_listarray+p]
                    if( sign[p,n]> A[m,len_listarray+p]):
                        sign[p,n] = A[m,len_listarray+p]

 # print sign      #-------------------> print signature matrix.
 final_output_list = []

 #Forming 5 bands. 4rows/band
 col_size = len_listarray
 rows_size = 4
 bandmatrix1 = matrix( [[None for x in range(col_size)] for x in range(rows_size)])
 bandmatrix2 = matrix( [[None for x in range(col_size)] for x in range(rows_size)])
 bandmatrix3 = matrix( [[None for x in range(col_size)] for x in range(rows_size)])
 bandmatrix4 = matrix( [[None for x in range(col_size)] for x in range(rows_size)])
 bandmatrix5 = matrix( [[None for x in range(col_size)] for x in range(rows_size)])
 band_no = 1
 k = 0
 a = 0
 b = 0
 c = 0
 d = 0
 for j in range(0,len(sign)):
     if j>=0 and j<4:
       bandmatrix1[k] = sign[j]
       k = k+1
  # print bandmatrix1
     if j>=4 and j<8:
       bandmatrix2[a] = sign[j]
       a = a+1
     if j>=8 and j<12:
       bandmatrix3[b] = sign[j]
       b = b+1
     if j>=12 and j<16:
         bandmatrix4[c] = sign[j]
         c = c+1
     if j>=16 and j<20:
        bandmatrix5[d] = sign[j]
        d = d+1
 # print bandmatrix1
 # print bandmatrix2
 # print bandmatrix3
 # print bandmatrix4
 # print bandmatrix5

 output_list = []
 r=0
 # for r in range (len(bandmatrix1)):
 for c in range (0,len_listarray):
     for z in range (c+1,len_listarray):
       if bandmatrix1[r,c] == bandmatrix1[r,z] and bandmatrix1[r+1,c] == bandmatrix1[r+1,z] and bandmatrix1[r+2,c] == bandmatrix1[r+2,z] and bandmatrix1[r+3,c] == bandmatrix1[r+3,z]:
         output_list = []
         # print "bandmatrix1[r,c]: ",bandmatrix1[r,c]
         # print "bandmatrix1[r,z]: ",bandmatrix1[r,z]
         output_list.append(user_list[c])
         output_list.append(user_list[z])
         output_list.sort()
         final_output_list.append(output_list)
         # print output_list
 temp_name = set()
 final_output_list_set = set(map(tuple,final_output_list))
 final_output_list_set = map(list,final_output_list_set)
 for element in range (len(final_output_list_set)):
     # print"*******************", final_output_list_set[element]
     temp_name.add(final_output_list_set[element][0])
     temp_name.add(final_output_list_set[element][1])
 # print temp_name
 s = temp_name
 # print len(final_output_list_set)

 w=0
 for c1 in range (0,len_listarray):
     for z1 in range (c1+1,len_listarray):
         if user_list[c1]!= s or user_list[z1]!=s:
              # print user_list[c1]
              # print user_list[z1]
              if bandmatrix2[w,c1] == bandmatrix2[w,z1] and bandmatrix2[w+1,c1] == bandmatrix2[w+1,z1] and bandmatrix2[w+2,c1] == bandmatrix2[w+2,z1] and bandmatrix2[w+3,c1] == bandmatrix2[w+3,z1]:
                 output_list = []
                 output_list.append(user_list[c1])
                 output_list.append(user_list[z1])
                 output_list.sort()
                 final_output_list.append(output_list)

 temp_name = set()
 final_output_list_set = set(map(tuple,final_output_list))
 final_output_list_set = map(list,final_output_list_set)
 for element in range (len(final_output_list_set)):
     # print final_output_list_set[element]
     # print len(final_output_list_set)
     temp_name.add(final_output_list_set[element][0])
     temp_name.add(final_output_list_set[element][1])
     # print temp_name
 s = temp_name
     # print s
 # print len(final_output_list_set)
 h=0
 for c2 in range (0,len_listarray):
         for z2 in range (c2+1,len_listarray):
             if user_list[c2]!= s or user_list[z2]!=s:
                  # print user_list[c2]
                  # print user_list[z2]
                  if bandmatrix3[h,c2] == bandmatrix3[h,z2] and bandmatrix3[h+1,c2] == bandmatrix3[h+1,z2] and bandmatrix3[h+2,c2] == bandmatrix3[h+2,z2] and bandmatrix3[h+3,c2] == bandmatrix3[h+3,z2]:
                     output_list = []
                     output_list.append(user_list[c2])
                     output_list.append(user_list[z2])
                     output_list.sort()
                     final_output_list.append(output_list)

 temp_name = set()
 final_output_list_set = set(map(tuple,final_output_list))
 final_output_list_set = map(list,final_output_list_set)
 for element in range (len(final_output_list_set)):
     # print final_output_list_set[element]
     temp_name.add(final_output_list_set[element][0])
     temp_name.add(final_output_list_set[element][1])
     # print temp_name
 s = temp_name
     # print s
 # print len(final_output_list_set)

 p=0
 for c3 in range (0,len_listarray):
         for z3 in range (c3+1,len_listarray):
             if user_list[c3]!= s or user_list[z3]!=s:
                  # print user_list[c2]
                  # print user_list[z2]
                  if bandmatrix4[p,c3] == bandmatrix4[p,z3] and bandmatrix4[p+1,c3] == bandmatrix4[p+1,z3] and bandmatrix4[p+2,c3] == bandmatrix4[p+2,z3] and bandmatrix4[p+3,c3] == bandmatrix4[p+3,z3]:
                     output_list = []
                     output_list.append(user_list[c3])
                     output_list.append(user_list[z3])
                     output_list.sort()
                     final_output_list.append(output_list)

 temp_name = set()
 final_output_list_set = set(map(tuple,final_output_list))
 final_output_list_set = map(list,final_output_list_set)
 for element in range (len(final_output_list_set)):
     # print final_output_list_set[element]
     temp_name.add(final_output_list_set[element][0])
     temp_name.add(final_output_list_set[element][1])
     # print temp_name
 s = temp_name
 # print len(final_output_list_set)


 t=0
 for c4 in range (0,len_listarray):
         for z4 in range (c4+1,len_listarray):
             if user_list[c4]!= s or user_list[z4]!=s:
                  # print user_list[c2]
                  # print user_list[z2]
                  if bandmatrix5[t,c4] == bandmatrix5[t,z4] and bandmatrix5[t+1,c4] == bandmatrix5[t+1,z4] and bandmatrix5[t+2,c4] == bandmatrix5[t+2,z4] and bandmatrix5[t+3,c4] == bandmatrix5[t+3,z4]:
                     output_list = []
                     output_list.append(user_list[c4])
                     output_list.append(user_list[z4])
                     output_list.sort()
                     final_output_list.append(output_list)

 temp_name = set()
 final_output_list_set = set(map(tuple,final_output_list))
 final_output_list_set = map(list,final_output_list_set)
 # if checker == True:
 for element in range (len(final_output_list_set)):
     # if checker == True:
      print final_output_list_set[element]
     # print len(final_output_list_set)
 listing = []
 listing = final_output_list_set
 # if checker!=True:
 # Rachna_Rajput_Recommendations.recomm_algo(json_data,listing)


if __name__ == '__main__':
    data = []
    with open(sys.argv[1]) as json_file: #Accessing the json data.
      for line in json_file:
          data.append(json.loads(line))

    lsh_algo(data)
