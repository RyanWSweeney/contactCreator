import csv

def create_vcard(name, office, practice, phone, email, company):
    vcard = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        f"N:{name}",
        f"FN:{name}",
        f"ORG:{company} Intern {office}",
        f"TEL;TYPE=WORK,VOICE:{phone}",
        f"EMAIL;TYPE=PREF,INTERNET:{email}"
    ]

    # Add notes based on practice
    if practice == 'MC':
        vcard.append("NOTE:Management Consultant")
    elif practice == 'TS':
        vcard.append("NOTE:Tech Consultant")

    vcard.append("END:VCARD")
    return '\n'.join(vcard)

# Read CSV and create vCard for each contact
vcards = []
with open('contactsInfo.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        vcards.append(create_vcard(row['Name'], row['Office'], row['Practice'], row['Phone Number'], row['Email Address'], "Company Name"))

# Save all vCards to a file
with open('contacts.vcf', 'w', encoding='utf-8') as vcf_file:
    vcf_file.write('\n'.join(vcards))

print("vCard file created successfully.")
