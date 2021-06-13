
resource "aws_ecs_cluster" "eco_mercy" {
  name = "eco-mercy"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}

resource "aws_ecs_task_definition" "eco_mercy_embulk_load" {
  family                = "eco_mercy"
  container_definitions = file("task_definitions/embulk_load.json")
}

resource "aws_ecs_service" "eco_mercy_embulk_load" {
  name            = "eco-mercy-embulk-load"
  cluster         = aws_ecs_cluster.eco_mercy.id
  task_definition = aws_ecs_task_definition.eco_mercy_embulk_load.arn
}