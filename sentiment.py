def analyze_sentiment(text):
    positive_words = ["bello", "ottimo", "fantastico", "meraviglioso", "positivo", "buono", "eccellente", "grande", "amato", "perfetto"]
    negative_words = ["brutto", "terribile", "peggiorato", "negativo", "orribile", "cattivo", "pessimo", "odioso", "scadente", "deludente"]

    words = text.lower().split()
    score = 0

    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1

    if score > 0:
        return "Positivo"
    elif score < 0:
        return "Negativo"
    else:
        return "Neutro"
