resource "null_resource" "string" {
  depends_on = [null_resource.dependency]

  provisioner "local-exec" {
    command = "printf ${var.string} >> /tmp/testTerraform"
  }
}

variable "string" {
  default = ""
}
