import logging
import json
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
  file_name = (file_to_clean.split('/')[-1]).split('.')[0]
  markdown_content = open(f"{file_to_clean}", "r").read()
  cleaned_string = ''
  for line in markdown_content.split('\n'):
    if not ('[' in line):
      line = line.replace('#', '')
      cleaned_string += line + '\n'
  logging.info(f'File = {file_to_clean} Cleaned')
  logging.info(f'Returning {file_name}')
  return cleaned_string, file_name


def synthesis_file(cleaned_string, file_name):
  logging.info(f'Synthesising file = {file_name}')
  logging.debug(cleaned_string)
  response = polly_client.start_speech_synthesis_task(
      OutputFormat='mp3',
      OutputS3BucketName='jorgehoyos',
      OutputS3KeyPrefix=file_name,
      Text=cleaned_string,
      TextType='text',
      VoiceId='Joanna'
  )
  logging.debug(json.dumps(response, default=str, indent=2))
  task_id = response['SynthesisTask']['TaskId']
  logging.info(f'Start speech task initiated with id {task_id}')
  return task_id


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


if __name__ == "__main__":
  markdown_files = sys.argv[1:]
  logging.info(f'Markdown files to clean = {markdown_files}')
  for file_to_clean in markdown_files:
    cleaned_string, file_name = clean_file(file_to_clean)
    task_id = synthesis_file(cleaned_string, file_name)
    download_audio(task_id)
