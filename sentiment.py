def analyze_sentiment(text):
    positive_words = {
        # Inglese
        "good": 1, "great": 2, "excellent": 2, "amazing": 2, "awesome": 2,
        "fantastic": 2, "wonderful": 2, "brilliant": 2, "superb": 2, "outstanding": 2,
        "perfect": 2, "beautiful": 1, "love": 2, "loved": 2, "loving": 1,
        "happy": 1, "happiness": 2, "joy": 2, "joyful": 2, "excited": 1,
        "exciting": 1, "impressive": 1, "incredible": 2, "magnificent": 2,
        "positive": 1, "best": 2, "better": 1, "nice": 1, "enjoy": 1,
        "enjoyed": 1, "enjoying": 1, "fun": 1, "funny": 1, "like": 1,
        "liked": 1, "useful": 1, "helpful": 1, "recommend": 1, "recommended": 1,
        "innovative": 1, "successful": 1, "success": 1, "win": 1, "winner": 1,
        "winning": 1, "safe": 1, "strong": 1, "powerful": 1, "hope": 1,
        "hopeful": 1, "promising": 1, "progress": 1, "improvement": 1, "improved": 1,
        "easy": 1, "efficient": 1, "smart": 1, "clever": 1, "genius": 2,

        # Italiano
        "bello": 1, "bella": 1, "ottimo": 2, "ottima": 2, "fantastico": 2,
        "fantastica": 2, "meraviglioso": 2, "meravigliosa": 2, "eccellente": 2,
        "perfetto": 2, "perfetta": 2, "buono": 1, "buona": 1, "bravo": 1,
        "brava": 1, "amore": 2, "felice": 1, "felicità": 2, "gioia": 2,
        "gioioso": 1, "positivo": 1, "positiva": 1, "migliore": 2, "meglio": 1,
        "piacevole": 1, "divertente": 1, "utile": 1, "consiglio": 1, "consigliato": 1,
        "innovativo": 1, "innovativa": 1, "successo": 1, "vincere": 1, "vincitore": 1,
        "forte": 1, "potente": 1, "speranza": 1, "promettente": 1, "progresso": 1,
        "miglioramento": 1, "migliorato": 1, "facile": 1, "efficiente": 1,
        "intelligente": 1, "geniale": 2, "straordinario": 2, "straordinaria": 2,
        "incredibile": 2, "stupendo": 2, "stupenda": 2, "magnifico": 2, "magnifica": 2,
    }

    negative_words = {
        # Inglese
        "bad": -1, "terrible": -2, "horrible": -2, "awful": -2, "disgusting": -2,
        "worst": -2, "worse": -1, "poor": -1, "disappointing": -2, "disappointed": -1,
        "hate": -2, "hated": -2, "hating": -1, "ugly": -1, "boring": -1,
        "useless": -2, "broken": -1, "fail": -2, "failed": -2, "failure": -2,
        "sad": -1, "sadness": -1, "unhappy": -1, "miserable": -2, "depressed": -2,
        "depression": -2, "angry": -1, "anger": -1, "furious": -2, "frustrated": -1,
        "frustrating": -1, "annoying": -1, "annoyed": -1, "dangerous": -2,
        "damage": -1, "damaged": -1, "corrupt": -2, "corrupted": -2, "evil": -2,
        "wrong": -1, "error": -1, "problem": -1, "issue": -1, "difficult": -1,
        "hard": -1, "impossible": -2, "weak": -1, "stupid": -2, "idiot": -2,
        "waste": -1, "wasted": -1, "lie": -2, "lied": -2, "fake": -2,
        "scam": -2, "fraud": -2, "toxic": -2, "violent": -2, "violence": -2,
        "crisis": -2, "disaster": -2, "catastrophe": -2, "terrible": -2,

        # Italiano
        "brutto": -1, "brutta": -1, "pessimo": -2, "pessima": -2, "terribile": -2,
        "orribile": -2, "schifoso": -2, "schifosa": -2, "peggiore": -2, "peggio": -1,
        "deludente": -2, "deluso": -1, "delusa": -1, "odio": -2, "odioso": -2,
        "odiosa": -2, "brutto": -1, "noioso": -1, "noiosa": -1, "inutile": -2,
        "rotto": -1, "rotta": -1, "fallire": -2, "fallito": -2, "fallita": -2,
        "fallimento": -2, "triste": -1, "tristezza": -1, "infelice": -1,
        "misero": -2, "misera": -2, "depresso": -2, "depressa": -2, "arrabbiato": -1,
        "arrabbiata": -1, "rabbia": -1, "furioso": -2, "furiosa": -2,
        "frustrato": -1, "frustrata": -1, "fastidioso": -1, "fastidiosa": -1,
        "pericoloso": -2, "pericolosa": -2, "danno": -1, "danneggiato": -1,
        "corrotto": -2, "corrotta": -2, "sbagliato": -1, "sbagliata": -1,
        "errore": -1, "problema": -1, "difficile": -1, "impossibile": -2,
        "debole": -1, "stupido": -2, "stupida": -2, "idiota": -2, "spreco": -1,
        "bugiardo": -2, "bugiarda": -2, "falso": -2, "falsa": -2, "truffa": -2,
        "tossico": -2, "tossica": -2, "violento": -2, "violenta": -2,
        "crisi": -2, "disastro": -2, "catastrofe": -2,
    }

    intensifiers = {
        "very": 1.5, "really": 1.5, "extremely": 2.0, "absolutely": 2.0,
        "incredibly": 2.0, "so": 1.3, "quite": 1.2, "totally": 1.5,
        "completely": 1.5, "utterly": 2.0, "highly": 1.5, "super": 1.5,
        "molto": 1.5, "davvero": 1.5, "estremamente": 2.0, "assolutamente": 2.0,
        "incredibilmente": 2.0, "così": 1.3, "abbastanza": 1.2, "totalmente": 1.5,
        "completamente": 1.5, "altamente": 1.5,
    }

    negations = {
        "not", "no", "never", "neither", "nor", "without", "hardly", "barely",
        "non", "no", "mai", "né", "senza", "appena",
    }

    if not text or text.strip() == "":
        return "Neutro"

    words = text.lower().split()
    score = 0.0
    i = 0

    while i < len(words):
        word = words[i].strip(".,!?;:\"'()[]{}")

        if word in positive_words or word in negative_words:
            word_score = positive_words.get(word, 0) + negative_words.get(word, 0)

            multiplier = 1.0
            if i > 0:
                prev = words[i - 1].strip(".,!?;:\"'()[]{}")
                if prev in intensifiers:
                    multiplier = intensifiers[prev]
                elif prev in negations:
                    multiplier = -1.0
            if i > 1:
                prev2 = words[i - 2].strip(".,!?;:\"'()[]{}")
                if prev2 in negations and words[i - 1].strip(".,!?;:\"'()[]{}") not in positive_words and words[i - 1].strip(".,!?;:\"'()[]{}") not in negative_words:
                    multiplier = -1.0

            score += word_score * multiplier

        i += 1

    if score > 1:
        return "Positivo"
    elif score < -1:
        return "Negativo"
    else:
        return "Neutro"