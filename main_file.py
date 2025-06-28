import random

subjects = [
    "An International Actor",
    "Indian Cricket team player ",
    "Gandhi G",
    "Islamabadi burger boy",
    "Iqra University students ",
    "Real Estate agent ",
    "Tiktoker ",
    "Diljit Dosanjh and Hania Amir ",
    "A food blogger",
    "A local Politician"
]


actions = [
    "announced their wedding",
    "started dancing on the motorway to protest load shedding",
    "resigned from their job during an Instagram live",
    "used ChatGPT to top the university",
    "solved Karachi’s traffic problem with a meme",
    "gave a motivational speech while making chai",
    "was hired as the captain of a PSL team",
    "proposed at Minar-e-Pakistan with a drone show",
    "accidentally booked a Careem to Mars",
    "replaced their final year project with a YouTube prank",
    "hosted a virtual mehndi on Google Meet",
    "organized a jalsa inside a gaming café",
]

objects_things = [
    "during load shedding",
    "at Minar-e-Pakistan",
    "while eating Anday wala Burger",
    "in a Zoom class with 2G internet",
    "inside a virtual mehndi on Google Meet",
    "while arguing with their phuppo",
    "in a PSL match crowd",
    "while drinking doodh patti at 3 AM",
    "after drinking 4 cups of Kashmiri chai",
    "while buying 3 mangoes for 1000 rupees",
    "from a qawwali night in LUMS hostel"
]
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    object_thing = random.choice(objects_things)

    headline = f'\nBREAKING NEWS: {subject} {action} {object_thing}'
    print(headline)

    ans = input("Do you want to Smile again 😁 (yes/no)) \n").strip().lower()
    if ans=='no':
        break

print("Thank You for using FunFake News Generator.", "\nBa-Byeeee👋👋")
exit