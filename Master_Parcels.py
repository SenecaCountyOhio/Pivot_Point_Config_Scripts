import csv
import sys

input_file = ("pre_config_data\\" + str(sys.argv[1]))
output_file = ("post_config_data\\" + str(sys.argv[1]))

post_fields = [
    'JUR',
    'ParcelID',
    'TaxYear',
    'Address',
    'TaxDistrict',
    'Owner',
    'Classification',
    'LandUseCode',
    'NeighbourhoodNumber',
]

reader = csv.DictReader(open(input_file, "r"))
writer = csv.DictWriter(open(output_file, "w", newline=""), fieldnames=post_fields)

writer.writeheader()

for each in reader:
    # compile address info
    address_list = [
        each['ADRNO'],
        each['ADRADD'],
        each['ADRDIR'],
        each['ADRSTR'],
        each['ADRSUF'],
        each['ADRSUF2']
    ]


    # remove any blank info
    for info in address_list:
        if info == "":
            address_list.remove(info)

    # join together in readeable format
    seperator = " "
    address = seperator.join(address_list)

    # create dictionary of post configuration
    post_config = {
        'JUR' : each['JUR'],
        'ParcelID' : each['PARID'],
        'TaxYear' : each['TAXYR'],
        'Address' : address,
        'TaxDistrict' : each['TAXDIST'],
        'Owner' : each['OWN1'],
        'Classification' : each['CLASS'],
        'LandUseCode' : each['LUC'],
        'NeighbourhoodNumber' : each['NBHD'],
    }

    writer.writerow(post_config)
