import tkinter
from tkinter import *

import re

Tokens = []


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.middle = None
        self.data = data
        self.count = 0

    def insertLeft(self, data):
        self.left = Node(data)
        self.left.count = self.count + 1
        return self.left

    def insertMiddle(self, data):
        self.middle = Node(data)
        self.middle.count = self.count + 1
        return self.middle

    def insertRight(self, data):
        self.right = Node(data)
        self.right.count = self.count + 1
        return self.right


def PrintTree(node):
    if node == None:
        return 0
    print(node.data)
    count1 = PrintTree(node.left)
    count2 = PrintTree(node.middle)
    count3 = PrintTree(node.right)
    if node.count > count1:
        count1 = node.count
    if count2 > count1:
        count1 = count2
    if count3 > count1:
        count1 = count3
    return count1


class MyFirstGUI:  # class definition

    # This is the initialize function for a class.
    # Variables belonging to this class will get created and initialized in this function
    # What is the self parameter? It represents this class itself.
    # By using self.functionname, you can call functions belonging to this class.
    # By using self.variablename, you can create and use variables belonging to this class.
    # It needs to be the first parameter of all the functions in your class
    def __init__(self, root):
        # Master is the default prarent object of all widgets.
        # You can think of it as the window that pops up when you run the GUI code.
        self.master = root
        root.geometry("1300x1000")
        self.master.title("Lexical Analysis for TinyPIe")
        self.latestParse = None
        # grid function puts a widget at a certain location
        # return value is none, please do not use it like self.label=Label().grad()
        # it will make self.label=none and you will no longer be able to change the label's content
        # self.label = Label(self.master, text="Cat Name: ")
        # self.label.grid(row=0,column=0,sticky=E)

        self.label = Label(self.master, text="Source Code Input: ")
        self.label.place(x=150, y=40)

        self.label = Label(self.master, text="Lexical Analyzed Result: ")
        self.label.place(x=650, y=40)

        self.label = Label(self.master, text="Parser Result: ")
        self.label.place(x=1075, y=40)

        self.label = Label(self.master, text="Current Processing Line:  ")
        self.label.place(x=150, y=530)

        self.leftEntry = Text(root, height=28, width=53, bg="light blue")
        self.leftEntry.place(x=5, y=80)

        self.nextline = Button(self.master, text="Next Line", command=self.nextline)
        self.nextline.place(x=300, y=560)

        self.quitbutton = Button(self.master, text="Quit", command=self.quit)
        self.quitbutton.place(x=250, y=560)

        self.displayTree = Button(self.master, text="Display Tree", command=self.callVisualizer)
        self.displayTree.place(x=300, y=600)

        self.rightEntry = Text(root, height=28, width=52, bg="white")
        self.rightEntry.place(x=475, y=80)

        self.iteration = Text(root, height=1, width=7, bg="light green")
        self.iteration.place(x=300, y=530)
        self.iteration.insert(tkinter.END, str(0))

        self.parserEntry = Text(root, height=28, width=52, bg="white")
        self.parserEntry.place(x=925, y=80)

        self.treeOutput = Canvas(root, height=260, width=870, bg="white")
        self.treeOutput.place(x=475, y=525)

    def visualizeTree(self, root):
        if root is None:
            text = self.treeOutput.create_text(175, 10, text="None", fill="black", font="Arial 8")
            bbox = self.treeOutput.bbox(text)
            self.treeOutput.create_rectangle(bbox, outline="blue")
            return
        amountOfLevels = PrintTree(root) + 1
        spacing = 250 / amountOfLevels

        text = self.treeOutput.create_text(175, 10, text=str(root.data), fill="black", font="Arial 8")
        bbox = self.treeOutput.bbox(text)
        self.treeOutput.create_rectangle(bbox, outline="blue")

        my_gui.visual(75, 10, spacing, root.left, 175, 10)
        my_gui.visual(175, 10, spacing, root.middle, 175, 10)
        my_gui.visual(275, 10, spacing, root.right, 175, 10)

    def visual(self, width, height, distance, subroot, parentX, parentY):
        if subroot is None:
            return
        height += distance
        text = self.treeOutput.create_text(width, height, text=str(subroot.data), fill="black", font="Arial 8")
        bbox = self.treeOutput.bbox(text)
        self.treeOutput.create_rectangle(bbox, outline="blue")
        self.treeOutput.create_line(parentX, parentY+5, width, height-5, fill="red")
        setLeft = width-50
        setRight = width+50
        my_gui.visual(setLeft, height, distance, subroot.left, width, height)
        my_gui.visual(width, height, distance, subroot.middle, width, height)
        if subroot.right is not None and subroot.right.data == 'math':
            setRight += 50
        my_gui.visual(setRight, height, distance, subroot.right, width, height)

    def callVisualizer(self):
        self.treeOutput.delete('all')
        self.visualizeTree(self.latestParse)

    def ifExp(self):
        if not Tokens:
            return
        self.parserEntry.insert(tkinter.END, "\n----parent node ifExp, finding children nodes:")
        self.parserEntry.insert(tkinter.END, "\n")
        self.latestParse = Node('ifExp')
        tupleTEMP = Tokens.pop(0)
        tokenStr = re.sub(r'[<]', '', tupleTEMP, count=1)
        tokenStr = re.sub(r'[>]', '', tokenStr, count=1)
        tokenStr = tokenStr.replace(" ", "")
        tokenStr = tokenStr.split(",")
        TempVar = tokenStr[1]
        TokenList = (tokenStr[0], tokenStr[1])
        tupleTEMP = Tokens.pop(0)
        tokenStr = re.sub(r'[<]', '', tupleTEMP, count=1)
        tokenStr = re.sub(r'[>]', '', tokenStr, count=1)
        tokenStr = tokenStr.replace(" ", "")
        tokenStr = tokenStr.split(",")
        TokenList = (tokenStr[0], tokenStr[1])
        tupleTEMP = Tokens.pop(0)
        tokenStr = re.sub(r'[<]', '', tupleTEMP, count=1)
        tokenStr = re.sub(r'[>]', '', tokenStr, count=1)
        tokenStr = tokenStr.replace(" ", "")
        tokenStr = tokenStr.split(",")
        TempVar2 = tokenStr[1]
        TokenList = (tokenStr[0], tokenStr[1])
        tupleTEMP = Tokens.pop(0)
        tokenStr = re.sub(r'[<]', '', tupleTEMP, count=1)
        tokenStr = re.sub(r'[>]', '', tokenStr, count=1)
        tokenStr = tokenStr.replace(" ", "")
        tokenStr = tokenStr.split(",")
        TokenList = (tokenStr[0], tokenStr[1])
        tupleTEMP = Tokens.pop(0)
        tokenStr = re.sub(r'[<]', '', tupleTEMP, count=1)
        tokenStr = re.sub(r'[>]', '', tokenStr, count=1)
        tokenStr = tokenStr.replace(" ", "")
        tokenStr = tokenStr.split(",")
        TokenList = (tokenStr[0], tokenStr[1])
        self.parserEntry.insert(tkinter.END, "child node (internal): if ( comparison_exp ) :\n   "
                                             "if ( comparison_exp ) : has child node (token):\n\t" +
                                TempVar + ">" + TempVar2)
        self.parserEntry.insert(tkinter.END, "\n")
        tempRoot = self.latestParse.insertMiddle('if ( comparison_exp ) :')
        tempRoot.insertMiddle(str(TempVar) + ">" + str(TempVar2))
        return

    def printExp(self):
        if not Tokens:
            return
        self.parserEntry.insert(tkinter.END, "\n----parent node printExp, finding children nodes:")
        self.parserEntry.insert(tkinter.END, "\n")
        self.latestParse = Node('printExp')

        tupleTEMP = Tokens.pop(0)
        tokenStr = re.sub(r'[<]', '', tupleTEMP, count=1)
        tokenStr = re.sub(r'[>]', '', tokenStr, count=1)
        tokenStr = tokenStr.replace(" ", "")
        tokenStr = tokenStr.split(",")
        TokenList = (tokenStr[0], tokenStr[1])
        printExpression = TokenList[1]
        tupleTEMP = Tokens.pop(0)
        tokenStr = re.sub(r'[<]', '', tupleTEMP, count=1)
        tokenStr = re.sub(r'[>]', '', tokenStr, count=1)
        tokenStr = tokenStr.replace(" ", "")
        tokenStr = tokenStr.split(",")
        TokenList = (tokenStr[0], tokenStr[1])

        self.parserEntry.insert(tkinter.END, "child node (internal): print (exp) :\n   "
                                             "print (exp) : has child node (exp):\n\t" +
                                printExpression)
        self.parserEntry.insert(tkinter.END, "\n")
        tempPrintRoot = self.latestParse.insertMiddle('print')
        anotherTempPrintRoot = tempPrintRoot.insertMiddle('(exp)')
        anotherTempPrintRoot.insertMiddle(printExpression)
        return

    def exp(self, TokenList):
        self.parserEntry.insert(tkinter.END, "\n----parent node floatexp, finding children nodes:")
        self.parserEntry.insert(tkinter.END, "\n")
        self.latestParse = Node('floatExp')

        # print(Tokens)
        # print("\n----parent node exp, finding children nodes:")
        typeT, token = TokenList
        if (typeT == "id"):
            self.parserEntry.insert(tkinter.END, "child node (internal): identifier\n   "
                                                 "identifier has child node (token):" + token +
                                    "\n    accept token from the list:" + TokenList[1])
            identifierParent = self.latestParse.insertLeft('identifier')
            identifierParent.insertMiddle(str(token))
            self.parserEntry.insert(tkinter.END, "\n")
            # print("child node (internal): identifier")
            # print("   identifier has child node (token):" + token)
            # print("     accept token from the list:" + TokenList[1])
            if not Tokens:
                return
            tupleTEMP = Tokens.pop(0)
            tokenStr = re.sub(r'[<]', '', tupleTEMP, count=1)
            tokenStr = re.sub(r'[>]', '', tokenStr, count=1)
            tokenStr = tokenStr.replace(" ", "")
            tokenStr = tokenStr.split(",")
            TokenList = (tokenStr[0], tokenStr[1])
        else:
            print("expect identifier as the first element of the expression!\n")
            return
        if TokenList[1] == "=":
            self.parserEntry.insert(tkinter.END, "child node (token):" + TokenList[1]
                                    + "\n     accept token from the list:" + TokenList[1])
            self.parserEntry.insert(tkinter.END, "\n")
            seperatorNode = self.latestParse.insertMiddle('seperator')
            seperatorNode.insertMiddle(TokenList[1])
            # print("child node (token):" + TokenList[1])
            # print("     accept token from the list:" + TokenList[1])
            tupleTemp = Tokens.pop(0)
            tokenStr = re.sub(r'[<]', '', tupleTemp, count=1)
            tokenStr = re.sub(r'[>]', '', tokenStr, count=1)
            tokenStr = tokenStr.replace(" ", "")
            tokenStr = tokenStr.split(",")
            TokenList = (tokenStr[0], tokenStr[1])
        else:
            print("expect = as the second element of the expression!")
            return
        self.parserEntry.insert(tkinter.END, "Child node (internal): math")
        self.parserEntry.insert(tkinter.END, "\n")
        # print("Child node (internal): math")
        self.math(TokenList, self.latestParse)


    def math(self, TokenList, chosenRoot):
        self.parserEntry.insert(tkinter.END, "\n----parent node math, finding children nodes:")
        self.parserEntry.insert(tkinter.END, "\n")
        mathRoot = chosenRoot.insertRight('math')
        # print("\n----parent node math, finding children nodes:")
        # print(TokenList)
        if (TokenList[0] == "float"):
            self.parserEntry.insert(tkinter.END, "child node (internal): float\n"
                                    + "   float has child node (token):" + TokenList[1])
            self.parserEntry.insert(tkinter.END, "\n")
            if Tokens:
                floatRoot2 = mathRoot.insertLeft('float')
                floatRoot2.insertMiddle(TokenList[1])
            else:
                floatRoot2 = mathRoot.insertMiddle('float')
                floatRoot2.insertMiddle(TokenList[1])

            # print("child node (internal): float")
            # print("   float has child node (token):" + TokenList[1])
            if not Tokens:
                return
            tupleTT = Tokens.pop(0)
            tokenStr = re.sub(r'[<]', '', tupleTT, count=1)
            tokenStr = re.sub(r'[>]', '', tokenStr, count=1)
            tokenStr = tokenStr.replace(" ", "")
            tokenStr = tokenStr.split(",")
            TokenList = (tokenStr[0], tokenStr[1])
            if (TokenList[1] == "+"):
                self.parserEntry.insert(tkinter.END, "child node (token):" + TokenList[1])
                self.parserEntry.insert(tkinter.END, "\n")
                operatorRoot = mathRoot.insertMiddle('operator')
                operatorRoot.insertMiddle(TokenList[1])
                # print("child node (token):" + TokenList[1])
                tupleTT = Tokens.pop(0)
                tokenStr = re.sub(r'[<]', '', tupleTT, count=1)
                tokenStr = re.sub(r'[>]', '', tokenStr, count=1)
                tokenStr = tokenStr.replace(" ", "")
                tokenStr = tokenStr.split(",")
                TokenList = (tokenStr[0], tokenStr[1])

                self.parserEntry.insert(tkinter.END, "child node (internal): math")
                self.parserEntry.insert(tkinter.END, "\n")
                # print("child node (internal): math")
                self.math(TokenList, mathRoot)
            elif TokenList[1] == "*":
                self.parserEntry.insert(tkinter.END, "child node (token): " + TokenList[1])
                self.parserEntry.insert(tkinter.END, "\n")
                operatorRoot = mathRoot.insertMiddle('operator')
                operatorRoot.insertMiddle(TokenList[1])
                # print("child node (token): " + TokenList[1])
                tupleTT = Tokens.pop(0)
                tokenStr = re.sub(r'[<]', '', tupleTT, count=1)
                tokenStr = re.sub(r'[>]', '', tokenStr, count=1)
                tokenStr = tokenStr.replace(" ", "")
                tokenStr = tokenStr.split(",")
                TokenList = (tokenStr[0], tokenStr[1])

                self.parserEntry.insert(tkinter.END, "child node (internal: math")
                self.parserEntry.insert(tkinter.END, "\n")
                # print("child node (internal: math")
                self.math(TokenList, mathRoot)
        elif (TokenList[0] == "int"):
            self.parserEntry.insert(tkinter.END, "child node (internal): int"
                                    + "\n   int has child node (token):" + TokenList[1])
            self.parserEntry.insert(tkinter.END, "\n")
            floatRoot2 = mathRoot.insertLeft('int')
            floatRoot2.insertMiddle(TokenList[1])
            # print("child node (internal): int")
            # print("   int has child node (token):" + TokenList[1])
            if not Tokens:
                return
            tupleTT = Tokens.pop(0)
            tokenStr = re.sub(r'[<]', '', tupleTT, count=1)
            tokenStr = re.sub(r'[>]', '', tokenStr, count=1)
            tokenStr = tokenStr.replace(" ", "")
            tokenStr = tokenStr.split(",")
            TokenList = (tokenStr[0], tokenStr[1])
            # print(TokenList)

            if (TokenList[1] == "+"):
                self.parserEntry.insert(tkinter.END, "child node (token):" + TokenList[1])
                self.parserEntry.insert(tkinter.END, "\n")
                operatorRoot = mathRoot.insertMiddle('operator')
                operatorRoot.insertMiddle(TokenList[1])
                # print("child node (token):" + TokenList[1])
                tupleTT = Tokens.pop(0)
                tokenStr = re.sub(r'[<]', '', tupleTT, count=1)
                tokenStr = re.sub(r'[>]', '', tokenStr, count=1)
                tokenStr = tokenStr.replace(" ", "")
                tokenStr = tokenStr.split(",")
                TokenList = (tokenStr[0], tokenStr[1])

                self.parserEntry.insert(tkinter.END, "child node (internal): math")
                self.parserEntry.insert(tkinter.END, "\n")
                # print("child node (internal): math")
                self.math(TokenList, mathRoot)
            elif TokenList[1] == "*":
                self.parserEntry.insert(tkinter.END, "child node (token): " + TokenList[1])
                self.parserEntry.insert(tkinter.END, "\n")
                operatorRoot = mathRoot.insertMiddle('operator')
                operatorRoot.insertMiddle(TokenList[1])
                # print("child node (token): " + TokenList[1])
                tupleTT = Tokens.pop(0)
                tokenStr = re.sub(r'[<]', '', tupleTT, count=1)
                tokenStr = re.sub(r'[>]', '', tokenStr, count=1)
                tokenStr = tokenStr.replace(" ", "")
                tokenStr = tokenStr.split(",")
                TokenList = (tokenStr[0], tokenStr[1])

                self.parserEntry.insert(tkinter.END, "child node (internal: math")
                self.parserEntry.insert(tkinter.END, "\n")
                # print("child node (internal: math")
                self.math(TokenList, mathRoot)
            else:
                print("error, you need + after the int in the math")

        else:
            print("error, math expects float or int")

    def nextline(self):
        global Tokens
        numnber = int(self.iteration.get(1.0, "end-1c"))
        numnber = numnber + 1
        self.iteration.delete(1.0, "end")
        self.iteration.insert(tkinter.END, str(numnber))

        tokenStr = self.leftEntry.get(float(numnber), float(numnber + 1))
        if re.match(r'if\s+', tokenStr) is not None:
            tokenStr = re.sub(r'if', '', tokenStr)
            Tokens.append('<key,if>')
            p = re.match(r'\s*[(]', tokenStr)
            if p is not None:
                tokenStr = re.sub(r'\s*[(]', '', tokenStr, count=1)
                Tokens.append('<sep, ' + p.group() + '>')
            p = re.match(r'\s*\d*\.\d+', tokenStr)
            if p is not None:
                tokenStr = re.sub(r'\s*\d*\.\d+', '', tokenStr, count=1)
                Tokens.append('<lit, ' + p.group() + '>')
            p = re.match(r'\s*\d+', tokenStr)
            if p is not None:
                tokenStr = re.sub(r'\s*\d+', '', tokenStr, count=1)
                Tokens.append('<lit, ' + p.group() + '>')
            p = re.match(r'\s*\w+', tokenStr)
            if p is not None:
                tokenStr = re.sub(r'\s*\w+', '', tokenStr, count=1)
                Tokens.append('<id, ' + p.group() + ">")
            p = re.match(r'\s*[>]|\s*=|\s*[+]|\s*[*]|\s*[<]', tokenStr)
            if p is not None:
                tokenStr = re.sub(r'\s*[>]|\s*=|\s*[+]|\s*[*]', '', tokenStr, count=1)
                Tokens.append('<op, ' + p.group() + '>')
            p = re.match(r'\s*\d*\.\d+', tokenStr)
            if p is not None:
                tokenStr = re.sub(r'\s*\d*\.\d+', '', tokenStr, count=1)
                Tokens.append('<lit, ' + p.group() + '>')
            p = re.match(r'\s*\d+', tokenStr)
            if p is not None:
                tokenStr = re.sub(r'\s*\d+', '', tokenStr, count=1)
                Tokens.append('<lit, ' + p.group() + '>')
            p = re.match(r'\s*\w+', tokenStr)
            if p is not None:
                tokenStr = re.sub(r'\s*\w+', '', tokenStr, count=1)
                Tokens.append('<id, ' + p.group() + ">")
            p = re.match(r'\s*[)]', tokenStr)
            if p is not None:
                tokenStr = re.sub(r'\s*[)]', '', tokenStr, count=1)
                Tokens.append('<sep, ' + p.group() + '>')
            p = re.match(r'\s*[:]', tokenStr)
            if p is not None:
                tokenStr = re.sub(r'\s*[:]', '', tokenStr, count=1)
                Tokens.append('<sep, ' + p.group() + '>')
            for i in Tokens:
                self.rightEntry.insert(tkinter.END, i)
                self.rightEntry.insert(tkinter.END, "\n")
            parser('if')

        elif re.match(r'else', tokenStr) is not None:
            tokenStr = re.sub(r'else', '', tokenStr, count=1)
            Tokens.append('<key,else>')
            if re.match(r'\s*[:]', tokenStr) is not None:
                tokenStr = re.sub(r'\s*[:]', '', tokenStr, count=1)
                Tokens.append('<sep,:>')

        elif re.match(r'int\s', tokenStr) is not None:
            tokenStr = re.sub(r'int\s+', '', tokenStr, count=1)
            Tokens.append('<key,int>')
            p = re.match(r'\s*\w+', tokenStr)
            if p is not None:
                tokenStr = re.sub(r'\s*\w+', '', tokenStr, count=1)
                Tokens.append('<id, ' + p.group() + '>')
            p = re.match(r'\s*[=]', tokenStr)
            if p is not None:
                tokenStr = re.sub(r'\s*[=]', '', tokenStr, count=1)
                Tokens.append('<op, ' + p.group() + '>')
                while tokenStr != "" and tokenStr != "\n" and tokenStr != ";" and tokenStr != ";\n":
                    p = re.match(r'\s*\d+', tokenStr)
                    if p is not None:
                        tokenStr = re.sub(r'\s*\d+', '', tokenStr, count=1)
                        Tokens.append('<int, ' + p.group() + '>')
                    p = re.match(r'\s*\w+', tokenStr)
                    if p is not None:
                        tokenStr = re.sub(r'\s*\w+', '', tokenStr, count=1)
                        Tokens.append('<id, ' + p.group() + '>')
                    p = re.match(r'\s*[+]|\s*[*]', tokenStr)
                    if p is not None:
                        tokenStr = re.sub(r'\s*[+]|\s*[.*]', '', tokenStr, count=1)
                        Tokens.append('<op, ' + p.group() + '>')


        elif re.match(r'float\s+', tokenStr) is not None:
            tokenStr = re.sub(r'float\s+', '', tokenStr, count=1)
            Tokens.append('<key,float>')
            p = re.match(r'\s*\w+', tokenStr)
            if p is not None:
                tokenStr = re.sub(r'\s*\w+', '', tokenStr, count=1)
                Tokens.append('<id, ' + p.group() + '>')
            p = re.match(r'\s*[=]', tokenStr)
            if p is not None:
                tokenStr = re.sub(r'\s*[=]', '', tokenStr, count=1)
                Tokens.append('<op, ' + p.group() + '>')
                while tokenStr != "" and tokenStr != "\n" and tokenStr != ";" and tokenStr != ";\n":

                    p = re.match(r'\s*\d*\.\d+', tokenStr)
                    if p is not None:
                        tokenStr = re.sub(r'\s*\d*\.\d+', '', tokenStr, count=1)
                        Tokens.append('<float, ' + p.group() + '>')
                    p = re.match(r'\s*\d+', tokenStr)
                    if p is not None:
                        tokenStr = re.sub(r'\s*\d+', '', tokenStr, count=1)
                        Tokens.append('<int, ' + p.group() + '>')
                    p = re.match(r'\s*\w+', tokenStr)
                    if p is not None:
                        tokenStr = re.sub(r'\s*\w+', '', tokenStr, count=1)
                        Tokens.append('<id, ' + p.group() + '>')
                    p = re.match(r'\s*[+]|\s*[*]', tokenStr)
                    if p is not None:
                        tokenStr = re.sub(r'\s*[+]|\s*[.*]', '', tokenStr, count=1)
                        Tokens.append('<op, ' + p.group() + '>')
            for i in Tokens:
                self.rightEntry.insert(tkinter.END, i)
                self.rightEntry.insert(tkinter.END, "\n")
            parser('float')

        elif re.match(r'\s+print', tokenStr) is not None:
            tokenStr = re.sub(r'\s+print', '', tokenStr, count=1)
            Tokens.append('<key,print>')
            p = re.match(r'[(]', tokenStr)
            if p is not None:
                tokenStr = re.sub(r'[(]', "", tokenStr, count=1)
                Tokens.append('<sep,' + p.group() + '>')
            p = re.split("\"", tokenStr)
            if p is not None:
                Tokens.append('<lit,' + p[1] + ">")
                tokenStr.replace("\"", "")
            p = re.findall(r'[)]', tokenStr)
            if p is not None:
                tokenStr = re.sub(r'[)]', "", tokenStr, count=1)
                Tokens.append('<sep,' + ')>')
            for i in Tokens:
                self.rightEntry.insert(tkinter.END, i)
                self.rightEntry.insert(tkinter.END, "\n")
            parser('print')

    def quit(self):
        quit()


def parser(type):
    if not Tokens:
        return
    tuple = Tokens.pop(0)
    tokenStr = re.sub(r'[<]', '', tuple, count=1)
    tokenStr = re.sub(r'[>]', '', tokenStr, count=1)
    tokenStr = tokenStr.split(",")
    ParserList = (tokenStr[0], tokenStr[1])
    tuple = Tokens.pop(0)
    tokenStr = re.sub(r'[<]', '', tuple, count=1)
    tokenStr = re.sub(r'[>]', '', tokenStr, count=1)
    tokenStr = tokenStr.split(",")
    ParserList = (tokenStr[0], tokenStr[1])
    if type == 'float':
        my_gui.exp(ParserList)
    elif type == 'if':
        my_gui.ifExp()
    else:
        my_gui.printExp()
    return


if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = MyFirstGUI(myTkRoot)
    myTkRoot.mainloop()
