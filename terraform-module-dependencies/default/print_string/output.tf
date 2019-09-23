resource "null_resource" "print_string" {
  provisioner "local-exec" {
    command = "echo -n ${var.string}"
  }
}
