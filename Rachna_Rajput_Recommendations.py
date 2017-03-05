import json
import sys




def recomm_algo(json_data,listout):  #loading josn files
 list_array = json_data
 len_listarray = len(list_array)


 result1 = (set(x for l in listout for x in l))      #finding the set of the names from the LSH output
 newlist = []
 for list0 in list_array:
     for i in range (len(result1)):
          if list0[0]==list(result1)[i]:
            newlist.append(list0)



 datalist = []                                                       #finding Jaccard Similarity of the complete data.
 for i in range (len(newlist)):
     for j in range (i+1,len(newlist)):
      intersection_set = set(newlist[i][1]).intersection(newlist[j][1])
      len_intersection_set = len(intersection_set)
      union_set = set(newlist[i][1]).union(newlist[j][1])
      len_union_set = len(union_set)
      jaccard_sim =len_intersection_set/float(len_union_set)
      if jaccard_sim!=0:
       answerlist = [[newlist[i][0],newlist[j][0]],jaccard_sim]
       datalist.append(answerlist)


 jac = []                                                        #extracting the jaccard similarity of the data which is in the output json file.
 for input in listout:
     for input1 in datalist:
         if input[0] in input1[0] and input[1] in input1[0]:
             list1 = []
             list1.append(input[0])
             list1.append(input[1])
             list1.append (input1[1])
             jac.append(list1)


 biglist = []                                              #forming a biglist which contains pairs and thier jaccard similarity

 for innerlist in newlist:
     wholelist = []
     innerdatalist=[]
     for inlist in jac:
         list22 = inlist[0]
         data = inlist[1]
         if innerlist[0]==inlist[0] or innerlist[0]==inlist[1]:
             inneranswerlist = []
             if innerlist[0]==inlist[0]:
               inneranswerlist = [inlist[1],inlist[2]]
             if innerlist[0]==inlist[1]:
                 inneranswerlist = [inlist[0],inlist[2]]
             innerdatalist.append(inneranswerlist)
     innerdatalist.sort(key=lambda x:x[1], reverse=True)
     wholelist.append(innerlist[0])
     wholelist.append(innerdatalist)
     biglist.append(wholelist)

 hugepeoplelist = []                                       #making a hugepeople list to store top 5 people
 for insidebiglist in biglist:
       peoplelist = []
       i=1
       jac_val = 0
       for insiderlist in insidebiglist[1]:
           if i > 5:
               list50 = []
               list2 = []
               list2 = insiderlist[1]
               if list2== jac_val:
                list50.append(insiderlist[0])
                list50.append(list2)
                peoplelist.append(list50)
           else:
                 list51 = []
                 list51.append(insiderlist[0])
                 list51.append(insiderlist[1])
                 peoplelist.append(list51)
                 i=i+1
                 jac_val = insiderlist[1]
       hugepeoplelist.append(peoplelist)



#__________________get the  movie for the Rachel____________________________
 combinemovielist = []
 for alist in hugepeoplelist:
     l1=[]
     for blist in alist:
         for clist in newlist:
             if blist[0] in clist[0]:
               l1.append(clist[1])
               break
     combinemovielist.append(l1)


 Globallist = []                              #having only those movies which are seen by 3 or more than 3 users.
 for peoplecount in range (len(listout)):
    for peoplemovie in combinemovielist:
         d = {}
         moviecount=[]
         for ilist in (peoplemovie):
             for j1 in range(len(ilist)):
                 if ilist[j1] in d:
                     d[ilist[j1]] = d[ilist[j1]]+1
                 else:
                     d[ilist[j1]] = 1
         for key in d:
             if d[key]>=3:
                 moviecount.append(key)
         Globallist.append(moviecount)
    break
 # print Globallist


#-----------------------movies not seen by Rachel but other users watched---------------------------------------------
 usermovielist = []
 for smalllist in biglist:
     for newsmalllist in newlist:
         if smalllist[0]==newsmalllist[0]:
             usermovielist.append(newsmalllist[1])




 intersection_list= []
 for i in range (len(Globallist)):

      intersection_list.append (list(set(Globallist[i])-set(usermovielist[i])))


 smallestlist = []
 for small in newlist:
     smallestlist.append(small[0])



 finallist = []                     #making the final list of the user and recommended movies.
 for counting in range (len(biglist)):
     finallist1 = []
     if intersection_list[counting]:
         finallist1.append(smallestlist[counting])
         finallist1.append(intersection_list[counting])
         finallist.append(finallist1)

 for inside in finallist:
     inside[1].sort()
 # print finallist

 encoder = json.JSONEncoder()                  # using encoder to encode the unicode list
 for i in range(len(finallist)):
     if finallist:
      print encoder.encode(finallist[i])







if __name__ == '__main__':
    data = []
    listoutput = []
    # inputdata1 = open(sys.argv[1])
    # inputdata2 = open(sys.argv[2])
    with open(sys.argv[1]) as json_file: #Accessing the json data.
      for line in json_file:
          data.append(json.loads(line))
    with open(sys.argv[2]) as json_file1:
      for line in json_file1:
          listoutput.append(json.loads(line))
    recomm_algo(data,listoutput)




