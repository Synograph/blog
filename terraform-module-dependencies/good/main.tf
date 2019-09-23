module "bonjour" {
  source = "./print_string"
  moduleName = "bonjour"

  string = "Bonjour "
}

module "synograph" {
  source = "./print_string"
  moduleName = "synograph"

  string = "Synograph "

  dependency = join(",", [module.bonjour.complete])
}

module "france" {
  source = "./print_string"
  moduleName = "france"

  string = "France"

  dependency = join(",", [module.synograph.complete])
}
