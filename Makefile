PREFIX ?= /usr/local
LUADIR ?= $(PREFIX)/share/lua/5.1

install:
	install -Dpm644 gpio.lua $(DESTDIR)$(LUADIR)/rpi/gpio.lua

uninstall:
	rm -f $(DESTDIR)$(LUADIR)/rpi/gpio.lua


.PHONY: install uninstall
