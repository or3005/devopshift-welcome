



/////////// lab 2 \\\\\\\\\\\\\
variable "myip" {
  default = ""
}


resource "null_resource" "check_public_ip" {
  provisioner "local-exec" {
    command = <<EOT
      if [ -z "${aws_instance.vm.public_ip}" ]; then
        echo "ERROR: Public IP address was not assigned." >&2
        exit 1
      fi
    EOT
  }

  depends_on = [aws_instance.vm]
}

output "vm_public_ip" {
  value      = aws_instance.vm.public_ip
  depends_on = [null_resource.check_public_ip]
  description = "Public IP address of the VM"
}
