resource "null_resource" "print_string" {
  depends_on = [null_resource.dependency]

  provisioner "local-exec" {
    command = "echo -n ${var.string} | tee -a /tmp/testTerraform"
  }
}

variable "string" {
  default = ""
}
