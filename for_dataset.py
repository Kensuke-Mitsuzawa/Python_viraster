#/usr/bin/python
# -*- coding:utf-8 -*-

__author__='Kensuke Mitsuzawa'
__version__='2013/7/25'

import translitr, sys, re, argparse, codecs;

"""
This code is written for converting arabic to latin toward specific file.
"""
def transliteration_whole(input_file_path, output_file_path):
    out=codecs.open(output_file_path, 'w', 'utf-8');
    with codecs.open(input_file_path, 'r', 'utf-8') as input_line:
        for line in input_line:    
            Ins=translitr.transliter(line);
            #print [Ins.arabic_to_unicode()];
            out.write(Ins.arabic_to_unicode());
    out.close();

def main():
    parser=argparse.ArgumentParser(description='');
    parser.add_argument('input_file_path');
    parser.add_argument('output_file_path');
    parser.add_argument('-m', '--mode', required=False, default='t', help='which separate type? t(tab)');
    args=parser.parse_args();
   
    transliteration_whole(args.input_file_path, args.output_file_path);

if __name__=='__main__':
    main();
