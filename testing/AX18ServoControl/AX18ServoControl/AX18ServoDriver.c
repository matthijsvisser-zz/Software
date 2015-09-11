#include "AX18ServoDriver.h"

unsigned char generateChecksum(unsigned char id, unsigned char address, unsigned char *data, unsigned length) {

	unsigned char checksum = id + (length + 3) + AX_WRITE_DATA + address;
	for(unsigned char i = 0; i < length; i++) {
		checksum += data[i];
	}
	return ~checksum;
}

void AX18FWrite(unsigned char id, unsigned char address, unsigned char *data, unsigned char length) {

	uart1_putc(AX_START);
	uart1_putc(AX_START);
	uart1_putc(id);
	uart1_putc(length + 3);
	uart1_putc(AX_WRITE_DATA);
	uart1_putc(address);

	for(unsigned char i = 0; i < length; i++) {
		uart1_putc(data[i]);
	}

	uart1_putc(generateChecksum(id, address, data, length));

}

// return lower byte
char signed16ToSigned8Lower(long data) {
	return data & 0xFF;
}

// return higher byte
char signed16ToSigned8Higher(long data) {
	return (data >> 8) & 0xFF; 
}

// return lower byte
unsigned char unsigned16ToUnsigned8Lower(unsigned long data) {
	return data & 0xFF;
}

// return higher byte
unsigned char unsigned16ToUnsigned8Higher(unsigned long data) {
	return (data >> 8) & 0xFF; 
}