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

import json
f8=open("wrt.txt","w")

f15=open("vanill.txt","r")
#f16=open("avg.txt","r")

data=json.load(f15)



flist=[]
fl=dict()


for i in files:
    f=open(i,"r")
    text=f.readlines()
    flc[i]= text


W_td=dict()
W_pn=dict()
biaspn=0.0
biastd=0.0



# for average perceptron
W_td_u=dict()
W_pn_u=dict()
biaspn_u=0.0
biastd_u=0.0
q=0



biaspn = data['PN']['b']
W_td = data['TD']['f']
biastd = data['TD']['b']
W_pn = data['PN']['f']
pos_neg_y = {"negative": -1, "positive": 1}
tru_d_y = {"deceptive": -1, "truthful": 1}




for path ,text in flc.iteritems():
        #label1,label2,fold,fname=path.split("/")[-4:]

    q=q+1
        #label1 = label1.split("_")[0]
        #label2 = label2.split("_")[0]

    text[-1] = text[-1].strip()

    tokens = " ".join(text)

    tokens = tokens.translate(None, string.punctuation).lower()

    tokens = [letter for letter in tokens.split() if (letter.isalnum()) and (letter not in sw)]
    tokens = ' '.join(tokens)

    tokens = ''.join([i for i in tokens if not i.isdigit()])

    tokens = tokens.split()

    features_temp = dict()


    for value in tokens:
        if value in features_temp:
            features_temp[value]=features_temp[value]+1
        else:
            features_temp[value]=1.0
    resulttd=biastd
    resultpn=biaspn

    for ii,jj in features_temp.iteritems():
        if ii in W_td:
            resulttd=resulttd+(jj*W_td[ii])


        if ii in W_pn:
            resultpn=resultpn+(jj*W_pn[ii])

    if (resulttd < 0):
        f8.write("deceptive ")
    else:
        f8.write("truthful ")

    if(resultpn<0):
        f8.write("negtive ")

    else:
        f8.write("positive ")






    f8.write(path)

    f8.write("\n")




f8.close()


