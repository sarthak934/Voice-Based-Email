import boto3

ses = boto3.client('ses')
polly = boto3.client('polly')

def lambda_handler(event, context):
    intent = event['currentIntent']['name']
    
    if intent == "SendEmailIntent":
        recipient = event['currentIntent']['slots']['Recipient']
        subject = event['currentIntent']['slots']['Subject']
        message = event['currentIntent']['slots']['Message']
        
        ses.send_email(
            Source="your-verified-email@example.com",  # Replace with your SES-verified email
            Destination={'ToAddresses': [recipient]},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': message}}
            }
        )
        return {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "Email sent successfully!"
                }
            }
        }
    
    elif intent == "ReadEmailIntent":
        # (Optional: Fetch real emails here)
        email_text = "You have no new emails."
        
        # Convert text to speech (Polly)
        response = polly.synthesize_speech(
            Text=email_text,
            OutputFormat="mp3",
            VoiceId="Joanna"
        )
        
        return {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "Here’s your email."
                }
            }
        }