URL_GRAPHS = https://turing.cs.hbg.psu.edu/txn131/file_instances
PATH_GRAPHS = graphs

PATTERN_PATH = pattern/$(PATH_GRAPHS)
NEW_PATH = new/$(PATH_GRAPHS)
NAC_PATH = nac/$(PATH_GRAPHS)

GENERATED_PATH = own-graphs

GRAPHS = DIMACS_cliques
CONVERTER = converter

download:
	mkdir $(PATH_GRAPHS)
	# Downloads the testing graphs
	wget $(URL_GRAPHS)/clique/$(GRAPHS).tar.gz
	tar xvf $(GRAPHS).tar.gz
	# Downloads the converter: bin -> ascii
	# to format the graphs downloaded
	wget $(URL_GRAPHS)/$(CONVERTER).tar.gz
	tar xvf $(CONVERTER).tar.gz
	chmod +x $(CONVERTER)/bin2asc
	# Applys the converter
	./scripts/convert.sh
	# Remove all the unnecessary lines
	# in graph´s files
	./scripts/transform.py
	rm $(PATH_GRAPHS)/*.clq
	# Move graphs to its folders
	cp $(PATH_GRAPHS)/* $(PATTERN_PATH)
	cp $(PATH_GRAPHS)/* $(NEW_PATH)
	cp $(PATH_GRAPHS)/* $(NAC_PATH)
	# Clean the workspace
	rm -rf $(GRAPHS) $(GRAPHS).tar.gz
	rm -rf $(CONVERTER) $(CONVERTER).tar.gz
	rm -r $(PATH_GRAPHS)

generate:
	# Create respective folders
	mkdir $(PATTERN_PATH)/$(GENERATED_PATH)
	mkdir $(NEW_PATH)/$(GENERATED_PATH)
	mkdir $(NAC_PATH)/$(GENERATED_PATH)
	# Generate graphs
	python ./scripts/graph-generator.py
	# Move them to its folders
	cp $(GENERATED_PATH)/* $(PATTERN_PATH)/$(GENERATED_PATH)
	cp $(GENERATED_PATH)/* $(NEW_PATH)/$(GENERATED_PATH)
	cp $(GENERATED_PATH)/* $(NAC_PATH)/$(GENERATED_PATH)
	# Clean the workspace
	rm -r $(GENERATED_PATH)
	
clean:
	rm -f $(wildcard $(PATTERN_PATH)/*.txt)
	rm -f $(wildcard $(NEW_PATH)/*.txt)
	rm -f $(wildcard $(NAC_PATH)/*.txt)

clean-gen:
	rm -r $(PATTERN_PATH)/$(GENERATED_PATH)
	rm -r $(NEW_PATH)/$(GENERATED_PATH)
	rm -r $(NAC_PATH)/$(GENERATED_PATH)

.PHONY: clean download
