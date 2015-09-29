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

FILE uartFileStream = FDEV_SETUP_STREAM(uart_printChar, NULL, _FDEV_SETUP_RW);


int main(void)
{
	uart_init(UART_BAUD_SELECT(UART_BAUD_RATE,F_CPU));
	uart1_init(UART_BAUD_SELECT(UART_BAUD_RATE,F_CPU));
	stdout = &uartFileStream;


	sei();
	
	AX18SetSpeed(BROADCAST_ID, 250);
	while(1) //infinite loop
	{
		AX18SetPosition(BROADCAST_ID, 200);
		_delay_ms(1000);
		AX18SetPosition(BROADCAST_ID, 800);
		_delay_ms(1000);
		
		//_delay_ms(1000);	
		//char buffer[2];
		//AX18FRead(55, AX_PRESENT_POSITION_L, buffer, 2);	
		//printf("Read 0x%x 0 0x%x\r\n", buffer[0], buffer[1]);
	}
	
	return 0;
}