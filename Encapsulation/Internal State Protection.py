class VotingSystem:

    def __init__(self, candidate, votes):
        self.candidate = candidate
        self.__vote = votes

    def add_votes(self, vote_num):
        if vote_num > 1 or vote_num < 0:
            print("Inavlid No.of VOTES --> Fraud")
        else:
            self.__vote += 1 
        
    def get_votes(self):
        return f"Candidate {self.candidate} has gotten {self.__vote} votes"
    
    vote = property(get_votes, add_votes)
    
C = VotingSystem("Ram", 120)

print(C.get_votes())

print(C.add_votes(1000))

C.add_votes(1)
print(C.get_votes())

print()

# Using property fucntion 
C2 = VotingSystem("Rama", 120)

print(C2.vote)

C2.vote = 1000

C2.vote = 1

print(C2.vote)

