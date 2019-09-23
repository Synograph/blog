module "bonjour" {
  source = "./print_string"

  string = "Bonjour "
}

module "synograph" {
  source = "./print_string"

  string = "Synograph "

  dependency = join(",", [module.bonjour.complete)
}

module "france" {
  source = "./print_string"

  string = "France"

  dependency = join(",", [module.synograph.complete])
}
