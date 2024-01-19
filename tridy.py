

            
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
            
        
