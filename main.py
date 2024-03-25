import pandas as pd 
import numpy as np
from tridy import   Objects1,  Objects2, Lang



def HarvestData(input1, input2):

    def doStuff(Objects , input):
        doc = pd.read_excel(input).to_numpy()
        width, height = doc.shape
        def findMenuBar(doc, width, height) ->int:
            for j in range(width):
                for i in range(height):
                    if doc[j][i] == 'unique\ndevice id':
                        cutof = j 
                        return cutof
        cutof = findMenuBar(doc, width, height) 
        doc = doc[cutof:]
        width, height = doc.shape

        header_dict = {}
        keys = []
        for i, item in enumerate(doc[0]):

            if str(item) != "nan":
                keys.append(item)
                header_dict[item] = i
        cout =0 
        for f,item in enumerate(doc):
            if cout == 5:
                lenToLoop = f 
                break
            if f ==0:
                continue
            else:
                if str(item[0]) == "nan":
                    cout += 1

        for i in range(width):
            if i == 0:
                continue
            else:
                prop = {}
                additional1,additional2 = False, False
                unique,indent = None, None
                for key in (keys):
                    
                        if "Created by Linde" in str(doc[i][header_dict[key]]):
                            return

                        if key == "unique\ndevice id": # HArd coded unique identifier, if thats change, it wount work 
                            if str(doc[i][header_dict[key]]) != "nan" or "Created by Linde" in str(doc[i][header_dict[key]]):
                                unique = doc[i][header_dict[key]]
                            else: 
                                additional1 = True
                        elif key == "identnumber":  # HArd coded unique identifier, if thats change, it wount work 
                            if str(doc[i][header_dict[key]]) != "nan" or "Created by Linde" in str(doc[i][header_dict[key]]):
                                indent = doc[i][header_dict[key]]
                            else: 
                                additional2 = True
                        else:
                            if "Created by Linde" in str(doc[i][header_dict[key]]):
                                continue
                            else:
                                prop[key] = [doc[i][header_dict[key]]]
                                
                if additional1  and additional2:
                    score = False
                    try:
                        for key in (keys):
                            if str(doc[i+1][header_dict[key]]) != "nan":
                                score = True
                                break
                    except:
                        continue

                    if score:     
                        for key in (keys):
                            if key == "unique\ndevice id" or key == "identnumber":
                                continue
                            if str(prop[key]) !="[nan]":
                                Objects.items[-1].properties[key].append(prop[key])
                    else:
                        continue
                else:
                    DoesUniqLineOverflow = []
                    for key in (keys):
                            if key == "unique\ndevice id" or key == "identnumber":
                                continue
                            else:
                                if str(doc[i][header_dict[key]]) == "nan":
                                    DoesUniqLineOverflow.append(True)
                                else:
                                    DoesUniqLineOverflow.append(False)
                                    
                                   
                                
                    
                    if (unique is not None and indent is None) and all(DoesUniqLineOverflow) == True:
                        Objects.items[-1].unique = f"{Objects.items[-1].unique}{unique}"
                    else:
                        Objects(unique= unique, indent = indent, properties= prop)
                           
    Objects1.items.clear()
    Objects2.items.clear()
    # Harvesting items 
    doStuff(input=input1 ,Objects=Objects1)
    doStuff(input=input2 ,Objects=Objects2)


    # Gather the duplicates items 
    index = [] 
    Duplicate_list_1 = []
    for i, items11 in enumerate(Objects1.items):
            h= items11.unique
            
            
            continueQ = False
            for check in  Duplicate_list_1:
                if items11.unique == check[0].unique:
                    continueQ = True
                    break
                
            if continueQ:
                continue
            for j,items12 in enumerate(Objects1.items):
                h2= items12.unique
                breakbool = False
                if len(index) != 0:
                            
                        for ind in index:
                            if ind == j:
                                breakbool = True
        
                if i == j:
                    continue
                if breakbool:
                    continue
                else:
                    if items12.unique == items11.unique and items12.indent == items11.indent: 
                        index.append(i)
                        index.append(j)
                        Duplicate_list_1.append([items11, items12])
                        print(f"Duplicate {items12.unique} {items11.unique}")
                        print(f"Duplicate {items12.indent} {items11.indent}")

    # Trim duplicate items from global list 
    DuplicateButOnlyList1 = [] 
    for item in Duplicate_list_1:
        DuplicateButOnlyList1.append(item[0])
        DuplicateButOnlyList1.append(item[1])
        
    Objects1.items = [item for i, item in enumerate(Objects1.items) if i not in index]

      
    #duplicates for second list 
    index2 = [] 
    Duplicate_list_2 = []
    for i, items11 in enumerate(Objects2.items):
            h= items11.unique
            continueQ = False
            for check in  Duplicate_list_2:
                if items11.unique == check[0].unique:
                    continueQ = True
                    break
                
            if continueQ:
                continue
                    
            for j,items12 in enumerate(Objects2.items):
                h2= items12.unique
                breakbool = False
                if len(index) != 0:
                            
                        for ind in index2:
                            if ind == j:
                                breakbool = True
        
                if i == j:
                    continue
                if breakbool:
                    continue
                else:
                    if items12.unique == items11.unique and items12.indent == items11.indent: 
                        index2.append(i)
                        index2.append(j)
                        Duplicate_list_2.append([items11, items12])

                        print(f"Duplicate {items12.unique} {items11.unique}")
                        print(f"Duplicate {items12.indent} {items11.indent}")

    # Trim duplicate items from global list 
    DuplicateButOnlyList2 = [] 
    for item in Duplicate_list_2:
        DuplicateButOnlyList2.append(item[0])
        DuplicateButOnlyList2.append(item[1])
        
    Objects2.items = [item for i, item in enumerate(Objects2.items) if i not in index2]
    class UniqAndIndentClass:
        UniqAndIndent = []
        def __init__(self, item1, item2):
            self.item1  = item1
            self.item2 = item2
            UniqAndIndentClass.UniqAndIndent.append(self)


    # Match must be UNIQ and INDENT atribute         
    for item1 in (Objects1.items): # jeden item v listu 1 muze byt vickrat v listu 2, nbevadi 
        ground = item1.unique
        for item2 in (Objects2.items):
            compare = item2.unique
            if item1.unique == item2.unique and item1.indent == item2.indent:
                UniqAndIndentClass(item1=item1, item2=item2)
                
    # Deleting this objects from global list 

    UnpackedListOfPairs_list1_and_list2 = []
    for item in (UniqAndIndentClass.UniqAndIndent):
        UnpackedListOfPairs_list1_and_list2.append(item.item1)
        UnpackedListOfPairs_list1_and_list2.append(item.item2)

    temp = []
    temp2 = [] 
    for  item1 in (Objects1.items):

        if item1 not in  UnpackedListOfPairs_list1_and_list2:
            temp.append(item1)
            
    for  item2 in (Objects2.items):    
        if item2 not in  UnpackedListOfPairs_list1_and_list2:
            temp2.append(item2)
            
    
    Objects1.items = temp 
    Objects2.items = temp2

          
    # Selectiong only UNIQ matching atribute 
    UniqIDandIndent = [] 
    for items in UniqAndIndentClass.UniqAndIndent:
        UniqIDandIndent.append(items.item1) # this is from input list1 
        
        
    OnlyUniq = []
    OnlyUniq_list2 = []
    OnlyUniqPairs = []
    for item1 in Objects1.items: 
        for item2 in Objects2.items:
            if item1.unique == item2.unique:
                if item1 in OnlyUniq:
                    continue
                elif item1 in UniqIDandIndent:
                    continue
                elif item1 in DuplicateButOnlyList1:
                    continue
                elif item2 in OnlyUniq_list2:
                    continue
                else:
                    OnlyUniq.append(item1)
                    OnlyUniq_list2.append(item2)
                    OnlyUniqPairs.append([item1, item2])
                    
                    
                    
    # Deleting Only uniq items from global list 
       
    list1 = [sublist[0] for sublist in OnlyUniqPairs]
    list2 = [sublist[1] for sublist in OnlyUniqPairs]  
    
    for items in list1:
        Objects1.items.remove(items)
          
    for items in list2:
        Objects2.items.remove(items) 
            

    # Matching only objects by its indent number 
    OnlyIndent= []
    OnlyIndent_list2= []
    OnlyIndentPairs= []
    for item1 in Objects1.items: 
        for item2 in Objects2.items:
            
            if item1.indent == item2.indent:
                if item1 in OnlyIndent:
                    continue
                elif item1 in UniqIDandIndent:
                    continue
                elif item1 in DuplicateButOnlyList1:
                    continue
                elif item2 in OnlyIndent_list2:
                    continue
                else:
                    OnlyIndent.append(item1)
                    OnlyIndent_list2.append(item2)
                    OnlyIndentPairs.append([item1, item2])
  
    list1.clear(), list2.clear()
    list1 = [sublist[0] for sublist in OnlyIndentPairs]
    list2 = [sublist[1] for sublist in OnlyIndentPairs]  

    for items in list1:
        Objects1.items.remove(items)
            
    for items in list2:
        Objects2.items.remove(items)    
        
                       
    # Deleting indent matched objects from global list -> only no matching values left 
    LeftOVer1=  Objects1.items
    leftOver2 = Objects2.items


    return [UniqAndIndentClass.UniqAndIndent,OnlyUniqPairs,OnlyIndentPairs, LeftOVer1, leftOver2, Duplicate_list_1,Duplicate_list_2 ]

