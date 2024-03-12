


def Start(input1, input2, html_report_path ):

    from main import HarvestData
    from translate import Translator
    import pandas as pd 
    from tridy import Lang
    Output =HarvestData(input1=input1, input2=input2)

    UniqAndIndent,UniqPairs,IndentPairs,LeftOVer1,LeftOVer2 ,duplicatePairsList = Output[0],Output[1], Output[2], Output[3], Output[4], Output[5]

    
    for location in [input1, input2]:
        Lang.set_lang(pd.read_excel(location).columns[0])
        
    #Checking items with same uniq number and indent number 
    class Checked:
        Uniq_ann_Indent = [] 
        def __init__(self, unique1, indent1, unique2, indent2):
            self.unique1 = unique1
            self.indent1 = indent1
            self.unique2 = unique2
            self.indent2 = indent2
            self.items  = []
            Checked.Uniq_ann_Indent.append(self)
            
        @classmethod
        def AddByUniq(cls, un,indent, val):
            for obj in cls.Uniq_ann_Indent:
                if obj.unique1 == un and obj.indent1 == indent:
                    obj.items.append(val)
    # Checking items with same uniq number 
    class Checked2:
        Uniq = [] 
        def __init__(self, unique1, indent1, unique2, indent2):
            self.unique1 = unique1
            self.indent1 = indent1
            self.unique2 = unique2
            self.indent2 = indent2
            self.items  = []
            Checked2.Uniq.append(self)
        @classmethod
        def AddByUniq(cls, un, val):
            for obj in cls.Uniq:
                if obj.unique1 == un:
                    obj.items.append(val)
    # Checking items with same indent number            
    class Checked3:
        Uniq = [] 
        def __init__(self, unique1, indent1, unique2, indent2):
            self.unique1 = unique1
            self.indent1 = indent1
            self.unique2 = unique2
            self.indent2 = indent2
            self.items  = []
            Checked3.Uniq.append(self)
        @classmethod
        def AddByUniq(cls, id, val):
            for obj in cls.Uniq:
                if obj.indent2 == id:
                    obj.items.append(val)

    for item in UniqAndIndent:
        item1, item2 = item.item1, item.item2 
        Checked(unique1=item1.unique, indent1=item1.indent,unique2=item2.unique, indent2=item2.indent)
        
        for prop in zip(item1.properties, item2.properties):
            
            prop1, prop2 = prop[0], prop[1]
            if str(item1.properties[prop1]).strip() == str(item2.properties[prop2]).strip():
                Checked.AddByUniq(un=item1.unique,indent=item1.indent, val=[True,prop1,str(item1.properties[prop1]).strip(),str(item2.properties[prop2]).strip() ])
            else:
                Checked.AddByUniq(un=item1.unique,indent=item1.indent, val=[False,prop1,str(item1.properties[prop1]).strip(),str(item2.properties[prop2]).strip() ])

    for item in UniqPairs:
        item1_uniq, item2_uniq = item[0].unique, item[1].unique
        Checked2(unique1=item[0].unique, indent1=item[0].indent,unique2=item[1].unique, indent2=item[1].indent)
        for prop in zip(item[0].properties, item[1].properties):
            prop1, prop2 = prop[0], prop[1]
            if str(item[0].properties[prop[0]]).strip() == str(item[1].properties[prop[1]]).strip():
                Checked2.AddByUniq(un=item1_uniq, val=[True,prop1,str(item[0].properties[prop[0]]).strip(),str(item[1].properties[prop[1]]).strip()])
            else:
                Checked2.AddByUniq(un=item1_uniq, val=[False,prop1,str(item[0].properties[prop[0]]).strip(),str(item[1].properties[prop[1]]).strip()])
                
                
                
    for item in IndentPairs:
        item1_indent, item2_indent = item[0].indent, item[1].indent
        Checked3(unique1=item[0].unique, indent1=item[0].indent,unique2=item[1].unique, indent2=item[1].indent)
        for prop in zip(item[0].properties, item[1].properties):
            prop1, prop2 = prop[0], prop[1]
            if str(item[0].properties[prop[0]]).strip() == str(item[1].properties[prop[1]]).strip():
                Checked3.AddByUniq(id=item1_indent, val=[True,prop1,str(item[0].properties[prop[0]]).strip(),str(item[1].properties[prop[1]]).strip()])
            else:
                Checked3.AddByUniq(id=item1_indent, val=[False,prop1,str(item[0].properties[prop[0]]).strip(),str(item[1].properties[prop[1]]).strip()]) 
        
        
    initLang = Lang.get_initial_lang()
    initLang = None
    if initLang is not None:
        
        def translate_text(text:str, target_language:str):
            """
            returns a translation txt to target language
            """
            translator= Translator(to_lang=target_language)
            translation = translator.translate(text)
            return translation
        def getLangDictPart(property:str):
            """
            returns a dictionary with transalation to every Lang.lang_vals
            """
            dict_to_return = {f"{initLang}" : property}
            
            for lang in Lang.lang_vals:
                if lang == initLang:
                    continue
                elif lang == 'cs':
                    try:
                        translated = Lang.Dict_enToCs[property]
                        
                    except:
                        translated = translate_text(text=property, target_language=lang)
                        
                    if "'\'" in translated:
                        translated.replace("'\'", "'\\'")
                    translated.replace("'", "`")
                    dict_to_return.update({"cs" : translated })
                else:

                    translated = translate_text(text=property, target_language=lang)
                    if "'\'" in translated:
                        translated.replace("\'", "'\\'")
                    translated.replace("'", "`")
                    dict_to_return.update({f"{lang}" : translated })
                    
            return dict_to_return
                    
            
         
        
        def onlyFirstItemPropertiesToTranslate(Object):
            for  item in (Object):
                lang_dict = {}
                for i,prop in  enumerate(item.items):
                    lang_dict.update(getLangDictPart(property=prop[1]))
                    prop[1] = str(lang_dict)
                    print(lang_dict)
                    lang_dict = {}
                    
                    if i ==len(item.items)-1:
                        return Object
                 

        listOfClsLists = [Checked.Uniq_ann_Indent]#  Checked2.Uniq, Checked3.Uniq]
        
        for clsList in listOfClsLists:
            Object_Lang = onlyFirstItemPropertiesToTranslate(clsList)
    
        Origin_mark = {}
        Origin_mark.update(getLangDictPart(property='Origin'))
        OLD_mark = {}
        OLD_mark.update(getLangDictPart(property='OLD'))
        NEW_mark ={}
        NEW_mark.update(getLangDictPart(property='NEW'))
        ONLY_mark = {}
        ONLY_mark.update(getLangDictPart(property='Only'))
        Found_NEW_mark ={}
        Found_NEW_mark.update(getLangDictPart(property='founded in NEW, missing in OLD'))
        Found_OLD_mark ={}
        Found_NEW_mark.update(getLangDictPart(property='founded in OLD, missing in NEW'))
        DUPLICATES_mark = {}
        DUPLICATES_mark.update(getLangDictPart(property='Duplicates'))
        UNIQandIND= {}
        UNIQandIND.update(getLangDictPart(property='Match Unique ID and Indent ID match'))
        UNIQmatch = {}
        UNIQmatch.update(getLangDictPart(property='Match Unique ID match'))
        INDmatch = {}
        INDmatch.update(getLangDictPart(property='INDENT ID match'))
        Nomatch ={}
        Nomatch.update(getLangDictPart(property='No Match'))
        Notfound ={}
        Notfound.update(getLangDictPart(property='Not Founded'))
        title={}
        title.update(getLangDictPart(property='Porovnani materialovych listu'))
    
    else:
        print("NO INITIAL LANGUAGE FOUND")
        from lookUpTable import headers, Origin_mark,OLD_mark,NEW_mark,ONLY_mark,Found_NEW_mark,Found_OLD_mark,DUPLICATES_mark,UNIQandIND,INDmatch,Nomatch,Notfound,title,Change,new_version
        from lookUpTable import old_version,search_mark,UNIQmatch,indent,uniq_device, show_error
        from lookUpTable import transfer_to_indentation_translations, transfer_to_duplicates_translations ,transfer_to_not_found_translations ,transfer_to_id_and_unique_translations ,transfer_to_unique_translations 
    
    import json
    import re 
    pattern = r'[^/]+$'
    match = re.search(pattern, input1)
    if match:
        input1_name = match.group(0)
    match = re.search(pattern, input2)
    if match:
        input2_name = match.group(0)
        
    html = "<table id='table1'>"   
    html +="<tr>\n"

    html +=f"<th class='LANG'data-lang-values={json.dumps(Origin_mark)}></th>\n"
    html +=f"<th  class='LANG'data-lang-values={json.dumps(uniq_device)}></th>\n"
    html +=f"<th class='LANG'data-lang-values={json.dumps(indent)}></th>\n"

    for j, prop in enumerate(Object_Lang[0].items if initLang is not None else headers):
            if initLang is not None:
                html +=f"<th class='LANG' data-lang-values={prop[1]}></th>\n"
            else:
                html +=f"<th class='LANG' data-lang-values={json.dumps(prop)}></th>\n"

        
    breakbool2 = False
    html += "</tr>\n"
    html += "<tr>\n"
    for i, item in enumerate(Checked.Uniq_ann_Indent):
        breakbool2 = False
        for j,prop in enumerate(item.items):
            if breakbool2:
                break 
            lenght = len(item.items)
            if j == 0: 
            
                html += "<tr>\n"
                html +=f"<th class='LANG' data-lang-values={json.dumps(OLD_mark)}></th>\n"
                html +=f"<th class='matchId'>{item.unique1}</th>\n"
                html +=f"<th class='matchId'>{item.indent1}</th>\n"

            html +=f"<th class={prop[0]}>{prop[2]}</th>\n"
            if j == lenght-1:
                html += "</tr>\n"
                html += "<tr>\n"
                for l,prop in enumerate(item.items):
                    lenght = len(item.items)
                    if l == 0:
                        html +=f"<th class='LANG' data-lang-values={json.dumps(NEW_mark)}></th>\n"
                        html +=f"<th class='matchId'>{item.unique2}</th>\n"
                        html +=f"<th class='matchId'>{item.indent2}</th>\n"
                    html +=f"<th class={prop[0]}>{prop[3]}</th>\n"
                    if l == lenght-1:
                        html += "</tr>\n"
                        html += "<tr>\n"
                        for m in range(lenght+3):
                            html +=f"<th id='space'></th>\n"
                        html += "</tr>\n"
                        breakbool2 = True
                        break        
   


    html += "</table>\n"
    html2 ="<table id='table2'>"  
    html2 +="<tr>\n"
    html2 +=f"<th class='LANG' data-lang-values={json.dumps(Origin_mark)}></th>\n"
    html2 +=f"<th  class='LANG'data-lang-values={json.dumps(uniq_device)}></th>\n"
    html2 +=f"<th class='LANG'data-lang-values={json.dumps(indent)}></th>\n"
    breakbool = False

    for j, prop in enumerate(Object_Lang[0].items if initLang is not None else headers):
            if initLang is not None:
                html2 +=f"<th class='LANG' data-lang-values={prop[1]}></th>\n"
            else:
                html2 +=f"<th class='LANG' data-lang-values={json.dumps(prop)}></th>\n"
            
    breakbool2 = False
    html2 += "</tr>\n"
    html2 += "<tr>\n"     
    for i,item in enumerate(Checked2.Uniq):
        breakbool2 = False
        for j,prop in enumerate(item.items):
            if breakbool2:
                break 
            lenght = len(item.items)
            if j == 0: 
            
                html2 += "<tr>\n"
                html2 +=f"<th class='LANG' data-lang-values={json.dumps(OLD_mark)}></th>\n"
                html2 +=f"<th class='matchId'>{item.unique1}</th>\n"
                html2 +=f"<th class='AdditionalMatch'>{item.indent1}</th>\n"
            html2 +=f"<th class={prop[0]}>{prop[2]}</th>\n"      
            if j == lenght-1:
                html2 += "</tr>\n"
                html2 += "<tr>\n"
                for l,prop in enumerate(item.items):
                    lenght = len(item.items)
                    if l == 0:
                        html2 +=f"<th class='LANG' data-lang-values={json.dumps(NEW_mark)}></th>\n"
                        html2 +=f"<th class='matchId'>{item.unique2}</th>\n"
                        html2 +=f"<th>{item.indent2}</th>\n"
                    html2 +=f"<th class={prop[0]}>{prop[3]}</th>\n"
                    if l == lenght-1:
                        html2 += "</tr>\n"
                        html2 += "<tr>\n"
                        for m in range(lenght+3):
                            html2 +=f"<th id='space'></th>\n"
                        html2 += "</tr>\n"
                        breakbool2 = True
                        break
                    
    html2 += "</table>\n"    
        

    html3 ="<table id='table3'>"  
    html3 +="<tr>\n"
    html3 +=f"<th class='LANG' data-lang-values={json.dumps(Origin_mark)}></th>\n"
    html3 +=f"<th  class='LANG'data-lang-values={json.dumps(uniq_device)}></th>\n"
    html3 +=f"<th class='LANG'data-lang-values={json.dumps(indent)}></th>\n"        
    breakbool = False

    for j, prop in enumerate(Object_Lang[0].items if initLang is not None else headers):
            if initLang is not None:
                html3 +=f"<th class='LANG' data-lang-values={prop[1]}></th>\n"
            else:
                html3 +=f"<th class='LANG' data-lang-values={json.dumps(prop)}></th>\n"
            
    breakbool2 = False
    html3 += "</tr>\n"
    html3 += "<tr>\n"     
    for i,item in enumerate(Checked3.Uniq):
        breakbool2 = False
        for j,prop in enumerate(item.items):
            if breakbool2:
                break 
            lenght = len(item.items)
            if j == 0: 
            
                html3 += "<tr>\n"
                html3 +=f"<th class='LANG' data-lang-values={json.dumps(OLD_mark)}></th>\n"
                html3 +=f"<th class='AdditionalMatch'>{item.unique1}</th>\n"
                html3 +=f"<th class='matchId'>{item.indent1}</th>\n"
            html3 +=f"<th class={prop[0]}>{prop[2]}</th>\n"      
            if j == lenght-1:
                html3 += "</tr>\n"
                html3 += "<tr>\n"
                for l,prop in enumerate(item.items):
                    lenght = len(item.items)
                    if l == 0:
                        html3 +=f"<th class='LANG' data-lang-values={json.dumps(NEW_mark)}></th>\n"
                        html3 +=f"<th >{item.unique2}</th>\n"
                        html3 +=f"<th class='matchId'>{item.indent2}</th>\n"
                    html3 +=f"<th class={prop[0]}>{prop[3]}</th>\n"
                    if l == lenght-1:
                        html3 += "</tr>\n"
                        html3 += "<tr>\n"
                        for m in range(lenght+3):
                            html3 +=f"<th id='space'></th>\n"
                        html3 += "</tr>\n"
                        breakbool2 = True
                        break
    html3 += "</table>\n"    


    html4 ="<table id='table4'>"  
    html4 +="<tr>\n"      
    breakbool = False
    import numpy as np
    try:
        maxLen_list = [duplicatePairsList[0],duplicatePairsList[1],duplicatePairsList[2],duplicatePairsList[3]]
        maxLen_arg = np.argmax(maxLen_list)
    except:
        maxLen_arg =0

    if maxLen_list[maxLen_arg] != 0:

        for i, item in enumerate(maxLen_list[maxLen_arg]):
            if breakbool:
                break
            if i >1:
                break
            if i ==0:
                html4 +=f"<th  class='LANG'data-lang-values={json.dumps(uniq_device)}></th>\n"
                html4 +=f"<th class='LANG'data-lang-values={json.dumps(indent)}></th>\n"
            for j, prop in enumerate(item[0].properties):
                html4 +=f"<th>{prop}</th>\n"
                if j == 10:
                    breakbool = True
                    break 
        try:
            html4 += "<tr>\n"  
            for m in range(len(item.properties)+2):
                html4 +=f"<th id='new'></th>\n"
            html4 += "</tr>\n"      
        except:
            pass

    #duplicatePairsList = [DuplicatePairs.UniqAndIndentMatch, DuplicatePairs.UniqMatch, DuplicatePairs.IndentMatch, DuplicatePairs.NoMatch]  
    if len(duplicatePairsList[0]) != 0: 
        for q, pair in enumerate(duplicatePairsList[0]): 
            if len(pair) != 0:
                item1, item2 =  pair[0], pair[1]
                html4 += "<tr>\n"
                if q ==0:
                    html4 += "<tr>\n"  
                    for m in range(len(item2.properties)+2):
                        html4 +=f"<th id='new'></th>\n"
                    html4 += "</tr>\n"
                    
                    
                    for m in range(len(item2.properties)+2):
                        if m == 0:
                            html4 +=f"<th id='new' class='LANG' data-lang-values={json.dumps(UNIQandIND)}></th>\n"
                        html4 +=f"<th></th>\n"
                        
                html4 += "</tr>\n"
                html4 += "<tr>\n"
                html4 +=f"<th class='noIDorUNQ'>{item1.unique}</th>\n"
                html4 +=f"<th class='noIDorUNQ'>{item1.indent}</th>\n"
                for it in item1.properties: 
                    html4 +=f"<th>{item1.properties[it]}</th>\n"
                html4 += "</tr>\n"
                
                html4 += "<tr>\n"
                html4 +=f"<th id='duplicate2'>{item2.unique}</th>\n"
                html4 +=f"<th id='duplicate2'>{item2.indent}</th>\n"
                for it in item2.properties: 
                    html4 +=f"<th>{item2.properties[it]}</th>\n"
                html4 += "</tr>\n"

            for m in range(len(item2.properties)+3):
                html4 +=f"<th id='space'></th>\n"
            html4 += "</tr>\n"
            html4 += "<tr>\n"

        html4 += "<tr>\n"  
        for m in range(len(item2.properties)+2):
            html4 +=f"<th id='new'></th>\n"
        html4 += "</tr>\n"

        for m in range(len(item2.properties)+2):
            if m == 0:
                html4 +=f"<th id='new' class='LANG' data-lang-values={json.dumps(UNIQmatch)}></th>\n"
            html4 +=f"<th></th>\n"
        html4 += "</tr>\n"
        
    if len(duplicatePairsList[1]) != 0:
        for pair in duplicatePairsList[1]: 
            if len(pair) != 0:
                item1, item2 =  pair[0], pair[1]
                html4 += "<tr>\n"
                html4 +=f"<th class='noIDorUNQ'>{item1.unique}</th>\n"
                html4 +=f"<th class='noIDorUNQ'>{item1.indent}</th>\n"
                for it in item1.properties: 
                    html4 +=f"<th>{item1.properties[it]}</th>\n"
                html4 += "</tr>\n"
                
                html4 += "<tr>\n"
                html4 +=f"<th id='duplicate2'>{item2.unique}</th>\n"
                html4 +=f"<th id='duplicate2'>{item2.indent}</th>\n"
                for it in item2.properties: 
                    html4 +=f"<th>{item2.properties[it]}</th>\n"
                    
                html4 += "</tr>\n" 
            for m in range(len(item2.properties)+3):
                html4 +=f"<th id='space'></th>\n"
            html4 += "</tr>\n"
            
        html4 += "<tr>\n"  
        for m in range(len(item2.properties)+2):
            html4 +=f"<th id='new'></th>\n"
        html4 += "</tr>\n"

        html4 += "<tr>\n"
        for m in range(len(item2.properties)+2):
            if m == 0:
                html4 +=f"<th id='new' class='LANG' data-lang-values={json.dumps(INDmatch)}></th>\n"
            html4 +=f"<th></th>\n"
        html4 += "</tr>\n"
        
    if len(duplicatePairsList[2]) != 0:
        for pair in duplicatePairsList[2]: 
            if len(pair) != 0:
                item1, item2 =  pair[0], pair[1]
                html4 += "<tr>\n"
                html4 +=f"<th class='noIDorUNQ'>{item1.unique}</th>\n"
                html4 +=f"<th class='noIDorUNQ'>{item1.indent}</th>\n"
                for it in item1.properties: 
                    html4 +=f"<th>{item1.properties[it]}</th>\n"
                html4 += "</tr>\n"
                
                html4 += "<tr>\n"
                html4 +=f"<th id='duplicate2'>{item2.unique}</th>\n"
                html4 +=f"<th id='duplicate2'>{item2.indent}</th>\n"
                for it in item2.properties: 
                    html4 +=f"<th>{item2.properties[it]}</th>\n"
                html4 += "</tr>\n" 
            for m in range(len(item2.properties)+3):
                html4 +=f"<th id='space'></th>\n"
            html4 += "</tr>\n"
            
        html4 += "<tr>\n"  
        for m in range(len(item2.properties)+2):
            html4 +=f"<th id='new'></th>\n"
        html4 += "</tr>\n"
            
        html4 += "<tr>\n"
        for m in range(len(item2.properties)+2):
            if m == 0:
                html4 +=f"<th id='new' class='LANG' data-lang-values={json.dumps(Nomatch)}></th>\n"
            html4 +=f"<th></th>\n"
        html4 += "</tr>\n"
        
    if len(duplicatePairsList[3]) != 0:
        for pair in duplicatePairsList[3]: 
            if len(pair) != 0:
                item1, item2 =  pair[0], pair[1]
                html4 += "<tr>\n"
                html4 +=f"<th class='noIDorUNQ'>{item1.unique}</th>\n"
                html4 +=f"<th class='noIDorUNQ'>{item1.indent}</th>\n"
                for it in item1.properties: 
                    html4 +=f"<th>{item1.properties[it]}</th>\n"
                html4 += "</tr>\n"
                
                html4 += "<tr>\n"
                html4 +=f"<th id='duplicate2'>{item2.unique}</th>\n"
                html4 +=f"<th id='duplicate2'>{item2.indent}</th>\n"
                for it in item2.properties: 
                    html4 +=f"<th>{item2.properties[it]}</th>\n"
                html4 += "</tr>\n" 
                
            for m in range(len(item2.properties)+3):
                html4 +=f"<th id='space'></th>\n"
            html4 += "</tr>\n"

    html4 += "</table>\n"     
        

    html5 ="<table id='table5'>"  
    html5 +="<tr>\n"        
    breakbool = False
    quit1, quit2 = False, False
    if len(LeftOVer1) != 0:
        html5 +=f"<th  class='LANG'data-lang-values={json.dumps(uniq_device)}></th>\n"
        html5 +=f"<th class='LANG'data-lang-values={json.dumps(indent)}></th>\n"
        for j, prop in enumerate(Object_Lang[0].items if initLang is not None else headers):
            if initLang is not None:
                html5 +=f"<th class='LANG' data-lang-values={prop[1]}></th>\n"
            else:
                html5 +=f"<th class='LANG' data-lang-values={json.dumps(prop)}></th>\n"
    else:
        quit1 = True
    if len(LeftOVer2) != 0:
        if quit1:
            for j, prop in enumerate(Object_Lang[0].items if initLang is not None else headers):
                if initLang is not None:
                    html5 +=f"<th class='LANG' data-lang-values={prop[1]}></th>\n"
                else:
                    html5 +=f"<th class='LANG' data-lang-values={json.dumps(prop)}></th>\n"
        else:
            pass
    else:
        quit2 = True

    if quit1 and quit2:
        html5 += "</table>\n"   
    else:
        breakbool2 = False
        html5 += "</tr>\n"    
        for lost in LeftOVer1:
                html5+= "<tr>\n" 
                for m in range(len(lost.properties)+2):
                    if m == 0:
                        html5 +=f"<th id='nomatch' class='LANG' data-lang-values={json.dumps(Found_OLD_mark)}></th>\n"
                html5 += "</tr>\n"
                
                html5 += "<tr>\n"
                html5 +=f"<th class='noIDorUNQ'>{lost.unique}</th>\n"
                html5 +=f"<th class='noIDorUNQ'>{lost.indent}</th>\n"
                for it in lost.properties: 
                    html5 +=f"<th>{lost.properties[it]}</th>\n"
                html5 += "</tr>\n"
                
        for lost in LeftOVer2:
                html5+= "<tr>\n" 
                for m in range(len(lost.properties)+2):
                    if m == 0:
                        html5 +=f"<th id='nomatch' class='LANG' data-lang-values={json.dumps(Found_NEW_mark)}></th>\n" #No match, list2
                html5 += "</tr>\n"
                
                html5 += "<tr>\n"
                html5 +=f"<th class='noIDorUNQ'>{lost.unique}</th>\n"
                html5 +=f"<th class='noIDorUNQ'>{lost.indent}</th>\n"
                for it in lost.properties: 
                    html5 +=f"<th>{lost.properties[it]}</th>\n"
                html5 += "</tr>\n"
        html5 += "</table>\n"      
        

      
      

    html_main = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
        
            body {{
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                text-align: center;
            }}

            h1 {{
                color: black;
                text-align: center;
            }}
            #separator {{
                border: none; /* Set border to none */
                background-color: transparent; /* Set background color to transparent */
            }}

            th, td {{
                border: 1px solid black; /* Add borders to table cells */
                padding: 5px; /* Add padding to table cells for spacing */
                text-align: left;
            }}
            table {{
                font-size: 14px; /* Adjust the font size */
                border-collapse: collapse; /* Combine table borders */
                width: 100%; /* Make the table width 100% of the container */
                table-layout: auto;
                width: auto;
                margin-left: auto;
                margin-right: auto;
            }}
            .False{{
                background-color: red;
            }}
            .True{{
                background-color: green;
            }}
            .separator {{
                border-bottom: 2px solid black;
            }}
            
            #space{{
                background-color: blue;
            }}
            
            .matchId{{
                background-color: gold;
            }}
            .noIDorUNQ{{
                background-color:white;
            }}
            
            #new{{
                background-color: violet;
            }}
            #nomatch{{
                background-color: violet;
            }}
            
            #input{{
                font-size: 20px
            }}
            
            .tooltip {{
                position: relative;
                cursor: default;
            }}
        
            .tooltip .tooltiptext {{
                visibility: hidden;
                padding: 0.25em 0.5em;
                background-color: black;
                color: #fff;
                text-align: center;
                /* Position the tooltip */
                position: absolute;
                z-index: 1;
                top: 100%;
                left: 100%;
                transition-property: visibility;
                transition-delay: 0s;
            }}
        
            .tooltip:hover .tooltiptext {{
                visibility: visible;
                transition-delay: 0.3s;
            }}

            #menuWrapper{{
                display: grid;
                justify-content: center;
                align-items: center;
                grid-template-columns:500px 500px 500px;
            }}

            #modal{{
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(0, 0, 0, 0.7);
                z-index: 3;
                visibility: hidden;
                
            }}
            #showFlags{{
          
                visibility: hidden;
                z-index: 4;

                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                width: 600px;
                height: 300px;
                background-color: aqua;
            }}

            .flagImage{{
                width: 40px;
                height: 40px;

            }}
            .flagImage_div{{
                width: 50px;
                height: 50px;
                text-align: center;
            }}
            #flex_wrap{{
                margin-top:40px;
                display: flex;
                flex-direction: row;
                gap:20px;
                justify-content: center;

            }}
            #ChooseLang{{
                margin-top: 50px;
                width: 100px;
                height: 50px;
            }}
            
            #language_bar{{
                display: flex;
                flex-direction: column;
                gap: 20px;
                justify-content: center;
                align-items: center;
            }}

            #flag_image{{
                width: 40px;
                height: 40px;
            }}
            
            #show_only_wrapper{{
                display: flex;
                flex-direction: row;
                gap: 20px;
                justify-content: center;
                align-items: center;
            }}

            #show_bar{{
                margin-top: 60px;
                position: absolute;
                width:290px;
                height: auto;
                background-color: whitesmoke;

                display: flex;
                flex-direction: column;
                gap: 10px;
            }}


            #search_flex{{
                display: flex;
                flex-direction: row;
                gap: 10px;
            }}

            #search_wrapper{{
                display: flex;
                flex-direction: column;
                align-items: center;

            }}
            .output{{
                border: 5px;
                border-style: solid;
            }}

            .highlighted {{
                background-color: orangered;
            }}
        </style>

            
    </head>
    <body>
        <div id="showFlags">
            <div id="flex_wrap">
            </div>
            <div><button id="ChooseLang">OK</button></div>
        </div>
        <div id='modal'></div>
        <h1 class='LANG' data-lang-values={json.dumps(title)}></h1>
        <div  id=menuWrapper>
            <div id="language_bar">                
                <img id=flag_image>
                <button id="lang_button", class='LANG' data-lang-values={json.dumps(Change)}></button>
            </div>

            <div> 
            <p id='input'  data-input='{input1_name}' class='LANG' data-lang-values={json.dumps(old_version)}></p> 
            <p id='input'  data-input='{input2_name}' class='LANG' data-lang-values={json.dumps(new_version)}></p> 
            </div>

            <div id="search_wrapper">
                <div id="search_flex">
                    <label for="search" id="label_search" class='LANG' data-lang-values={json.dumps(search_mark)}></label>
                    <input id="serch">
                    <button class='LANG' data-lang-values={json.dumps(search_mark)}></button>
                </div>
                <div id="show_bar"></div>
            </div>
        </div>
        <br>
        <hr>
        <br>
        <div id="show_only_wrapper"> 
        
            <button id="Show Errors" class='LANG' data-lang-values={json.dumps(show_error)}></button>
            <button id="transfer_ID_UN"  class='LANG' data-lang-values= {json.dumps(transfer_to_id_and_unique_translations)}></button>
            <button id="transfer_UN"  class='LANG' data-lang-values= {json.dumps(transfer_to_unique_translations )}></button>
            <button id="transfer_ID"  class='LANG' data-lang-values= {json.dumps( transfer_to_indentation_translations)}></button>
            <button id="transfer_DUPLICATES"  class='LANG' data-lang-values={json.dumps( transfer_to_duplicates_translations)} ></button>
            <button id="transfer_notFound"  class='LANG' data-lang-values={json.dumps(transfer_to_not_found_translations)} ></button>
        </div>
        <br>
        <hr>
        <h2 for='table1' class='LANG' data-lang-values={json.dumps(UNIQandIND)}></h2>
        {html}
        <br>
        <hr>
        <h2 for='table2' class='LANG' data-lang-values= {json.dumps(UNIQmatch)}></h2>
        {html2}
        <br>
        <hr>
        <h2 for='table3'class='LANG' data-lang-values={json.dumps(INDmatch)}></h2>
        {html3}
        <br>
        <hr>
        <h2 for='table4' class='LANG' data-lang-values={json.dumps(DUPLICATES_mark)}></h2>
        {html4}
        <br>
        <hr>
        <h2 for='table5' class='LANG' data-lang-values={json.dumps(Notfound)}></h2>
        {html5}


    </body>
    
    <script>
                let highlight = null;
                function getSelectedLanguage() {{
                    return localStorage.getItem('selectedLanguage') || 'en';
                }}
                
                function setSelectedLanguage(lang) {{
                    localStorage.setItem('selectedLanguage', lang);
                }}


                let selectedImg = null;
                let choosenKey;
                window.addEventListener('load', ()=>{{

                    let lang = getSelectedLanguage()
                    if (lang){{
                        document.querySelectorAll('.LANG').forEach(function(element) {{
                            let dict = JSON.parse(element.dataset.langValues.replace(/'/g, '"'));
                            if (element.id =='input'){{
                                element.innerText = '';
                                element.innerText = `${{element.dataset.input}}: ${{dict[lang]}}`;
                            }}else{{
                                element.innerText =  dict[lang]
                            }}
                            
                            document.getElementById('flag_image').src = `dependencies/${{lang}}.png`; 
                        }});
                    }}
                    else{{
                        document.querySelectorAll('.LANG').forEach(function(element) {{
                            let dict = JSON.parse(element.dataset.langValues.replace(/'/g, '"'));
                            element.innerText =  dict['en']
                        }});
                    }}

                }})

            
                document.getElementById('lang_button').addEventListener('click',()=>{{
                    document.getElementById('modal').style.visibility = 'visible';
                    document.getElementById('showFlags').style.visibility = 'visible';
                    const flex = document.getElementById('flex_wrap')
                        while (flex.firstChild){{
                            flex.removeChild(flex.firstChild)
                        }}

                    
                    const lang_list = ['en', 'fr', 'it', 'pt', 'zh', 'nl', 'es','cs', 'de']
                    

                        for (const item of lang_list){{
                            const img = document.createElement('img')
                            const img_div = document.createElement('div')
                            img.src = `dependencies/${{item}}.png`; 
                            img.alt= item
                            img.className = 'flagImage'
                            img_div.className = 'flagImage_div'
                            img_div.appendChild(img)
                            flex.appendChild(img_div)
                            img_div.addEventListener('click',()=>{{
                                document.getElementById('flag_image').src = `dependencies/${{item}}.png`; 
                                if (selectedImg){{
                                    selectedImg.style.backgroundColor = ''
                                }}
                                selectedImg = img_div 
                                img_div.style.backgroundColor = 'orange'
                                
                            }})
                        }}

                }})


                function changeLang(lang, element){{
                    
                    console.log(element)
                    const txt  = element.innerText.replace(/'/g, '"');
                    element.innerText = JSON.parse(txt)[lang]


                }}
                document.getElementById('ChooseLang').addEventListener('click', ()=>{{


                document.getElementById('modal').style.visibility = 'hidden';
                document.getElementById('showFlags').style.visibility = 'hidden';
               
                if (selectedImg){{
                    console.log(selectedImg.firstChild.alt)
                    choosenKey = selectedImg.firstChild.alt
                    setSelectedLanguage(choosenKey)
                }}else{{
                    choosenKey = 'en'
                }}
                document.querySelectorAll('.LANG').forEach(function(element) {{
                    
                    
                    console.log(element.dataset.langValues);
                    let dict = JSON.parse(element.dataset.langValues.replace(/'/g, '"'));
                    if (element.id =='input'){{
                        element.innerText = '';
                        element.innerText = `${{element.dataset.input}}: ${{dict[choosenKey]}}`;
                    }}else{{
                        element.innerText = ''
                        element.innerText =  dict[choosenKey];
                    }}
                    }});
                }})
            
                document.getElementById('Show Errors').addEventListener('click', () => {{
                const trueElements = document.querySelectorAll('.True');
                
                trueElements.forEach(function (trueElement) {{
                  const parentRow = trueElement.closest('tr');
                  const correspondingFalseElement = parentRow.querySelector('.False');
                  const nextRow = parentRow.nextElementSibling;
                  if (!correspondingFalseElement) {{
                    parentRow.style.display = 'none';
                    if (nextRow && nextRow.tagName === 'TR' && nextRow.children.length > 0) {{
                      nextRow.style.display = 'none';
                    }}
                  }}
                }});
                
                }});
              
                document.getElementById('transfer_notFound').addEventListener('click',()=>{{
                    const table =document.getElementById('table5')
                    table.scrollIntoView()
                }})
                
                
                document.getElementById('transfer_ID_UN').addEventListener('click',()=>{{
                    const table =document.getElementById('table1')
                    table.scrollIntoView()
                }})
               
                        
                document.getElementById('transfer_UN').addEventListener('click',()=>{{
                    const table =document.getElementById('table2')
                    table.scrollIntoView()
                }})       
                document.getElementById('transfer_ID').addEventListener('click',()=>{{
                    const table =document.getElementById('table3')
                    table.scrollIntoView()
                }})   
                
                
               
                document.getElementById('transfer_DUPLICATES').addEventListener('click',()=>{{
                    const table =document.getElementById('table4')
                    table.scrollIntoView()
                }})  
                let c;
                const clickedRows = []
                const show_bar = document.getElementById('show_bar')
                show_bar.style.visibility = 'hidden'
                document.getElementById('serch').addEventListener('input',()=>{{
                    
                    show_bar.style.visibility = 'visible'
                    while ( show_bar.firstChild){{
                        show_bar.removeChild(show_bar.firstChild)
                    }}
                    let items_to_search = document.querySelectorAll('.matchId, .noIDorUNQ, .AdditionalMatch' )
                    let value = document.getElementById('serch').value
                    if (value ===''){{
                        show_bar.style.visibility = 'hidden'
                        return
                    }}
                    items_to_search.forEach(item =>{{
                        const founded = item.innerText.toLowerCase()
                    const boolean = founded.includes(value.toLowerCase())
                    console.log()
                    if(boolean){{
                        const row = item.closest('tr')
                        let display = (row.style.display == 'none')
                        if (!display){{
                            const div = document.createElement('div')
                            div.className= 'output'
                            div.innerText = item.innerText
                            show_bar.appendChild(div)
                            c=0;
                            /*clickedRows.push(row)*/
                            div.addEventListener('click', ()=>{{
                                show_bar.style.visibility = 'hidden'
                                row.scrollIntoView()
                                row.querySelectorAll('th').forEach(element =>{{
                                    clickedRows.push([element,  window.getComputedStyle(element).backgroundColor ])
                                    element.style.backgroundColor = 'orange'
                                }})
                                
                            }})

                        }}
                    }}
                    }})
                }})

               
                document.addEventListener('click',()=>{{

                        c+=1
                        if (c==2){{
                            c=0
                            for (let item of clickedRows){{
                               item[0].style.backgroundColor = item[1]
                            }}
                        }}
                        
                        
                }})
    </script>
    </html>

    """
    print("Created HTML string")
    print(html_report_path)
    with open(html_report_path, 'w', encoding='utf-8') as file:
        file.write(html_main)
    print("Created HTML file")
    