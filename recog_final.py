
Case_statements = ['if','elif','while','for']
functions = ['print','max','len']
datatypes = ['string', 'int', 'list']
operators = ['equals', 'in']
basic_changers = {'comma':',','quote':"'","greater":'>','less':'<','equal':'=','close':')',"open":'(','equals':' = ','space':' ','colon':':','plus':'+','minus':'-','modulo':'%','times':'*','power':'**','dot':'.'}
methods = ['upper','lower']
#spacer = ['return']

# Formats a method (input: name method, output: name.method())
def check_if_method(query,word):
    if query.index(word) != len(query)-1 and query[query.index(word)+1] in methods:
        return word



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

    #checks through functions
    if query[index] in functions:
        funcount = 0
        string = False
        written += query[index]
        written +="("
        if query[index] == 'string':
            written+= "'"

            #could change this so it adds at the bottom but I'm too lazy. Maybe later
        for word in query[index+1:len(query)]:
            #checks for subs
            if check_basic_changers(word,written):
                written = check_basic_changers(word,written)
            #checks for methods
            elif word in methods:
                if written[len(written)-1] == " ":
                    written = written[0:len(written)-1]
                written += "."+word+"()"
            #deals with nested function
            elif word in functions :
                funcount +=1
                written +=(word + "(") 
            else:
                written = written + word
        #ends the function and deals with conditionals if they are there
        written += ")"+")"*funcount 
        if Case:
            written += ':'
        return written
     # function definitions
    if query[0]== 'def':
        functions.insert(0,query[1])
        written = 'def '+query[1]+'('
        if len(query)>2:
            for word in query[2:len(query)]:
                written += word+','
        written=written[0:len(written)-1] + '):'      
       
       #concantinates and formats everything not already done
    else:
        for word in query[index:len(query)]:
            if check_basic_changers(word,written):
                written = written[0:len(written)-1]
                written = check_basic_changers(word,written)
            elif word in methods:
                if written[len(written)-1] == " ":
                    written = written[0:len(written)-1]
                written += "."+word+"()"
            else:
                written += word + ' '
    if Case:
        written += ":"
    return written


    



    
print(test_recog(['def','fun','message']))
print(test_recog(['if','len','message','greater','5']))
print(test_recog(['message','equals','message','upper']))
print(test_recog(['return','message']))
print('')
print(test_recog(['text','equals','quote','hello','judges','quote']))
print(test_recog(['print','fun','text']))
#print(test_recog(['print','print','text','lower','upper']))