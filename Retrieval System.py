import os

def builddictionary(folder):
    dirs=os.listdir(folder)
    dic={}
    for fname in dirs:
        wordcounts={}
        dic[fname]=wordcounts
        if fname=='.DS_Store':
            continue
        text=open(folder+'/'+ fname,'r')
        for line in text:
            line=line.split('\n')
            line=line[0]
            if line not in wordcounts:
                wordcounts[line]=1
            else:
                wordcounts[line]=wordcounts[line]+1     
    return dic
    
def computesimilarity(doc1,doc2):
    dot_product=0
    for word in doc1:
        if word in doc2:
            dot_product=dot_product+(doc1[word]*doc2[word])
        else:
            continue
    return dot_product

def topsimilardocs(query, dic, k):
    tupofsimilar=()
    for eachfile in dic:
        similarity=computesimilarity(query,dic[eachfile])
        tupofsimilar+= ((eachfile, similarity),)
    tupofsimilar=tuple(sorted(tupofsimilar,key=lambda x: x[1], reverse=True))
    tupofsimilar=tupofsimilar[0:k]
    return tupofsimilar

def main():
    folder1=raw_input('enter your document folder')
    dic=builddictionary(folder1)
    folder2=raw_input('enter your query file folder')
    dicofquery=builddictionary(folder2)
    queryid=raw_input('enter your query id:')
    k=5
    tupofsimilar=topsimilardocs(dicofquery[queryid],dic,k)
    print 'Top 5 similar documents to query '+queryid+' is:'
    for doc,similarity in tupofsimilar:
        print doc + ' '+ str(similarity)

while True:
    main()


          
    
