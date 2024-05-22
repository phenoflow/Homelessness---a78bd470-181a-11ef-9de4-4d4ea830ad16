# Luchenski S, 2024.

import sys, csv, re

codes = [{"code":"G81689","system":"icd10"},{"code":"J82217","system":"icd10"},{"code":"L81661","system":"icd10"},{"code":"Y00049","system":"icd10"},{"code":"Y00182","system":"icd10"},{"code":"Y01057","system":"icd10"},{"code":"Y00256","system":"icd10"},{"code":"Y00054","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('homelessness-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["homelessness-healthcare---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["homelessness-healthcare---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["homelessness-healthcare---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
