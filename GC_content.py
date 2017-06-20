seq = 'AACGTCgTCACTCCAGGCcACTTCCGGCATAAGCATTAGCATAAAGCGCGTGAGA'

#Initialize the GC counter
n_gc = 0

#loop through the sequence and count g's and c's
for base in seq:
    if base in 'GCgc':
        n_gc += 1

print(n_gc / len(seq))
