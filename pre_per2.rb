#!/usr/bin/ruby
# -*- coding: utf-8 -*-
#
# pre_per.rb: normalizes Persian texts
#
#-------------------------------------------------------------------------------
# Copyright (C) 2012  Mojgan Seraji  <mojgan.seraji@lingfil.uu.se>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#-------------------------------------------------------------------------------
#
#
#

require 'rubygems'
#re-written by Kensuke Mistuzawa
require './virastar/lib/virastar'

my_file = ARGV[0].to_s

open(my_file,"r:UTF-8") do |f|
  while line = f.gets
    newline = line.persian_cleanup
    # my own edit rules
    # Suffixations
    
    newline.gsub!(/\s+(((زا(ی)?)?|ام?|ات|اش|ای?(د)?|ایم?|اند?)[\.\!\?\،]*)\s+/,'‌\1 ')
   
    newline.gsub!(/\s+(های)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(هاای)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(ایی)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(ای)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(ی)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(یی)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(م|ت|ش|مان|تان|شان)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(هایی|هایم|هایت|هایش|هایمان|هایتان|هایشان)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(م|ی|د|یم|ید|ند)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(ان)\s+/,'‌\1 ')

    newline.gsub!(/\s+(ین)\s+/,'‌\1 ')

    newline.gsub!(/\s+(ات)\s+/,'‌\1 ')

    newline.gsub!(/\s+(جات)\s+/,'‌\1 ')

    newline.gsub!(/\s+(آور)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(نشین)\s+/,'‌\1 ')  
    
    newline.gsub!(/(\s+)(ابداع)\s+(کننده)(\s+)/,'‌\1\2‌\3\4')
    
    newline.gsub!(/(\s+)(ابر)\s+(اتم)(\s+)/,'‌\1\2‌\3\4')
    
    newline.gsub!(/\s+(پاش(ی)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(پوش(ان)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(شناس(ی)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(شکن(ی)?)\s+/,'‌\1 ')
      
    newline.gsub!(/\s+(پذیر(ی)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(اندود)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(فشان(ی|ها(ی)?))\s+/,'‌\1 ')
    
    newline.gsub!(/(\s+)(آبله)\s+(مرغان)(\s+)/,'‌\1\2‌\3\4')
    
    newline.gsub!(/\s+(سازی)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(آلود(ی)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(آمیز(ی)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(زدا(ی(ی)?)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(انگیز(ی)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(خیز(ی)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(پور)\s+/,'‌\1 ')
    
    newline.gsub!(/(\s+)(آزاد)\s+(راه)(\s+)/,'‌\1\2‌\3\4')
    
    newline.gsub!(/(\s+)(راه)\s+(آهن)(\s+)/,'‌\1\2‌\3\4')
    
    newline.gsub!(/(\s+)(راه)\s+(حل)(\s+)/,'‌\1\2‌\3\4')
    
    newline.gsub!(/(\s+)(راه)\s+(حلی)(\s+)/,'‌\1\2‌\3\4')
    
    newline.gsub!(/(\s+)(راه)\s+(اندازی)(\s+)/,'‌\1\2‌\3\4')
    
    newline.gsub!(/\s+(سوزی(ها(ی)?)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(پراکنی)\s+/,'‌\1 ')
    
    newline.gsub!(/(\s+)(اثنی)\s+(عشر)(\s+)/,'‌\1\2‌\3\4')
    
    newline.gsub!(/(\s+)(اثنی)\s+(عشری)(\s+)/,'‌\1\2‌\3\4')
    
    newline.gsub!(/\s+(خوری)\s+/,'‌\1 ')
   
    newline.gsub!(/\s+(گویان)\s+/,'‌\1 ')

    newline.gsub!(/(\s+)(دوان)\s+(دوان)(\s+)/,'‌\1\2‌\3\4')

    newline.gsub!(/\s+(افکنی)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(دان(ان)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(پرور(ی)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(پریش(ی)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(نویس(ی(ی)?)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(ربایان)\s+/,'‌\1 ')

    newline.gsub!(/\s+(کشان(ی)?)\s+/,'‌\1 ')
    
    newline.gsub!(/(\s+)(کشان)\s+(کشان)(\s+)/,'‌\1\2‌\3\4')
    
    newline.gsub!(/(\s+)(الدرم)\s+(بلدرم)(\s+)/,'‌\1\2‌\3\4')
    
    newline.gsub!(/\s+(وار(ه)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(مداران)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(ساله)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(پاشیدگی)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(شناسان)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(وند)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(کاران(ه)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(پژوه(ی)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(زا(یی|ای)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(زدایی)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(ریزان)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(کنندگی)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(زاد)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(سنج(ی)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(کنان)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(پرداز(ی)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(رسانی)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(زی)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(وار(ه)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(یاب(ی)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(گان(ه)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(پیما(ها(ی(ی)?)?)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(گی)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(گر(ی)?)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(یت)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(کان)\s+/,'‌\1 ')

    newline.gsub!(/\s+(اک)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(ناک)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(ک)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(انه)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(ه)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(مند)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(ور)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(گین)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(سار)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(ساعته)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(اً)\s+/,'‌\1 ')

    newline.gsub!(/\s+(ار)\s+/,'‌\1 ')
    
    newline.gsub!(/\s+(گار)\s+/,'‌\1 ')
    
    
    # Prefix notations
=begin      
    newline.gsub!(/\s+(نا)\s+/,'‌ \1‌')    
    
    newline.gsub!(/\s+(غیر)\s+/,'‌ \1‌') 
    
    newline.gsub!(/\s+(بی)\s+/,'‌ \1‌') 

    newline.gsub!(/\s+(فرا)\s+/,'‌ \1‌') 
   
    newline.gsub!(/\s+(عدم)\s+/,'‌ \1‌') 
    
    newline.gsub!(/\s+(سوء)\s+/,'‌ \1‌') 
    
    newline.gsub!(/\s+(سوأ)\s+/,'‌ \1‌') 
=end
#from here I rewrite for my purpose
    newline.gsub!(/\s+(نا)\s+/,' \1‌')    
    
    newline.gsub!(/\s+(غیر)\s+/,' \1‌') 
    
    newline.gsub!(/\s+(بی)\s+/,' \1‌') 

    newline.gsub!(/\s+(فرا)\s+/,' \1‌') 
   
    newline.gsub!(/\s+(عدم)\s+/,' \1‌') 
    
    newline.gsub!(/\s+(سوء)\s+/,' \1‌') 
    
    newline.gsub!(/\s+(سوأ)\s+/,' \1‌') 
 
    puts newline
  end
end

