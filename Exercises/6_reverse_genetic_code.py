# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:50:00 2022

@author: quill
"""

cdn = {}
cdn['ttt'] = cdn['ttc'] = 'F phenylalanine'
cdn['tta'] = cdn['ttg'] = 'L leucine'
cdn['tct'] = cdn['tcc'] = cdn['tca'] = cdn['tcg'] = 'S serine'
cdn['tat'] = cdn['tac'] = 'Y tyrosine'
cdn['taa'] = cdn['tag'] = '* stop'
cdn['tgt'] = cdn['tgc'] = 'C cysteine'
cdn['tga'] = '* stop'
cdn['tgg'] = 'W tryptophan'
cdn['ctt'] = cdn['ctc'] = cdn['cta'] = cdn['ctg'] = 'L leucine'
cdn['cct'] = cdn['ccc'] = cdn['cca'] = cdn['ccg'] = 'P proline'
cdn['cat'] = cdn['cac'] = 'H histidine'
cdn['caa'] = cdn['cag'] = 'Q glutamine'
cdn['cgt'] = cdn['cgc'] = cdn['cga'] = cdn['cgg'] = 'R arginine'
cdn['att'] = cdn['atc'] = cdn['ata'] = 'I isoleucine'
cdn['atg'] = 'M methionine'
cdn['act'] = cdn['acc'] = cdn['aca'] = cdn['acg'] = 'T threonine'
cdn['aat'] = cdn['aac'] = 'N asparagine'
cdn['aaa'] = cdn['aag'] = 'K lysine'
cdn['agt'] = cdn['agc'] = 'S serine'
cdn['aga'] = cdn['agg'] = 'R arginine'
cdn['gtt'] = cdn['gtc'] = cdn['gta'] = cdn['gtg'] = 'V valine'
cdn['gct'] = cdn['gcc'] = cdn['gca'] = cdn['gcg'] = 'A alanine'
cdn['gat'] = cdn['gac'] = 'D aspartic acid'
cdn['gaa'] = cdn['gag'] = 'E glutamic acid'
cdn['ggt'] = cdn['ggc'] = cdn['gga'] = cdn['ggg'] = 'G glycine'

# we start by storing seperately the keys and values in two seperate lists

letter = []
codons = []


for i in cdn.values():
    letter.append(i[0])
    
for i in cdn.keys():
    codons.append(i)
    
#create new dict from the values of cdn (letters)   
aacid = dict.fromkeys(letter)


    
#add the new values by iterating over the keys of aacid (letters)
for ltr in aacid:
    #init with list
    aacid[ltr] = []
    #append codon based on index of the tested letter
    for index,ltr2 in enumerate(letter):
        if ltr2 == ltr:
            aacid[ltr].append(codons[index])
            
print(sorted(aacid["F"]))
    
