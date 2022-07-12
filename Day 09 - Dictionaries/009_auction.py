import art

print(art.logo)
print("Welcome to your personal auction!")
auction = {}
end_auction = ""


def highest_bidder(auction):
    winner = ""
    highest_offer = 0
    for offer in auction:
        if auction[offer] > highest_offer:
            winner = offer
            highest_offer = auction[offer]
    print(f"\nThe winner is {winner} with a bid of ${highest_offer}")


while end_auction != "N":
    name = input("\nWhat's your name?: ").capitalize()
    bid = int(input("What's your bid?: $"))
    auction[name] = bid
    end_auction = input("Are there any other bidders? [Y] or [N]: ").upper()

highest_bidder(auction)
