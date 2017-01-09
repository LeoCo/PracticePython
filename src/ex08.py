# Make a two-player Rock-Paper-Scissors game.

victory = "Even"

player_a = input("Player a: ")
player_b = input("Player b: ")

if player_a == player_b:
    pass
elif player_a == "r" and player_b == "p":
    victory = "Player B"
elif player_a == "r" and player_b == "s":
    victory = "Player A"
