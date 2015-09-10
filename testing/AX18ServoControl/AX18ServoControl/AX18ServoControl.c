#ifndef F_CPU
#define F_CPU 16000000UL // 16 MHz clock speed
#endif

#define UART_BAUD_RATE 9600


#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdlib.h>

#include "IOPorts_ATMega.h"
#include "uart.h"

int main(void)
{
	uart_init(UART_BAUD_SELECT(UART_BAUD_RATE,F_CPU));
	
	DDRB = 0xFF;

	sei();
	while(1) //infinite loop
	{
		PORTB = PIN0_bm;
		_delay_ms(1000); 
		PORTB = 0x00; 
		_delay_ms(1000);
		uart_puts("hoi");
	}
}