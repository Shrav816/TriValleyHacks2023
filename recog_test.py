
Case_statements = ['if','elif','while','for']
functions = ['print','max','len','upper']
datatypes = ['string', 'int', 'list']
operators = ['equals', 'in']
basic_changers = {'comma':',','quote':"'","greater":'>','less':'<','equal':'=','close':')',"open":'(','equals':' = ','space':' ','colon':':','plus':'+','minus':'-','modulo':'%','times':'*','power':'**','dot':'.'}
methods = ['upper']
#spacer = ['return']

# Formats a method (input: name method, output: name.method())
def check_if_method(query,word):
    if query.index(word) != len(query)-1 and query[query.index(word)+1] in methods:
        return word
def createMethod(query):
    if "quote" in query:
        string = createString(query, [i for i, x in enumerate(query) if x == "quote"])
    else:
        string = ""
        for s in query[:len(string) - 1]:
            string += s
    return string + "." + query[len(query) - 1] + "()"

# Formats a string (input: quote input quote, output: "input")
def createString(query, quoteLocation):
    string = ""
    for s in query[quoteLocation[0] + 1: quoteLocation[1]]:
        string += s + " "
    string = string[:len(string) - 1]
    return "\"" + string + "\""


def check_basic_changers(word,written):
    if word in basic_changers:
        return written + basic_changers[word]
def test_recog(query):
    written = ''
    index = 0
    Case = False
    #checking through case statements
    if query[0] in Case_statements:   
        written += query[0]+' '
        index+=1
        Case = True
        #for word in query:
        
            #written += " "
            #if word == 'equals':
               # written += "=="
            #else:
               # written += word 
        #written += ":"
    #checking through functions
    if query[index] in functions:
        funcount = 0
        string = False
        #deal with other functions later 
        written += query[index]
        written +="("
        if query[index] == 'string':
            written+= "'"
        
            #print("going into function",query[index:len(query)])
        for word in query[index+1:len(query)]:
            if check_basic_changers(word,written):
                written = check_basic_changers(word,written)
           
            
            elif word in functions :
                funcount +=1
                written +=(word + "(") 
            else:
                written = written + word
            
            #else:
               # written += ","
            #if string:
                #written+= "'"
        written += ")"+")"*funcount 
        if Case:
            written += ':'
        return written
    #other persons code -- not currently working
     # function definitions
    if query[0]== 'def':
        functions.insert(0,query[1])
        written = 'def '+query[1]+'('
        if len(query)>2:
            for word in query[2:len(query)]:
                written += word+','
        written=written[0:len(written)-1] + '):'      
        #print(written)
            #written += createMethod(query)
    else:
        for word in query[index:len(query)]:
            if check_basic_changers(word,written):
                written = written[0:len(written)-1]
                written = check_basic_changers(word,written)
            elif word in methods:
                written = written[0:len(written)-1]
                written += "."+word+"()"
            else:
                written += word + ' '
    if Case:
        written += ":"
    return written

def recursive_test_recog(query,type_tracker="none",reString=""):
    type_dict = {"function":")","case":":"}
    print("function starting")
    if len(query) == 0:
        print("base case:",reString)
        return reString + type_dict[type_tracker]
    #checking through case statements
    if query[0] in Case_statements:
        reString = reString + query[0] + " "
        print("case statement:",reString)
        return recursive_test_recog(query[1:len(query)],type_tracker,reString)

    #checking through functions
    #print("functions")
    if query[0] in functions:
        reString = reString + query[0] + "("
        print("function:",reString)
        return recursive_test_recog(query[1:len(query)],'function',reString)
    



    
print(test_recog(['def','fun','message']))
print(test_recog(['if','len','message','greater','5']))
print(test_recog(['message','equals','message','upper']))
print(test_recog(['return','message']))
print('')
print(test_recog(['text','equals','quote','hello','judges','quote']))
print(test_recog(['print','fun','text']))