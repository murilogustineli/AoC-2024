sample_instructions = "mul(48,648)mul(637,618):#?^ {/*?<mul(506,718)&:why()@]mul(910,151)who(){*@{where()#mul(624,757)>why()+mul(739,690)mul(74,266)who()%][]*}who()mul(662,558)select()>>! ?!^/"


def load_data(file_path: str) -> str:
    with open(file_path, "r") as file:
        content = file.read()
    return content


def find_multiplications(instructions: str) -> list:
    import re

    # search for mul() in the sample_instructions
    multiplications = re.findall(r"mul\((\d+),(\d+)\)", instructions)
    return multiplications


def multiply_and_sum(multiplications: list) -> int:
    # multiply the two numbers in each tuple
    result = [int(x) * int(y) for x, y in multiplications]
    # sum the results
    result = sum(result)
    return result


if __name__ == "__main__":
    import re

    # load data
    instructions = load_data("data_03.txt")
    # search for mul() in the sample_instructions
    multiplications = find_multiplications(instructions)
    # multiply the two numbers in each tuple and sum the results
    result = multiply_and_sum(multiplications)
    print(multiplications[:10])
    print(f"result: {result}")
