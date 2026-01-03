from input_processing import InputProcessing

def main():
    equation = input("Please enter an equation: ")
    input_processer = InputProcessing(equation)

    while input_processer.has_next():
        print(input_processer.get_next())

if __name__ == "__main__":
    main()