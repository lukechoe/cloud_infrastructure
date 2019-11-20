import main as buckets
import dynamo as db
import json

b = buckets.b

#for obj in b.objects.all():
#    print(obj.key)
#db.putId('asdf', '1', 'sample speech to text')

#a = db.getIdByRp(1)

def postToCloud(file, id, rpId, lst, fileNameinS3):
    # file = .wav
    # id = unique ID from server
    # rpId = which rasberrypi {1,2,3,4} for now
    # txt = the speech to text
    print("Uploading to cloud")
    buckets.uploadFileToAws(file, fileNameinS3)
    db.putId(id,rpId,lst,file)
    return

def retrieveByRasberryPiId(id):
    lst = db.getIdByRp(id)
    return lst

def downloadFile(fileName):
    buckets.getAudioFileByKey(fileName)

# SAMPLE method use
#listOfQuestions = ["question1", "question2"]
#postToCloud('sample.wav', '125122', '123', listOfQuestions , "fileNameInS3.wav")

#res = retrieveByRasberryPiId('123')
#print(res[0][0]) --> audioId
#print(res[0][1]) --> type(list)
#print(res[0][1][0]) --> first question from array
#print(res[1][0]) --> next audioId .. and so on

#downloadFile("fileNameInS3.wav")
#or
#downloadFile("fileNameInS3.wav", "../../audios/randomfolder") to specify path for file download
