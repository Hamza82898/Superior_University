
class VoterNode:
    def __init__(self, voter_id, name):
        self.voter_id = voter_id
        self.name = name
        self.next = None


class VoterLinkedList:
    def __init__(self):
        self.head = None

    def register_voter(self, voter_id, name):
        new_node = VoterNode(voter_id, name)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Voter {name} registered successfully.")

    def display_voters(self):
        current = self.head
        print("\n--- Registered Voters ---")
        while current:
            print(f"Voter ID: {current.voter_id}, Name: {current.name}")
            current = current.next


class BSTNode:
    def __init__(self, voter_id):
        self.voter_id = voter_id
        self.left = None
        self.right = None


class VoterBST:
    def __init__(self):
        self.root = None

    def insert(self, voter_id):
        self.root = self._insert_recursive(self.root, voter_id)

    def _insert_recursive(self, node, voter_id):
        if not node:
            return BSTNode(voter_id)
        if voter_id < node.voter_id:
            node.left = self._insert_recursive(node.left, voter_id)
        else:
            node.right = self._insert_recursive(node.right, voter_id)
        return node

    def search(self, voter_id):
        return self._search_recursive(self.root, voter_id)

    def _search_recursive(self, node, voter_id):
        if not node:
            return False
        if node.voter_id == voter_id:
            return True
        elif voter_id < node.voter_id:
            return self._search_recursive(node.left, voter_id)
        else:
            return self._search_recursive(node.right, voter_id)


class VoteGraph:
    def __init__(self):
        self.graph = {}

    def add_vote(self, voter_id):
        if voter_id in self.graph:
            self.graph[voter_id] += 1
        else:
            self.graph[voter_id] = 1

    def detect_fraud(self, voter_id):
        return self.graph.get(voter_id, 0) > 1


class VoterStack:
    def __init__(self):
        self.stack = []

    def push(self, voter_id):
        self.stack.append(voter_id)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def display(self):
        print("\n--- Last Voters (Stack) ---")
        for voter in reversed(self.stack):
            print(voter)


class VoterQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, voter_id):
        self.queue.append(voter_id)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def display(self):
        print("\n--- Voter Queue ---")
        for voter in self.queue:
            print(voter)


class VotingSystem:
    def __init__(self):
        self.voters = VoterLinkedList()
        self.voter_bst = VoterBST()
        self.vote_graph = VoteGraph()
        self.voter_stack = VoterStack()
        self.voter_queue = VoterQueue()
        self.candidates = ["Areesha", "Uzair", "Ali"]
        self.votes = {candidate: 0 for candidate in self.candidates}

    def register_voter(self, voter_id, name):
        self.voters.register_voter(voter_id, name)
        self.voter_bst.insert(voter_id)
        self.voter_queue.enqueue(voter_id)  

    def cast_vote(self, voter_id):
        if not self.voter_bst.search(voter_id):
            print("Voter ID not found! Please register first.")
            return

        if self.vote_graph.detect_fraud(voter_id):
            print("Fraud detected! You have already voted.")
            return

        if voter_id not in self.voter_queue.queue:
            print("You are not in the voting line!")
            return

        print("\nCandidates:", self.candidates)
        choice = input("Enter candidate name to vote: ")
        if choice not in self.candidates:
            print("Invalid candidate!")
            return

        self.votes[choice] += 1
        self.vote_graph.add_vote(voter_id)
        self.voter_stack.push(voter_id)  
        self.voter_queue.dequeue()       
        print(f"Vote casted successfully for {choice}!")

    def show_results(self):
        print("\n--- Election Results ---")
        sorted_results = sorted(self.votes.items(), key=lambda x: x[1], reverse=True)
        for candidate, count in sorted_results:
            print(f"{candidate}: {count} votes")
        print("\nWinner:", sorted_results[0][0])

    def show_registered_voters(self):
        self.voters.display_voters()

    def show_voting_queue(self):
        self.voter_queue.display()

    def show_recent_voters(self):
        self.voter_stack.display()

# Main Function
def main():
    voting_system = VotingSystem()

    while True:
        print("\n--- Online Voting System ---")
        print("1. Register Voter")
        print("2. Cast Vote")
        print("3. Show Results")
        print("4. Show Registered Voters")
        print("5. Show Voter Queue")
        print("6. Show Last Voters (Stack)")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            voter_id = input("Enter Voter ID: ")
            name = input("Enter Name: ")
            voting_system.register_voter(voter_id, name)

        elif choice == '2':
            voter_id = input("Enter your Voter ID: ")
            voting_system.cast_vote(voter_id)

        elif choice == '3':
            voting_system.show_results()

        elif choice == '4':
            voting_system.show_registered_voters()

        elif choice == '5':
            voting_system.show_voting_queue()

        elif choice == '6':
            voting_system.show_recent_voters()

        elif choice == '7':
            print("Exiting system. Thank you!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
