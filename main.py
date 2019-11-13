import boto3

s3 = boto3.resource('s3')

def test():
    for bucket in s3.buckets.all():
        print(bucket.name)

b = s3.Bucket('firstbucketluke')
#b.upload_file("1.JPG", "file")

def uploadFileToAws(file):
    s3.Object('firstbucketluke', file).put(Body='body', Metadata={'typeOfAudio': 'filler'})

    
def getAudioFileByKey(key):
    s3.download_file('firstbucketluke', key, 'tmp.wav')

"""
for key in b.objects.all():
    k = key.load()
    print(key.e_tag)
    print(type(k))
"""

#for obj in b.objects.all():
 #   print(obj.key)
