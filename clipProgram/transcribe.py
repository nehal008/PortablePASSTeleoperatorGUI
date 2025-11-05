# -*- coding: utf-8 -*-
import time
import boto3
import pandas as pd
import ffmpy

#takes an audio file(convFile) and converts to an mp3 format using ffmpy
def convert(convFile):
    trans_file = convFile.split('.')[0] + ".wav"
    ff = ffmpy.FFmpeg(
        inputs = {convFile: '-y'},
        outputs = {trans_file: None})
    
    ff.run()
    return trans_file

#uploads the prepared audio file(file) to aws so it can be transcribed
def upload(file, aws_id, aws_key):
    session = boto3.Session(
        aws_access_key_id=aws_id,
        aws_secret_access_key=aws_key,
    )
    s3 = session.resource('s3')
    # Filename - File to upload
    # Bucket - Bucket to upload to (the top level directory under AWS S3)
    # Key - S3 object name (can contain subdirectories). If not specified then file_name is used
    s3.meta.client.upload_file(Filename=file, Bucket='speech-clip-s3-bucket', Key=file)

#transcribe audio file and call helper functions as needed
def amazonTranscribe(audio_file, key_file):
    #open key file and retrieve aws creds
    cred_file = open(key_file, 'r')
    creds = cred_file.readlines()
    aws_id = creds[1]
    aws_key = creds[2]
    aws_id = aws_id.strip()
    
    transcribe = boto3.client('transcribe',
    aws_access_key_id = aws_id,
    aws_secret_access_key = aws_key,
    region_name = 'us-east-1')
    
    file_format = audio_file.split('.')[1]
    
    if file_format != 'wav':
        audio_file = convert(audio_file)
        file_format = 'wav'
        
    upload(audio_file, aws_id, aws_key)
    
    job_uri = 's3://speech-clip-s3-bucket/'+ audio_file # your S3 access link
    # Usually, I put like this to automate the process with the file name
    # "s3://bucket_name" + audio_file_name    # Usually, file names have spaces and have the file extension like .mp3
    # we take only a file name and delete all the space to name the job
    job_name = audio_file + str(time.time()) #(audio_file_name.split('.')[0]).replace(" ", "")    # file format  

    # check if name is taken or not
    transcribe.start_transcription_job(
      TranscriptionJobName=job_name,
      Media={'MediaFileUri': job_uri},
      MediaFormat = file_format,
      LanguageCode='en-US')

    #runs until the transcription is done, pauses for 2 seconds each time the job status is called
    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            print('done')
            break
        time.sleep(2)
        
    if status == None:
        print('transcription error')
    else:
        text = pd.read_json(status['TranscriptionJob']['Transcript']['TranscriptFileUri'])
        text = text['results'][1][0]['transcript']
        
    return text



        