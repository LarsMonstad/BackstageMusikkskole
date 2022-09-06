import csv
import sys

#CREATED BY LARS Monstad for Backstage Musikkskole / Ancha AS 

# SETTINGS: 
#Converting CSV to  VCF (Electronic Business Cards) for phone. Great tool for importing all customers into Phone. 
#Just change Row number to match your csv data. 
#Firstname: row[0]
#Fullname: row[7], remember to remove the stripname function. 
#Email: row[2]
#Cell: row[3]
#pronouns: row[8]

# How to use 
#convertvcf.py csv

def stripname(x):
    x = x.split(' ', 1)[0]
    return x

def stripchar(x):
    x = x[0]
    return x

def convert(file):
    with open( file, 'r' ) as source:
        reader = csv.reader( source )
        next(reader, None)
        allvcf = open('ALL.vcf', 'w')
        i = 0
        for row in reader:
            if not row[0]:
                next(reader, None)
            elif stripchar(row[0]) == "#":
                next(reader, None)
            else:
                #Create individual contact files 
                vcf = open(stripname(row[7]) + ' ' + row[0] + ' ' + row[8] + ".vcf", 'w')
                vcf.write( 'BEGIN:VCARD' + "\n")
                vcf.write( 'VERSION:3.0' + "\n")
                vcf.write( 'N:' + row[0] + ';' + stripname(row[7]) + ';' + row[8] + "\n")
                vcf.write( 'FN:' + stripname(row[7]) + ' ' + row[0] + ' ' + row[8] + "\n")
                vcf.write( 'ORG:' + 'ATI' + "\n")
                vcf.write( 'TEL;CELL:' + row[3] + "\n")
                vcf.write( 'EMAIL:' + row[2] + "\n")
                vcf.write( 'END:VCARD' + "\n")
                vcf.write( "\n")
                vcf.close()

                #create the contact file for ALL contacts 
                allvcf.write( 'BEGIN:VCARD' + "\n")
                allvcf.write( 'VERSION:3.0' + "\n")
                allvcf.write( 'N:' + row[0] + ';' + stripname(row[7]) + ';' + row[8] + "\n")
                allvcf.write( 'FN:' + stripname(row[7]) + ' ' + row[0] + ' ' + row[8] + "\n")
                allvcf.write( 'ORG:' + 'ATI' + "\n")
                allvcf.write( 'TEL;CELL:' + row[3] + "\n")
                allvcf.write( 'EMAIL:' + row[2] + "\n")
                allvcf.write( 'END:VCARD' + "\n")
                allvcf.write( "\n")

            i += 1#counts

        allvcf.close()
        print (str(i) + " vcf contacts created")

def main(args):
    if len(args) != 2:
        print ( "Error Usage:")
        print ( args[0] + " filename")
        return
    convert(args[1])

if __name__ == '__main__':
    main(sys.argv)
