def read(blast):
    df= pd.read_csv(blastfile, sep='\t', names = ["qseqid", "sseqid", "pident", "length", "mismatch", "gapopen", "qstart", "qend", "sstart", "send", "evalue", "bitscore", "sseq"])
    sseqid = df["sseqid"].values.tolist()
    return(sseqid)

def annot(proteome):
    outgroups=[]
    for record in SeqIO.parse(proteomefile, "fasta"):
        if (record.id).rstrip() in sseqid:
            outgroups.append(record)
    SeqIO.write(outgroups, annot, "fasta")
    return annot

def ids(annot):
    with open(annot) as handle:
        accession=[]
        for record in SeqIO.parse(handle, "fasta"):
            record.id=record.id.split("|")[1]
            record.description=""
            accession.append(record)
        SeqIO.write(accession, ids, "fasta")
        return ids

def main(proteomefile, annot):
    outgroups = extract_seqs(proteomefile)
    extract_ids(annot)
    return


