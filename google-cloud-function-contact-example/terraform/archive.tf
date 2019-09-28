data "archive_file" "contactFormSource" {
  type        = "zip"
  output_path = "${path.module}/contactForm/contactFormSource.zip"

  source {
    content  = "${path.module}/contactForm/main.py"
    filename = "main.py"
  }

  source {
    content  = "${path.module}/contactForm/requirements.py"
    filename = "requirements.txt"
  }
}
