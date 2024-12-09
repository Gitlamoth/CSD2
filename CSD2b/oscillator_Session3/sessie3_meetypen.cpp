//
// Created by braml on 03/12/2024.
//

pointers:


int add(intx, int y) {
  return x + y;
}


void addPointer(int* x, int y) {
  *x += y;
}

void addByReference(int& x, int y) {\
x += y;
}