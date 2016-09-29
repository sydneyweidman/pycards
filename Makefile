
ETAGS = /usr/bin/etags

.PHONY: all clean tags

tags: TAGS

TAGS:
	@echo "Making tags..."
	find ./ -name "*.py" -exec ${ETAGS} -l python -a -o TAGS {} \;

clean:
	@echo "Cleaning up..."
	-rm -f TAGS
