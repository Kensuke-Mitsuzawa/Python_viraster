#/usr/bin/python
# -*- coding:utf-8 -*-
__author__='Kensuke Mitsuzawa'
__version__='2013/11/11'

import os, commands, translitr, sys, re, argparse, codecs;

"""
This code is written for converting arabic and to latin and latin to arabic toward specific file.
"""

def transliteration_whole(input_file_path, output_file_path, args):
    print 'Whole transliteration'
    print 'Mode is {}'.format(args.mode);
    out=codecs.open(output_file_path, 'w', 'utf-8');
    if args.mode=='a_l':
        if args.preper==True:
            status_tuple=commands.getstatusoutput('ruby1.8 ./pre_per2.rb {0} > {1}'.format(input_file_path, './tmp_file_1'));
            if status_tuple[0]!=0:
                sys.exit(status_tuple);
            with codecs.open('./tmp_file_1', 'r', 'utf-8') as input_line:
                for line in input_line:
                    Ins=translitr.transliter(line);
                    out.write(Ins.arabic_to_unicode());
        else:
            with codecs.open(input_file_path, 'r', 'utf-8') as input_line:
                for line in input_line:    
                    Ins=translitr.transliter(line);
                    out.write(Ins.arabic_to_unicode());
        os.remove('./tmp_file_1');
    elif args.mode=='l_a':
        with codecs.open(input_file_path, 'r', 'utf-8') as input_line:
            for line in input_line:
                Ins=transliter.transliter(line);
                out.write(Ins.unicode_to_arabic());
    out.close();

def latin_to_arabic(input_file_path, output_file_path, sep_type, column_n):
    print 'Transliterate from Latin to Arabic'
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
    print 'Transliterate from Arabic to Latin'
    out=codecs.open(output_file_path, 'w', 'utf-8');
    if args.preper==True:
        status_tuple=commands.getstatusoutput('ruby1.8 ./pre_per2.rb {0} > {1}'.format(input_file_path, './tmp_file_1'));
        if status_tuple[0]!=0:
            sys.exit(status_tuple);
        with codecs.open('./tmp_file_1', 'r', 'utf-8') as input_line:
            for line in input_line:
                items=line.split(sep_type);
                Ins=translitr.transliter(line.split(sep_type)[column_n]);
                if column_n==0:
                    out.write(Ins.arabic_to_unicode()+sep_type+sep_type.join(items[column_n+1:-1])+u'\n' );
                elif column_n==-1:
                    out.write(sep_type.join(items[0:len(items)-1])+sep_type+Ins.arabic_to_unicode()+u'\n' );
                #TODO　あと，ここに中間のindexに対する記述をしていく
        os.remove('./tmp_file_1');

    else:
        with codecs.open(input_file_path, 'r', 'utf-8') as lines:
            for line in lines:
                items=line.split(sep_type);
                Ins=translitr.transliter(line.split(sep_type)[column_n]);
                if column_n==0:
                    out.write(Ins.arabic_to_unicode()+sep_type+sep_type.join(items[column_n+1:-1])+u'\n' );
                elif column_n==-1:
                    out.write(sep_type.join(items[0:len(items)-1])+sep_type+Ins.arabic_to_unicode()+u'\n' );
    out.close();

def main():
    parser=argparse.ArgumentParser(description='');
    parser.add_argument('input_file_path');
    parser.add_argument('output_file_path');
    parser.add_argument('-s', '--sep', required=False, default='\t', help='which separate type? t(tab)');
    parser.add_argument('-preper', '--preper', action='store_true', help='If you use preper2 from arabic to unicode, add this flag')
    parser.add_argument('-m', '--mode', required=True, help='a_l or l_a');
    parser.add_argument('-c_m', '--column_n', required=False, default=0, help='column number');
    parser.add_argument('-w', '--whole', required=False, default=False, action='store_true',help='whole mode, True if -w flag');
    args=parser.parse_args();
    if args.preper==True:
        print 'Preper:True';
    else:
        print 'Preper:False';
    if args.whole==True: 
        transliteration_whole(args.input_file_path, args.output_file_path, args);
    elif args.mode=='l_a':
        latin_to_arabic(args.input_file_path, args.output_file_path, args.sep, args.column_n);
    elif args.mode=='a_l':
        arabic_to_latin(args.input_file_path, args.output_file_path, args.sep, args.column_n, args);

if __name__=='__main__':
    main();
