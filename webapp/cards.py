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
        {"name": "The Fool", "url": "the_fool", "image": "images/00.jpeg",
         "desc": "Immaturity, sincerity, a free spirit. One who naturally knows their will and is worry free. A dreamer, careless and disinterested in practical matters. Travel.",
         "rdesc": "Folly, failure, madness. Hindered travel.",
         "long_desc": "",
         "sequence": 1},

        {"name": "The Magician", "url": "the_magician", "image": "images/01.jpeg",
         "desc": "Will, creativeness, adroitness, mastery, elasticity, autonomy, eloquence, craft, cunning. May imply a new beginning. The Magus is an autonomous person that knows where they are going and how to achieve their ends.",
         "rdesc": "Indecision, weak will, ineptitude, dilettante. Deceitfulness, trickery.",
         "long_desc": "",
         "sequence": 2},

        {"name": "The High Priestess", "url": "the_high_priestess", "image": "images/02.jpeg",
         "desc": "Hidden influence. Silence, patience, equilibrium. Slow but firm. Pondered decision. Advice, tuition. Psychic ability. The manifestation of the eternal feminine in a spiritual way.",
         "rdesc": "Deceptive, secret, or sly manner. Lazyness, intolerance. Delays. False ideas, moodiness, doubt, superficiality.",
         "long_desc": "",
         "sequence": 3},

        {"name": "The Empress", "url": "the_empress", "image": "images/03.jpeg",
         "desc": "Understanding, charm, kindness, beauty, pleasure, success, safety, trust. Nurturing, positive development.",
         "rdesc": "False appearance, vanity, disdain, frivolity. Sterility. Delays. Careless spending.",
         "long_desc": "",
         "sequence": 4},

        {"name": "The Emperor", "url": "the_emperor", "image": "images/04.jpeg",
         "desc": "Stability. Power. Being in control of yourself/situation. Ambition. Leadership. Firmness of purpose. A dominant male person.",
         "rdesc": "Loss of control. Emotional immaturity and bondage to parents. Possibility of being defrauded of one's inheritance. Ill-temper. Stubbornness. Fall. Loss of wealth. Megalomaniac.",
         "long_desc": "",
         "sequence": 5},

        {"name": "The High Priest", "url": "the_high_priest", "image": "images/05.jpeg",
         "desc": "Wisdom, endurance, persistence, patience, help from superiors, good advice, a good teacher, organization, peace, goodness of heart.",
         "rdesc": "Tendency to over criticize or being unduly concerned with the morals of others. Incapable of dealing efficiently with practical matters, especially finances. Unconventionality, illogical, superstitious, unable to behave coherently.",
         "long_desc": "",
         "sequence": 6},

        {"name": "The Lover", "url": "the_lover", "image": "images/06.jpeg",
         "desc": "Union, decision, choice, marriage, love, the union of opposites, attraction. Balance, openness to inspiration. Harmony of the inner and outer aspect of life.",
         "rdesc": "Disorder, failure, danger of a broken relationship or a wrong choice, quarrels, infidelity. Emotional instability. Dangerous temptation.",
         "long_desc": "",
         "sequence": 7},

        {"name": "The Chariot", "url": "the_chariot", "image": "images/07.jpeg",
         "desc": "Triumph of the will, to surmount opposition, success. Self-control, ability to determinate the own destiny. Good news. Great physical and mental strength. Swiftness. The transitory power. Travel.",
         "rdesc": "Generalized disorder. Illness. Dangerous restlessness. Danger of a violent accident.",
         "long_desc": "",
         "sequence": 8},

        {"name": "Justice", "url": "justice", "image": "images/08.jpeg",
         "desc": "Conformity to moral rightness in action or attitude. The power to maintain equilibrium between the necessities and responsibilities of life. Justice, balance, adjustment. In order to keep things balanced certain things must be sacrificed. May refer to law matters, trials, marriages, divorces, etc. Integrity, moderation.",
         "rdesc": "Fanaticism, injustice, inequality, legal complications. Harsh judgment. Insecurity, imbalance.",
         "long_desc": "",
         "sequence": 9},

        {"name": "The Hermit", "url": "the_hermit", "image": "images/09.jpeg",
         "desc": "Prudence, wisdom, patience, silence, spiritual advance, divine inspiration, circumspection, retirement from participation in current events, solitude. Pilgrimage. Quest for wisdom. Could be a teacher. A period of spiritual and intellectual personal development.",
         "rdesc": "Immaturity, viciousness, darkness, stubbornness, deception, betrayal, too much or insufficient prudence. Misanthrope, misogyny, celibacy, excessively shy person. Hidden enemies.",
         "long_desc": "",
         "sequence": 10},

        {"name": "The Wheel of Fortune", "url": "the_wheel_of_fortune", "image": "images/10.jpeg",
         "desc": "Change, evolution, success, good fortune, fate. Happiness, abundance. New conditions.",
         "rdesc": "Retarded progress. Delays, setbacks.",
         "long_desc": "",
         "sequence": 11},

        {"name": "Strength", "url": "strength", "image": "images/11.jpeg",
         "desc": "Sublimation or regulation of the passions and lower instincts. Power, energy, great love. Spirit ruling over matter. Action, courage. Success. Powerful will and great physical strength. The inner strength to tame the lust.",
         "rdesc": "Discord, ruin, stubbornness, abuse of power. Weakness.",
         "long_desc": "",
         "sequence": 12},

        {"name": "The Hanged Man", "url": "the_hanged_man", "image": "images/12.jpeg",
         "desc": "Fortitude, wisdom. Self-imposed limitations. Voluntary sacrifice leading to new insight or initiation through tribulations and ordeals. Redemption through sacrifice, loss. Prophetic power. Suspended decisions. Choice requiring contemplation.",
         "rdesc": "Arrogance, egotism, resistance to spiritual influences. Absorption in physical matters. Wasted effort. False prophecy. Failure.",
         "long_desc": "",
         "sequence": 13},

        {"name": "Death", "url": "death", "image": "images/13.jpeg",
         "desc": "Complete transformation. Death and rebirth. The end of something. Evolution from one state to another.",
         "rdesc": "Stagnation, death, petrification. Incurable ill person. Broken marriage.",
         "long_desc": "",
         "sequence": 14},

        {"name": "Temperance", "url": "temperance", "image": "images/14.jpeg",
         "desc": "Careful consideration, patience, moderation, adaptation, tempering, self-control. To temper, to combine, to exercise self-restraint. Patience, bringing together two opposites carefully blending them. Good marriage. Working in harmony with others, good management. Something is brewing. Great talent and creative involvement. Striving for Transcendence through works. Alchemy. The union of opposites refined by the fire of the Will.",
         "rdesc": "Disorder, conflict, unfortunate combinations, quarrels. Possibility of shipwreck.",
         "long_desc": "",
         "sequence": 15},

        {"name": "The Devil", "url": "the_devil", "image": "images/15.jpeg",
         "desc": "Fate (wrong or good). Seductive power, blind impulse. Temptation, obsession. Sexual deviation. A disturbed mental state. Earthly passions are turning you inside and out.",
         "rdesc": "Harmful, fate, wrong use of force, weakness, blindness, disorder. Malefic effects. The pathetic human condition of choosing illusion over truth.",
         "long_desc": "",
         "sequence": 16},

        {"name": "The House of God", "url": "the_house_of_god", "image": "images/16.jpeg",
         "desc": "Sudden changes without choice, collapse, escape from prison or bondages, accident. Plans will fall, intentions will break down. Bankruptcy. Sudden death. Enlightenment.",
         "rdesc": "Complete confusion. The gain of freedom at great cost. False accusations, oppression.",
         "long_desc": "",
         "sequence": 17},

        {"name": "The Star", "url": "the_star", "image": "images/17.jpeg",
         "desc": "Hope, unexpected help, insight and clarity of vision, inspiration, flexibility. Great love will be given and received. Good health.",
         "rdesc": "Arrogance, pessimism, stubbornness. Illness. Error of judgment.",
         "long_desc": "",
         "sequence": 18},

        {"name": "The Moon", "url": "the_moon", "image": "images/18.jpeg",
         "desc": "Intuition, threshold of an important change, arduous and obscure path, development of psychic powers.",
         "rdesc": "Unforeseen perils, secret foes, hallucination, self-deception, hysteria, disorientation. Blackmailer.",
         "long_desc": "",
         "sequence": 19},

        {"name": "The Sun", "url": "the_sun", "image": "images/19.jpeg",
         "desc": "Glory. Material happiness. Happy marriage or relationship, collaboration. Success. Pleasure. Energy, motivation, inspiration to others.",
         "rdesc": "Anoyances, disguise. Arrogance. Broken engagement or lost job.",
         "long_desc": "",
         "sequence": 20},

        {"name": "Judgement", "url": "judgement", "image": "images/20.jpeg",
         "desc": "Radical change, resurrection to a new life. A work (or life) well done. Willingness to try something new. Good judgment and discernment. Creative power and influence over family and career. Forgiveness. Awakening. Legal judgments, in one's favor.",
         "rdesc": "Spiritual vacillation, weakness, wrong judgment. Illness. Separation. Adverse legal judgment.",
         "long_desc": "",
         "sequence": 21},

        {"name": "The World", "url": "the_world", "image": "images/21.jpeg",
         "desc": "Success granted. Rewards. Travel, emigration, change of residence.",
         "rdesc": "Hindrances, stagnation. Hard work to bring success.",
         "long_desc": "",
         "sequence": 22},

         {"name": "King of Swords", "url": "king_of_swords", "image": "images/swki.jpeg",
         "desc": "A very good ally or counselor - clever and self-controlled with some authority. Also they can be modern, analytical and very strong. The card may also mean a lawsuit.",
         "rdesc": "Deceitful and malicious person. They may be a dangerous enemy, violent and powerful.",
         "long_desc": "",
         "sequence": 23},

        {"name": "Queen of Swords", "url": "queen_of_swords", "image": "images/swqu.jpeg",
         "desc": "A graceful but stern person. They have keen insight and good judgment. May be a dancer, a widow/er or a childless person. This card also means privation and mourning.",
         "rdesc": "Playfully mischievous. Dangerous enemy. Jealous and narrow-minded person.",
         "long_desc": "",
         "sequence": 24},

        {"name": "Knight of Swords", "url": "knight_of_swords", "image": "images/swkn.jpeg",
         "desc": "Audacious, clever and gallant; spirited young person. They may be domineering and unstable but they have the better intentions.",
         "rdesc": "Harsh, fanatic, extravagant. Tyranic and aggressive. Dangerous enemy.",
         "long_desc": "",
         "sequence": 25},

        {"name": "Page of Swords", "url": "page_of_swords", "image": "images/swpa.jpeg",
         "desc": "Logic and penetrating young person. Mentally and physically dexterous. Spying. Messages.",
         "rdesc": "Frivolous, revengeful and cunning person. Indiscretion. Impotence. Unforeseen perturbation.",
         "long_desc": "",
         "sequence": 26},

        {"name": "Ace of Swords", "url": "ace_of_swords", "image": "images/sw01.jpeg",
         "desc": "Conquest. Triumph through trouble. Intense activity. Gestation or parturition.",
         "rdesc": "Disaster or conquest followed by disaster. Great loss. Violent death. Infertility.",
         "long_desc": "",
         "sequence": 27},

        {"name": "Two of Swords", "url": "two_of_swords", "image": "images/sw02.jpeg",
         "desc": "Peace. Balanced forces. Indecision. Strength. Friendship.",
         "rdesc": "Disloyalty. Change, sometimes in the wrong direction. Quarrel",
         "long_desc": "",
         "sequence": 28},

        {"name": "Three of Swords", "url": "three_of_swords", "image": "images/sw03.jpeg",
         "desc": "Sorrow. Separation, quarrel, tears. Delay. Absence.", "rdesc": "Confusion, loss, error.",
         "long_desc": "",
         "sequence": 29},

        {"name": "Four of Swords", "url": "four_of_swords", "image": "images/sw04.jpeg",
         "desc": "Truce. Solitude. Stagnation. Recovering from illness. Exile. Retreat.",
         "rdesc": "Renewed activity. Surprise. Prudence and economy are advised.",
         "long_desc": "",
         "sequence": 30},

        {"name": "Five of Swords", "url": "five_of_swords", "image": "images/sw05.jpeg",
         "desc": "Defeat. Failure. Loss. Powerlessness. Separation. Lies. Death.",
         "rdesc": "Risk of loss or defeat. Funeral. Weakness.",
         "long_desc": "",
         "sequence": 31},

        {"name": "Six of Swords", "url": "six_of_swords", "image": "images/sw06.jpeg",
         "desc": "Science. Journey by water, revelation, study. Intelligent effort. Success after anxiety.",
         "rdesc": "Stagnation. Unfavorable result. Intellectual pride.",
         "long_desc": "",
         "sequence": 32},

        {"name": "Seven of Swords", "url": "seven_of_swords", "image": "images/sw07.jpeg",
         "desc": "Futility. Partial or unpredictable result. Dreams, vacillation. Travel by land.",
         "rdesc": "Quarrels. Slanders. Disenchantment in family or friendship.",
         "long_desc": "",
         "sequence": 33},

        {"name": "Eight of Swords", "url": "eight_of_swords", "image": "images/sw08.jpeg",
         "desc": "Interference. Restriction. Temporal sickness or captivity. Indecision.",
         "rdesc": "New beginnings. Freedom from the past bondages.",
         "long_desc": "",
         "sequence": 34},

        {"name": "Nine of Swords", "url": "nine_of_swords", "image": "images/sw09.jpeg",
         "desc": "Cruelty. Suffering. Misery. Sickness. Martyrdom. Burden. May be death of a loved one.",
         "rdesc": "Patience, faithfulness, unselfishness.",
         "long_desc": "",
         "sequence": 35},

        {"name": "Ten of Swords", "url": "ten_of_swords", "image": "images/sw10.jpeg",
         "desc": "Ruin. Total defeat. Death. The end of an illusion.", "rdesc": "Transitory success. Improvement.",
         "long_desc": "",
         "sequence": 36},

        {"name": "King of Disks", "url": "king_of_disks", "image": "images/peki.jpeg",
         "desc": "A married person, wealthy and clever in money matters. Patient and laborious, they are an experienced chief and a reliable ally.",
         "rdesc": "Vicious and greedy person. Beware or gamblers or speculators. Easy to bribe, they may be a dangerous person.",
         "long_desc": "",
         "sequence": 37},

        {"name": "Queen of Disks", "url": "queen_of_disks", "image": "images/pequ.jpeg",
         "desc": "Charming and generous person. Pragmatic and quiet, but ambitious. Opulence, security.",
         "rdesc": "A foolish and temperamental person. Prone to suspicion ad fearful of failure. Negligence.",
         "long_desc": "",
         "sequence": 38},

        {"name": "Knight of Disks", "url": "knight_of_disks", "image": "images/pekn.jpeg",
         "desc": "Mature and responsible, a trustworthy and laborious person. A capable manager. An important matter concerning money.",
         "rdesc": "Dull, lazy or clumsy person. Careless. Stagnation.",
         "long_desc": "",
         "sequence": 39},

        {"name": "Page of Disks", "url": "page_of_disks", "image": "images/pepa.jpeg",
         "desc": "A learned young person, careful and reflective. Good management, kind and benevolent. The bearer of good news and messages.",
         "rdesc": "Wasteful, illogical, rebellious youth. Bad news or lost of money.",
         "long_desc": "",
         "sequence": 40},

        {"name": "Ace of Disks", "url": "ace_of_disks", "image": "images/pe01.jpeg",
         "desc": "The beginning of prosperity and wealth. Pleasure and beauty.",
         "rdesc": "Success is delayed or it does not give happiness. Greed.",
         "long_desc": "",
         "sequence": 41},

        {"name": "Two of Disks", "url": "two_of_disks", "image": "images/pe02.jpeg",
         "desc": "Change. Alternation of gain and loss. Equilibrium in the midst of change. Ability to adapt to new circumstances. Some complications. Unstable mood.",
         "rdesc": "Uncertainty. Difficulty adapting to new circumstances.",
         "long_desc": "",
         "sequence": 42},

        {"name": "Three of Disks", "url": "three_of_disks", "image": "images/pe03.jpeg",
         "desc": "Works. Task well done. Commercial transactions. Professional growth. Dignity. A male child.",
         "rdesc": "Unsufficient skill or knowledge to achieve the goal. Fruitless work. Lack of seriousness.",
         "long_desc": "",
         "sequence": 43},

        {"name": "Four of Disks", "url": "four_of_disks", "image": "images/pe04.jpeg",
         "desc": "Power. Purely material gain and security. A gift or an inheritance. A female child. Greed.",
         "rdesc": "Prejudice. Limitation. Sudden check in progress or loss. Reckeless spending of money.",
         "long_desc": "",
         "sequence": 44},

        {"name": "Five of Disks", "url": "five_of_disks", "image": "images/pe05.jpeg",
         "desc": "Worry. Loss of money or employment. Poverty. Defeat. Lovers. Sympathy found in the midst of trouble.",
         "rdesc": "New employment or opportunity. Productive work. Misfortune in love.",
         "long_desc": "",
         "sequence": 45},

        {"name": "Six of Disks", "url": "six_of_disks", "image": "images/pe06.jpeg",
         "desc": "Success. Material gain and power. Sharing wealth with others.",
         "rdesc": "Transitory gains. Prodigality. Bribery. 'Purse-proud'.",
         "long_desc": "",
         "sequence": 46},

        {"name": "Seven of Disks", "url": "seven_of_disks", "image": "images/pe07.jpeg",
         "desc": "Failure. Defeat. Loss of money. Hard work but little gain. Greedy.",
         "rdesc": "Delayed success after hard work. Work done for the love of work without expecting retribution.",
         "long_desc": "",
         "sequence": 47},

        {"name": "Eight of Disks", "url": "eight_of_disks", "image": "images/pe08.jpeg",
         "desc": "Prudence. The first steps of a profitable profession. Learning a business or profession. Ability in material affairs. A brunette.",
         "rdesc": "Greedy. Selfish in a petty way. Vanity.",
         "long_desc": "",
         "sequence": 48},

        {"name": "Nine of Disks", "url": "nine_of_disks", "image": "images/pe09.jpeg",
         "desc": "Gain. Practical wisdom limited to everyday affairs and the home. Stability. Solitude. Inheritance.",
         "rdesc": "Loss of friendship or a material thing. Cancelled project. Beware of knavery.",
         "long_desc": "",
         "sequence": 49},

        {"name": "Ten of Disks", "url": "ten_of_disks", "image": "images/pe10.jpeg",
         "desc": "Wealth. Fulfillment of material fortune. Family matters. Inheritance. House.",
         "rdesc": "Family misfortune. Loss of inheritance. Beware of risky projects.",
         "long_desc": "",
         "sequence": 50},

        {"name": "King of Cups", "url": "king_of_cups", "image": "images/cuki.jpeg",
         "desc": "A person skilled in law or trade and interested in science, art, religion or philosophy. A good friend, liberal, idealistic and creative. Kind and willing to take some responsibility.",
         "rdesc": "A superficial person, easily enthusiastic, but with little depth of character. Untruthful, ruthless and vicious.",
         "long_desc": "",
         "sequence": 51},

        {"name": "Queen of Cups", "url": "queen_of_cups", "image": "images/cuqu.jpeg",
         "desc": "Dreamy, calm, poetic, imaginative, kind yet not willing to take much trouble for another.",
         "rdesc": "Dishonest and vicious person, not to be trusted.",
         "long_desc": "",
         "sequence": 52},

        {"name": "Knight of Cups", "url": "knight_of_cups", "image": "images/cukn.jpeg",
         "desc": "A young person, may be an artist, who is graceful and poetic. They are an indolent dreamer of sensual pleasures. Can mean a messenger, a proposition or an invitation.",
         "rdesc": "Lazy and deceitful, a dissolute and merciless person.",
         "long_desc": "",
         "sequence": 53},

        {"name": "Page of Cups", "url": "page_of_cups", "image": "images/cupa.jpeg",
         "desc": "Quiet and studious youth, but also sweet and dreamy. News or proposition.",
         "rdesc": "A sensual libertine, not harmful but neither helpful. Unpleasant news. Flatterer, selfish.",
         "long_desc": "",
         "sequence": 54},

        {"name": "Ace of Cups", "url": "ace_of_cups", "image": "images/cu01.jpeg",
         "desc": "Harmony, fertility, happiness, beginning of great love.",
         "rdesc": "Discord, false love, instability.",
         "long_desc": "",
         "sequence": 55},

        {"name": "Two of Cups", "url": "two_of_cups", "image": "images/cu02.jpeg",
         "desc": "Love. Harmony, warm friendship. Close relation with a kindred soul. Good for business and love.",
         "rdesc": "Opposition. False love. Folly, misunderstanding.",
         "long_desc": "",
         "sequence": 56},

        {"name": "Three of Cups", "url": "three_of_cups", "image": "images/cu03.jpeg",
         "desc": "Abundance. Pleasure, hospitality, success. The good things of life.",
         "rdesc": "Sensuality or food and drink intemperance.",
         "long_desc": "",
         "sequence": 57},

        {"name": "Four of Cups", "url": "four_of_cups", "image": "images/cu04.jpeg",
         "desc": "Luxury. Abandonment to desire. New ambition.",
         "rdesc": "Luxury that does not provide happiness. Dissatisfaction with material success. Turning point in life.",
         "long_desc": "",
         "sequence": 58},

        {"name": "Five of Cups", "url": "five_of_cups", "image": "images/cu05.jpeg",
         "desc": "Disappointment. Unexpected misfortune. Partial loss. Friendship or love gone. Inheritance.",
         "rdesc": "New happiness. Return of an old friend or love. Alliance.",
         "long_desc": "",
         "sequence": 59},

        {"name": "Six of Cups", "url": "six_of_cups", "image": "images/cu06.jpeg",
         "desc": "Pleasure. Happiness coming from the past. Nostalgia. Success.",
         "rdesc": "Uncertainty. Living too much in the past. Worthless associates. Inheritance.",
         "long_desc": "",
         "sequence": 60},

        {"name": "Seven of Cups", "url": "seven_of_cups", "image": "images/cu07.jpeg",
         "desc": "Debauch. Foolish expectations. Illusory dreams, deceit. Intoxication. Drug addiction.",
         "rdesc": "New will. Intelligent decision. Short travels.",
         "long_desc": "",
         "sequence": 61},

        {"name": "Eight of Cups", "url": "eight_of_cups", "image": "images/cu08.jpeg",
         "desc": "Indolence. Instability. Material success abandoned, may be for something higher. Decline in interest. Wandering.",
         "rdesc": "Joy, happiness. A new love or interest in material things..",
         "long_desc": "",
         "sequence": 62},

        {"name": "Nine of Cups", "url": "nine_of_cups", "image": "images/cu09.jpeg",
         "desc": "Happiness. Complete material success and well-being. You will get what you wish.",
         "rdesc": "Imperfection, deceit. Intemperance. You will not get what you wish.",
         "long_desc": "",
         "sequence": 63},

        {"name": "Ten of Cups", "url": "ten_of_cups", "image": "images/cu10.jpeg",
         "desc": "Satiety. Perfect love and lasting contentment. Peace, friendship.",
         "rdesc": "Dissipation, loss of friendship. Betrayal. Waste.",
         "long_desc": "",
         "sequence": 64},

        {"name": "King of Clubs", "url": "king_of_clubs", "image": "images/waki.jpeg",
         "desc": "Courageous, swift and generous person. Passionate and strong. Paternalistic and proud. May be a country gentleman, generally married. Unexpected heritage; a good marriage.",
         "rdesc": "Despotic, bigoted, prejudiced, evil-minded.",
         "long_desc": "",
         "sequence": 65},

        {"name": "Queen of Clubs", "url": "queen_of_clubs", "image": "images/waqu.jpeg",
         "desc": "Kind, energetic but calm person. Conservative, pragmatic and authoritarian. Fruitful in mind and body.",
         "rdesc": "Domineering, jealous, dogmatic and irrational. Quick to take offense.",
         "long_desc": "",
         "sequence": 66},

        {"name": "Knight of Clubs", "url": "knight_of_clubs", "image": "images/wakn.jpeg",
         "desc": "A young and energetic person. Swift and daring. May be noble and generous but also violent and hasty.",
         "rdesc": "Jealous, weak and intolerant person. Quarrel, discord, frustration.",
         "long_desc": "",
         "sequence": 67},

        {"name": "Page of Clubs", "url": "page_of_clubs", "image": "images/wapa.jpeg",
         "desc": "Young and brilliant. Enthusiastic and daring. A messenger or bearer of tidings.",
         "rdesc": "Frivolous youth. Theatrical and shallow. Cruel, oppressive.",
         "long_desc": "",
         "sequence": 68},

        {"name": "Ace of Clubs", "url": "ace_of_clubs", "image": "images/wa01.jpeg",
         "desc": "Creation, birth. The power or ability to begin or to follow through energetically with a plan or task; enterprise and determination. Beginning of an enterprise, invention or adventure.",
         "rdesc": "Fall. To lose or postpone something (employment, enterprise, etc.). False starts.",
         "long_desc": "",
         "sequence": 69},

        {"name": "Two of Clubs", "url": "two_of_clubs", "image": "images/wa02.jpeg",
         "desc": "Dominion. Maturity. Boldness with self-control. Influence.",
         "rdesc": "Disturbance. Indifferent to or disregardful of consequences. Fear, illness.",
         "long_desc": "",
         "sequence": 70},

        {"name": "Three of Clubs", "url": "three_of_clubs", "image": "images/wa03.jpeg",
         "desc": "Virtue. Established strength, realization of hope, nobility. Cooperation, partnership.",
         "rdesc": "Inconsistency, deception, treachery. Loss, robbery.",
         "long_desc": "",
         "sequence": 71},

        {"name": "Four of Clubs", "url": "four_of_clubs", "image": "images/wa04.jpeg",
         "desc": "Completion. Settlement, peace, harmony. Romance, marriage, society.",
         "rdesc": "Insecurity. Uneasiness, unreliableness. Contradictions, incomplete happiness.",
         "long_desc": "",
         "sequence": 72},

        {"name": "Five of Clubs", "url": "five_of_clubs", "image": "images/wa05.jpeg",
         "desc": "Strife. Competition, lawsuit, obstacles, violence, fighting.",
         "rdesc": "Dangerous indecision, treachery, complication.",
         "long_desc": "",
         "sequence": 73},

        {"name": "Six of Clubs", "url": "six_of_clubs", "image": "images/wa06.jpeg",
         "desc": "Victory after strife. Good news. Progress, helping friends.",
         "rdesc": "Postponement. Insolence, excessive pride. Treason.",
         "long_desc": "",
         "sequence": 74},

        {"name": "Seven of Clubs", "url": "seven_of_clubs", "image": "images/wa07.jpeg",
         "desc": "Valor. Victory through courage. Struggle. Fierce competition. Certain success.",
         "rdesc": "Uncertainty and fear. Pregnancy. False appearance.",
         "long_desc": "",
         "sequence": 75},

        {"name": "Eight of Clubs", "url": "eight_of_clubs", "image": "images/wa08.jpeg",
         "desc": "Swiftness. Hasty decision. Air travel, messages. Love letter. Hyperactivity. Great hopes.",
         "rdesc": "Opposition. Jealousy. Delay in business or love affair.",
         "long_desc": "",
         "sequence": 76},

        {"name": "Nine of Clubs", "url": "nine_of_clubs", "image": "images/wa09.jpeg",
         "desc": "Strength. Capability of enduring a long struggle and achieve the final victory. Recovery from sickness.",
         "rdesc": "Weakness, delays, sickness. Adversity.",
         "long_desc": "",
         "sequence": 77},

        {"name": "Ten of Clubs", "url": "ten_of_clubs", "image": "images/wa10.jpeg",
         "desc": "Oppression. Imbalance and selfishness. Heavy burden. Force detached from spiritual sources. A problem may be solved soon.",
         "rdesc": "Annoyances. Treason. Separation, emigration. Some loses.",
         "long_desc": "",
         "sequence": 78},

    ]
    return deck
