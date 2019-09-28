import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import Flask, redirect

def handleContactForm(request):
    request_json = request.get_json()

    if request_json and 'email' in request_json:
        email = request_json['email']
    if request_json and 'name' in request_json:
        name = request_json['name']
    if request_json and 'message' in request_json:
        message = request_json['message']

    # Send to Synograph
    sendMail('contact@synograph.com',
             email,
             'Contact Synograph.com: ' + name,
             message)

    # Send to customer
    sendMail(email,
             'contact@synograph.com',
             'Merci de nous avoir contacté!',
             '''Bonjour' + name + ',
             Merci de nous avoir contacté!
             Nous reviendrons vers vous aussi rapidement que possible :)

             A bientôt. L\'équipe Synograph''')

    return redirect("https://www.synograph.com/thanks", code=302)

def sendMail(toAddress,fromAddress,mailSubject,htmlMessage):
    message = Mail(
    from_email=fromAddress,
    to_emails=toAddress,
    subject=mailSubject,
    html_content=htmlMessage)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
