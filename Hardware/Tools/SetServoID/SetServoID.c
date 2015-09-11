/*
 * SetServoID.c
 *
 * Created: 11-9-2015 12:28:19
 *  Author: mv
 */ 

#include "SetServoID.h"

#define THISID 0x55 // Change value

int main(void)
{
	uart1_init(UART_BAUD_SELECT(UART_BAUD_RATE,F_CPU));
	sei();

	setID(THISID);

    while(1)
    {
        ledState(1);
        _delay_ms(1000);
        ledState(0); 
        _delay_ms(1000);z
    }
}

/**
 * Sets the ID of the connected AX18 servo. Only one servo must be connected at a time.
 * @param IDnumber Programs the wanted ID in the servo.
 */
void setID (unsigned char IDnumber)
{
	unsigned char checksum = ~(BROADCAST_ID + AX_LED_LENGTH + AX_WRITE_DATA + AX_ID + IDnumber);
	uart1_putc(AX_START);
	uart1_putc(AX_START);
	uart1_putc(BROADCAST_ID);
	uart1_putc(AX_LED_LENGTH);
	uart1_putc(AX_WRITE_DATA);
	uart1_putc(AX_ID);
	uart1_putc(IDnumber);
	uart1_putc(checksum);
}

/**
 * Turns the indication led on the servo on or off.
 * @param Status The status of the indication led.
 */
void ledState (unsigned char Status)
{
	unsigned char Checksum = ~(THISID + AX_LED_LENGTH + AX_WRITE_DATA + AX_LED + Status);
	uart1_putc(AX_START);              // Send Instructions over Serial
	uart1_putc(AX_START);
	uart1_putc(THISID);
	uart1_putc(AX_LED_LENGTH);
	uart1_putc(AX_WRITE_DATA);
	uart1_putc(AX_LED);
	uart1_putc(Status);
	uart1_putc(Checksum);
}