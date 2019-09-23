resource "null_resource" "print_string" {
  provisioner "local-exec" {
    command = "printf ${var.string} >> /tmp/testTerraform"
  }
}

variable "string" {
  default = ""
}
