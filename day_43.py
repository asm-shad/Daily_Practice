# TF-IDF DATA Science strategy
# Cosie Similarity 
# Analyze the content - description, genre, author
# TF-IDF - Term Frequency - Inverse Document Frequency algorithm, text -> number, [the, a, an = get low score], [science, comedy = high score]
# each descriptive word change into vector[magnitude and direction]
# Each of these vector use trigonometic formula
# Cosie measures the similarity or the angle between the vector, more similar the word more related they are
# These are done by sklearn we are just follow it

import pandas as pd

data = [
    {
        "title": "The Silent Patient",
        "author": "Alex Michaelides",
        "genre": "Psychological Thriller",
        "description": "A famous painter stops speaking after shooting her husband. A therapist becomes obsessed with uncovering her dark secret."
    },
    {
        "title": "Project Hail Mary",
        "author": "Andy Weir",
        "genre": "Science Fiction",
        "description": "A lone astronaut wakes up with amnesia on a spaceship. He must save humanity by solving an impossible scientific mystery."
    },
    {
        "title": "Where the Crawdads Sing",
        "author": "Delia Owens",
        "genre": "Literary Fiction",
        "description": "A lonely girl grows up in North Carolina marshes. She becomes a murder suspect when a popular man dies."
    },
    {
        "title": "The Night Circus",
        "author": "Erin Morgenstern",
        "genre": "Fantasy",
        "description": "Two young magicians compete in a magical circus. Their contest turns into love, threatening their very existence."
    },
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "genre": "Self-Help",
        "description": "Learn how tiny changes create remarkable results. Discover practical strategies to build good habits and break bad ones."
    },
    {
        "title": "The Thursday Murder Club",
        "author": "Richard Osman",
        "genre": "Mystery",
        "description": "Four elderly friends solve cold cases for fun. They suddenly face a real murder in their peaceful retirement village."
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "Science Fiction",
        "description": "A young nobleman must survive on a dangerous desert planet. He leads an uprising against powerful enemies controlling precious spice."
    },
    {
        "title": "Beach Read",
        "author": "Emily Henry",
        "genre": "Romance",
        "description": "Two rival writers with writer's block swap genres. They challenge each other while staying in neighboring beach houses."
    },
    {
        "title": "The Guest List",
        "author": "Lucy Foley",
        "genre": "Thriller",
        "description": "A glamorous wedding on a remote island turns deadly. Every guest has a secret and someone will not survive."
    },
    {
        "title": "Circe",
        "author": "Madeline Miller",
        "genre": "Fantasy",
        "description": "The banished daughter of a Greek god discovers her power. She must choose between gods, mortals, and her own kind."
    },
    {
        "title": "The Vanishing Half",
        "author": "Brit Bennett",
        "genre": "Historical Fiction",
        "description": "Twin sisters run away from their small black community. One lives as white while the other never leaves home."
    },
    {
        "title": "Educated",
        "author": "Tara Westover",
        "genre": "Memoir",
        "description": "A girl raised by survivalist parents never attends school. She eventually escapes to pursue education and a new life."
    },
    {
        "title": "The Midnight Library",
        "author": "Matt Haig",
        "genre": "Fantasy",
        "description": "A depressed woman finds a library between life and death. Each book lets her try a different version of her life."
    },
    {
        "title": "Klara and the Sun",
        "author": "Kazuo Ishiguro",
        "genre": "Literary Fiction",
        "description": "An artificial friend observes human behavior while waiting to be bought. She learns about love, loss, and sacrifice."
    },
    {
        "title": "The Seven Husbands of Evelyn Hugo",
        "author": "Taylor Jenkins Reid",
        "genre": "Historical Fiction",
        "description": "A reclusive Hollywood icon finally tells her true story. She reveals secrets about her seven marriages and one true love."
    },
    {
        "title": "Mexican Gothic",
        "author": "Silvia Moreno-Garcia",
        "genre": "Horror",
        "description": "A socialite receives a desperate letter from her cousin. She enters a decaying mansion with terrifying dark secrets."
    },
    {
        "title": "The Invisible Life of Addie LaRue",
        "author": "V.E. Schwab",
        "genre": "Fantasy",
        "description": "A woman makes a deal to live forever but be forgotten. Three centuries later, she meets someone who remembers her."
    },
    {
        "title": "Malibu Rising",
        "author": "Taylor Jenkins Reid",
        "genre": "Contemporary Fiction",
        "description": "Four famous siblings throw an annual end-of-summer party. The night spirals out of control with secrets and fire."
    },
    {
        "title": "The Paris Apartment",
        "author": "Lucy Foley",
        "genre": "Mystery",
        "description": "A woman arrives at her brother's Paris apartment. He is missing and every neighbor in the building has something to hide."
    },
    {
        "title": "Tomorrow, and Tomorrow, and Tomorrow",
        "author": "Gabrielle Zevin",
        "genre": "Contemporary Fiction",
        "description": "Two friends collaborate to create successful video games. Their creative partnership spans decades of joy, rivalry, and tragedy."
    }
]

df = pd.DataFrame(data)
df.to_csv("books.csv", index=False)
print("✅ Dataset Created.")