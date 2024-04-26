class Trie:
#T(C(N))==O(N) and S(C(1)) as it requires non memory space allocation iteratively
    def __init__(self):
        self.root={}#Initlizing Root 
        
    def insert(self, word: str) -> None:

        cur=self.root#inserting Current Node in Tree

        for letter in word:#Iterating Word's Letter
            if letter not in cur:#checking current letter
                cur[letter]={}#initializing current letter
            cur=cur[letter]#Word's Current Letter Contiguous alloct

        cur['*']=''#initializing Current index val

    def search(self, word: str) -> bool:

        cur=self.root#Trie's Current Root Declare
        for letter in word:#Iterating th
            if letter not in cur:
                return False#printing False to the Word's  unmatched letter
            cur=cur[letter]#Word's fixed Memory Allocation

        return '*' in cur#Printing * to Word's Matched Letter 
        
    def startsWith(self, prefix: str) -> bool:#Word's Starting Letter(Prefix) func decalre

        cur=self.root#Tree's Initialized Node declare
        for letter in prefix:#iterating Prefix's Each letter 
            if letter not in cur:#Checking  Word's each Letter
                return False
            cur=cur[letter]

        return True#Printing true to the Word's Matched Letter
