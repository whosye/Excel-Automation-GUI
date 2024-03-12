



headers = ["{'en': 'pos.-no.', 'fr': 'Pos. No.', 'it': 'N° pos.', 'pt': 'Número da Pos.', 'zh': 'pos.-no.', 'nl': 'Positie nr.', 'es': 'N.º de PDV', 'cs': 'Pozice', 'de': 'Pos.-Nr.'}",
"{'en': 'amount-nlength', 'fr': 'montant-nlongueur', 'it': 'importo-nlunghezza', 'pt': 'quantidade-ncomprimento', 'zh': '金额-n长度', 'nl': 'hoeveelheid-nlengte', 'es': 'cantidad-nlongitud', 'cs': 'množství-ndélka', 'de': 'Menge-nLänge'}",
"{'en': 'drawing number', 'fr': 'numéro de plan', 'it': 'Numero del disegno', 'pt': 'número do desenho:', 'zh': '图纸编号', 'nl': 'tekeningnummer', 'es': 'número de plano', 'cs': 'Číslo výkresu', 'de': 'Zeichnungsnummer'}",
"{'en': 'description', 'fr': 'description', 'it': 'descrizione', 'pt': 'descrição', 'zh': '说明', 'nl': 'Beschrijving', 'es': 'descripción', 'cs': 'Popis', 'de': 'Beschreibung'}",
"{'en': 'type-nline', 'fr': 'ligne de type', 'it': 'La linea del tipo', 'pt': 'linha de tipo', 'zh': '型线', 'nl': 'typeregel', 'es': 'línea de tipo', 'cs': 'řádek typu', 'de': 'Typ-Zeile'}",
"{'en': 'cross-sec. (mm²)', 'fr': 'cross-sec. (mm²)', 'it': 'cross-sec. (mm²)', 'pt': 'cross-sec. (mm²)', 'zh': '交叉秒针(mm ²)', 'nl': 'cross-sec. (mm²)', 'es': 'seg. transversal (mm²)', 'cs': 'Průřez v (mm²)', 'de': 'Querschnitt (mm²)'}",
"{'en': 'unsulation-ndiameter', 'fr': 'diam\u00e8tre --ndisolation', 'it': 'diametro --ndell isolamento', 'pt': 'di\u00e2metro de--nn\u00e3o isolamento', 'zh': '\u7edd\u7f18-n\u76f4\u5f84', 'nl': 'onge\u00efsoleerde-ndiameter', 'es': 'di\u00e1metro de/nla insolaci\u00f3n', 'cs': 'pr\u016fm\u011br -nodizolov\u00e1n\u00ed',  'de': 'Isolationsdurchmesser'}",
"{'en': 'color', 'fr': 'couleur', 'it': 'colore', 'pt': 'cor', 'zh': '彩色', 'nl': 'kleur', 'es': 'color', 'cs': 'Barva',  'de': 'Farbe'}",
"{'en': 'additional text', 'fr': 'texte additionnel', 'it': 'Testo aggiuntivo', 'pt': 'Texto adicional', 'zh': '附加文字', 'nl': 'Aanvullende tekst', 'es': 'TEXTO ADICIONAL', 'cs': 'Text navíc', 'de': 'Zusätzlicher Text'}",
"{'en': 'supplier', 'fr': 'fournisseur/fournisseurs /distributeur/prestataire', 'it': 'fornitore', 'pt': 'fornecedor', 'zh': '供应商', 'nl': 'Leverancier', 'es': 'equipamiento original', 'cs': 'Dodavatel', 'de': 'Lieferant'}",
"{'en': 'supplier material', 'fr': 'matériel du fournisseur', 'it': 'Materiale da Fornitore', 'pt': 'material do fornecedor', 'zh': '供应商材料', 'nl': 'leveranciersmateriaal', 'es': 'Materia prima del proveedor', 'cs': 'Dovávaný materiál', 'de': 'Lieferantenmaterial'}"]

indent = "{'en': 'Indent','fr': 'Indentation','it': 'Rientro','pt': 'Indentação','zh': '缩进','nl': 'Inspringen','es': 'Sangría','cs': 'Odsazení', 'de' :'Einzug' }"
uniq_device = "{'en': 'Unique device id','fr': 'Identifiant unique du dispositif', 'it': 'ID dispositivo unico', 'pt': 'ID de dispositivo único', 'zh': '唯一设备标识', 'nl': 'Unieke apparaat-ID', 'es': 'ID único del dispositivo', 'cs': 'Jedinečný identifikátor zařízení',  'de': 'Eindeutige Gerätekennung'}"


OLD_mark = "{'en': 'OLD', 'fr': 'VIEUX', 'it': 'OBSOLETA', 'pt': 'ANTIGA', 'zh': '旧的', 'nl': 'OUDE', 'es': 'VIEJA', 'cs': 'STARÉ', 'de': 'ALT' }"
Origin_mark = "{'en': 'Origin', 'fr': 'Origine', 'it': 'Origine', 'pt': 'Origem', 'zh': '原始内容', 'nl': 'Oorsprong', 'es': 'Origen', 'cs': 'Zdroj',  'de': 'Ursprung'}"
NEW_mark ="{'en': 'NEW', 'fr': 'NOUVEAU', 'it': 'NUOVA', 'pt': 'NOVO', 'zh': '新品上市', 'nl': 'NIEUW', 'es': 'NUEVA', 'cs': 'NOVÝ',  'de': 'NEU'}"
ONLY_mark = "{'en': 'Only', 'fr': 'Seulement', 'it': 'Solo il', 'pt': 'Apenas', 'zh': '仅此一项', 'nl': 'Slechts', 'es': 'Sólo', 'cs': 'Pouze ',  'de': 'Nur'}"
Found_NEW_mark = "{'en': 'founded in NEW, missing in OLD', 'fr': 'fondée dans l...le VIEUX', 'it': 'fondata nel NUOVO,... nel VECCHIO', 'pt': 'fundada no NOVO, d...da no ANTIGO', 'zh': '成立于新，缺少于旧', 'nl': 'opgericht in NIEUW, ve...t in OUD', 'es': 'fundado en NUEVO, f...e en ANTIGUO', 'cs': 'založeno v NOVÉM, chybí ve STARÉM', 'de' : 'Gegründet in NEU, fehlt in ALT'}"
Found_OLD_mark = "{'en': 'founded in OLD, missing in NEW', 'fr': 'fondée dans l`ANCIEN, disparue dans le NOUVEAU', 'it': 'fondata nel VECCHIO, mancante nel NUOVO', 'pt': 'fundada no ANTIGO, desaparecida no NOVO', 'zh': '成立于旧，缺少于新', 'nl': 'opgericht in OUD, vermist in NIEUW', 'es': 'fundado en ANTIGUO, faltante en NUEVO', 'cs': 'založeno ve STARÉM, chybí v NOVÉM', 'de' : 'Gegründet im ALTEN, fehlt im NEUEN'}"
DUPLICATES_mark = "{'en': 'Duplicates', 'fr': 'Doublons', 'it': 'Duplicati', 'pt': 'Duplicações', 'zh': '重复项', 'nl': 'Duplicaten', 'es': 'Duplicados', 'cs': 'Duplicity', 'de' : 'Duplikate'}"
Nomatch = "{'en': 'No Match', 'fr': 'Aucune Concordance', 'it': 'Nessuna corrispondenza', 'pt': 'Sem Correspondência', 'zh': '沒有相符', 'nl': 'Geen match', 'es': 'Nada coincide', 'cs': 'Žádná shoda', 'de' :'keine Übereinstimmung' }"
Notfound ="{'en': 'Not Founded', 'fr': 'Non fondé', 'it': 'Non fondata', 'pt': 'Não fundado', 'zh': '未建立', 'nl': 'Niet opgericht', 'es': 'No fundado', 'cs': 'Nezaloženo', 'de' : 'nicht gefunden'}"
title="{'en': 'Comparison of material sheets', 'fr': 'Comparatif des fiches matériaux', 'it': 'Confronto delle schede dei materiali', 'pt': 'Comparação de folhas de materiais', 'zh': '材质板材对比', 'nl': 'Vergelijking van materiaalplaten', 'es': 'Comparación de hojas de materiales.', 'cs': 'Porovnani materialovych listu', 'de' : 'Vergleich von Materialblättern'}"
Change = "{'en': 'Change Language', 'fr': 'Changer de langue', 'it': 'Cambia lingua', 'pt': 'Mudar idioma', 'zh': '改变语言', 'nl': 'Taal wijzigen', 'es': 'Cambiar idioma', 'cs': 'Zvol jazyk', 'de' : 'Sprache ändern'}"
new_version = "{'en': 'NEW version','fr': 'Nouvelle version','it': 'Nuova versione','pt': 'Nova versão','zh': '新版本','nl': 'Nieuwe versie','es': 'Nueva versión','cs': 'Nová verze' , 'de' :'Neue Version'}"
old_version = "{'en': 'OLD version','fr': 'Ancienne version','it': 'Vecchia versione','pt': 'Versão antiga','zh': '舊版','nl': 'Oude versie','es': 'Versión antigua','cs': 'Stará verze', 'de' : 'Alte Version'}"
search_mark ="{'en': 'Search','fr': 'Rechercher','it': 'Cerca','pt': 'Pesquisar','zh': '搜索','nl': 'Zoeken','es': 'Buscar','cs': 'Hledat', 'de' :'Suchen'}"

show_error = "{'en': 'Show Errors','fr': 'Afficher les erreurs','it': 'Mostra errori','pt': 'Mostrar erros','zh': '显示错误','nl': 'Fouten weergeven','es': 'Mostrar errores','cs': 'Zobrazit chyby', 'de' : 'Fehler anzeigen'}"
UNIQandIND = "{'en': 'Match: Unique device id and Indent','fr': 'Correspondance : Identifiant unique du dispositif et Indentation','it': 'Corrispondenza: ID dispositivo unico e Rientro','pt': 'Correspondência: ID de dispositivo único e Indentação','zh': '匹配：唯一设备标识和缩进','nl': 'Overeenkomst: Unieke apparaat-ID en Inspringen','es': 'Coincidencia: ID único del dispositivo y Sangría','cs': 'Shoda: Jedinečný identifikátor zařízení a Odsazení', 'de' : 'Übereinstimmung: Eindeutige Geräte-ID und Einzug'}"
UNIQmatch = "{'en': 'Match: Unique device id','fr': 'Correspondance : Identifiant unique du dispositif','it': 'Corrispondenza: ID dispositivo unico','pt': 'Correspondência: ID de dispositivo único','zh': '匹配：唯一设备标识','nl': 'Overeenkomst: Unieke apparaat-ID','es': 'Coincidencia: ID único del dispositivo','cs': 'Shoda: Jedinečný identifikátor zařízení', 'de' :'Übereinstimmung: Eindeutige Geräte-ID'}"
INDmatch ="{'en': 'Match: Indent','fr': 'Correspondance : Indentation','it': 'Corrispondenza: Rientro','pt': 'Correspondência: Indentação','zh': '匹配：缩进','nl': 'Overeenkomst: Inspringen','es': 'Coincidencia: Sangría','cs': 'Shoda: Odsazení', 'de' : 'Übereinstimmung: Einrücken'}"



transfer_to_indentation_translations ="{'en': 'Transfer to Indentation','fr': 'Transf\u00e9rer vers lindentation','it': 'Trasferire allindentazione', 'pt': 'Transferir para a indenta\u00e7\u00e3o', 'zh': '\u8f6c\u79fb\u5230\u7f29\u8fdb', 'nl': 'Overdragen naar inspringen', 'es': 'Transferir a la sangr\u00eda','cs': 'P\u0159en\u00e9st do odsazen\u00ed'}"
transfer_to_duplicates_translations = "{ 'en': 'Transfer to Duplicates', 'fr': 'Transférer vers les doublons', 'it': 'Trasferire ai duplicati', 'pt': 'Transferir para duplicatas', 'zh': '转移到重复项', 'nl': 'Overdragen naar duplicaten', 'es': 'Transferir a duplicados', 'cs': 'Přenést do duplicit'}"
transfer_to_not_found_translations = "{'en': 'Transfer to Not Found','fr': 'Transférer vers non trouvé','it': 'Trasferire a non trovato','pt': 'Transferir para não encontrado','zh': '转移到未找到','nl': 'Overdragen naar niet gevonden','es': 'Transferir a no encontrado','cs': 'Přenést do nenalezeno'}"
transfer_to_id_and_unique_translations = "{ 'en': 'Transfer to ID and Unique', 'fr': 'Transférer vers ID et unique', 'it': 'Trasferire a ID e unico', 'pt': 'Transferir para ID e exclusivo', 'zh': '转移到ID和唯一', 'nl': 'Overdragen naar ID en uniek', 'es': 'Transferir a ID y único', 'cs': 'Přenést na ID a unikátní'}"


transfer_to_unique_translations = "{ 'en': 'Transfer to Unique', 'fr': 'Transférer vers unique', 'it': 'Trasferire a unico', 'pt': 'Transferir para exclusivo', 'zh': '转移到唯一', 'nl': 'Overdragen naar uniek', 'es': 'Transferir a único', 'cs': 'Přenést do unikátního'}"


