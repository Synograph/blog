from flask import Flask, redirect

def handleContactForm(request):
    request_json = request.get_json()

    if request_json and 'email' in request_json:
        email = request_json['email']
    if request_json and 'name' in request_json:
        name = request_json['name']
    if request_json and 'message' in request_json:
        message = request_json['message']

    sendMail(email,
             'contact@synograph.com',
             'Merci de nous avoir contacté!',
             '''Bonjour' + name + ',
             Merci de nous avoir contacté!
             Nous reviendrons vers vous aussi rapidement que possible :)

             A bientôt. L\'équipe Synograph''')

    sendMail('contact@synograph.com',
             email,
             'Contact Synograph.com: ' + name,
             message)

    return redirect("https://www.synograph.com/thanks", code=302)

def sendMail(to,from,subject,message):
    return True
