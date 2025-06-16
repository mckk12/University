# Maciej Ciepiela, 347677

CC = gcc
CFLAGS = -std=gnu17 -Wall -Wextra -O2

SRC = main.c transporting.c sending.c receiving.c
OBJ = $(SRC:.c=.o)
EXEC = transport

all: $(EXEC)

$(EXEC): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f *.o

distclean: clean
	rm -f $(EXEC)
