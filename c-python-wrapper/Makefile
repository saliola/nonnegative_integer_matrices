all:
	gcc nonneg_int_vectors.c
	./a.out

python-wrapper:
	gcc -fPIC -shared -o nonneg_int_vectors.so nonneg_int_vectors.c

clean:
	rm -f a.out
	rm -f *.so
