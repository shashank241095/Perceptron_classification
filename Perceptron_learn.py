import os
import glob
import sys
import collections

import string

c=1.0
sw = ["a", "able", "about", "above", "across", "again", "ain't", "all", "almost", "along", "also", "am",
              "among", "amongst", "an", "and", "anyhow", "anyone", "anyway", "anyways", "appear", "are", "around", "as",
              "a's", "aside", "ask", "asking", "at", "away", "be", "became", "because", "become", "becomes", "becoming",
              "been", "before", "behind", "below", "beside", "besides", "between", "beyond", "both", "brief", "but",
              "by", "came", "can", "come", "comes", "consider", "considering", "corresponding", "could", "do", "does",
              "doing", "done", "down", "downwards", "during", "each", "edu", "eg", "eight", "either", "else",
              "elsewhere", "etc", "even", "ever", "every", "ex", "few", "followed", "following", "follows", "for",
              "former", "formerly", "from", "further", "furthermore", "get", "gets", "getting", "given", "gives", "go",
              "goes", "going", "gone", "got", "gotten", "happens", "has", "have", "having", "he", "hed", "hence", "her",
              "here", "hereafter", "hereby", "herein", "here's", "hereupon", "hers", "herself", "he's", "hi", "him",
              "himself", "his", "how", "hows", "i", "i'd", "ie", "if", "i'll", "i'm", "in", "inc", "indeed", "into",
              "inward", "is", "it", "it'd", "it'll", "its", "it's", "itself", "i've", "keep", "keeps", "kept", "know",
              "known", "knows", "lately", "later", "latter", "latterly", "lest", "let", "let's", "looking", "looks",
              "ltd", "may", "maybe", "me", "mean", "meanwhile", "might", "most", "my", "myself", "name", "namely", "nd",
              "near", "nearly", "need", "needs", "neither", "next", "nine", "no", "non", "now", "nowhere", "of", "off",
              "often", "oh", "ok", "okay", "old", "on", "once", "one", "ones", "only", "onto", "or", "other", "others",
              "ought", "our", "ours", "ourselves", "out", "over", "own", "per", "placed", "que", "quite", "re",
              "regarding", "said", "same", "saw", "say", "saying", "says", "second", "secondly", "see", "seeing",
              "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "seven", "several",
              "she", "she'd", "she'll", "she's", "since", "six", "so", "some", "somebody", "somehow", "someone",
              "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "specified", "specify",
              "specifying", "still", "sub", "such", "sup", "sure", "take", "taken", "tell", "tends", "th", "than",
              "that", "thats", "that's", "the", "their", "theirs", "them", "themselves", "then", "thence", "there",
              "thereafter", "thereby", "therefore", "therein", "theres", "there's", "thereupon", "these", "they",
              "they'd", "they'll", "they're", "they've", "think", "third", "this", "those", "though", "three",
              "through", "thru", "thus", "to", "together", "too", "took", "toward", "towards", "tried", "tries",
              "truly", "try", "trying", "t's", "twice", "two", "un", "under", "up", "upon", "us", "use", "used", "uses",
              "using", "usually", "value", "various", "very", "via", "viz", "vs", "want", "wants", "was", "wasn't",
              "way", "we", "we'd", "we'll", "went", "were", "we're", "weren't", "we've", "what", "whatever", "what's",
              "when", "whence", "whenever", "when's", "where", "whereafter", "whereas", "whereby", "wherein", "where's",
              "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom",
              "who's", "whose", "why", "why's", "will", "willing", "wish", "with", "within", "without", "won't",
              "would", "wouldn't", "yes", "yet", "you", "you'd", "you'll", "your", "you're", "yours", "yourself",
              "yourselves", "you've"]


curr_path=sys.argv[1]

files = glob.glob(os.path.join(curr_path, '*/*/*/*.txt'))
flc = collections.defaultdict(list)


f8=open("fil8.txt","w")
flist=[]
fl=dict()


for i in files:
    f=open(i,"r")
    text=f.readlines()
    flc[i]= text





def clean(tokens):
    if len(tokens) >= 5:

        if tokens.endswith("or"):
            tokens = tokens[:-2]

    return tokens



def powerclean(text):
    tokens = " ".join(text)

    tokens = tokens.translate(None, string.punctuation).lower()

    tokens = [clean(letter) for letter in tokens.split() if (letter.isalnum()) and (letter not in sw)]



    tokens = ' '.join(tokens)

    tokens = ''.join([i for i in tokens if not i.isdigit()])

    tokens = tokens.split()


    return tokens




def activation(temp_features,W_td,W_pn):
    a = 0
    a_pn = 0
    for keyt, v in features_temp.iteritems():
        if keyt in W_td:
            a = a + (W_td[keyt] * v)

        if keyt in W_pn:
            a_pn = a_pn + (v * W_pn[keyt])

    a = a + biastd

    a_pn = a_pn + biaspn

    return a,a_pn


# 2 classes feature with bias
W_td=dict()
W_pn=dict()
biaspn=0.0
biastd=0.0


W_td_u=dict()
W_pn_u=dict()
biaspn_u=0.0
biastd_u=0.0
q=0
pos_neg_y = {"negative": -1, "positive": 1}
tru_d_y = {"deceptive": -1, "truthful": 1}
for loop in range(0,20):

    for path ,text in flc.items():
        label1,label2,fold,fname=path.split("/")[-4:]

        q=q+1
        label1 = label1.split("_")[0]
        label2 = label2.split("_")[0]

        text[-1] = text[-1].strip()

        tokens=powerclean(text)

        features_temp = dict()

        for value in tokens:

            if value in features_temp:
                features_temp[value]=features_temp[value]+1
            else:
                features_temp[value]=1.0

        a,a_pn=activation(features_temp,W_td,W_pn)




        truthful_decptive_class=0.0
        positive_negative_class=0.0
        truthful_decptive_class=a*tru_d_y[label2]

        positive_negative_class=a_pn*pos_neg_y[label1]


        if(truthful_decptive_class<=0):
            biastd = biastd + tru_d_y[label2]
            biastd_u = biastd_u + (c * tru_d_y[label2])

            for kk,vv in features_temp.iteritems():

                if kk in W_td_u:

                    W_td_u[kk] = W_td_u[kk] + (c * tru_d_y[label2] * vv)

                else:
                    W_td_u[kk] = c * tru_d_y[label2] * vv

                if kk in W_td:

                    W_td[kk]=W_td[kk]+(tru_d_y[label2]*vv)

                else:
                    W_td[kk]=tru_d_y[label2]*vv




        if(positive_negative_class<=0):

            biaspn = biaspn + pos_neg_y[label1]
            biaspn_u = biaspn_u + (c * pos_neg_y[label1])
            for k, v_pn in features_temp.iteritems():

                if k in W_pn_u:

                    W_pn_u[k] = W_pn_u[k] + (c * pos_neg_y[label1] * v_pn)

                else:
                    W_pn_u[k] = c * pos_neg_y[label1] * v_pn

                if k in W_pn:

                    W_pn[k] = W_pn[k] + (pos_neg_y[label1] * v_pn)

                else:
                    W_pn[k] = (pos_neg_y[label1] * v_pn)



        c=c+1




print biaspn
print biastd
avg_Wpn=dict()
avg_Wtd=dict()
avg_biaspn=biaspn-(biaspn_u/c)
avg_biastd=biastd-(biastd_u/c)


for i,j in W_td.iteritems():
    avg_Wtd[i]=W_td[i]-(W_td_u[i]/c)

for ii,jj in W_pn.iteritems():
    avg_Wpn[ii]=W_pn[ii]-(W_pn_u[ii]/c)




filea=open("avg.txt","w")
filev=open("vanill.txt","w")

filev.write(str(W_pn))
filev.write("\n")

filev.write(str(W_td))
filev.write("\n")

filev.write(str(biaspn))
filev.write("\n")

filev.write(str(biastd))


filea.write(str(avg_Wpn))
filea.write("\n")

filea.write(str(avg_Wtd))
filea.write("\n")

filea.write(str(avg_biaspn))
filea.write("\n")

filea.write(str(avg_biastd))



filea.close()
filev.close()



