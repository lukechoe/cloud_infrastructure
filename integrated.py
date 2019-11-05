import main as buckets
import dynamo as db

b = buckets.b

#for obj in b.objects.all():
#    print(obj.key)
#db.putId('asdf', '1', 'sample speech to text')

#a = db.getIdByRp(1)

def postToCloud(file, id, rpId, txt):
    # file = .wav
    # id = unique ID from server
    # rpId = which rasberrypi {1,2,3,4} for now
    # txt = the speech to text
    print("Uploading to cloud")
    buckets.uploadFileToAws(file)
    db.putId(id,rpId,txt)
    return 

def retrieveByRasberryPiId(id):
    lst = db.getId(id)
    return lst
