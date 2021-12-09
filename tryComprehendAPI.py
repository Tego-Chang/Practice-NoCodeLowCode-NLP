import boto3
from pathlib import Path

client = boto3.client("comprehend")
oms_txt = Path('temp.txt').read_text()
response = client.detect_sentiment(
    Text = oms_txt,
    LanguageCode = 'en'
)
print(response)