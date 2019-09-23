resource "null_resource" "dependency" {
  triggers = {
    dependency = var.dependency
  }
}

resource "null_resource" "complete" {
  depends_on = [null_resource.string]
}

variable "dependency" {
  default = ""
}

variable "moduleName" {
  default = ""
}

output "complete" {
  value = "${var.dependency}${var.dependency == "" ? "" : "->"}${var.moduleName}(${null_resource.complete.id})"
}
