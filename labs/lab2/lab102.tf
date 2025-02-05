
provider "aws" {
  region = var.region
}

variable "region" {
  default = "us-east-1"
}
/////////// lab 2 \\\\\\\\\\\\\
variable "myip" {
  default = ""
}

data "aws_instance" "yaniv_instance_id" {
instance_id="i-09df7e0ed385f871b"
}

output "yaniv_public_ip" {
  value = data.aws_instance.yaniv-vm.public_ip
  
}
data "aws_instance" "yaniv-vm" {

  filter {

  name = "tag:Name"
  values = [ "yaniv-vm" ]
  }

}



# Define a data source to fetch an existing Azure Public IP
# data "azurerm_public_ip" "example" {
#   name                = "existing-public-ip"
#   resource_group_name = "my-resource-group"
# }

# # Reference the IP address later in the configuration
# output "public_ip_address" {
#   value = data.azurerm_public_ip.example.ip_address
# }

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
