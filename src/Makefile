## compiler
CC=gcc
# directories
ODIR=lib
#files
SRC1 = double.c
SRC2 = sum.c
SRC3 = struct.c
SRC4 = struct2.c
OBJ1 = $(ODIR)/double.so
OBJ2 = $(ODIR)/sum.so
OBJ3 = $(ODIR)/struct.so
OBJ4 = $(ODIR)/struct2.so
# default target
all: $(OBJ1) $(OBJ2) $(OBJ3) $(OBJ4)
# rule to build shared objects
$(ODIR)/%.so: %.c
		mkdir -p $(@D)
		$(CC) -fPIC -shared -o $@ $<

.PHONY: clean
clean:
		rm -rf $(ODIR)/*.so
