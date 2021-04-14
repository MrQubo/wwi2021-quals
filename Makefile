BUILD_DIR ?= build

$(BUILD_DIR)/README.pdf: README.md
	mkdir -p $(BUILD_DIR)
	pandoc --from=gfm --to=pdf --output=$@ $+
