#ifndef F_CPU
#define F_CPU 16000000UL // 16 MHz clock speed
#endif

#define UART_BAUD_RATE 1000000

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdlib.h>
#include <stdio.h>

#include "AX18ServoDriver.h"
#include "IOPorts_ATMega.h"
#include "uart.h"

FILE uartFileStream = FDEV_SETUP_STREAM(uart1_printChar, NULL, _FDEV_SETUP_RW);

int main(void)
{
	uart_init(UART_BAUD_SELECT(UART_BAUD_RATE,F_CPU));
	uart1_init(UART_BAUD_SELECT(UART_BAUD_RATE,F_CPU));
	DDRB = 0xFF;

	sei();
	AX18Speed(BROADCAST_ID, 150);
	while(1) //infinite loop
	{
		
		
		AX18Position(BROADCAST_ID, 0);
		_delay_ms(10000);
		AX18Position(BROADCAST_ID, 1023);
		//AX18Position(BROADCAST_ID, 50);
		_delay_ms(10000);		
	}
	
	return 0;
}