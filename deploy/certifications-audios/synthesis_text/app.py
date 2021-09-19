import logging
import json
import re
import time
import sys
import boto3
polly_client = boto3.client('polly')
s3_resource = boto3.resource('s3')
logging.basicConfig(level=logging.INFO)


def clean_file(file_to_clean):
  """Cleans a file from the character # that is found in markdown files
  Parameters
  ----------
  file_to_clean : markdown file
    Path to the file to clean
  """

  logging.info(f'Cleaning file = {file_to_clean}')
  new_file_name = (file_to_clean.split('/')[-1]).split('.')[0]
  text = open(f"{new_file_name}", "w")
  lecture = open(f"{file_to_clean}", "r")
  for line in lecture:
    if not ('[' in line):
      line = line.replace('#', '')
      text.write(line)
  text.close()
  lecture.close()
  logging.info(f'File = {file_to_clean} Cleaned')
  synthesis_file(new_file_name)


def synthesis_file(file):
  logging.info(f'Synthesising file = {file}')
  file_content = (open(f"{file}", "r").read())
  logging.debug(file_content)
  response = polly_client.start_speech_synthesis_task(
      OutputFormat='mp3',
      OutputS3BucketName='jorgehoyos',
      OutputS3KeyPrefix=file,
      Text=file_content,
      TextType='text',
      VoiceId='Joanna'
  )
  logging.debug(json.dumps(response, default=str, indent=2))
  task_id = response['SynthesisTask']['TaskId']
  logging.info(f'Start speech task initiated with id {task_id}')
  download_audio(task_id)


def download_audio(task_id):
  logging.info(f'Getting task {task_id} status')
  task_status = get_task_status(task_id)
  while task_status['SynthesisTask']['TaskStatus'] != 'completed':
    logging.info(f'Task {task_id} not yet completed, waiting...')
    time.sleep(10)
    task_status = get_task_status(task_id)
  audio_key = task_status['SynthesisTask']['OutputUri'].split('/')[-1]
  logging.info(f'Downloading object {audio_key}')
  bucket = task_status['SynthesisTask']['OutputUri'].split('/')[-2]
  downloaded_file = audio_key.split('.')[0] + '.mp3'
  s3_resource.Bucket(bucket).download_file(audio_key, downloaded_file)


def get_task_status(task_id):
  task_status = polly_client.get_speech_synthesis_task(
      TaskId=task_id
  )
  return task_status


def lambda_handler(event, context):
  """Lambda function that takes a markdown file, cleans it as txt and
  uses polly to synthesis it as an audio

  Parameters
  ----------
  event: dict, required
      API Gateway Lambda Proxy Input Format
  context: object, required
      Lambda Context runtime methods and attributes

  Returns
  ------
  API Gateway Lambda Proxy Output Format: dict
  """

  markdown_files = sys.argv[1:]
  logging.info(f'Markdown files to clean = {markdown_files}')
  for file_to_clean in markdown_files:
    clean_file(file_to_clean)
  print(json.dumps(event))
  body = event['body']
  return {
      "statusCode": 200,
      "body": json.dumps({
          "message": "hello world from aws.",
          "commit": body
          # "location": ip.text.replace("\n", "")
      }),
  }
