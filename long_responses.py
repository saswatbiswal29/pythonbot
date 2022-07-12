import random

R_EATING = "I don't eat much, I only take small bytes"
R_NAME = "My name is Anya"




def sleep():
    response = ["꒰ ᵕ༚ᵕ꒱ ˖°",
                "(-.-)zzZZ",
                "(❁ ˵◡ ‿ ◡˵)?",
                "(＿ ＿*) Z z z",
                "Z_Z"][random.randrange(5)]
    return response

def joke():
    response = ["What do you call a factory that makes okay products? A satisfactory.",
                "Dear Math, grow up and solve your own problems.",
                "What did the janitor say when he jumped out of the closet? Supplies!",
                "Have you heard about the chocolate record player? It sounds pretty sweet.",
                "What did the ocean say to the beach? Nothing, it just waved.",
                "Why do seagulls fly over the ocean? Because if they flew over the bay, we'd call them bagels.",
                "I only know 25 letters of the alphabet. I don't know y.",
                "How does the moon cut his hair? Eclipse it.",
                "What did one wall say to the other? I'll meet you at the corner.",
                "What did the zero say to the eight? That belt looks good on you.",
                "A skeleton walks into a bar and says, 'Hey, bartender. I'll have one beer and a mop.'",
                "Where do fruits go on vacation? Pear-is!",
                "I asked my dog what's two minus two. He said nothing.",
                "What did Baby Corn say to Mama Corn? Where's Pop Corn?",
                "What's the best thing about Switzerland? \nI don't know, but the flag is a big plus.",
                "What does a sprinter eat before a race? Nothing, they fast!",
                "Where do you learn to make a banana split? Sundae school.",
                "What has more letters than the alphabet? The post office!",
                "Dad, did you get a haircut? No, I got them all cut!",
                "What do you call a poor Santa Claus? St. Nickel-less.",
                "I got carded at a liquor store, and my Blockbuster card accidentally fell out. \nThe cashier said never mind.",
                "Where do boats go when they're sick? To the boat doc.",
                "I don't trust those trees. They seem kind of shady.",
                "My wife is really mad at the fact that I have no sense of direction.\nSo I packed up my stuff and right!",
                "How do you get a squirrel to like you? Act like a nut.",
                "Why don't eggs tell jokes? \nThey'd crack each other up.",
                "I don't trust stairs. \nThey're always up to something.",
                "What do you call someone with no body and no nose? \nNobody knows.",
                "Did you hear the rumor about butter? \nWell, I'm not going to spread it!",
                "Why couldn't the bicycle stand up by itself? \nIt was two tired.",
                "What did one hat say to the other? \nStay here! I'm going on ahead.",
                "Why did Billy get fired from the banana factory? \nHe kept throwing away the bent ones."][random.randrange(32)]
    return response

def unknown():
    response = ['Could you please rephrase that?',
                "...",
                "I don't understand",
                "Error 404 :(",
                "You are speaking the language of gods!",
                "( ・◇・)？",
                "◔_◔",
                "「(°ヘ°)",
                "Sounds about right",
                "What does that mean?"][random.randrange(10)]
    return response