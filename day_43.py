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
"description": "Criminal psychotherapist obsessed with uncovering why famous painter murdered husband then stopped speaking. Dark twist ending reveals shocking betrayal."
},
{
"title": "Project Hail Mary",
"author": "Andy Weir",
"genre": "Science Fiction",
"description": "Ailing astronaut with amnesia wakes alone on interstellar ship. Must solve astrophysics puzzle using science to save Earth from extinction-level event."
},
{
"title": "Where the Crawdads Sing",
"author": "Delia Owens",
"genre": "Literary Fiction",
"description": "Abandoned marsh girl becomes naturalist and murder suspect. Courtroom drama interweaves coming-of-age survival story with romantic betrayal mystery."
},
{
"title": "The Night Circus",
"author": "Erin Morgenstern",
"genre": "Fantasy",
"description": "Magical competition between two illusionists unfolds within black-and-white circus. Love develops as they manipulate time, matter, and human perception."
},
{
"title": "Atomic Habits",
"author": "James Clear",
"genre": "Self-Help",
"description": "Practical framework showing tiny 1% improvements compound into remarkable transformation. Evidence-based strategies for identity-based habit formation."
},
{
"title": "The Thursday Murder Club",
"author": "Richard Osman",
"genre": "Mystery",
"description": "Retired septuagenarians in posh village solve cold cases using life experience. Developer's murder forces them to outsmart police and real killer."
},
{
"title": "Dune",
"author": "Frank Herbert",
"genre": "Science Fiction",
"description": "Noble boy becomes messianic leader of desert planet Arrakis. Must control spice production while navigating political intrigue and ecological warfare."
},
{
"title": "Beach Read",
"author": "Emily Henry",
"genre": "Romance",
"description": "Literary fiction writer and commercial romance author swap genres. Former college rivals challenge each other while processing past relationship trauma."
},
{
"title": "The Guest List",
"author": "Lucy Foley",
"genre": "Thriller",
"description": "Luxury wedding on storm-swept Irish island turns fatal. Multiple POVs reveal interlocking secrets among guests, staff, and wedding party."
},
{
"title": "Circe",
"author": "Madeline Miller",
"genre": "Fantasy",
"description": "Banished Titan daughter discovers witchcraft power on isolated island. Feminist retelling exploring immortality, motherhood, and Odysseus encounter."
},
{
"title": "The Vanishing Half",
"author": "Brit Bennett",
"genre": "Historical Fiction",
"description": "Identical twin sisters from black community choose opposite racial identities. Generational saga spanning 1950s-90s about passing, family, and belonging."
},
{
"title": "Educated",
"author": "Tara Westover",
"genre": "Memoir",
"description": "Survivalist family rejects hospitals and schools. Seventeen-year-old homeschooled girl enters formal education, causing psychological rupture with past."
},
{
"title": "The Midnight Library",
"author": "Matt Haig",
"genre": "Fantasy",
"description": "Suicidal woman enters quantum library between life and death. Each book offers alternate life exploring different career, relationship, and regret choices."
},
{
"title": "Klara and the Sun",
"author": "Kazuo Ishiguro",
"genre": "Literary Fiction",
"description": "Artificial Friend observes humanity while awaiting purchase. Solar-powered AI learns about love, sacrifice, and her programmed obsolescence."
},
{
"title": "The Seven Husbands of Evelyn Hugo",
"author": "Taylor Jenkins Reid",
"genre": "Historical Fiction",
"description": "Aging Hollywood icon reveals true bisexual identity to unknown journalist. Golden Age secrets about studio system manipulation and hidden love."
},
{
"title": "Mexican Gothic",
"author": "Silvia Moreno-Garcia",
"genre": "Horror",
"description": "Glamorous socialite investigates cousin's disturbing marriage invitation. Deco-era mansion contains fungal entity controlling family through dream manipulation."
},
{
"title": "The Invisible Life of Addie LaRue",
"author": "V.E. Schwab",
"genre": "Fantasy",
"description": "Desperate woman makes Faustian deal to live freely but be instantly forgotten. Three centuries pass before antique shop worker unexpectedly remembers her."
},
{
"title": "Malibu Rising",
"author": "Taylor Jenkins Reid",
"genre": "Contemporary Fiction",
"description": "Famous four siblings host annual party exploding into chaos. Night alternates between wild party and flashbacks showing famous father's abandonment."
},
{
"title": "The Paris Apartment",
"author": "Lucy Foley",
"genre": "Mystery",
"description": "Journalist arrives at brother's luxury Paris building to find him missing. Claustrophobic thriller revealing every glamorous tenant as potential killer."
},
{
"title": "Tomorrow, and Tomorrow, and Tomorrow",
"author": "Gabrielle Zevin",
"genre": "Contemporary Fiction",
"description": "Childhood friends reunite to create revolutionary video games. Decades-long creative partnership exploring collaboration, identity, illness, and artistic legacy."
}
]

df = pd.DataFrame(data)
df.to_csv("books.csv", index=False)
print("✅ Dataset Created.")