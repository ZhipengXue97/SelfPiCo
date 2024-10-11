# Extracted from https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
def barcode_generator():
    serial_number = 10000  # Initial barcode
    while True:
        yield serial_number
        serial_number += 1


barcode = barcode_generator()
while True:
    number_of_lightbulbs_to_generate = int(input("How many lightbulbs to generate? "))
    barcodes = [next(barcode) for _ in range(number_of_lightbulbs_to_generate)]
    print(barcodes)

    # function_to_create_the_next_batch_of_lightbulbs(barcodes)

    produce_more = input("Produce more? [Y/n]: ")
    if produce_more == "n":
        break

for barcode in barcode_generator():
    print(barcode)

