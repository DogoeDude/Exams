class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, score):
        if score <= 10:
            self.score += score
        else:
            print(f"Score denied for {self.name}. The score should not exceed 10 points.")

    def __str__(self):
        return f"{self.name}: {self.score}"

class LinkedListNode:
    def __init__(self, player):
        self.player = player
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, player):
        new_node = LinkedListNode(player)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

def get_winner(players):
    max_score = 0
    winners = []
    current = players.head

    while current:
        if current.player.score > max_score:
            max_score = current.player.score
            winners = [current.player]
        elif current.player.score == max_score:
            winners.append(current.player)
        current = current.next

    return winners

def main():
    num_players = int(input("Enter the number of players: "))

    players_array = []
    players_stack = []
    players_linked_list = LinkedList()

    for i in range(num_players):
        name = input(f"Enter the name of Player {i + 1}: ")
        player = Player(name)
        players_array.append(player)
        players_stack.append(player)
        players_linked_list.append(player)

    rounds = 3

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}")
        for player in players_array:
            while True:
                try:
                    score = int(input(f"Enter the score for {player.name}: "))
                    if 0 <= score <= 10:
                        player.add_score(score)
                        break  # Exit the loop when a valid score is provided
                    else:
                        print("Invalid input. Please enter a score between 0 and 10.")
                except ValueError:
                    print("Invalid input. Please enter a valid score.")

        for player in players_array:
            print(player)


    print("\nScores after all rounds (Arrays):")
    for player in players_array:
        print(player)

    print("\nScores after all rounds (Stacks):")
    for player in players_stack:
        print(player)

    print("\nScores after all rounds (Linked List):")
    current = players_linked_list.head
    while current:
        print(current.player)
        current = current.next

    print("\nDetermining the winner...")

    winners_array = get_winner(players_linked_list)
    winners_stack = get_winner(players_linked_list)
    winners_linked_list = get_winner(players_linked_list)

    if winners_array:
        print("\nWinner(s) (Arrays):")
        for winner in winners_array:
            print(winner)

    if winners_stack:
        print("\nWinner(s) (Stacks):")
        for winner in winners_stack:
            print(winner)

    if winners_linked_list:
        print("\nWinner(s) (Linked List):")
        for winner in winners_linked_list:
            print(winner)

if __name__ == "__main__":
    main()
