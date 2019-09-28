resource "google_storage_bucket" "contactFormSource" {
  name = "contact-form-source"
}

resource "google_storage_bucket_object" "contactFormSource" {
  name   = "contactFormSource.zip"
  bucket = "${google_storage_bucket.contactFormSource.name}"
  source = data.archive_file.contactFormSource.output_path
}

resource "google_cloudfunctions_function" "contactForm" {
  name                  = "contactForm"
  description           = "Handle the Contact Form of a website"
  runtime               = "python37"
  max_instances         = 5
  available_memory_mb   = 128
  timeout               = 10
  source_archive_bucket = "${google_storage_bucket.contactFormSource.name}"
  source_archive_object = "${google_storage_bucket_object.contactFormSource.name}"
  trigger_http          = true
  entry_point           = "handleContactForm"
  environment_variables = {
    CONTACT_EMAIL = var.,
    CONTACT_FORM_INTERNAL_TEMPLATE_ID = var.,
    CONTACT_FORM_CLIENT_TEMPLATE_ID = var.,
    SENDGRID_API_KEYs = var.,
   }
}

output "contactFormHttpsTriggerUrl" {
  value = google_cloudfunctions_function.contactForm.https_trigger_url
  description = "URL which triggers function execution"
}
