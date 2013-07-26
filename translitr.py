
# -*- coding:utf-8 -*-
__authot__='Kensuke Mitsuzawa';
__version__='0.03';

import sys, codecs, itertools, re;

class transliter:
    """
    Input is assumed as type:string encoding:utf-8.
    """
    def __init__(self, sequence):
        self.sequence=sequence;
        self.exceptin_words=[u' ', u':', u'\n', u'\t', u'>', u'-', u'.', u'\u0650'];
    
    def clean_up(self): 
        #Diacritics
        diacritics = set([u'\u0610',u'\u0611',u'\u0612',u'\u0613',u'\u0614',u'\u0615',u'\u0616',
                          u'\u0617',u'\u0618',u'\u0619',u'\u061a',u'\u064b',u'\u064c',u'\u064d',
                          u'\u064e',u'\u064f',u'\u0650',u'\u0651',u'\u0652',u'\u0653',u'\u0654',
                          u'\u0655',u'\u0656',u'\u0657',u'\u0658',u'\u0659',u'\u065a',u'\u065b',
                          u'\u065c',u'\u065d',u'\u065e',u'\u065f',u'\u0670',u'\u06d6',u'\u06d7',
                          u'\u06d8',u'\u06d9',u'\u06da',u'\u06db',u'\u06dc',u'\u06df',u'\u06e0',
                          u'\u06e1',u'\u06e2',u'\u06e3',u'\u06e4',u'\u06e7',u'\u06e8',u'\u06ea',
                          u'\u06eb',u'\u06ec',u'\u06ed'])
        for item in diacritics:
            self.cleaned_sequence=re.sub(item, u'', self.sequence);    
        return self.cleaned_sequence; 
    
    def arabic_to_inter(self):
        "Input of this method is the unicode type of arabic(persian) character."
        self.arabic_uni_map={};

        self.arabic_uni_map.setdefault(u'\u0654', 'arabic_hamza_above');
        self.arabic_uni_map.setdefault(u"\u0622", 'arabic_alef_madda_above');
        self.arabic_uni_map.setdefault(u"\u0623", 'arabic_alef_hamza_above');
        self.arabic_uni_map.setdefault(u'ب', 'be');
        self.arabic_uni_map.setdefault(u'پ', 'pe');
        self.arabic_uni_map.setdefault(u'ت', 'te');
        self.arabic_uni_map.setdefault(u'ث', 'se_1');
        self.arabic_uni_map.setdefault(u'ج', 'jim');
        self.arabic_uni_map.setdefault(u'چ', 'ch');
        self.arabic_uni_map.setdefault(u'ح', 'he');       
        self.arabic_uni_map.setdefault(u'خ', 'x');
        self.arabic_uni_map.setdefault(u'د', 'd');
        self.arabic_uni_map.setdefault(u'ذ', 'zal');
        self.arabic_uni_map.setdefault(u'ر', 'r');
        self.arabic_uni_map.setdefault(u'ز', 'ze');
        self.arabic_uni_map.setdefault(u'ژ', 'je');
        self.arabic_uni_map.setdefault(u'س', 'se_2');
        self.arabic_uni_map.setdefault(u'ش', 'sh');
        self.arabic_uni_map.setdefault(u'ص', 'sad');
        self.arabic_uni_map.setdefault(u'ض', 'zad');
        self.arabic_uni_map.setdefault(u'ع', 'ein');
        self.arabic_uni_map.setdefault(u'غ', 'qein');
        self.arabic_uni_map.setdefault(u'ف', 'f');
        self.arabic_uni_map.setdefault(u'ق', 'qaf');
        self.arabic_uni_map.setdefault(u'گ', 'gaf');
        self.arabic_uni_map.setdefault(u'ل', 'l');
        self.arabic_uni_map.setdefault(u'م', 'm');
        self.arabic_uni_map.setdefault(u'ن', 'n');
        self.arabic_uni_map.setdefault(u'و', 'v');
        self.arabic_uni_map.setdefault(u'ه', 'h');
        self.arabic_uni_map.setdefault(u'ط', 'ta');
        self.arabic_uni_map.setdefault(u'ظ', 'za');
        self.arabic_uni_map.setdefault(u'\u0649', 'alef_maksusa'); #U0649 is ARABIC_ALEF_MAKSUSA
        self.arabic_uni_map.setdefault(u"\u064A", 'arabic_ye');
        self.arabic_uni_map.setdefault(u"\u06CC", 'persian_ye');
        self.arabic_uni_map.setdefault(u"\u0643", 'arabic_keh');
        self.arabic_uni_map.setdefault(u"\u06A9", 'persian_keh');
        #diacritics from here
        self.arabic_uni_map.setdefault(u'\u0621', 'arabic_hamza');
        self.arabic_uni_map.setdefault(u"\u0627", 'arabic_alef');
        self.arabic_uni_map.setdefault(u"\u064b", 'arabic_fathatan');
        self.arabic_uni_map.setdefault(u"\u060C", 'arabic_comma');
        self.arabic_uni_map.setdefault(u"\u061B", 'arabic_semicolon');
        self.arabic_uni_map.setdefault(u"\u061F", 'arabic_question');
        self.arabic_uni_map.setdefault(u"\u066A", 'arabic_percent');
        self.arabic_uni_map.setdefault(u"\u00ab", 'arabic_quotation_open');
        self.arabic_uni_map.setdefault(u"\u00bb", 'arabic_quotation_close');
        self.arabic_uni_map.setdefault(u"\u200C", 'ZWNJ');
        self.arabic_uni_map.setdefault(u"۰", 'zero');
        self.arabic_uni_map.setdefault(u"۱", 'one');
        self.arabic_uni_map.setdefault(u"۲", 'two');
        self.arabic_uni_map.setdefault(u"۳", 'three');
        self.arabic_uni_map.setdefault(u"۴", 'four');
        self.arabic_uni_map.setdefault(u"۵", 'five');
        self.arabic_uni_map.setdefault(u"۶", 'six');
        self.arabic_uni_map.setdefault(u"۷", 'seven');
        self.arabic_uni_map.setdefault(u"۸", 'eight');
        self.arabic_uni_map.setdefault(u"۹", 'nine');
        #self.arabic_uni_map.setdefault(u"\u0629", 'arabic_teh_marbuta');        
        #self.arabic_uni_map.setdefault(u"\u06C0", 'arabic_he_yeh_above');
        self.arabic_uni_map.setdefault(u"\u0626", 'arabic_ye_hamza_above');
        #self.arabic_uni_map.setdefault(u"\u0624", 'arabic_v_hamza_above');
        #self.arabic_uni_map.setdefault(u"\u0651", 'arabic_shadda');
        #self.arabic_uni_map.setdefault(u"\u064E", 'arabic_fatha'); 
        #self.arabic_uni_map.setdefault(u'\u064F', 'arabic_damma'); 
        #self.arabic_uni_map.setdefault(u"\u0650", 'arabic_kasra'); 

        return self.arabic_uni_map;
        #return self.sequence;

    def unicode_original(self):
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
        self.char_map.setdefault('se_1', u'ç');
        self.char_map.setdefault('jim', u'j');
        self.char_map.setdefault('he', u'ħ');
        self.char_map.setdefault('x', u'x');
        self.char_map.setdefault('d', u'd');
        self.char_map.setdefault('zal', u'đ');
        self.char_map.setdefault('r', u'r');
        self.char_map.setdefault('arabic_r_small_v_below', u'ř');
        self.char_map.setdefault('ze', u'z');
        self.char_map.setdefault('se_2', u's');
        self.char_map.setdefault('sh', u'š');
        self.char_map.setdefault('sad', u'ş');
        self.char_map.setdefault('zad', u'ź');
        self.char_map.setdefault('ta',u'ţ');
        self.char_map.setdefault('za', u'ẓ');
        self.char_map.setdefault('ein', u"'");
        self.char_map.setdefault('qein', u'q');
        self.char_map.setdefault('f', u'f');
        #self.char_map.setdefault('v', u'\u06A4'); #arabic veh
        self.char_map.setdefault('qaf', u'ŕ');
        self.char_map.setdefault('arabic_keh', u'K');
        self.char_map.setdefault('persian_keh', u'K');
        self.char_map.setdefault('gaf', u'g');
        self.char_map.setdefault('l', u'l');
        self.char_map.setdefault('m', u'm');
        self.char_map.setdefault('n', u'n');
        self.char_map.setdefault('h', u'h');
        self.char_map.setdefault('v', u'w');
        self.char_map.setdefault('persian_ye', u'y');
        self.char_map.setdefault('alef_maksusa', u'Ý');
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
    def arabic_to_unicode(self):
        self.char_map=self.unicode_original();
        self.intermap=self.arabic_to_inter();
        #remove diacritic_marks form input sequece
        self.cleaned_sequence=self.clean_up();
        self.unicode_char=u'';
        self.converted_sequence=u'';
        for char in self.sequence:
            if char in self.exceptin_words:
                self.unicode_char=char;
            elif char not in self.intermap:
                self.unicode_char=char; 
            else:
                self.unicode_char=self.char_map[self.intermap[char]];
            self.converted_sequence=self.converted_sequence+self.unicode_char;
        return self.converted_sequence;
    def unicode_to_arabic(self):
        char_map=self.unicode_original();
        
        del self.char_map['arabic_keh']; del self.char_map['arabic_ye'];
        self.reversed_char_map=dict(zip(self.char_map.itervalues(), self.char_map.iterkeys())); 
        
        self.intermap=self.arabic_to_inter();
        self.reversed_intermap=dict(zip(self.intermap.itervalues(), self.intermap.iterkeys()));
        del self.reversed_intermap['arabic_ye']; del self.reversed_intermap['arabic_keh'];
        
        self.unicode_char=u'';
        self.converted_sequence=u'';
        for char in self.sequence:
            if char not in self.reversed_char_map:
                self.unicode_char=char;
            else:
                self.unicode_char=self.reversed_intermap[self.reversed_char_map[char]];
            self.converted_sequence=self.converted_sequence+self.unicode_char;
        return self.converted_sequence;


def main():
    input_file_all_line=codecs.open(sys.argv[1], 'r', 'utf-8').read(); 
    unicode_writeout=codecs.open('unicode_sequecen', 'w', 'utf-8');
    ins=transliter(input_file_all_line);
    unicode_sequence=ins.arabic_to_unicode();
    unicode_writeout.write(unicode_sequence);

    arabic_sequence=codecs.open('reveresed_arabic', 'w', 'utf-8');
    ins_2=transliter(unicode_sequence);
    reversed_arabic_sequence=ins_2.unicode_to_arabic();
    arabic_sequence.write(reversed_arabic_sequence);

if __name__=='__main__':
    ex_sent=u'من کتاب دادم';
    ins=transliter(ex_sent);
    print ins.arabic_to_unicode();

    ex_sent_2=u'mn tw ra dÝdm';
    ins_2=transliter(ex_sent_2);
    print ins_2.unicode_to_arabic();

    main();

