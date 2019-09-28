data "archive_file" "contactFormSource" {
  type        = "zip"
  output_path = "${path.module}/contactFormSource.zip"

  source_dir = "${path.module}/contactForm"
}
