resource "google_cloudfunctions_function" "synographContactForm" {
  name                  = "synographContactForm"
  description           = "Handle the Contact Form on Synograph website"
  runtime               = "python3.7"
  max_instances         = 5
  available_memory_mb   = 128
  source_repository     = ./synographContactForm/
  trigger_http          = true
  entry_point           = "handleContactForm"
}

output "synographContactFormHttpsTriggerUrl" {
  value = google_cloudfunctions_function.synographContactForm.https_trigger_url
  description = "URL which triggers function execution"
}
