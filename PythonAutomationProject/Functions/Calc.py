from PyQt5.QtGui import QTextCursor

class Calculator:

    def __init__(self, ui):
        self.ui = ui

        self.ui.NumButton1.clicked.connect(lambda: self.pressedNum("1"))
        self.ui.NumButton2.clicked.connect(lambda: self.pressedNum("2"))
        self.ui.NumButton3.clicked.connect(lambda: self.pressedNum("3"))
        self.ui.NumButton4.clicked.connect(lambda: self.pressedNum("4"))
        self.ui.NumButton5.clicked.connect(lambda: self.pressedNum("5"))
        self.ui.NumButton6.clicked.connect(lambda: self.pressedNum("6"))
        self.ui.NumButton7.clicked.connect(lambda: self.pressedNum("7"))
        self.ui.NumButton8.clicked.connect(lambda: self.pressedNum("8"))
        self.ui.NumButton9.clicked.connect(lambda: self.pressedNum("9"))
        self.ui.NumButton0.clicked.connect(lambda: self.pressedNum("0"))

        self.ui.OpButtonTimes.clicked.connect(lambda: self.pressedOp("*"))
        self.ui.OpButtonPlus.clicked.connect(lambda: self.pressedOp("+"))
        self.ui.OpButtonMinus.clicked.connect(lambda: self.pressedOp("-"))
        self.ui.OpButtonDivide.clicked.connect(lambda: self.pressedOp("/"))

        self.ui.LetButtonC.clicked.connect(self.Clear)
        self.ui.LetButtonEquals.clicked.connect(self.getSum)

        self.uniOp = ' '
        self.cursor = self.ui.SumOutPut.textCursor()
        self.firstNum = ' '
        self.secondNum = ' '
        self.symbol = ' '

    def pressedNum(self, number):
        self.cursor.movePosition(self.cursor.End)
        self.cursor.insertText(number)


    def pressedOp(self, operator): 
        self.uniOp = operator
        self.cursor.movePosition(self.cursor.End)
        self.cursor.insertText(operator)
        

    def Clear(self):
        self.ui.SumOutPut.setPlainText("")
        self.firstNum = ' '
        self.secondNum = ' '
        self.symbol = ' '
        self.uniOp = ' '



    def getSum(self):
        equation = self.ui.SumOutPut.toPlainText()
        if self.uniOp == ' ':
            self.ui.SumOutPut.setPlainText("Error No Operator") 
            return
        
        self.firstNum, self.symbol, self.secondNum = equation.partition(self.uniOp)

        if self.firstNum == "":
            self.firstNum = "0"
        elif self.secondNum == "":
            self.secondNum = "0"

        try:

            if (self.symbol == "+"):
                Sum = float(self.firstNum) + float(self.secondNum)

            elif (self.symbol == "*"):
                Sum = float(self.firstNum) * float(self.secondNum)

            elif (self.symbol == "/"):
                Sum = float(self.firstNum) / float(self.secondNum)

            elif (self.symbol == "-"):
                Sum = float(self.firstNum) - float(self.secondNum)

            self.ui.SumOutPut.setPlainText(str(Sum))
            self.firstNum = str(Sum) 
            self.uniOp = ' '

        except Exception as e:
            self.ui.SumOutPut.setPlainText(str(e))