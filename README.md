# Voice-Based-Email

Final System Flow – Key Steps:

1. User speaks: “Send email to john@example.com.”

2. Amazon Lex detects intent and extracts slots: Recipient, Subject, MessageBody.

3. Lex passes data to AWS Lambda for processing.

4. Lambda formats and sends the email using Amazon SES.

5. Lambda returns response to Lex.

6. Lex responds to user: “Email sent successfully.”
