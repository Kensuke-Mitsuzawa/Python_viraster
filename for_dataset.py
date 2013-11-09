#/usr/bin/python
# -*- coding:utf-8 -*-

__author__='Kensuke Mitsuzawa'
__version__='2013/09/11'

import translitr, sys, re, argparse, codecs;

"""
This code is written for converting arabic and to latin and latin to arabic toward specific file.
"""
def transliteration_whole(input_file_path, output_file_path):
    out=codecs.open(output_file_path, 'w', 'utf-8');
    print 'OK'
    with codecs.open(input_file_path, 'r', 'utf-8') as input_line:
        for line in input_line:    
            Ins=translitr.transliter(line);
            out.write(Ins.arabic_to_unicode());
    out.close();

def latin_to_arabic(input_file_path, output_file_path, sep_type, column_n):
    out=codecs.open(output_file_path, 'w', 'utf-8');
    with codecs.open(input_file_path, 'r', 'utf-8') as input_line:
        for line in input_line:
            items=line.split(sep_type);
            Ins=translitr.transliter(line.split(sep_type)[column_n]);
            if column_n==0:
                out.write(Ins.unicode_to_arabic()+sep_type+sep_type.join(items[column_n+1:-1])+u'\n' );
            elif column_n==-1:
                out.write(sep_type.join(items[0:len(items)-1])+sep_type+Ins.unicode_to_arabic()+u'\n' );
            #TODO　あと，ここに中間のindexに対する記述をしていく
    out.close();

def arabic_to_latin(input_file_path, output_file_path, sep_type, column_n):
    out=codecs.open(output_file_path, 'w', 'utf-8');
    with codecs.open(input_file_path, 'r', 'utf-8') as input_line:
        for line in input_line:
            items=line.split(sep_type);
            Ins=translitr.transliter(line.split(sep_type)[column_n]);
            if column_n==0:
                out.write(Ins.arabic_to_unicode()+sep_type+sep_type.join(items[column_n+1:-1])+u'\n' );
            elif column_n==-1:
                out.write(sep_type.join(items[0:len(items)-1])+sep_type+Ins.arabic_to_unicode()+u'\n' );
            #TODO　あと，ここに中間のindexに対する記述をしていく
def main():
    parser=argparse.ArgumentParser(description='');
    parser.add_argument('input_file_path');
    parser.add_argument('output_file_path');
    parser.add_argument('-s', '--sep', required=False, default='\t', help='which separate type? t(tab)');
    parser.add_argument('-m', '--mode', required=True, help='a_l or l_a');
    parser.add_argument('-c_m', '--column_n', required=False, default=0, help='column number');
    parser.add_argument('-w', '--whole', required=False, default=False, action='store_true',help='whole mode, True if -w flag');
    args=parser.parse_args();
    if args.whole==True: 
        transliteration_whole(args.input_file_path, args.output_file_path);
    elif args.mode=='l_a':
        latin_to_arabic(args.input_file_path, args.output_file_path, args.sep, args.column_n);
    elif args.mode=='a_l':
        arabic_to_latin(args.input_file_path, args.output_file_path, args.sep, args.column_n);

if __name__=='__main__':
    main();
