resource "null_resource" "string" {
  depends_on = [null_resource.dependency]

  provisioner "local-exec" {
    command = "printf %s ${var.string} >> /tmp/testTerraform"
  }
}

variable "string" {
  default = ""
}
