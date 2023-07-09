datatypes = ['string', 'int', 'list']
functions = ["print", "len", "range", "map", "input", "type", "abs", "str", "int", "float", "bool", "max",
             "min", "sorted", "sum", "enumerate"]
methods = ["lower", "upper", "strip", "split", "replace", "join", "append", "remove", "count", "clear", "keys",
           "values", "index", "sort", "copy", "insert", "count", "isalpha", "isdigit"]
case_statements = ['if', 'elif', 'else', 'while', 'for']
keywords = ['in', 'return']
basic_changers = {'comma': ',', "greater": '>', 'less': '<', 'equal': '==',
                  'equals': '=', 'space': ' ', 'colon': ':', 'plus': '+', 'minus': '-', 'modulo': '%', 'times': '*',
                  'power': '**', 'dot': '.', 'open' : '(', 'close' : ')'}


# # spacer = ['return']
#
# # Formats a method (input: name method, output: name.method())
# def check_if_method(query, word):
#     if query.index(word) != len(query) - 1 and query[query.index(word) + 1] == 'dot':
#         print(query[query.index(word) + 1])
#         return word

# Formats a string (input: quote input quote, output: "input")
def createString(query, quoteLocation):
    string = ""
    for s in query[quoteLocation[0] + 1: quoteLocation[1]]:
        string += s + " "
    string = string[:len(string) - 1]
    return "\"" + string + "\""

# Formats a method (input: name method, output: name.method())
def createMethod(method, query):
    if "quote" in query:
        string = createString(query, [i for i, x in enumerate(query) if x == "quote"])
    else:
        string = ""
        string += query[query.index(method) - 1]
    return string + "." + query[len(query) - 1] + "()"

# Formats a function (input: function input, output: function(input))
def createFunction(function, query):
    result = function + "("

    if "quote" in query:
        string = createString(query, [i for i, x in enumerate(query) if x == "quote"])
    else:
        if query.index("close") - query.index("open") == 2:
            string = ""
            for s in query[query.index("open") + 1:query.index("close")]:
                string += s
        else:
            string = ""
            for i in range(query.index("open") + 1, query.index("close")):
                if i == query.index("close") - 1:
                    string += query[i]
                else:
                    string += query[i] + ", "
    result += string + ")"

    return result

def checkBasicChangers(word):
    if word in basic_changers:
        return " " + basic_changers[word] + " "

def createCaseStatements(keyword, query):
    string = ""
    for word in query:
        if word in basic_changers:
            string += checkBasicChangers(word)
    return keyword + string + ":"

def testRecog(query):
    endword = " stop "
    queryinput = query.lower().split(endword)

    # Parses query into individual words
    queries = []
    for q in queryinput:
        queries.append(q.split())

    written = ''
    index = 0

    for query in queries:
        quote = [i for i, x in enumerate(query) if x == "quote"]
        for entryIndex in range(len(query)):
            if query[entryIndex] in methods:
                written += createMethod(query[entryIndex], query)
            elif query[entryIndex] in functions:
                written += createFunction(query[entryIndex], query)
            elif query[entryIndex] in case_statements:
                written += query[entryIndex] + " "
            elif query[entryIndex] in basic_changers:
                written += checkBasicChangers(query[entryIndex])
            elif query[entryIndex].isdigit():
                written += query[entryIndex]
            elif query[entryIndex] in keywords:
                written += query[entryIndex] + " "
            elif query[entryIndex] == "def":
                string = ""
                string += createFunction(query[1], query[1:])
                written += "def " + string + ":"
                functions.append(query[entryIndex])
            elif entryIndex != 0 and query[entryIndex - 1] == "variable":
                written += query[entryIndex]
            elif query[entryIndex] == "quote":
                if len(quote) >= 2:
                    written += createString(query, quote)
                    quote = quote[2:]
            else:
                written += ""

        if query[0] in case_statements:
            written += ":"

    # checking through case statements
    # if query[0] in Case_statements:
    #     written += query[0] + ' '
    #     index += 1
        # for word in query:

        # written += " "
        # if word == 'equals':
        # written += "=="
        # else:
        # written += word
        # written += ":"
    # checking through functions
    # if query[index] in functions:
    #     funcount = 0
    #     string = False
        # deal with other functions later
        # written += query[index]
        # written += "("
        # if query[index] == 'string':
        #     written += "'"

            # print("going into function",query[index:len(query)])
        # for word in query[index + 1:len(query)]:
        #     if check_basic_changers(word, written):
        #         written = check_basic_changers(word, written)
        #
        #
        #     elif word in functions:
        #         funcount += 1
        #         written += (word + "(")
        #     else:
        #         written = written + word
            # else:
            # written += ","
            # if string:
            # written+= "'"
        # written += ")" + ")" * funcount
        # return written
    # other persons code -- not currently working
    # function definitions
    # if query[0] == 'def':
    #     functions.insert(0, query[1])
    #     written = 'def ' + query[1] + '('
    #     if len(query) > 2:
    #         for word in query[2:len(query)]:
    #             written += word + ','
    #     written = written[0:len(written) - 1] + '):'
    #     # print(written)
    #     # written += createMethod(query)
    # else:
    #     method = False
    #     for word in query[index:len(query)]:
    #         if check_basic_changers(word, written):
    #             written = check_basic_changers(word, written)
    #         elif word in methods:
    #             written += "." + word + "()"
    #         elif check_if_method(query, word):
    #             written += check_if_method(query, word)
    #         else:
    #
    #             written += word + ' '

    return written


# print(testRecog(['def', 'fun', 'message']))
# print(testRecog(['if', 'len', 'message', 'greater', '5']))
# print(testRecog(['message', 'equals', 'message', 'upper']))
# print(testRecog(['return', 'message']))
# print(testRecog(['text', 'equals', 'quote', 'hello', 'judges', 'quote']))

print(testRecog("def fun open message close"))
print(testRecog("if len open message close greater 5"))
print(testRecog("variable message equals message upper"))
print(testRecog("return variable message"))
print(testRecog("variable text equals quote hello judges quote"))
print(testRecog("print open fun open variable text close close"))