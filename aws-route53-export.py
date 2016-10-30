import os 
import json 
import sys
import csv

def getIDjson():
	command = os.system("aws route53 list-hosted-zones>liste.json")
	with open("liste.json") as data_file:
		list=json.load(data_file)	
	command = os.system("rm liste.json") 
	command = os.system("echo #infoAWS.csv>>infoAWS.csv")
	fname = "infoAWS.csv"
	fichier = open(fname,"wb")
	writer = csv.writer(fichier)
	writer.writerow(('Name','Id','Type','Ip'))
	
	for i in range (0,2000):
		try:
			id=list["HostedZones"][i]["Id"]
			idid = id[12:40]
			name=list["HostedZones"][i]["Name"]
			aws = "aws route53 list-resource-record-sets --hosted-zone-id "
			aws += idid
			aws += " >e.json"
			command = os.system(aws)
			with open ("e.json") as e:
				info = json.load(e)
			print "\n"
			print "\n"
			print "\n"
			print idid
			print "\n"
			for j in range (0,200):
				try:
					type=info["ResourceRecordSets"][j]["Type"]
					if (info["ResourceRecordSets"][j]["Type"]=="CNAME") or (info["ResourceRecordSets"][j]["Type"]=="A") :
						ip = info["ResourceRecordSets"][j]["ResourceRecords"][0]["Value"] 
						writer.writerow((name,idid,type,ip))
					else : 
						writer.writerow((name,idid,type,'false'))
				except:
					print "Type Finish"
					break
		except:
			print "Finish"
			break
	
	fichier.close()
def main():
	command = os.system("clear")
	
	getIDjson()
	
if __name__=='__main__':
	main()