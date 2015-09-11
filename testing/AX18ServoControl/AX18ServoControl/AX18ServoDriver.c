#include "AX18ServoDriver.h"

/**
 * Generates checksum
 * @param  id      Servo identifier
 * @param  address Servo memory write address
 * @param  data    Data to write to memory
 * @param  length  Length of data
 * @return         Checksum
 */
unsigned char generateChecksum(unsigned char id, unsigned char address, unsigned char *data, unsigned length) {

	unsigned char checksum = id + (length + 3) + AX_WRITE_DATA + address;
	for(unsigned char i = 0; i < length; i++) {
		checksum += data[i]
	}
	return ~checksum;
}

/**
 * Writes to the Servo
 * @param id      Servo identifier
 * @param address Servo memory write address
 * @param data    Data to write to memory
 * @param length  Length of data
 */
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

/**
 * Set goal position of servo. Range of position is 0 - 1023.
 * @param id  Servo identifier
 * @param pos Goal position
 */
void AX18Position(unsigned char id, unsigned long pos) {

	unsigned char buffer[2] = {
		unsigned16ToUnsigned8Lower(pos), 
		unsigned16ToUnsigned8Higher(pos)};

	AX18FWrite(id, AX_GOAL_POSITION_L, buffer, 2);
}

/**
 * Set speed of servo. This speed will be used in both JOIN and WHEEL mode.
 * @param id    Servo identifier
 * @param speed Speed
 */
void AX18Speed(unsigned char id, unsigned long speed) {
	unsigned char buffer[2] = {
		unsigned16ToUnsigned8Lower(speed), 
		unsigned16ToUnsigned8Higher(speed)};

	AX18FWrite(id, AX_GOAL_SPEED_L, buffer, 2);
}

/**
 * Returns lower byte of signed 16 bit value
 * @param  data 16 bit signed value
 * @return      lower byte
 */
char signed16ToSigned8Lower(long data) {
	return data & 0xFF;
}

/**
 * Returns higher byte of signed 16 bit value
 * @param  data 16 bit signed value
 * @return      higher byte
 */
char signed16ToSigned8Higher(long data) {
	return (data >> 8) & 0xFF; 
}

/**
 * Returns lower byte of unsigned 16 bit value
 * @param  data 16 bit unsigned value
 * @return      lower byte
 */
unsigned char unsigned16ToUnsigned8Lower(unsigned long data) {
	return data & 0xFF;
}

/**
 * Returns higher byte of unsigned 16 bit value
 * @param  data 16 bit unsigned value
 * @return      higher byte
 */
unsigned char unsigned16ToUnsigned8Higher(unsigned long data) {
	return (data >> 8) & 0xFF; 
}