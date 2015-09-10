#ifndef F_CPU
#define F_CPU 16000000UL // 16 MHz clock speed
#endif

#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
	DDRD = PIN0;
	while(1) //infinite loop
	{
		PORTD = PIN0;
		_delay_ms(1000); 
		PORTD = 0x00; 
		_delay_ms(1000);
	}
}