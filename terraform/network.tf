resource "aws_vpc" "eco_mercy" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "eco_mercy" {
  vpc_id     = aws_vpc.eco_mercy.id
  cidr_block = "10.0.1.0/24"
}
