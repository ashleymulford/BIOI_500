#import biopython classes
from Bio.Seq import Seq
from Bio import SeqIO

file = open("/Users/ashle/Downloads/rosalind_long.txt")

slist = []

#pull ids and seqs out of file
for record in SeqIO.parse(file, "fasta"):
    slist.append(str(record.seq))

longest_overlap_start = ""
longest_overlap_end = ""
count = 0
for i in range(len(slist)):
    seq1 = slist[i]
    for seq in slist:
        #seqs will overlap by at least 50% so len/2+1
        for i in range(1, int(len(seq1)/2)+1):
            #get start and end substring of seq1
            start = seq1[:-i]
            end = seq1[i:]
            #calculate overlap quantity being tested
            overlap_quant = len(seq1)-i
            #check if seq start/ends with the end/start of seq1
            if seq.endswith(start):
                #if overlap amount exceeds max, save seqs and update count
                if (overlap_quant)>count:
                    count = overlap_quant
                    longest_overlap_start = seq
                    longest_overlap_end = seq1
            if seq.startswith(end):
                if (overlap_quant)>count:
                    count = overlap_quant
                    longest_overlap_start = seq1
                    longest_overlap_end = seq
overlap_list = [longest_overlap_start, longest_overlap_end, count]

#get values from list output from longest overlap
count_index = len(overlap_list)-1
s1 = overlap_list[0]
s2 = overlap_list[1]
#count will always be last item in list
ov_count = overlap_list[count_index]
#get merged string
s3 = s1 + s2[ov_count:]
#remove old strings from list and add new merged string
slist.remove(s1)
slist.remove(s2)
slist.append(s3)


###once we have initial merged string in slist, use functions
###merged string is in last position in slist


#function - find string with longest overlap with merged string
def longest_overlap(seq_list):
    longest_overlap_start = ""
    longest_overlap_end = ""
    count = 0
    seq1 = seq_list[len(seq_list)-1]
    for seq in seq_list:
        #seqs will overlap by at least 50% so len/2+1
        for i in range(1, int(len(seq1))):
            #get start and end substring of seq1
            start = seq1[:-i]
            end = seq1[i:]
            #calculate overlap quantity being tested
            overlap_quant = len(seq1)-i
            #check if seq start/ends with the end/start of seq1
            if seq.endswith(start):
                #if overlap amount exceeds max, save seqs and update count
                if (overlap_quant)>count:
                    count = overlap_quant
                    longest_overlap_start = seq
                    longest_overlap_end = seq1
            if seq.startswith(end):
                if (overlap_quant)>count:
                    count = overlap_quant
                    longest_overlap_start = seq1
                    longest_overlap_end = seq
    #as long as overlap occurs
    if count != 0:
        #add values to list and return
        overlap_list = [longest_overlap_start, longest_overlap_end, count]
        return overlap_list
    #in case there is no overlap
    else:
        overlap_list = seq_list
        overlap_list.append(0)
        return overlap_list
        

#function - merge output of longest_overlap together to get one string
def merge_and_remove(ov_pair, seq_list):
    #get values from list output from longest_overlap
    count_index = len(ov_pair)-1
    s1 = ov_pair[0]
    s2 = ov_pair[1]
    #count will always be last item in list
    ov_count = ov_pair[count_index]
    #if overlap
    if ov_count != 0:
        #get merged string
        s3 = s1 + s2[ov_count:]
        #remove old strings from list and add new merged string
        seq_list.remove(s1)
        seq_list.remove(s2)
        seq_list.append(s3)
        print(seq_list)
        #return updated, shorter list
        return seq_list
    #if no overlap
    else:
        print(seq_list)
        superstring = ""
        for i in range(len(seq_list)):
            #removes extra zero from list
            if seq_list[i] != 0:
                #concatinate remaining strings
                superstring = superstring + seq_list[i]
        #empty list so while loop ends
        seq_list = []
        #print sequence
        print(superstring)
        return seq_list



#go through list until one superstring
while len(slist)>1:
    overlap_pair = longest_overlap(slist)
    slist = merge_and_remove(overlap_pair, slist)

#only print if seq in list, only happens if always overlap until one superseq
if len(slist) != 0:
    print(slist[0])


