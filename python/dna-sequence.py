class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dna_window = 10
        n = len(s)

        seen = set()
        repeated = set()
        for i in range(n-dna_window+1):
            dna_seq = s[i:i+dna_window]
            if dna_seq in seen:
                repeated.add(dna_seq)
            else:
                seen.add(dna_seq)
        return list(repeated)