provider "aws" {
 region = var.region
}


variable "region" {
 default = "us-east-1"
}

output "print_region" {
  value = var.region
}


# Mocked IP var
variable "emptyip" {
   default = ""
}

variable "ingress_port" {
  
}

variable "ingress_protocol" {
  
}

variable "outgress_port" {
  
}

variable "outgress_protocol" {
  
}

variable "cidr_blocks" {
  
}

resource "aws_security_group" "sg" {
 ingress {
   from_port   = var.ingress_port
   to_port     = var.ingress_port
   protocol    = var.ingress_protocol
   cidr_blocks = var.cidr_blocks
 }

 
 egress {
   from_port   = var.outgress_port
   to_port     = var.outgress_port
   protocol    = var.outgress_protocol
   cidr_blocks = var.cidr_blocks
 }
}


variable "ami_id" {
  
}

variable "instance_type" {
  
}

variable "machine-name" {
    
 }


resource "aws_instance" "vm" {
#   ami           = "ami-0c02fb55956c7d316"
 ami = var.ami_id
 instance_type = var.instance_type


 vpc_security_group_ids = [aws_security_group.sg.id]
 
 tags = {
   Name = var.machine-name
 }
}


output "vm_public_ip" {
 value       = aws_instance.vm.public_ip
 description = "Public IP address of the VM"
 depends_on = [ null_resource.check_public_ip ]
}


resource "null_resource" "check_public_ip" {
 provisioner "local-exec" {
   command = <<EOT
     if [ -z "${aws_instance.vm.public_ip}" ]; then
       echo "ERROR: Public IP address was not assigned." >&2
       exit 1
       else
       echo "We got the IP! ${aws_instance.vm.public_ip}"
     fi
   EOT
 }


 depends_on = [aws_instance.vm]
}