# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 18:20:37 2022

@author: quill
"""

from Bio import ExPASy, SeqIO

def fetch_genbank(sid):
    #fetches a genbank file (sid = sequence ID) from Uniprot
    try:
        handle = ExPASy.get_sprot_raw(sid)
        seq = SeqIO.read(handle,'swiss')
        SeqIO.write(seq, sid+'.genbank','genbank')
        #print(sid,'sequence length',len(seq))
    except Exception:
        print (sid,'not found')

def read_genbank(fname):
    #extracts the organism name and the sequence
    #from a local genbank file
    f = open(fname)
    for p in SeqIO.parse(f,'genbank'):
        break
    f.close()
    return p.annotations['organism'],str(p.seq)
    
#fetch a genbank file for a specific sequence ID 
#and read in the organism and the sequence.

fetch_genbank('B4F440')

organism,seq = read_genbank('B4F440.genbank')

print(organism)
print(seq)