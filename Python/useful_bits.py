import random

def rand_seqs(minlen,maxlen):
	i = minlen
	seqs = []
	while i <= maxlen:
		rand_seq = ''.join(random.choice(['A','T','C','G']) for x in range(i))
		seqs.append(rand_seq)
		i += 1
	return seqs

def parse_fasta(lines):
	seqnum = 0
	for line in lines:
		if line.count('>'):
			seqnum += 1
	lineeach = [str]*(seqnum *2)
	i = 0
	for line in lines:
		if line.count('>'):
			if i > 0:
				i += 1
			line = line.replace('>','')
			lineeach[i] = line.rstrip()
			i += 1
		else:
			if isinstance(lineeach[i], types.StringTypes):
				lineeach[i] = lineeach[i] + line.rstrip()
			else:
				lineeach[i] = line.rstrip()
	ret = [str]*((len(lineeach)/2))
	i = 0
	j = 0
	while i < len(lineeach):
		ret[j] = [lineeach[i],lineeach[i+1]]
		i += 2
		j += 1
	return ret

def print_to_clipboard(string):
	from Tkinter import Tk
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(string)
	r.destroy()