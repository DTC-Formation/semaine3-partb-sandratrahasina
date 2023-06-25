def affichage_mot_a_trouver(mot_a_trouver : str, labels : list): 
    mots = []
    for l in list(mot_a_trouver):
        if(l in labels):
            mots.append(l)
        else:
            mots.append('-')
    return "".join(mots)
