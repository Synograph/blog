import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import redirect


def handleContactForm(request):
    contactEmail = os.environ.get('CONTACT_EMAIL')
    basePathSite = 'https://www.synograph.com'
    content = dict()

    # Check form entry
    content['email'] = request.form['email']
    content['firstName'] = request.form['firstName']
    content['lastName'] = request.form['lastName']
    content['message'] = request.form['message']
    content['company'] = request.form['company']
    content['_next'] = request.form['_next']
    content['_oops'] = request.form['_oops']

    # Send to Contact email
    sendMail(content['email'],
             contactEmail,
             content,
             os.environ.get('CONTACT_FORM_INTERNAL_TEMPLATE_ID'))

    # Send to Client
    sendMail(contactEmail,
             content['email'],
             content,
             os.environ.get('CONTACT_FORM_CLIENT_TEMPLATE_ID'))

    return redirect(basePathSite + content['_next'], code=302)


def sendMail(fromAddress, toAddress, content, templateId):
    message = Mail(
        from_email=fromAddress,
        to_emails=toAddress,
        subject='none',
        html_content='none')
    message.dynamic_template_data = {
        'firstName': content['firstName'],
        'lastName': content['lastName'],
        'company': content['company'],
        'email': content['email'],
        'message': content['message']}
    message.template_id = templateId
    try:
        sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sendgrid_client.send(message)
        return response.status_code
    except Exception as e:
        print(e)
        return e
