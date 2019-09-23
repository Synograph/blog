resource "null_resource" "print_string" {
  provisioner "local-exec" {
    command = "printf %s ${var.string} >> /tmp/testTerraform"
  }
}

variable "string" {
  default = ""
}
