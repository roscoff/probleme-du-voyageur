import numpy as np
import random

#nomenclature
#n : nombre de ville
#m : taille de l'échantillon
#D : carte des distance (matrice n*n)
#P : liste de solutions


#genere distance entre 10 et 500 unités
distMin = 10
distMax = 500
def carto(n):
    D = np.random.randint(distMin, distMax, size=(n,n)) 
    D = (D + D.transpose()) // 2
    np.fill_diagonal(D, 0)
    return D

def populat(n, m):
    numsVilles = np.arange(2, n+1)
    P = np.zeros(shape=(n, m), dtype=int)
    P[0, :] = 1
    for c in range(m):
        np.random.shuffle(numsVilles)
        P[1:,c] = numsVilles
    return P

def calculAdapt(sol, D):
    dist = 0
    for i in range(1, len(sol)-1):
        dist = dist + D[sol[i-1]-1, sol[i]-1]
    dist = dist + D[sol[len(sol)-1]-1 , 0]
    return dist

#retourne les > 50% meilleurs solutions
def selectElit(P, D):
    adapts = calculAdapt(P, D)
    top_id = adapts.argsort()[:len(adapts)//2]
    return P[:,top_id]

def selectTourn(P, D):
    gagnants = np.zeros(shape=(P.shape[0], 0), dtype=int)
    for i in range((len(P)//2)-1):
        ids = np.random.randint(0, P.shape[1], size=(2))
        combatants = P[:, ids]
        gagnant = selectElit(combatants, D)
        gagnants = np.c_[ gagnants, gagnant] #ajoute la colonne gagnant a gagnants
    return gagnants

def croisement(parents):
    i = 1 #debut de croisement
    j = (parents.shape[0]-1) // 2 #largeur de croisement
    enfants = np.copy(parents)

    gene = np.flip(enfants[i:i+j,:], axis=1) #genes croisé
    enfants[i:i+j,:] = gene #copy les genes avec croisement

    diffs1 = np.setdiff1d(gene[:,0],gene[:,1], assume_unique=True)
    diffs2 = np.setdiff1d(gene[:,1],gene[:,0], assume_unique=True)

    for t in range(len(diffs1)): #elimine les doublons en échangant les differences
        enfants[i+j:,0][enfants[i+j:,0] == diffs2[t]] = diffs1[t]
        enfants[i+j:,1][enfants[i+j:,1] == diffs1[t]] = diffs2[t]

    return enfants

def mutation(individu):
    i, j = np.random.choice(len(individu)-1, size=2, replace=False)+1
    mutant = np.copy(individu)
    temp = mutant[i]
    mutant[i] = mutant[j]
    mutant[j] = temp
    return mutant

# la fonction genetiq retourne une solution possible parmis les meilleurs 
# pour résoudre le probleme du voyageur
#n nombre de ville
#m taille de l'échantillon
#t nombre de mutations moy par solution
#i nombre d'iteration
#D la carte
def genetiq(n, m, D, t, i, funcSelection):
    genese = populat(n, m)
    for it in range(i):
        #selection
        genese = funcSelection(genese, D)
        #croisement
        for c in range(genese.shape[1] // 2): #forme des couples
            parents = genese[:,c:c+2]
            enfants = croisement(parents)
            genese = np.append(genese, enfants, axis=1)
        np.random.shuffle(genese.transpose())
        # mutation
        for c in range(round(genese.shape[1]*t)):
            r = random.randint(0, genese.shape[1]-1)
            genese[:, r] = mutation(genese[:, r])

    #retourne le meilleur
    adapts = calculAdapt(genese, D)
    top_id = adapts.argsort()[:1]
    return genese[:,top_id]



#premier test avec n = 10 par selection elite
n = 10
carte = carto(n)
solution = genetiq(n, 32, carte, 0.5, 800, selectElit)
print("PREMIER TEST n = 10\nla carte choisie\n", carte)
print("la solution retenue\n", solution.transpose(),  "\navec un score de", calculAdapt(solution, carte), "l'esperance est de ", (n+1)*(distMax-distMin)/2)


#second test avec n = 80 par selection elite
n = 80
carte = carto(n)
solution = genetiq(n, 32, carte, 0.5, 800, selectElit)
print("\nSECOND TEST n = 80\nla carte choisie\n", carte)
print("la solution retenue\n", solution.transpose(),  "\navec un score de ", calculAdapt(solution, carte), "l'esperance est de ", (n+1)*(distMax-distMin)/2)



#comparation de la fonction selectTourn avec selectElit
n = 45
carte = carto(n)
print("\nTEST comparaison de la fontion selectElite avec selectTourn")
solutionElite = genetiq(n, 64, carte, 0.5, 300, selectElit)
print("avec la fonction Elite score : ", calculAdapt(solutionElite, carte), "l'esperance est de ", (n+1)*(distMax-distMin)/2)
solutionTourn = genetiq(n, 64, carte, 0.5, 300, selectTourn)
print("avec la fonction Tourn score : ", calculAdapt(solutionTourn, carte), "l'esperance est de ", (n+1)*(distMax-distMin)/2)
