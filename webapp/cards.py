import random


# does what it says on the tin
def shuffle_deck(deck):
    random.shuffle(deck)


# pick card(s) - call this method multiple times to draw multiple unique cards from the deck
def get_card(deck):
    num = random.randint(0, len(deck) - 1)  # the minus 1 fixes the zero indexed array out-of-range error
    card = deck[num]
    del (deck[num])  # so we don't get the same card twice if we're calling this multiple times for the same hand
    rev = random.randint(-1, 1)  # is card reversed? zero (false) or 1 (true)
    drawn = (card, rev)  # tuple of card dictionary + 1 or zero for reversal
    return drawn


# array of dicts for each card
def get_deck():
    deck = [

        {"name": "The Magician", "url": "the_magician", "image": "images/01.jpeg",
         "desc": "The start of something. Beginner’s luck. Having various tools and means at our disposal. Use of supernatural forces. Creating reality with mind power. Training and acquisition of practical skills. Improvisation. Display or show for other people.",
         "message": "create a new reality",
         "rdesc": "Trickery, sleight of hand, cheating. Showing off, pretending. Lack of self-awareness about body, sexuality, or basic motives. Near miss due to inexperience or inaccuracy.",
         "sequence": 1,
         "cardtype": "major"},

        {"name": "The Popess", "url": "the_popess", "image": "images/02.jpeg",
         "desc": "Wisdom combining intellect and intuition. A spiritual mother. A woman hiding her strengths in a world of men. Modesty. Secrets, something hidden, mystery. Getting a hint of something which remains largely unknown. Impossible to give a definite answer now.",
         "message": "know how to set boundaries",
         "rdesc": "Need to hide our true nature behind the conventions of normal society. Conservative approach to sex and the body. Emotional blockage.",
         "sequence": 2,
         "cardtype": "major"},

        {"name": "The Empress", "url": "the_empress", "image": "images/03.jpeg",
         "desc": "Abundance, growth, productivity. Natural or human touch within an artificial framework. Emotional intelligence. Protection and care. Motherhood. A powerful female figure. Strong feminine identity.",
         "message": "act from the guts",
         "rdesc": "Impulsive behavior, someone difficult to reason with. Over-protectiveness, excessive involvement in the life of others. Problems with a strong mother figure.",
         "sequence": 3,
         "cardtype": "major"},

        {"name": "The Emperor", "url": "the_emperor", "image": "images/04.jpeg",
         "desc": "Practical and material achievements. Matters relating to the workplace or source of income. Authority and control, a commanding position. A protective father figure, patron or sponsor. Assertiveness. Military affairs.",
         "message": "show leadership and responsibility",
         "rdesc": "Belligerence, violence, trying to solve things by brute force. Dictatorship. Possibility of sexual abuse. Difficulty in coping with a dominant father figure. Denial and hiding of inner weaknesses.",
         "sequence": 4,
         "cardtype": "major"},

        {"name": "The Pope", "url": "the_pope", "image": "images/05.jpeg",
         "desc": "Teacher, instructor, or counselor. Education and knowledge, academic expertise. Organized religion, conventional medicine or psychology. Spiritual father. Consultation or treatment by a specialist. Marriage.",
         "message": "respect knowledge and education",
         "rdesc": "Excessive adhesion to conventions and outdated norms. Bureaucracy, an oppressive establishment. Hypocrisy, discrimination. Divorce.",
         "sequence": 5,
         "cardtype": "major"},

        {"name": "The Lover", "url": "the_lover", "image": "images/06.jpeg",
         "desc": "Love, amorous relationship. Emotional entanglement. Need to make a choice, or to disengage oneself from past influences. Inclinations of the heart correspond to the will of heaven. Small steps actually taken are the visible signs of inner desire.",
         "message": "follow the path of the heart.",
         "rdesc": "Complex relationship between several people, e.g., a romantic triangle or a tension between mother and wife. Hesitation, quandary. Confusion as to one’s own feeling and will.",
         "sequence": 6,
         "cardtype": "major"},

        {"name": "The Chariot", "url": "the_chariot", "image": "images/07.jpeg",
         "desc": "Victory or an achievement putting the querent in a strong and protected position. Ambition, energy, motivation to move forward. Public honor. Power and high status.",
         "message": "dare and win",
         "rdesc": "Inner weakness hidden behind external show-off. Arrogance, vanity. Over-protectiveness, emotional closure. Confusion about one’s goals. Losing the simple touch with people and reality.",
         "sequence": 7,
         "cardtype": "major"},

        {"name": "Justice", "url": "justice", "image": "images/08.jpeg",
         "desc": "Law and order, legal and court issues. A fair and balanced judgment. A developed conscience. Rationality, reasoning by clear rules and common norms. Touch of grace and humanity beyond the objective considerations.",
         "message": "act with reason and by the accepted norms",
         "rdesc": "Petty accountability, a critical and judgmental attitude, guilt feelings. Repressive control of self and of others. Negative ideas blocking change and advance.",
         "sequence": 8,
         "cardtype": "major"},

        {"name": "The Hermit", "url": "the_hermit", "image": "images/09.jpeg",
         "rdesc": "A closed and reclusive attitude. Isolation, loneliness. Fixed ideas. Excessive caution and suspicion, a critical approach looking for defects. Hidden and denied desires.",
         "message": "look for the essence of things",
         "desc": "A quest for truth or for spiritual understanding. Concentrating on a clear purpose. Caution, careful examination. Self-privation for the sake of a meaningful cause. Loyalty to principles, strong faith.",
         "sequence": 9,
         "cardtype": "major"},

        {"name": "Wheel of Fortune", "url": "the_wheel_of_fortune", "image": "images/10.jpeg",
         "desc": "Change in circumstances and position. A rise after a fall. Gambling, putting faith in capricious luck. Life cycles, closure of circles. Adapting to the routine of everyday life. A hint to previous incarnations.",
         "message": "accept life’s ups and downs",
         "rdesc": "A decline after a period of rising. Danger lurks at the summit. Moving in a closed circle. Capricious mood changes. Feeling powerless to affect one’s situation.",
         "sequence": 10,
         "cardtype": "major"},

        {"name": "Strength", "url": "strength", "image": "images/11.jpeg",
         "desc": "Power and courage to face challenges. Controlled expression of creative urges, drives and desires. Mobilization of inner resources towards a common goal. Taking risks.",
         "message": "take control of yourself",
         "rdesc": "Need to keep things under control leads to constant tensions. A risk of losing one’s grip. Internal conflicts and unrealistic assessment of one’s own forces may lead to failure.",
         "sequence": 11,
         "cardtype": "major"},

        {"name": "The Hanged Man", "url": "the_hanged_man", "image": "images/12.jpeg",
         "desc": "Seeing things from a unique point of view. Enduring difficulties for a worthy cause. A period of deep self examination. Passivity, acceptance of reality even if it is the opposite of what one expects.",
         "message": "look at things from the opposite perspective",
         "rdesc": "Isolation. Emotional stance of a victim. Inability to act. Denying one’s own unique qualities, striving to be “normal” at all costs. Living in one’s private and imaginary reality.",
         "sequence": 12,
         "cardtype": "major"},

        {"name": " ", "url": "13", "image": "images/13.jpeg",
         "desc": "The end of something whose time has come. Cutting off past influences or attachment to dominant figures. Giving up the superfluous and keeping only the essential. Disintegration of the old makes room for the new.",
         "message": "give up what is over",
         "rdesc": "Difficulty in coping with loss or change. Temporary difficulties, a trying challenge. Disintegration. Re-alization of a painful truth. Does not predict future death, but may reflect anxiety about dying or mourning over a loss which has already happened.",
         "sequence": 13,
         "cardtype": "major"},

        {"name": "Temperance", "url": "temperance", "image": "images/14.jpeg",
         "desc": "Reconciliation, compromise, relaxation of tensions. Integration of opposites. Ability to do the seemingly impossible. A slow process of distillation and improvement. Patience, perseverance. Self-improvement.",
         "message": "find the golden mean",
         "rdesc": "Going back and forth without making real progress. Losing patience with a lengthy process. Emotion-al preoccupation with oneself, pushing away others who might come to help.",
         "sequence": 14,
         "cardtype": "major"},

        {"name": "The Devil", "url": "the_devil", "image": "images/15.jpeg",
         "desc": "A burst of creativity. Paradoxes and contradictions. Irony and mocking of common norms. Acting from desires, passions and impulses. Moving on from a past family trauma.",
         "message": "express passion and desire.",
         "rdesc": "Temptation, attraction to the dark and forbidden. Exploitation, egotism, domination. Compulsive self-gratification. Senseless behavior has its price. Difficulty in detaching oneself from an unhealthy bond.",
         "sequence": 15,
         "cardtype": "major"},

        {"name": "House of God", "url": "the_house_of_god", "image": "images/16.jpeg",
         "desc": "Breaking up of solid structures. Getting free from confinement. Sudden breakthrough after long preparations. Sparkling sexual encounter. Success lies in simplicity and modesty.",
         "message": "return to the solid ground of reality",
         "rdesc": "Shock, collapse of projects or trusted structures. A fall from an apparently solid and secure position. Chaos, confusion, difficulty in understanding what is going on. Vanity and pride lead to failure.",
         "sequence": 16,
         "cardtype": "major"},

        {"name": "The Star", "url": "the_star", "image": "images/17.jpeg",
         "desc": "Openness, simplicity, return to nature. Purity, honesty. Showing yourself “as you are,” accepting one’s body and desires. Generosity. Luck from heaven. Intuitive feeling of guidance or energy coming from a higher plane.",
         "message": "flow from a pure source",
         "rdesc": "Naive optimism and wishful-thinking. Exposing oneself to danger or abuse. Difficulty in setting proper boundaries. Squandering, wastefulness.",
         "sequence": 17,
         "cardtype": "major"},

        {"name": "The Moon", "url": "the_moon", "image": "images/18.jpeg",
         "desc": "Deep emotions, perhaps related to a mother or feminine figure. A different experience of reality. Longing for the unreachable. Finding one’s hidden strengths. Occupation with the remote past. A hidden treasure.",
         "message": "don’t be afraid to go deep down",
         "rdesc": "Vague and disturbing feelings. Emotional difficulties, a period of depression. Danger lurking under the surface. Retreat, the road ahead is hard to find.",
         "sequence": 18,
         "cardtype": "major"},

        {"name": "The Sun", "url": "the_sun", "image": "images/19.jpeg",
         "desc": "Light and warmth, abundance, blessings. Pleasant feeling, emotional or physical healing. Partnership, trust, sharing, brotherhood. Human touch. An ideal father figure. Matters relating to children. Setting limits in a moderate and non-oppressive way.",
         "message": "find suitable partners",
         "rdesc": "Living in a limited space, difficulty to face reality “in the open.” Immaturity, dependence on others. Someone or something too intense and energetic to feel comfortable with. An absent father.",
         "sequence": 19,
         "cardtype": "major"},

        {"name": "Judgement", "url": "judgement", "image": "images/20.jpeg",
         "desc": "Revelation, enlightenment, a new understanding. A turning point in a therapy process. Healing of a family relationship. Disclosure, secrets revealed, publicity. Birth of a baby or of a new thing.",
         "message": "awaken to spiritual reality",
         "rdesc": "Revelation of something that should have been kept hidden. Lack of privacy. Unpleasant realization. Problems related to child-parent relations. Too much noise and drama.",
         "sequence": 20,
         "cardtype": "major"},

        {"name": "The World", "url": "the_world", "image": "images/21.jpeg",
         "desc": "Completion of a process. Balanced activity and achievements in various domains. Contact with far places. Harmony and correspondence between different planes. Pregnancy, something new is about to be born. The Dance of Life.",
         "message": "everything is perfect as it is",
         "rdesc": "Life in a bubble, difficulty in sharing your world with others. Disconnection of inner feelings from external life. Preoccupation with oneself, idealized self-image, inability to move forward.",
         "sequence": 21,
         "cardtype": "major"},

        {"name": "The Fool", "url": "the_fool", "image": "images/00.jpeg",
         "desc": "Freedom from conventions and norms. Something or someone unique and exceptional. Options kept open. Giving up control, spontaneity. Uncertainty, attention to the here and now. Going on a trip.",
         "message": "keep on the move",
         "rdesc": "Difficulty in choosing and committing oneself to something stable. Restlessness. Lack of purpose. Getting lost. Foolish behavior. Eccentricity, lack of acceptance by the social environment. Difficulty in planning ahead.",
         "sequence": 22,
         "cardtype": "major"},

        {"name": "King of Swords", "url": "king_of_swords", "image": "images/swki.jpeg",
         "desc": "A very good ally or counselor - clever and self-controlled with some authority. Also they can be modern, analytical and very strong. The card may also mean a lawsuit.",
         "rdesc": "Deceitful and malicious person. They may be a dangerous enemy, violent and powerful.",
         "sequence": 23,
         "cardtype": "minor"},

        {"name": "Queen of Swords", "url": "queen_of_swords", "image": "images/swqu.jpeg",
         "desc": "A graceful but stern person. They have keen insight and good judgment. May be a dancer, a widow/er or a childless person. This card also means privation and mourning.",
         "rdesc": "Playfully mischievous. Dangerous enemy. Jealous and narrow-minded person.",
         "sequence": 24,
         "cardtype": "minor"},

        {"name": "Knight of Swords", "url": "knight_of_swords", "image": "images/swkn.jpeg",
         "desc": "Audacious, clever and gallant; spirited young person. They may be domineering and unstable but they have the better intentions.",
         "rdesc": "Harsh, fanatic, extravagant. Tyrannic and aggressive. Dangerous enemy.",
         "sequence": 25,
         "cardtype": "minor"},

        {"name": "Page of Swords", "url": "page_of_swords", "image": "images/swpa.jpeg",
         "desc": "Logic and penetrating young person. Mentally and physically dexterous. Spying. Messages.",
         "rdesc": "Frivolous, revengeful and cunning person. Indiscretion. Impotence. Unforeseen perturbation.",
         "sequence": 26,
         "cardtype": "minor"},

        {"name": "Ace of Swords", "url": "ace_of_swords", "image": "images/sw01.jpeg",
         "desc": "Conquest. Triumph through trouble. Intense activity. Gestation or parturition.",
         "rdesc": "Disaster or conquest followed by disaster. Great loss. Violent death. Infertility.",
         "sequence": 27,
         "cardtype": "minor"},

        {"name": "Two of Swords", "url": "two_of_swords", "image": "images/sw02.jpeg",
         "desc": "Peace. Balanced forces. Indecision. Strength. Friendship.",
         "rdesc": "Disloyalty. Change, sometimes in the wrong direction. Quarrel",
         "sequence": 28,
         "cardtype": "minor"},

        {"name": "Three of Swords", "url": "three_of_swords", "image": "images/sw03.jpeg",
         "desc": "Sorrow. Separation, quarrel, tears. Delay. Absence.", "rdesc": "Confusion, loss, error.",
         "sequence": 29,
         "cardtype": "minor"},

        {"name": "Four of Swords", "url": "four_of_swords", "image": "images/sw04.jpeg",
         "desc": "Truce. Solitude. Stagnation. Recovering from illness. Exile. Retreat.",
         "rdesc": "Renewed activity. Surprise. Prudence and economy are advised.",
         "sequence": 30,
         "cardtype": "minor"},

        {"name": "Five of Swords", "url": "five_of_swords", "image": "images/sw05.jpeg",
         "desc": "Defeat. Failure. Loss. Powerlessness. Separation. Lies. Death.",
         "rdesc": "Risk of loss or defeat. Funeral. Weakness.",
         "sequence": 31,
         "cardtype": "minor"},

        {"name": "Six of Swords", "url": "six_of_swords", "image": "images/sw06.jpeg",
         "desc": "Science. Journey by water, revelation, study. Intelligent effort. Success after anxiety.",
         "rdesc": "Stagnation. Unfavorable result. Intellectual pride.",
         "sequence": 32,
         "cardtype": "minor"},

        {"name": "Seven of Swords", "url": "seven_of_swords", "image": "images/sw07.jpeg",
         "desc": "Futility. Partial or unpredictable result. Dreams, vacillation. Travel by land.",
         "rdesc": "Quarrels. Slanders. Disenchantment in family or friendship.",
         "sequence": 33,
         "cardtype": "minor"},

        {"name": "Eight of Swords", "url": "eight_of_swords", "image": "images/sw08.jpeg",
         "desc": "Interference. Restriction. Temporal sickness or captivity. Indecision.",
         "rdesc": "New beginnings. Freedom from the past bondage.",
         "sequence": 34,
         "cardtype": "minor"},

        {"name": "Nine of Swords", "url": "nine_of_swords", "image": "images/sw09.jpeg",
         "desc": "Cruelty. Suffering. Misery. Sickness. Martyrdom. Burden. May be death of a loved one.",
         "rdesc": "Patience, faithfulness, unselfishness.",
         "sequence": 35,
         "cardtype": "minor"},

        {"name": "Ten of Swords", "url": "ten_of_swords", "image": "images/sw10.jpeg",
         "desc": "Ruin. Total defeat. Death. The end of an illusion.", "rdesc": "Transitory success. Improvement.",
         "sequence": 36,
         "cardtype": "minor"},

        {"name": "King of Disks", "url": "king_of_disks", "image": "images/peki.jpeg",
         "desc": "A married person, wealthy and clever in money matters. Patient and laborious, they are an experienced chief and a reliable ally.",
         "rdesc": "Vicious and greedy person. Beware of gamblers or speculators. Easy to bribe, possibly a dangerous person.",
         "sequence": 37,
         "cardtype": "minor"},

        {"name": "Queen of Disks", "url": "queen_of_disks", "image": "images/pequ.jpeg",
         "desc": "Charming and generous person. Pragmatic and quiet, but ambitious. Opulence, security.",
         "rdesc": "A foolish and temperamental person. Prone to suspicion and fearful of failure. Negligence.",
         "sequence": 38,
         "cardtype": "minor"},

        {"name": "Knight of Disks", "url": "knight_of_disks", "image": "images/pekn.jpeg",
         "desc": "Mature and responsible, a trustworthy and laborious person. A capable manager. An important matter concerning money.",
         "rdesc": "Dull, lazy or clumsy person. Careless. Stagnation.",
         "sequence": 39,
         "cardtype": "minor"},

        {"name": "Page of Disks", "url": "page_of_disks", "image": "images/pepa.jpeg",
         "desc": "A learned young person, careful and reflective. Good management, kind and benevolent. The bearer of good news and messages.",
         "rdesc": "Wasteful, illogical, rebellious youth. Bad news or lost of money.",
         "sequence": 40,
         "cardtype": "minor"},

        {"name": "Ace of Disks", "url": "ace_of_disks", "image": "images/pe01.jpeg",
         "desc": "The beginning of prosperity and wealth. Pleasure and beauty.",
         "rdesc": "Success is delayed or it does not give happiness. Greed.",
         "desc": "A good start in material things. Financial and physical stability. A practical perspective. A significant sum of money. Utilitarian approach. Greed. Something basic and unsophisticated.",
         "sequence": 41,
         "cardtype": "minor"},

        {"name": "Two of Disks", "url": "two_of_disks", "image": "images/pe02.jpeg",
         "desc": "Change. Alternation of gain and loss. Equilibrium in the midst of change. Ability to adapt to new circumstances. Some complications. Unstable mood.",
         "rdesc": "Uncertainty. Difficulty adapting to new circumstances.",
         "desc": "Duality. Two options or two elements. Collaborating while keeping distance. A winding road, advancing in complex ways. Recognition and acknowledgment.",
         "sequence": 42,
         "cardtype": "minor"},

        {"name": "Three of Disks", "url": "three_of_disks", "image": "images/pe03.jpeg",
         "desc": "Works. Task well done. Commercial transactions. Professional growth. Dignity. A male child.",
         "rdesc": "Insufficient skill or knowledge to achieve the goal. Fruitless work. Lack of seriousness.",
         "sequence": 43,
         "cardtype": "minor"},

        {"name": "Four of Disks", "url": "four_of_disks", "image": "images/pe04.jpeg",
         "desc": "Power. Purely material gain and security. A gift or an inheritance. A female child. Greed.",
         "rdesc": "Prejudice. Limitation. Sudden stop in progress or loss. Reckless spending of money.",
         "sequence": 44,
         "cardtype": "minor"},

        {"name": "Five of Disks", "url": "five_of_disks", "image": "images/pe05.jpeg",
         "desc": "Worry. Loss of money or employment. Poverty. Defeat. Lovers. Sympathy found in the midst of trouble.",
         "rdesc": "New employment or opportunity. Productive work. Misfortune in love.",
         "sequence": 45,
         "cardtype": "minor"},

        {"name": "Six of Disks", "url": "six_of_disks", "image": "images/pe06.jpeg",
         "desc": "Success. Material gain and power. Sharing wealth with others.",
         "rdesc": "Transitory gains. Prodigality. Bribery. 'Purse-proud'.",
         "sequence": 46,
         "cardtype": "minor"},

        {"name": "Seven of Disks", "url": "seven_of_disks", "image": "images/pe07.jpeg",
         "desc": "Failure. Defeat. Loss of money. Hard work but little gain. Greedy.",
         "rdesc": "Delayed success after hard work. Work done for the love of work without expecting retribution.",
         "sequence": 47,
         "cardtype": "minor"},

        {"name": "Eight of Disks", "url": "eight_of_disks", "image": "images/pe08.jpeg",
         "desc": "Prudence. The first steps of a profitable profession. Learning a business or profession. Ability in material affairs.",
         "rdesc": "Greedy. Selfish in a petty way. Vanity.",
         "sequence": 48,
         "cardtype": "minor"},

        {"name": "Nine of Disks", "url": "nine_of_disks", "image": "images/pe09.jpeg",
         "desc": "Gain. Practical wisdom limited to everyday affairs and the home. Stability. Solitude. Inheritance.",
         "rdesc": "Loss of friendship or a material thing. Cancelled project. Beware of knavery.",
         "sequence": 49,
         "cardtype": "minor"},

        {"name": "Ten of Disks", "url": "ten_of_disks", "image": "images/pe10.jpeg",
         "desc": "Wealth. Fulfillment of material fortune. Family matters. Inheritance. House.",
         "rdesc": "Family misfortune. Loss of inheritance. Beware of risky projects.",
         "sequence": 50,
         "cardtype": "minor"},

        {"name": "King of Cups", "url": "king_of_cups", "image": "images/cuki.jpeg",
         "desc": "A person skilled in law or trade and interested in science, art, religion or philosophy. A good friend, liberal, idealistic and creative. Kind and willing to take some responsibility.",
         "rdesc": "A superficial person, easily enthusiastic, but with little depth of character. Untruthful, ruthless and vicious.",
         "sequence": 51,
         "cardtype": "minor"},

        {"name": "Queen of Cups", "url": "queen_of_cups", "image": "images/cuqu.jpeg",
         "desc": "Dreamy, calm, poetic, imaginative, kind yet not willing to take much trouble for another.",
         "rdesc": "Dishonest and vicious person, not to be trusted.",
         "sequence": 52,
         "cardtype": "minor"},

        {"name": "Knight of Cups", "url": "knight_of_cups", "image": "images/cukn.jpeg",
         "desc": "A young person, may be an artist, who is graceful and poetic. They are an indolent dreamer of sensual pleasures. Can mean a messenger, a proposition or an invitation.",
         "rdesc": "Lazy and deceitful, a dissolute and merciless person.",
         "sequence": 53,
         "cardtype": "minor"},

        {"name": "Page of Cups", "url": "page_of_cups", "image": "images/cupa.jpeg",
         "desc": "Quiet and studious youth, but also sweet and dreamy. News or proposition.",
         "rdesc": "A sensual libertine, not harmful but neither helpful. Unpleasant news. Flatterer, selfish.",
         "sequence": 54,
         "cardtype": "minor"},

        {"name": "Ace of Cups", "url": "ace_of_cups", "image": "images/cu01.jpeg",
         "desc": "Harmony, fertility, happiness, beginning of great love.",
         "rdesc": "Discord, false love, instability.",
         "sequence": 55,
         "cardtype": "minor"},

        {"name": "Two of Cups", "url": "two_of_cups", "image": "images/cu02.jpeg",
         "desc": "Love. Harmony, warm friendship. Close relation with a kindred soul. Good for business and love.",
         "rdesc": "Opposition. False love. Folly, misunderstanding.",
         "sequence": 56,
         "cardtype": "minor"},

        {"name": "Three of Cups", "url": "three_of_cups", "image": "images/cu03.jpeg",
         "desc": "Abundance. Pleasure, hospitality, success. The good things of life.",
         "rdesc": "Sensuality or food and drink intemperance.",
         "sequence": 57,
         "cardtype": "minor"},

        {"name": "Four of Cups", "url": "four_of_cups", "image": "images/cu04.jpeg",
         "desc": "Luxury. Abandonment to desire. New ambition.",
         "rdesc": "Luxury that does not provide happiness. Dissatisfaction with material success. Turning point in life.",
         "sequence": 58,
         "cardtype": "minor"},

        {"name": "Five of Cups", "url": "five_of_cups", "image": "images/cu05.jpeg",
         "desc": "Disappointment. Unexpected misfortune. Partial loss. Friendship or love gone. Inheritance.",
         "rdesc": "New happiness. Return of an old friend or love. Alliance.",
         "sequence": 59,
         "cardtype": "minor"},

        {"name": "Six of Cups", "url": "six_of_cups", "image": "images/cu06.jpeg",
         "desc": "Pleasure. Happiness coming from the past. Nostalgia. Success.",
         "rdesc": "Uncertainty. Living too much in the past. Worthless associates. Inheritance.",
         "sequence": 60,
         "cardtype": "minor"},

        {"name": "Seven of Cups", "url": "seven_of_cups", "image": "images/cu07.jpeg",
         "desc": "Debauch. Foolish expectations. Illusory dreams, deceit. Intoxication. Drug addiction.",
         "rdesc": "New will. Intelligent decision. Short travels.",
         "sequence": 61,
         "cardtype": "minor"},

        {"name": "Eight of Cups", "url": "eight_of_cups", "image": "images/cu08.jpeg",
         "desc": "Indolence. Instability. Material success abandoned, may be for something higher. Decline in interest. Wandering.",
         "rdesc": "Joy, happiness. A new love or interest in material things..",
         "sequence": 62,
         "cardtype": "minor"},

        {"name": "Nine of Cups", "url": "nine_of_cups", "image": "images/cu09.jpeg",
         "desc": "Happiness. Complete material success and well-being. You will get what you wish.",
         "rdesc": "Imperfection, deceit. Intemperance. You will not get what you wish.",
         "sequence": 63,
         "cardtype": "minor"},

        {"name": "Ten of Cups", "url": "ten_of_cups", "image": "images/cu10.jpeg",
         "desc": "Satiety. Perfect love and lasting contentment. Peace, friendship.",
         "rdesc": "Dissipation, loss of friendship. Betrayal. Waste.",
         "sequence": 64,
         "cardtype": "minor"},

        {"name": "King of Clubs", "url": "king_of_clubs", "image": "images/waki.jpeg",
         "desc": "Courageous, swift and generous person. Passionate and strong. Paternalistic and proud. May be a country gentleman, generally married. Unexpected heritage; a good marriage.",
         "rdesc": "Despotic, bigoted, prejudiced, evil-minded.",
         "sequence": 65,
         "cardtype": "minor"},

        {"name": "Queen of Clubs", "url": "queen_of_clubs", "image": "images/waqu.jpeg",
         "desc": "Kind, energetic but calm person. Conservative, pragmatic and authoritarian. Fruitful in mind and body.",
         "rdesc": "Domineering, jealous, dogmatic and irrational. Quick to take offense.",
         "sequence": 66,
         "cardtype": "minor"},

        {"name": "Knight of Clubs", "url": "knight_of_clubs", "image": "images/wakn.jpeg",
         "desc": "A young and energetic person. Swift and daring. May be noble and generous but also violent and hasty.",
         "rdesc": "Jealous, weak and intolerant person. Quarrel, discord, frustration.",
         "sequence": 67,
         "cardtype": "minor"},

        {"name": "Page of Clubs", "url": "page_of_clubs", "image": "images/wapa.jpeg",
         "desc": "Young and brilliant. Enthusiastic and daring. A messenger or bearer of tidings.",
         "rdesc": "Frivolous youth. Theatrical and shallow. Cruel, oppressive.",
         "sequence": 68,
         "cardtype": "minor"},

        {"name": "Ace of Clubs", "url": "ace_of_clubs", "image": "images/wa01.jpeg",
         "desc": "Creation, birth. The power or ability to begin or to follow through energetically with a plan or task; enterprise and determination. Beginning of an enterprise, invention or adventure.",
         "rdesc": "Fall. To lose or postpone something (employment, enterprise, etc.). False starts.",
         "sequence": 69,
         "cardtype": "minor"},

        {"name": "Two of Clubs", "url": "two_of_clubs", "image": "images/wa02.jpeg",
         "desc": "Dominion. Maturity. Boldness with self-control. Influence.",
         "rdesc": "Disturbance. Indifferent to or disregardful of consequences. Fear, illness.",
         "sequence": 70,
         "cardtype": "minor"},

        {"name": "Three of Clubs", "url": "three_of_clubs", "image": "images/wa03.jpeg",
         "desc": "Virtue. Established strength, realization of hope, nobility. Cooperation, partnership.",
         "rdesc": "Inconsistency, deception, treachery. Loss, robbery.",
         "sequence": 71,
         "cardtype": "minor"},

        {"name": "Four of Clubs", "url": "four_of_clubs", "image": "images/wa04.jpeg",
         "desc": "Completion. Settlement, peace, harmony. Romance, marriage, society.",
         "rdesc": "Insecurity. Uneasiness, unreliability. Contradictions, incomplete happiness.",
         "sequence": 72,
         "cardtype": "minor"},

        {"name": "Five of Clubs", "url": "five_of_clubs", "image": "images/wa05.jpeg",
         "desc": "Strife. Competition, lawsuit, obstacles, violence, fighting.",
         "rdesc": "Dangerous indecision, treachery, complication.",
         "sequence": 73,
         "cardtype": "minor"},

        {"name": "Six of Clubs", "url": "six_of_clubs", "image": "images/wa06.jpeg",
         "desc": "Victory after strife. Good news. Progress, helping friends.",
         "rdesc": "Postponement. Insolence, excessive pride. Treason.",
         "sequence": 74,
         "cardtype": "minor"},

        {"name": "Seven of Clubs", "url": "seven_of_clubs", "image": "images/wa07.jpeg",
         "desc": "Valor. Victory through courage. Struggle. Fierce competition. Certain success.",
         "rdesc": "Uncertainty and fear. Pregnancy. False appearance.",
         "sequence": 75,
         "cardtype": "minor"},

        {"name": "Eight of Clubs", "url": "eight_of_clubs", "image": "images/wa08.jpeg",
         "desc": "Swiftness. Hasty decision. Air travel, messages. Love letter. Hyperactivity. Great hopes.",
         "rdesc": "Opposition. Jealousy. Delay in business or love affair.",
         "sequence": 76,
         "cardtype": "minor"},

        {"name": "Nine of Clubs", "url": "nine_of_clubs", "image": "images/wa09.jpeg",
         "desc": "Strength. Capability of enduring a long struggle and achieve the final victory. Recovery from sickness.",
         "rdesc": "Weakness, delays, sickness. Adversity.",
         "sequence": 77,
         "cardtype": "minor"},

        {"name": "Ten of Clubs", "url": "ten_of_clubs", "image": "images/wa10.jpeg",
         "desc": "Oppression. Imbalance and selfishness. Heavy burden. Force detached from spiritual sources. A problem may be solved soon.",
         "rdesc": "Annoyances. Treason. Separation, emigration. Some loses.",
         "sequence": 78,
         "cardtype": "minor"},

    ]
    return deck
