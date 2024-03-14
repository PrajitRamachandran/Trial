import random

R_EATING = "Well, being a computer I don't eat human foods, I get my energy from my battery and other components of this device."
R_ADVICE = "As I am a simple rule based bot any advice I give may not be reliable so consider Checking the internet."
R_LOVE = "If I were a human being I would have definetly loved you but being a bot inside this computer all I can do is help you with your querries and doubts"
R_MONDAY = "Sure Prajit Your Monday Routine consists of Chest and Tricep Classes"
R_TUESDAY = "Sure Prajit Your Tuesday Routine consists of Back and Bicep Classes"
R_WEDNESDAY = "Sure Prajit Your Wednesday Routine consists of Legs and shoulder Classes"
R_THURSDAY = "Sure Prajit Your Thursday Routine consists of Chest and Tricep Classes"
R_FRIDAY = "Sure Prajit Your Friday Routine consists of Back and Bicep Classes"
R_SATURDAY = "Sure Prajit Your Saturday Routine consists of Legs and shoulder Classes"
R_SUNDAY = "Sunday is rest day, rest plays a key role in fitness"
R_POEM = "I am over you, Then my eyes meet yours once more, and I fall in love."

def unknown():
    response = ["Could you please re-phrase that? ",
                "Pardon",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response