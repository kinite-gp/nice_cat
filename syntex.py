import book

syntax = {
    "python" : {
        "key" : 
            [
            "continue",
            "import",
            "from",
            "print",
            "while",
            "break",
            "exit",
            "elif ",
            "else ",
            "for ",
            "in ",
            "if ",
            ],
        "char" : 
            [
                "{",
                "}",
                "[",
                "]",
                "=",
                ":",
                ".",
                ",",
                "+",
                "*",
                "/",
                "^",
                "%",
                ")",
                "("
                
            ]
    }
}






def py(text):
    global cot
    two_cot = False
    one_cot = False
    new_text = ""

    for c in syntax["python"]["char"] :
        text = text.replace(c,f"{book.color['lblue']}{c}{book.color['reset']}")

    for k in syntax["python"]["key"] :
        text = text.replace(k,f"{book.color['green']}{k}{book.color['reset']}")
        
    

    for char in text:
        if char == '"':
            if not two_cot and not one_cot:
                new_text = new_text + f"{book.color['green']}{char}"
                two_cot = True
            elif two_cot:
                new_text = new_text + f"{char}{book.color['reset']}"
                two_cot = False
        elif char == "'":
            if not one_cot and not two_cot:
                new_text = new_text + f"{book.color['green']}{char}"
                one_cot = True
            elif one_cot:
                new_text = new_text + f"{char}{book.color['reset']}"
                one_cot = False
        else:
            new_text = new_text + char

    text = new_text.split("\n")[:-1]



    return text

