import csv
import sys

input_file = ("pre_config_data\\" + str(sys.argv[1]))
output_file = ("post_config_data\\" + str(sys.argv[1]))

post_fields = [
    'Matchstring',
    'Created',
    'Note',
    'User',
]

reader = csv.DictReader(open(input_file, "r"))
writer = csv.DictWriter(open(output_file, "w", newline=""), fieldnames=post_fields)

writer.writeheader()

for each in reader:
    # compile note info
    noteList = [
        each['Purpose'],
        each['OpenFlag'],
        each['PermitNumber'],
        each['Price'],
    ]

    # join together in readeable format
    seperator = "|"
    note = seperator.join(noteList)

    # create dictionary of post configuration
    post_config = {
        'Matchstring' : each['ParcelID'],
        'Created' : each['PERMDT'],
        'Note' : note,
        'User' : 'jrenwand@senecacountyohio.gov',
    }

    writer.writerow(post_config)
