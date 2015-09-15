#include "uart.h"
#include "AX18ServoDriver.h"

/**
 * Generate checksum for Writing
 * @param  id      Servo identifier
 * @param  address Servo memory write address
 * @param  data    Data to write to memory
 * @param  length  Length of data
 * @return         Checksum
 */
unsigned char generateTxChecksum(unsigned char id, unsigned char address, unsigned char *data, unsigned length) {

	unsigned char checksum = id + (length + 3) + AX_WRITE_DATA + address;
	for(unsigned char i = 0; i < length; i++) {
		checksum += data[i];
	}
	return ~checksum;
}

/**
 * Generate checksum for Reading
 * @param  id      Servo identifier
 * @param  error   Error returned from Servo
 * @param  address Servo memory read address
 * @param  data    received data
 * @param  length  length of received data
 * @return         checksum
 */
unsigned char generateRxChecksum(unsigned char id, unsigned char error, unsigned char address, unsigned char *data, unsigned char length) {

	unsigned char checksum = id + (length + 3) + error + AX_READ_DATA + address;
	for(unsigned char i = 0; i < length; i+=) {
		checksum += data[i];
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

	// Enable Uart Tx so we can send
	UART1_CONTROL |= (1<<UART1_BIT_TXEN);

	uart1_putc(AX_START);
	uart1_putc(AX_START);
	uart1_putc(id);
	uart1_putc(length + 3);
	uart1_putc(AX_WRITE_DATA);
	uart1_putc(address);

	for(unsigned char i = 0; i < length; i++) {
		uart1_putc(data[i]);
	}

	uart1_putc(generateTxChecksum(id, address, data, length));

}

/**
 * Reads from the servo
 * @param id      Servo identifier
 * @param address Servo memory read address
 * @param buffer  Buffer to save data
 * @param length  Length to read
 * @return        Error occurred, return 0 on success, 1 on error
 */
unsigned char AX18FRead(unsigned char id, unsigned char address, unsigned char *buffer, unsigned char length) {

	// Clear Rx buffer so we can receive fresh data
	uart1_clearRxBuffer();

	// Enable Uart Tx so we can send
	UART1_CONTROL |= (1<<UART1_BIT_TXEN);

	uart1_putc(AX_START);
	uart1_putc(AX_START);
	uart1_putc(id);
	uart1_putc(length + 3);
	uart1_putc(AX_READ_DATA);
	uart1_putc(address);
	uart1_putc(length);


	uart1_putc(generateTxChecksum(id, AX_READ_DATA, address, /* x */, length));

	// Disable Uart Tx for we can receive
	UART1_CONTROL ~= (1<<UART1_BIT_TXEN);

	unsigned char RxState, RxDataCount, Error = 0;
	unsigned char RxServoId, RxLength, RxError, RxChecksum;

	// Wait a couple of micro seconds to receive some data
	_delay_us(TX_READ_DELAY_TIME);

	// Loop trough all received bytes
	while(uart1_canRead() > 0) {
		char c = uart1_getc();
		printf("READ (0x%x) STATE (%d)", c, RxState);

		switch(RxState) {
			case 0:
				if(c == AX_START) {
					RxState = 1;
				}
			break;

			case 1:
				if(c == AX_START) {
					RxState = 2;
				} else {
					RxState = 0;
				}
			break;

			case 2:
				if(c != AX_START) {
					RxServoId = c;
					RxState = 3;
				} else {
					RxState = 0;
					Error = 1;
				}
			break;

			case 3:
				RxLength = c;
				RxState = 4;
			break;

			case 4:
				RxError = c;
				RxState = 5;
			break;

			case 5:
				if(RxDataCount > length) {
					RxChecksum = c;
					RxState = 6;
					break;
				}

				buffer[RxDataCount++] = c;
			break;

			// There is no state 5 unless we got more data then expected...
			case 6:
				Error = 1;
			break;

		}
	}
	if(generateRxChecksum(RxServoId, RxError, ) != RxChecksum) {
		Error = 1;
	}

	return Error;
	
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
	AX18FWrite(BROADCAST_ID, AX_GOAL_POSITION_L, buffer, 2);
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