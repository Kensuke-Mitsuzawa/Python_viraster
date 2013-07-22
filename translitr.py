#! /usr/bin/python
# -*- coding:utf-8 -*-

import sys, codecs;

class transliter:
    """
    Input is assumed as type:string encoding:utf-8.
    """
    def __init__(self, sequence):
        self.sequence=sequence;
    def python_unicode(self):
        self.unicode_map={};
        coding='utf-8';
        self.unicode_map.setdefault('alf', unicode('ا', coding));
        self.unicode_map.setdefault('be', unicode('ب', coding));
        self.unicode_map.setdefault('pe', unicode('پ', coding));
        self.unicode_map.setdefault('t1', unicode('ت', coding));
        self.unicode_map.setdefault('s1', unicode('ث', coding));
        self.unicode_map.setdefault('j1', unicode('ج', coding));
        self.unicode_map.setdefault('ch', unicode('چ', coding));
        self.unicode_map.setdefault('h1', unicode('ح', coding));       
        self.unicode_map.setdefault('x', unicode('خ', coding));
        self.unicode_map.setdefault('d', unicode('د', coding));
        self.unicode_map.setdefault('z1', unicode('ذ', coding));
        self.unicode_map.setdefault('r', unicode('ر', coding));
        self.unicode_map.setdefault('z2', unicode('ز', coding));
        self.unicode_map.setdefault('j2', unicode('ژ',coding));
        self.unicode_map.setdeault('s1', unicode('س', coding));
        self.unicode_map.setdefault('sh', unicode('ش', coding));
        self.unicode_map.setdefault('s2', unicode('ص', coding));
        self.unicode_map.setdefault('z2', unicode('ض', coding));
        self.unicode_map.setdefault('t2', unicode(u'ط', coding));
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




if __name__=='__main__':
    ex_sent=u'من کتاب دادم';
    ins=transliter(ex_sent);
    print ins.python_unicode();



