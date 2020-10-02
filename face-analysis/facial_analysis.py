import boto3
import json
import os


client = boto3.client('rekognition', aws_session_token=os.getenv('aws_session_token'),
                      aws_access_key_id=os.getenv('aws_access_key_id'),
                      aws_secret_access_key=os.getenv('aws_secret_access_key'))
# client = boto3.client('rekognition')

file = open('image.jpg', 'rb').read()

response = client.detect_faces(
    Image={
        'Bytes': file
    },
    Attributes=['ALL']
)

# print(response['FaceDetails'])
for face in response['FaceDetails']:
    print(json.dumps(face,indent=4,sort_keys=True))


for face in response['FaceDetails']:
    print("Age range of candidate: " + str(face['AgeRange']['Low']) + ' and ' + str(face['AgeRange']['High']) + ' years old')
    print("Gender of candidate: " + str(face['Gender']["Value"]))
    print("Emotional state of candidate: " + str(face['Emotions'][1]["Type"]))

    Sunglass = str(face['Sunglasses']['Value'])

    if Sunglass == 'True':
        print("The detected face is wearing sunglasses")
    else:
        print("The detected face is not wearing sunglasses")

    Mustache = str(face['Mustache']['Value'])
    Gender = str(face['Gender']['Value'])

    if str(face['Gender']["Value"]) == 'Male':
        if Mustache == 'True':
            print("The detected face has mustache")
        else:
            print("The detected face doesn't have mustache")



