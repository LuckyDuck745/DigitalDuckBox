import random
import time

def duck_decider():
    print("🦆 Welcome to the DigitalDuckBox Decider!")
    question = input("What is your question, human? ")
    
    print("\nThinking...")
    # Add a little "processing" delay for effect
    time.sleep(1.5)
    
    responses = [
        "Quack! (That's a definite YES)",
        "Waddle waddle... (Probably not)",
        "*Flaps wings enthusiastically* (YES!)",
        "The pond is murky. Ask again later.",
        "Quack? (I'm not sure, try a different snack first)",
        "NO. *Angry duck noises*"
    ]
    
    print(f"\nTHE DUCK SAYS: {random.choice(responses)}")

if __name__ == "__main__":
    duck_decider()
