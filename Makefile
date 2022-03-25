RUN = poetry run
PROJECT = data_manifesto
SRC = src
SCHEMA_DIR = $(SRC)/linkml/
SCHEMA_ROOT = $(SCHEMA_DIR)/$(PROJECT).yaml
DEST = generated

gen:
	$(RUN) gen-project -d $(DEST) $(SCHEMA_ROOT) && mv $(DEST)/*.py $(SRC)/$(PROJECT)/datamodel/

