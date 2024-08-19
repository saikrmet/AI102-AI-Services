from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def main():
    global ai_endpoint
    global ai_key

    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        # Get user input (until they enter "quit")
        userText =''
        while userText.lower() != 'quit':
            userText = input('\nEnter some text ("quit" to stop)\n')
            if userText.lower() != 'quit':
                keyPhrases = GetKeyPhrases(userText)
                print('Key Phrases:', keyPhrases)

    except Exception as ex:
        print(ex)

def GetKeyPhrases(text):

    # Create client using endpoint and key
    credential = AzureKeyCredential(ai_key)
    client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)

    # Call the service to get the detected language
    keyPhrases = client.extract_key_phrases(documents=[text])[0]
    if not keyPhrases.is_error:
        return keyPhrases.key_phrases


if __name__ == "__main__":
    main()