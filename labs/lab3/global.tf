provider "aws" {
 region = var.region
}

variable "region" {
 default = "us-east-1"
}


variable "vm_name" {
 default = "vm-Or"
}

data "aws_ami" "findimage"{
    owners = [ "self" ]
  filter {
    name   = "name"
    values = ["terraform-workshop-image-do-not-delete"]
  }

}

variable "admin_username" {
 default = "admin-user"
}

variable "admin_password" {
 default = "Password123!"
}

variable "vm_size" {
 default = "t2.micro"
}
resource "aws_instance" "ami" {
  ami           = data.aws_ami.findimage.id
  instance_type = "t2.micro"

}
data "aws_ami" "myprav"{
    owners = [ "self" ]
}