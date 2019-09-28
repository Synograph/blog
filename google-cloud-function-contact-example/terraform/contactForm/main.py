import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import redirect


def handleContactForm(request):
    request_json = request.get_json()
    contactEmail = os.environ.get('CONTACT_EMAIL')
    basePathSite = os.environ.get('BASE_PATH_SITE')
    content = dict()

    # Check form entry
    if request_json and 'email' in request_json:
        content['email'] = request_json['email']
    if request_json and 'firstName' in request_json:
        content['firstName'] = request_json['firstName']
    if request_json and 'lastName' in request_json:
        content['lastName'] = request_json['lastName']
    if request_json and 'message' in request_json:
        content['message'] = request_json['message']
    if request_json and 'company' in request_json:
        content['company'] = request_json['company']
    if request_json and '_next' in request_json:
        content['_next'] = request_json['_next']

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
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)