#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 16:29:24 2022

@author: muntabir
"""
import urllib.parse, urllib.request, json
import pandas as pd


def CallWikifier(text, lang="en", threshold=0.9):
    # Prepare the URL.
    data = urllib.parse.urlencode([
        ("text", text), ("lang", lang),
        ("userKey", "qjtjcmrbvorvuxfzfyxxoucagxpreb"),
        ("pageRankSqThreshold", "%g" % threshold), ("applyPageRankSqThreshold", "true"),
        ("nTopDfValuesToIgnore", "200"), ("nWordsToIgnoreFromList", "200"),
        ("wikiDataClasses", "true"), ("wikiDataClassIds", "false"),
        ("support", "true"), ("ranges", "false"), ("minLinkFrequency", "2"),
        ("includeCosines", "false"), ("maxMentionEntropy", "3")
        ])
    url = "http://www.wikifier.org/annotate-article"
    # Call the Wikifier and read the response.
    req = urllib.request.Request(url, data=data.encode("utf8"), method="POST")
    with urllib.request.urlopen(req, timeout = 60) as f:
        response = f.read()
        response = json.loads(response.decode("utf8"))
    # Output the annotations.
    for annotation in response["annotations"]:
        print("%s (%s)" % (annotation["title"], annotation["url"]))


data = pd.read_csv("./data/metadata_abstract.csv")
## we are reading only two rows. To read all rows remove the list slicing
for abstract in data['text'][0:2]:
    wikify = CallWikifier(abstract)
    print("\n")
    
    
### Examples of Abstract
"""SOME ASPECTS OF RADIATION INDUCED NUCLEATION OF WATER by Chih-Ping Tso Submitted to the Department of Nuclear Engineering on August 11, 1970 in partial fulfillment of the requirements for the degree of Master of Science. ABSTRACT Experimental data for the determination of superheats of separately, fission fragments and fast neutrons in water were taken with an experimen- (2) tally modified set up of Bell: Attempts to correlate both data from present work and from Bell with theory led to apparent inadequacies with the theory. The theory is based on an 'Energy Balance Method' developed by Bell. This method was also used to compute threshold superheat for (5) benzene, for later comparison with data from another investigator when this reference becomes available. Application of this Energy Balance Method to predict fission neutrons induced nucleation and alpha particles induced nucleation (alpha particles from (n,x) reaction on Boron) at Pressurised Water Reactor conditions indicated that radiation induced nucleation for monoenergetic neutrons and alphas present in reactor may be effective in causing initiation of nucleate boiling. However, detailed consideration of all neutron energies present (spectrum) was not accomplished to arrived at a definite conclu- sion for this reactor case. Thesis Supervisor Neil E. Todreas Title Assistant Professor"""

"""PROCEDURES AS A REPRESENTATION FOR DATA IN A COMPUTER PROGRAM FOR UNDERSTAND : NG NATURAL LANGUAGE by Terry Winograd Submitted to the Department of Mathematics on August 24, 1970 in partial fulfillment of the requirements for the degree of Doctor of Philosophy ABSTRACT This paper describes a system for the computer understanding of English. The system answers questions, executes commands, and accepts information in normal English dialog. It uses semantic information and context to understand discourse and to disambiguate sentences. It combines a complete syntactic analysis of each sentence with a "heuristic understander" which uses different kinds of information about a sentence, other parts of the discourse, and general information about the world in deciding what the sentence means. It is based on the belief that a computer cannot deal reasonably with language unless it can "understand" the subject it is discussing. The program is given a detailed model of the knowledge needed by a simple robot having only a hand and an eye. We can give it instructions to manipulate toy objects, interrogate it about the scene, and give it information it will use in deduction. In addition to knowing the properties of toy objects, the program has a simple model of its own mentality. It can remember and discuss its plans and actions as well as carry them out. It enters into a dialog with a person, responding to English sentences with actions and English replies, and asking for clarification when its heuristic programs cannot understand a sentence through use of context and physical knowledge. In the programs, syntax, semantics and inference are integrated in a "vertical" system in which each part is constantly communicating with the others. We have explored several techniques for integrating the large bodies of complex knowledge needed to understand language. We use Systomic Grammar, a type of syntactic analysis which is designed to deal with semantics. Rather than concentrating on the exact form of rules for the shapes of inguistic constituents, it is structured around choices for conveying meaning. It abstracts the relevant features of the linguistic structures which are important for interpreting their meaning. We represent many kinds of knowledge in the form of procedures rather than tables of rules or lists of patterns. By developing special procedural languages for grammar, semantics, and deductive logic, we gain the flexibility and power of programming languages while retaining the regularity and understandability of simpler rule forms. Each piece of knowledge can be a procedure, and can call on any other piece of knowledge in the system. Thesis Supervisor: Seymour A. ?apert Title: Professor of Applied Mathematics"""

