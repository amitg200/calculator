from evaluator import Evaluator

def main():

    while(True):
        try:
            equation = input("Please enter an equation: ")
            if equation == "exit":
                break
            evaluator = Evaluator(equation)
            print(evaluator.evaluate())
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()