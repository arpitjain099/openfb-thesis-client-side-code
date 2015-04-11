import csv
from pymongo import MongoClient
client = MongoClient()
db=client.thesisdb
from time import gmtime, strftime
collection=db.tasks
#print db
username="arpitjain099"

collection_rec=db.recruiter
#collection_rec.insert({"ada":"dada"})
#collection_rec.find_one({u'username':username})["count"]=11
#print collection_rec
count= collection_rec.find_one({"username":username})['count']

#print count
#print val
defaultquestions=["Is this image profane or not?","Is this comment profane or not?", "Categorize this image into 5 categories","Categorize this book","Give 5 tags to this article","Give 5 tags for this image"," Which of the variants look good to you?","Which of the variants matches the description?","Is this ad appealing to you?","Grade the sentiment expressed in this tweet","Grade the sentiment expressed in this user comment","From the product review, is the customer satisfied?", "Which image is better?", "Which design is more soothing?","How will you rank this MP3 file?","Help us rate this place"]
with open('tasksheet.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile)
	#spamreader=spamreader[17:]
	for index,row in enumerate(spamreader):
		if index > 20 and row[0]>'0' and row[0]<'17':
			
			count=count+1
			if row[0]=='1':
				question=defaultquestions[0]
				if row[2]!="":
					question=row[2]
				post={"question":question,"taskid":username+'_'+str(count),"username":username,"imgurl":row[1],"textcontent":"","mp3url":"","img1":"","img2":"","heading":"","summary":"","tasksymbol":1,"dateofadding":str(strftime("%d-%m-%Y %H:%M:%S", gmtime()))}
				#print "fa"
				collection.insert(post)
				#collection.find_one()
			elif row[0]=='2':
				question=defaultquestions[1]
				if row[2]!="":
					question=row[2]
				post={"question":question,"taskid":username+'_'+str(count),"username":username,"imgurl":"","textcontent":row[1],"mp3url":"","img1":"","img2":"","heading":"","summary":"","tasksymbol":2,"dateofadding":str(strftime("%d-%m-%Y %H:%M:%S", gmtime()))}
				#print "fa"
				collection.insert(post)
				#collection.find_one()
			elif row[0]=='3':
				question=defaultquestions[2]
				if row[2]!="":
					question=row[2]
				post={"question":question,"taskid":username+'_'+str(count),"username":username,"imgurl":row[1],"textcontent":"","mp3url":"","img1":"","img2":"","heading":"","summary":"","tasksymbol":3,"dateofadding":str(strftime("%d-%m-%Y %H:%M:%S", gmtime()))}
				#print "fa"
				collection.insert(post)
			elif row[0]=='4':
				question=defaultquestions[3]
				if row[3]!="":
					question=row[3]
				post={"question":question,"taskid":username+'_'+str(count),"username":username,"imgurl":"","textcontent":"","mp3url":"","img1":"","img2":"","heading":row[1],"summary":row[2],"tasksymbol":4,"dateofadding":str(strftime("%d-%m-%Y %H:%M:%S", gmtime()))}
				#print "fa"
				collection.insert(post)
			elif row[0]=='5':
				question=defaultquestions[3]
				if row[3]!="":
					question=row[3]
				post={"question":question,"taskid":username+'_'+str(count),"username":username,"imgurl":"","textcontent":"","mp3url":"","img1":"","img2":"","heading":row[1],"summary":row[2],"tasksymbol":5,"dateofadding":str(strftime("%d-%m-%Y %H:%M:%S", gmtime()))}
				#print "fa"
				collection.insert(post)
			elif row[0]=='6':
				question=defaultquestions[5]
				if row[2]!="":
					question=row[2]
				post={"question":question,"taskid":username+'_'+str(count),"username":username,"imgurl":row[1],"textcontent":"","mp3url":"","img1":"","img2":"","heading":"","summary":"","tasksymbol":6,"dateofadding":str(strftime("%d-%m-%Y %H:%M:%S", gmtime()))}
				#print "fa"
				collection.insert(post)

			elif row[0]=='7':
				question=defaultquestions[6]
				if row[3]!="":
					question=row[3]
				post={"question":question,"taskid":username+'_'+str(count),"username":username,"imgurl":"","textcontent":"","mp3url":"","img1":row[1],"img2":row[2],"heading":"","summary":"","tasksymbol":7,"dateofadding":str(strftime("%d-%m-%Y %H:%M:%S", gmtime()))}
				#print "fa"
				collection.insert(post)
			elif row[0]=='8':
				question=defaultquestions[7]
				if row[3]!="":
					question=row[3]
				post={"question":question,"taskid":username+'_'+str(count),"username":username,"imgurl":"","textcontent":"","mp3url":"","img1":row[2],"img2":row[3],"heading":"","summary":"","tasksymbol":8,"dateofadding":str(strftime("%d-%m-%Y %H:%M:%S", gmtime()))}
				#print "fa"
				collection.insert(post)
			elif row[0]=='9':
				question=defaultquestions[8]
				if row[2]!="":
					question=row[2]
				post={"question":question,"taskid":username+'_'+str(count),"username":username,"imgurl":row[1],"textcontent":"","mp3url":"","img1":"","img2":"","heading":"","summary":"","tasksymbol":9,"dateofadding":str(strftime("%d-%m-%Y %H:%M:%S", gmtime()))}
				#print "fa"
				collection.insert(post)
			elif row[0]=='10':
				question=defaultquestions[9]
				if row[2]!="":
					question=row[2]
				post={"question":question,"taskid":username+'_'+str(count),"username":username,"imgurl":"","textcontent":row[1],"mp3url":"","img1":"","img2":"","heading":"","summary":"","tasksymbol":10,"dateofadding":str(strftime("%d-%m-%Y %H:%M:%S", gmtime()))}
				#print "fa"
				collection.insert(post)
			elif row[0]=='11':
				question=defaultquestions[10]
				if row[2]!="":
					question=row[2]
				post={"question":question,"taskid":username+'_'+str(count),"username":username,"imgurl":"","textcontent":row[1],"mp3url":"","img1":"","img2":"","heading":"","summary":"","tasksymbol":11,"dateofadding":str(strftime("%d-%m-%Y %H:%M:%S", gmtime()))}
				#print "fa"
				collection.insert(post)

			elif row[0]=='12':
				question=defaultquestions[11]
				if row[2]!="":
					question=row[2]
				post={"question":question,"taskid":username+'_'+str(count),"username":username,"imgurl":"","textcontent":row[1],"mp3url":"","img1":"","img2":"","heading":"","summary":"","tasksymbol":12,"dateofadding":str(strftime("%d-%m-%Y %H:%M:%S", gmtime()))}
				#print "fa"
				collection.insert(post)
			elif row[0]=='13':
				question=defaultquestions[12]
				if row[3]!="":
					question=row[3]
				post={"question":question,"taskid":username+'_'+str(count),"username":username,"imgurl":"","textcontent":"","mp3url":"","img1":row[2],"img2":row[3],"heading":"","summary":"","tasksymbol":13,"dateofadding":str(strftime("%d-%m-%Y %H:%M:%S", gmtime()))}
				#print "fa"
				collection.insert(post)
			elif row[0]=='14':
				question=defaultquestions[13]
				if row[3]!="":
					question=row[3]
				post={"question":question,"taskid":username+'_'+str(count),"username":username,"imgurl":"","textcontent":"","mp3url":"","img1":row[2],"img2":row[3],"heading":"","summary":"","tasksymbol":14,"dateofadding":str(strftime("%d-%m-%Y %H:%M:%S", gmtime()))}
				#print "fa"
				collection.insert(post)
			elif row[0]=='15':
				question=defaultquestions[14]
				if row[2]!="":
					question=row[2]
				post={"question":question,"taskid":username+'_'+str(count),"username":username,"imgurl":"","textcontent":"","mp3url":row[1],"img1":"","":"","heading":"","summary":"","tasksymbol":15,"dateofadding":str(strftime("%d-%m-%Y %H:%M:%S", gmtime()))}
				#print "fa"
				collection.insert(post)
			post = collection_rec.find_one({"username":username})
			post["count"]=count
			collection_rec.save(post)