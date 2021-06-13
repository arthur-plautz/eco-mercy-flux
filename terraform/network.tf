resource "aws_vpc" "eco_mercy" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "eco-mercy"
  }
}

resource "aws_subnet" "eco_mercy" {
  vpc_id     = aws_vpc.eco_mercy.id
  cidr_block = "10.0.0.0/24"
  
  tags = {
    Name = "eco-mercy"
  }
}
