

            
class Objects1:
    items = []
    
    def __init__(self, properties, unique = None, indent=None):
        self.unique     = unique
        self.indent     = indent
        self.properties  = properties
        Objects1.items.append(self)
        
class Objects2:
    items = []
    
    def __init__(self, properties, unique = None, indent=None):
        self.unique     = unique
        self.indent     = indent
        self.properties  = properties
        Objects2.items.append(self)
class Lang:
    initial_lang = None
    lang_vals = ['en', 'fr', 'it', 'pt', 'zh', 'nl', 'es','cs']
    
    Dict_enToCs =   {
                "pos.-no." : "Pozice",
                "amount/" : "Množství",
                "length" : "Délka",
                "drawing number" : "Číslo výkresu",
                "description" : "Popis",
                "type" : "Typ",
                "line": "Čára",
                "cross-sec. (mm²)" : "Průřez v (mm²)",
                "unsulation" :"Izolace",
                "diameter" :"Průřez",
                "color" :"Barva",
                "additional text" :"Text navíc",
                "supplier": "Dodavatel",
                "supplier material" :"Dovávaný materiál"
                }
    @classmethod
    def set_lang(cls, val):
        if val.lower() not in cls.lang_vals:
            return False
        else:
            if cls.initial_lang is not None and val != cls.initial_lang:
                return False
            else:
                cls.initial_lang = val.lower()

    @classmethod
    def get_initial_lang(cls):
        return cls.initial_lang
    
    
#################################
from dataclasses import dataclass
from typing import List

K = 'device\ndesignation.1'
L = 'pin'
AJ = 'device\ndesignation.2'
AK = 'pin.1'
headers_to_check = ['signal', 'cross-sec. (mm²)\nsingle core', 'color', 'type', 'identnumber.1']

@dataclass
class Storage:
    K: str
    L: str
    AJ: str
    AK: str
    headers_to_check: List[str]

storage= Storage(K, L, AJ, AK, headers_to_check)
    


class TwoPairs:
    twoPairs_old = [] 
    twoPairs_new = [] 
    twoPairs_newDevice_new = []
    twoPairs_newDevice_old = []
    
    
    def __init__(self, startDevice,startPin,endDevice,endPin, data, var) -> None:
        self.startDevice = startDevice
        self.startPin = startPin
        self.endDevice = endDevice
        self.endPin = endPin
        self.data = data 
        if var == "old":
            TwoPairs.twoPairs_old.append(self)
        elif var == "new":
            TwoPairs.twoPairs_new.append(self)
        
    @classmethod
    def printAll(cls, var):
        if var == 'old':
            desired_list = cls.twoPairs_old 
        elif var =="new":
            desired_list = cls.twoPairs_new
            
        for item in desired_list :
            print(f"{item.startDevice} - {item.startPin} - {item.endDevice} - {item.endPin} - {item.data[0]}, {item.data[1]}, {item.data[2]}, {item.data[3]}, {item.data[4]}")   
            
    @staticmethod     
    def extractFromExcel(doc, var):
        
        for index, row in doc.iterrows():
            if str(row[storage.K]) =="nan" and str(row[storage.AJ]) =="nan" :
                continue
            else:
                partData = []
                for header in storage.headers_to_check: 
                    partData.append(row[header])
                    
                TwoPairs(startDevice=row[storage.K], startPin=row[storage.L],endDevice=row[storage.AJ], endPin=row[storage.AK],data=partData, var= var)

       

    
class Pairs:
    fullMatch = [] 
    fullMatchDataCheck = []
    startDevMatch = []
    startDevMatchCheck = []
    noMatch = []
    @classmethod
    def compareFullMatch(cls,oldList,newList):
        print(f"initial. lengh start {len(oldList)}")
        print(f"initial. lengh end {len(newList)}")
        appended = [] 
        
        
        for itemOld in oldList: 
            for itemNew in newList: 
                if itemNew in appended or itemOld in appended:
                    continue
                else:
                    if str(itemOld.startDevice)== str(itemNew.startDevice)  and str(itemOld.startPin) == str(itemNew.startPin) and str(itemOld.endDevice) == str(itemNew.endDevice) and str(itemOld.endPin) == str(itemNew.endPin):
                        cls.fullMatch.append([itemOld, itemNew])
                        appended.append(itemOld)
                        appended.append(itemNew)
                        continue
                
        for item in cls.fullMatch: 
            oldList.remove(item[0])
            newList.remove(item[1])
            
        appended = [] 
        for itemOld in oldList: 
            for itemNew in newList: 
                if itemNew in appended or itemOld in appended:
                    continue
                else:
                    if str(itemOld.startDevice)== str(itemNew.startDevice):
                        appended.append(itemOld)
                        appended.append(itemNew)
                        cls.startDevMatch.append([itemOld, itemNew])
                        continue
                
        for item in cls.startDevMatch: 
            oldList.remove(item[0])
            newList.remove(item[1])
            
        for item in zip(newList, oldList):
            new, old = item[0], item[1]
            cls.noMatch.append([new, old]) 
        
                
    @classmethod
    def checking(cls):
        for i,item in enumerate(cls.fullMatch):
            if i != 0:
                cls.fullMatchDataCheck.append(partialChecker)
            partialChecker = [] # for one object 
            old = item[0]
            new = item[1]
            
            for j,info in enumerate((zip(old.data, new.data))):
                old_info, new_info  = info[0], info[1]
                if str( old_info) != str(new_info):
                    partialChecker.append(False)
                else:
                    partialChecker.append(True)
                    
                if i == len(cls.fullMatch)-1 and j == len(old.data)-1:
                    print("last")
                    cls.fullMatchDataCheck.append(partialChecker)
                    partialChecker = []
                    
        for i,item in enumerate(cls.startDevMatch):
            if i != 0:
                cls.startDevMatchCheck.append(partialChecker)
            partialChecker = [] # for one object 
            old = item[0]
            new = item[1]
            
            for j,info in enumerate((zip(old.data, new.data))):
                old_info, new_info  = info[0], info[1]
                if str( old_info) != str(new_info):
                    partialChecker.append(False)
                else:
                    partialChecker.append(True)
                    
                if i == len(cls.startDevMatch)-1 and j == len(old.data)-1:
                    print("last")
                    cls.startDevMatchCheck.append(partialChecker)
                    partialChecker = []                 
                    
                    
                                     
    @classmethod
    def printFullMatchPairs(cls):
        print(len(Pairs.fullMatch))
        print(len(Pairs.fullMatch))
        
        for item in Pairs.fullMatch:
            print(f"{item[0].startDevice} - {item[0].startPin} - {item[0].endDevice} - {item[0].endPin}")
            print(f"{item[1].startDevice} - {item[1].startPin} - {item[1].endDevice} - {item[1].endPin}")
            print("\n")
        for item in Pairs.startDevMatch:
            print(f"{item[0].startDevice} - {item[0].startPin} - {item[0].endDevice} - {item[0].endPin}")
            print(f"{item[1].startDevice} - {item[1].startPin} - {item[1].endDevice} - {item[1].endPin}")
            print("\n")
        for item in zip(TwoPairs.twoPairs_new,TwoPairs.twoPairs_old):
            print(f"{item[0].startDevice} - {item[0].startPin} - {item[0].endDevice} - {item[0].endPin}")
            print(f"{item[1].startDevice} - {item[1].startPin} - {item[1].endDevice} - {item[1].endPin}")
            print("\n")
            
            
            
            

