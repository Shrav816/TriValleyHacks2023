# Different Python categories
datatypes = ['string', 'int', 'list']
functions = ["print", "len", "range", "map", "input", "type", "abs", "str", "int", "float", "bool", "max",
             "min", "sorted", "sum", "enumerate"]
methods = ["lower", "upper", "strip", "split", "replace", "join", "append", "remove", "count", "clear", "keys",
           "values", "index", "sort", "copy", "insert", "count", "isalpha", "isdigit"]
case_statements = ['if', 'elif', 'else', 'while', 'for']
keywords = ['in', 'return']
basic_changers = {'comma': ',', "greater": '>', 'less': '<', 'equal': '==',
                  'equals': '=', 'space': ' ', 'colon': ':', 'plus': '+', 'minus': '-', 'modulo': '%', 'times': '*',
                  'power': '**', 'dot': '.'}

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

# Formats a nested function
def createNestedFunction(function, query):
    result = ""
    functionIndex = 0
    openIndices = []

    for i in range(len(query)):
        if query[i] == "open":
            openIndices.append(i)
            functionIndex += 1

    for i in openIndices:
        result += query[i - 1] + "("

    if "quote" in query:
        string = createString(query, [i for i, x in enumerate(query) if x == "quote"])
    else:
        closeIndex = query.index("close")
        query.reverse()
        openIndex = query.index("open")
        query.reverse()

        if closeIndex - openIndex == 2:
            string = ""
            for s in query[openIndex + 1:closeIndex]:
                string += s
        elif closeIndex - openIndex > 2:
            string = ""
            for i in range(openIndex + 1, closeIndex):
                if i == closeIndex - 1:
                    string += query[i]
                else:
                    string += query[i] + ", "

    result += string + (")" * functionIndex)

    return result

# Formats basic changers listed above
def checkBasicChangers(word):
    if word in basic_changers:
        return " " + basic_changers[word] + " "

# Formats case statements
def createCaseStatements(keyword, query):
    string = ""
    for word in query:
        if word in basic_changers:
            string += checkBasicChangers(word)
    return keyword + string + ":"

# Classifying and calculating all categories
def testRecog(query):
    endword = " stop "
    queryinput = query.lower().split(endword)

    # Parses query into individual words
    queries = []
    for q in queryinput:
        queries.append(q.split())

    written = ''

    for query in queries:
        quote = [i for i, x in enumerate(query) if x == "quote"]
        for entryIndex in range(len(query)):
            if query[entryIndex] in methods:
                written += createMethod(query[entryIndex], query)
            elif query[entryIndex] in functions:
                functionIndex = 0
                for i in range(len(query)):
                    if query[i] == "open":
                        functionIndex += 1
                if functionIndex == 1:
                    written += createFunction(query[entryIndex], query)
                else:
                    written += createNestedFunction(query[entryIndex], query)
            elif query[entryIndex] in case_statements:
                written += query[entryIndex] + " "
            elif query[entryIndex] in basic_changers:
                written += checkBasicChangers(query[entryIndex])
            elif query[entryIndex].isdigit() and query[entryIndex] not in written:
                written += query[entryIndex]
            elif query[entryIndex] in keywords:
                written += query[entryIndex] + " "
            elif query[entryIndex] == "def":
                written += "def " + createFunction(query[entryIndex + 1], query[entryIndex + 1:]) + ":"
            elif entryIndex != 0 and query[entryIndex - 1] == "variable":
                written += query[entryIndex]
            elif query[entryIndex] == "quote" and query[entryIndex - 1] == "variable":
                if len(quote) >= 2:
                    written += createString(query, quote)
                    quote = quote[2:]
            else:
                written += ""

        if query[0] in case_statements:
            written += ":"
        written += "\n"

    return written

# Test 1
print(testRecog("variable age equals input open quote what is your age quote close"))

# Test 2
print(testRecog("def fun open message close stop if len open message close greater 5 stop "
                "variable message equals message upper stop return variable message stop variable text equals quote hello "
                "judges quote stop print open fun open text close close"))
