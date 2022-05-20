SILENT     = @
# -m32    x86
# -mx32   x86/64
# -m64    x64
ARCH       =
VERSION    = -DCLIPS_MAJOR=6 \
			 -DCLIPS_MINOR=24 \
			 -DPYCLIPS_MINOR=24 \
			 -DPYCLIPS_MAJOR=6 \
			 -DPYCLIPS_PATCHLEVEL=7 \
			 -DPYCLIPS_INCREMENTAL=348

CC         = gcc
AR         = ar rcs
LD         = ld
# Compiler flags
CFLAGS     = $(ARCH) -g -Wall -O2 -fPIC \
			 -fstack-protector-strong \
			 -fno-strict-aliasing \
			 -pthread \
			 -fwrapv \
			 -Wdate-time \
			 -Werror=format-security \
			 -Wformat \
			 -Wno-unused-result \
			 -Wsign-compare
# -D_FORTIFY_SOURCE=2
# -DPYCLIPS
# -c clipsmodule.c
# -fPIC
# -I./clipssrc
# -I/usr/include/python3.8
# -o build/temp.linux-x86_64-3.8/clipsmodule.o
# -DNDEBUG

# Preprocessor flags
CPPFLAGS   = $(VERSION)
# Linker flags
LDFLAGS    = -lm



CXX        = g++
CXXFLAGS   =
RM         = rm -f
MK         = mkdir -p

# SRC_DIR    = .
OBJ_DIR    = ./obj
LIB_DIR    = ./lib
BIN_DIR    = ./bin

TARGETS    = $(LIB_DIR)/libclips.so $(LIB_DIR)/libclips.a $(BIN_DIR)/clips
SOURCES    = $(filter-out main.c, $(wildcard *.c))
OBJECTS    = $(SOURCES:%.c=$(OBJ_DIR)/%.o)

all: prep_dirs $(TARGETS)

$(BIN_DIR)/clips: $(OBJ_DIR)/main.o $(LIB_DIR)/libclips.a
	$(SILENT) echo -n "Generating $@... "
	$(SILENT) $(CC) $^ -o $@ -L$(LIB_DIR) -lclips $(LDFLAGS)
	$(SILENT) echo "Done"

$(LIB_DIR)/libclips.a: $(OBJECTS)
	$(SILENT) echo -n "Packing $@... "
	$(SILENT) $(AR) $@ $^ -o
	$(SILENT) echo "Done"

$(LIB_DIR)/libclips.so: $(OBJECTS)
	$(SILENT) echo -n "Linking $@... "
	$(SILENT) $(CC) $^ -shared -o $@ $(CFLAGS) $(CPPFLAGS) $(LDFLAGS)
	$(SILENT) echo "Done"

$(OBJ_DIR)/%.o: %.c
	$(SILENT) echo "Building $@"
	$(SILENT) $(CC) -c -o $@ $(CFLAGS) $(CPPFLAGS) $<

prep_dirs:
	$(SILENT) $(MK) $(LIB_DIR)
	$(SILENT) $(MK) $(OBJ_DIR)
	$(SILENT) $(MK) $(BIN_DIR)

clean_objects:
	$(SILENT) $(RM) $(OBJ_DIR)/*
	$(SILENT) $(RM) *.o

clean_targets:
	$(SILENT) $(RM) $(TARGETS)

clean: clean_objects clean_targets