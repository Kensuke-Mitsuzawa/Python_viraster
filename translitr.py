#! /usr/bin/python
# -*- coding:utf-8 -*-

import sys, codecs;

class transliter:
    """
    Input is assumed as type:string encoding:utf-8.
    """
    def __init__(self, sequence):
        self.sequence=sequence;
    def converting_to_other(self):
        "Input of this method is the unicode type of arabic(persian) character."
        self.sequence=(self.sequence).replace(u'ا', self.char_map['alf']);
        self.sequence=(self.sequence).replace(u'ب', self.char_map['be']);
        self.sequence=(self.sequence).replace(u'پ', self.char_map['pe']);
        self.sequence=(self.sequence).replace(u'ت', self.char_map['te']);
        self.sequence=(self.sequence).replace(u'ث', self.char_map['se']);
        self.sequence=(self.sequence).replace(u'ج', self.char_map['jim']);
        self.sequence=(self.sequence).replace(u'چ', self.char_map['ch']);
        self.sequence=(self.sequence).replace(u'ح', self.char_map['he']);       
        self.sequence=(self.sequence).replace(u'خ', self.char_map['x']);
        self.sequence=(self.sequence).replace(u'د', self.char_map['d']);
        self.sequence=(self.sequence).replace(u'ذ', self.char_map['zal']);
        self.sequence=(self.sequence).replace(u'ر', self.char_map['r']);
        self.sequence=(self.sequence).replace(u'ز', self.char_map['ze']);
        self.sequence=(self.sequence).replace(u'ژ', self.char_map['je']);
        self.sequence=(self.sequence).replace(u'س', self.char_map['se']);
        self.sequence=(self.sequence).replace(u'ش', self.char_map['sh']);
        self.sequence=(self.sequence).replace(u'ص', self.char_map['sad']);
        self.sequence=(self.sequence).replace(u'ض', self.char_map['zad']);
        self.sequence=(self.sequence).replace(u'ع', self.char_map['ein']);
        self.sequence=(self.sequence).replace(u'غ', self.char_map['qein']);
        self.sequence=(self.sequence).replace(u'ف', self.char_map['f']);
        self.sequence=(self.sequence).replace(u'ق', self.char_map['qaf']);
        self.sequence=(self.sequence).replace(u'گ', self.char_map['gaf']);
        self.sequence=(self.sequence).replace(u'ل', self.char_map['l']);
        self.sequence=(self.sequence).replace(u'م', self.char_map['m']);
        self.sequence=(self.sequence).replace(u'ن', self.char_map['n']);
        self.sequence=(self.sequence).replace(u'و', self.char_map['v']);
        self.sequence=(self.sequence).replace(u'ه', self.char_map['h']);
        self.sequence=(self.sequence).replace(u'ط', self.char_map['ta']);
        self.sequence=(self.sequence).replace(u'ظ', self.char_map['za']);
        self.sequence=(self.sequence).replace(u"\u064A", self.char_map['arabic_ye']);
        self.sequence=(self.sequence).replace(u"\u06CC", self.char_map['persian_ye']);
        self.sequence=(self.sequence).replace(u"\u0643", self.char_map['arabic_keh']);
        self.sequence=(self.sequence).replace(u"\u06A9", self.char_map['persian_keh']);
        #diacritics from here
        self.sequence=(self.sequence).replace(u'\u0654', self.char_map['arabic_hamza_above']);
        self.sequence=(self.sequence).replace(u"\u0622", self.char_map['arabic_alef_madda_above']);
        self.sequence=(self.sequence).replace(u"\u0627", self.char_map['arabic_alef']);
        self.sequence=(self.sequence).replace(u"\u064b", self.char_map['arabic_fathatan']);
        self.sequence=(self.sequence).replace(u"\u060C", self.char_map['arabic_comma']);
        self.sequence=(self.sequence).replace(u"\u061B", self.char_map['arabic_semicolon']);
        self.sequence=(self.sequence).replace(u"\u061F", self.char_map['arabic_question']);
        self.sequence=(self.sequence).replace(u"\u066A", self.char_map['arabic_percent']);
        self.sequence=(self.sequence).replace(u"\u00ab", self.char_map['arabic_quotation_open']);
        self.sequence=(self.sequence).replace(u"\u00bb", self.char_map['arabic_quotation_close']);
        self.sequence=(self.sequence).replace(u"\u200C", self.char_map['ZWNJ']);
        self.sequence=(self.sequence).replace(u"۰", self.char_map['zero']);
        self.sequence=(self.sequence).replace(u"۱", self.char_map['one']);
        self.sequence=(self.sequence).replace(u"۲", self.char_map['two']);
        self.sequence=(self.sequence).replace(u"۳", self.char_map['three']);
        self.sequence=(self.sequence).replace(u"۴", self.char_map['four']);
        self.sequence=(self.sequence).replace(u"۵", self.char_map['five']);
        self.sequence=(self.sequence).replace(u"۶", self.char_map['six']);
        self.sequence=(self.sequence).replace(u"۷", self.char_map['seven']);
        self.sequence=(self.sequence).replace(u"۸", self.char_map['eight']);
        self.sequence=(self.sequence).replace(u"۹", self.char_map['nine']);
        #self.sequence=(self.sequence).replace(u"\u0629", self.char_map['arabic_teh_marbuta']);        
        #self.sequence=(self.sequence).replace(u"\u06C0", self.char_map['arabic_he_yeh_above']);
        #self.sequence=(self.sequence).replace(u"\u0626", self.char_map['arabic_yes_hamza_above']);
        #self.sequence=(self.sequence).replace(u"\u0624", self.char_map['arabic_v_hamza_above']);
        #self.sequence=(self.sequence).replace(u"\u0651", self.char_map['arabic_shadda']);
        #self.sequence=(self.sequence).replace(u"\u064E", self.char_map['arabic_fatha']); 
        #self.sequence=(self.sequence).replace(u'\u064F', self.char_map['arabic_damma']); 
        #self.sequence=(self.sequence).replace(u"\u0650", self.char_map['arabic_kasra']); 

        return self.sequence;

    def original_unicode(self):
        #Defines one-to-one correspondance between arabic character and ratin character. Some diacritics is omitted because they are rarely used.
        self.char_map={};
        self.char_map.setdefault('arabic_comma', u',');
        self.char_map.setdefault('arabic_semicolon', u';');
        self.char_map.setdefault('arabic_question', u'?');
        self.char_map.setdefault('arabic_hamza', u'°');
        self.char_map.setdefault('arabic_alef_madda_above', u'ā');
        self.char_map.setdefault('arabic_alef_hamza_above', u'á');
        self.char_map.setdefault('arabic_va_hamza_above', u'ú');
        self.char_map.setdefault('arabic_alef_hamza_below', u'E');
        self.char_map.setdefault('arabic_ye_hamza_above', u'´');
        self.char_map.setdefault('alf', u'a');
        self.char_map.setdefault('arabic_alef', u'a');
        self.char_map.setdefault('be', u'b');
        self.char_map.setdefault('arabic_heh_hamza_above', u'T');
        self.char_map.setdefault('te', u't');
        self.char_map.setdefault('se', u'ç');
        self.char_map.setdefault('jim', u'j');
        self.char_map.setdefault('he', u'ħ');
        self.char_map.setdefault('x', u'x');
        self.char_map.setdefault('d', u'd');
        self.char_map.setdefault('zal', u'đ');
        self.char_map.setdefault('r', u'r');
        self.char_map.setdefault('arabic_r_small_v_below', u'ř');
        self.char_map.setdefault('ze', u'z');
        self.char_map.setdefault('se', u's');
        self.char_map.setdefault('sh', u'š');
        self.char_map.setdefault('sad', u'ş');
        self.char_map.setdefault('zad', u'ź');
        self.char_map.setdefault('ta',u'ţ');
        self.char_map.setdefault('za', u'ẓ');
        self.char_map.setdefault('ein', u"'");
        self.char_map.setdefault('qein', u'q');
        self.char_map.setdefault('f', u'f');
        self.char_map.setdefault(u'\u06A4', u'v'); #arabic veh
        self.char_map.setdefault('qaf', u'ق');
        self.char_map.setdefault('arabic_keh', u'K');
        self.char_map.setdefault('persian_keh', u'K');
        self.char_map.setdefault('gaf', u'g');
        self.char_map.setdefault('l', u'l');
        self.char_map.setdefault('m', u'm');
        self.char_map.setdefault('n', u'n');
        self.char_map.setdefault('h', u'h');
        self.char_map.setdefault('v', u'w');
        self.char_map.setdefault('persian_ye', u'Ý');
        self.char_map.setdefault('arabic_ye', u'Y');
        self.char_map.setdefault('arabic_fathatan', u'e');
        self.char_map.setdefault('arabic_hamza_above', u'`');
        self.char_map.setdefault('ch', u'č');
        self.char_map.setdefault('pe', u'p');
        self.char_map.setdefault('je', u'ž');
        self.char_map.setdefault('arabic_heh_hamza_above', u'X');
        self.char_map.setdefault('persian_ye', u'y');
        self.char_map.setdefault('arabic_ye', u'y');
        self.char_map.setdefault('zero', u'0');
        self.char_map.setdefault('one', u'1');
        self.char_map.setdefault('two', u'2');
        self.char_map.setdefault('three', u'3');
        self.char_map.setdefault('four', u'4');
        self.char_map.setdefault('five', u'5');
        self.char_map.setdefault('six', u'6');
        self.char_map.setdefault('seven', u'7');
        self.char_map.setdefault('eight', u'8');
        self.char_map.setdefault('nine', u'9');
        self.char_map.setdefault('ZWNJ', u'_');
        self.char_map.setdefault("arabic_percent", u'%');
        self.char_map.setdefault("arabic_quotation_open", u'{');
        self.char_map.setdefault("arabic_quotation_close", u'}');

        return self.char_map;

    def conv_map_iso_233_3_1999(self):
        #character mapping to ISO 233-3:1999
        # I don't recommend use this mapping because this irreversible, I mean 3 'zar','ze','za' character has same mapping roman character 'z' and it's impossible to change to arabic correctly again.
        self.char_map={};
        self.char_map.setdefault('alf', u'â');
        self.char_map.setdefault('arabic_alef_madda_above', u'ā'); #modified to distinguish from normal â
        self.char_map.setdefault('be', u'b');
        self.char_map.setdefault('pe', u'p');
        self.char_map.setdefault('te', u't');
        self.char_map.setdefault('se', u'\u0304\u0073'); #replced to macron+s
        self.char_map.setdefault('jim', u'j');
        self.char_map.setdefault('ch', u'c');
        self.char_map.setdefault('he', u'\u0307\u0068'); #replace to dot_above+h 
        self.char_map.setdefault('x', u'\u0304\u006B') #replace to macron+k
        self.char_map.setdefault('d', u'd');
        self.char_map.setdefault('zal', u'\u0304\u007A') #replace to macron+z
        self.char_map.setdefault('r', u'r');
        self.char_map.setdefault('ze', u'z');
        self.char_map.setdefault('je', u'z');
        self.char_map.setdefault('se', u's');
        self.char_map.setdefault('sh', u'\u0161'); #caron s
        self.char_map.setdefault('sad', u'\u0307\u0073'); #replace to dot_above+s
        self.char_map.setdefault('zad', u'\u0307\u007A'); #dot_above+z
        self.char_map.setdefault('t2', u'\u0307\u0074');
        self.char_map.setdefault('zad', u'z');
        self.char_map.setdefault('ein', u'‘');
        self.char_map.setdefault('gein', u'\u0307\u0067'); #dot_above+g
        self.char_map.setdefault('f', u'\u0307\u0066');
        self.char_map.setdefault('qaf', u'q');
        self.char_map.setdefault('arabic_keh', u'k');
        self.char_map.setdefault('persian_keh', u'k');
        self.char_map.setdefault('gaf', u'q');
        self.char_map.setdefault('l', u'l');
        self.char_map.setdefault('m', u'm');
        self.char_map.setdefault('n', u'n');
        self.char_map.setdefault('v', u'v');
        self.char_map.setdefault('h', u'h');
        self.char_map.setdefault('arabic_ye', u'y');
        self.char_map.setdefault('persian_ye', u'y');
        self.char_map.setdefault('arabic_heh_hamza_above', u'X');
        self.char_map.setdefault('zero', u'0');
        self.char_map.setdefault('one', u'1');
        self.char_map.setdefault('two', u'2');
        self.char_map.setdefault('three', u'3');
        self.char_map.setdefault('four', u'4');
        self.char_map.setdefault('five', u'5');
        self.char_map.setdefault('six', u'6');
        self.char_map.setdefault('seven', u'7');
        self.char_map.setdefault('eight', u'8');
        self.char_map.setdefault('nine', u'9');
        self.char_map.setdefault('ZWNJ', u'_');

        return self.char_map;
    def fa_to_dehdari(self):
        #This code is following Jon Dehdari's converting chart See:http://www.ling.ohio-state.edu/~jonsafari/persian_charmaps.pdf
        self.sequence=(self.sequence).replace(u'ا', u'A');
        self.sequence=(self.sequence).replace(u'ب', u'b');
        self.sequence=(self.sequence).replace(u'پ', u'p');
        self.sequence=(self.sequence).replace(u'ت', u't');
        self.sequence=(self.sequence).replace(u'ث', u'V');
        self.sequence=(self.sequence).replace(u'ج', u'j');
        self.sequence=(self.sequence).replace(u'چ', u'c');
        self.sequence=(self.sequence).replace(u'ح', u'H');       
        self.sequence=(self.sequence).replace(u'خ', u'x');
        self.sequence=(self.sequence).replace(u'د', u'd');
        self.sequence=(self.sequence).replace(u'ذ', u'L');
        self.sequence=(self.sequence).replace(u'ر', u'r');
        self.sequence=(self.sequence).replace(u'ز', u'z');
        self.sequence=(self.sequence).replace(u'ژ', u'J');
        self.sequence=(self.sequence).replace(u'ژ', u'J');
        self.sequence=(self.sequence).replace(u'س', u's');
        self.sequence=(self.sequence).replace(u'ش', u'C');
        self.sequence=(self.sequence).replace(u'ص', u'S');
        self.sequence=(self.sequence).replace(u'ض', u'D');
        self.sequence=(self.sequence).replace(u'ط', u'T');
        self.sequence=(self.sequence).replace(u'ظ', u'Z');
        self.sequence=(self.sequence).replace(u'ع', u'E');
        self.sequence=(self.sequence).replace(u'غ', u'G');
        self.sequence=(self.sequence).replace(u'ف', u'f');
        self.sequence=(self.sequence).replace(u'ق', u'q');
        self.sequence=(self.sequence).replace(u'ك', u'K');
        self.sequence=(self.sequence).replace(u'گ', u'g');
        self.sequence=(self.sequence).replace(u'ل', u'l');
        self.sequence=(self.sequence).replace(u'م', u'm');
        self.sequence=(self.sequence).replace(u'ن', u'n');
        self.sequence=(self.sequence).replace(u'و', u'u');
        self.sequence=(self.sequence).replace(u'ه', u'h');
        self.sequence=(self.sequence).replace(u"\u064A", u'y'); 
        self.sequence=(self.sequence).replace(u"\u064E", u'a'); 
        self.sequence=(self.sequence).replace(u'\u064f', u'o'); 
        self.sequence=(self.sequence).replace(u"\u0650", u'e'); 
        self.sequence=(self.sequence).replace(u"\u0622", u'0');#Is it valid? I think it's simply mistake...
        self.sequence=(self.sequence).replace(u"\u0627", u'0');
        self.sequence=(self.sequence).replace(u"\u0629", u'P');
        self.sequence=(self.sequence).replace(u"\u06A9", u'k');
        self.sequence=(self.sequence).replace(u"\u06cc", u'i');
        self.sequence=(self.sequence).replace(u"\u0621", u'M');
        self.sequence=(self.sequence).replace(u"\u06C0", u'X');
        self.sequence=(self.sequence).replace(u"\u0626", u'I');
        self.sequence=(self.sequence).replace(u"\u0624", u'U');
        self.sequence=(self.sequence).replace(u"\u064b", u'N');
        self.sequence=(self.sequence).replace(u"\u0651", u'~');        
        self.sequence=(self.sequence).replace(u"\u060C", u',');
        self.sequence=(self.sequence).replace(u"\u061B", u';');
        self.sequence=(self.sequence).replace(u"\u061F", u'?');
        self.sequence=(self.sequence).replace(u"\u066A", u'%');
        self.sequence=(self.sequence).replace(u"\u00ab", u'{');
        self.sequence=(self.sequence).replace(u"\u00bb", u'}');
        self.sequence=(self.sequence).replace(u"\u200C", u'_');
        return self.sequence;
    def main(self):
        char_map=self.original_unicode();
        self.sequence=self.converting_to_other();
        return self.sequence;

if __name__=='__main__':
    ex_sent=u'من کتاب دادم';
    ins=transliter(ex_sent);
    print ins.main();



